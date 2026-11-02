"""
Hair oiliness analyzer - parametric 3D model (all dimensions in mm).

Parts (print each flat, PLA/PETG, 0.2 mm layers; print the base and
cassette in BLACK or dark filament so the optics stay light-tight):
  base_body.stl      measuring unit shell with optical tunnel (print upside down)
  base_plate.stl     bottom lid, 4x M3 screws
  cassette.stl       strip carrier - blotting paper goes in the recess on the underside
  sampler_sleeve.stl outer sleeve of the spring press (print cap-down)
  sampler_piston.stl piston + foot that holds the cassette (print foot-down)

Hardware: ESP32-C3 SuperMini, TSL2591 breakout, 5 mm white LED, 0.96" I2C OLED,
12x12 mm tactile button, 3 mm status LED, compression spring ~9 mm OD x 50 mm,
1x M3x8 screw (sampler peg), 4x M3x8 screws (base plate).

Run:  pip install manifold3d trimesh numpy ; python model.py
"""
import os
import numpy as np
import trimesh
from manifold3d import Manifold, CrossSection

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "stl")
SEG = 64

# ---------------------------------------------------------------- parameters
# cassette (strip carrier)
CAS_W, CAS_L, CAS_T = 26.0, 56.0, 1.6
CAS_WIN = 12.0            # optical window (square)
CAS_WIN_X = 14.0          # window centre measured from the cassette tip
CAS_PAPER = 16.0          # blotting-paper recess on the underside
CAS_TAB_L, CAS_TAB_H = 10.0, 5.0

# base unit
B_L, B_W, B_H = 95.0, 60.0, 34.0
B_R, WALL = 7.0, 2.2
PLATE_T = 2.0
SLOT_W, SLOT_H = CAS_W + 0.8, CAS_T + 0.4       # tunnel clearance
SLOT_Z = 12.0                                     # tunnel floor height
INSERT = CAS_L - CAS_TAB_L                        # how far the cassette goes in
OPT_X = INSERT - CAS_WIN_X                        # optical axis (from front face)
OPT_Y = B_W / 2
BLOCK_X1 = OPT_X + 16                             # rear end of optics block
BLOCK_Y = (B_W / 2 - SLOT_W / 2 - 5, B_W / 2 + SLOT_W / 2 + 5)
BOSS_D, BOSS_IN = 7.0, 6.5

# sampler
SL_OD, SL_ID, SL_H, SL_CAP = 26.0, 20.4, 62.0, 3.0
SL_SLOT_W, SL_SLOT_Z0, SL_SLOT_Z1 = 3.4, 8.0, 22.0
PI_D, PI_L = 20.0, 45.0
PI_PEG_Z = 24.0                                   # peg hole height above foot top
FOOT_X, FOOT_Y, FOOT_H = 32.0, 34.0, 9.0
FOOT_GROOVE_W, FOOT_GROOVE_D = CAS_W + 0.3, CAS_T        # cassette flush, paper protrudes ~0.1 mm


# ---------------------------------------------------------------- helpers
def box(x0, y0, z0, x1, y1, z1):
    return Manifold.cube([x1 - x0, y1 - y0, z1 - z0]).translate([x0, y0, z0])


def cyl(d, h, x=0, y=0, z=0, d2=None, seg=SEG):
    return Manifold.cylinder(h, d / 2, (d2 if d2 else d) / 2, seg).translate([x, y, z])


def cyl_x(d, h, x, y, z):
    """cylinder along +X starting at x"""
    return Manifold.cylinder(h, d / 2, d / 2, SEG).rotate([0, 90, 0]).translate([x, y, z])


def cyl_y(d, h, x, y, z):
    """cylinder along +Y starting at y"""
    return Manifold.cylinder(h, d / 2, d / 2, SEG).rotate([-90, 0, 0]).translate([x, y, z])


def rrect(L, W, r):
    cs = [CrossSection.circle(r, SEG).translate([x, y])
          for x in (r, L - r) for y in (r, W - r)]
    return CrossSection.batch_hull(cs)


def rounded_block(L, W, H, r, chamfer=0.0):
    body = rrect(L, W, r).extrude(H - chamfer)
    if chamfer <= 0:
        return body
    top = rrect(L - 2 * chamfer, W - 2 * chamfer, max(r - chamfer, 0.5)).extrude(0.01) \
        .translate([chamfer, chamfer, H - 0.01])
    return Manifold.batch_hull([body, top])


# ---------------------------------------------------------------- cassette
def cassette():
    """Fork-shaped carrier: the window is a slot open at the tip, so the backing
    pad in the sampler foot can slide into it and press the paper flat.
    The blotting paper (about 16 x 16 mm) is stuck to the underside with thin
    double-sided tape along its two edges, outside the optical window."""
    c = box(0, 0, 0, CAS_L, CAS_W, CAS_T)
    # chamfered tip so it slides in easily
    c = c - box(-1, -1, CAS_T - 0.6, 1.2, CAS_W + 1, CAS_T + 1)
    wx = CAS_WIN_X
    c = c - box(-1, CAS_W / 2 - CAS_WIN / 2, -1,
                wx + CAS_WIN / 2, CAS_W / 2 + CAS_WIN / 2, CAS_T + 1)
    # shallow marks showing where the paper goes (on top, printed side up)
    for yy in (CAS_W / 2 - CAS_PAPER / 2, CAS_W / 2 + CAS_PAPER / 2 - 0.6):
        c = c - box(wx - CAS_PAPER / 2, yy, CAS_T - 0.3, wx + CAS_PAPER / 2, yy + 0.6, CAS_T + 1)
    # grip tab / insertion stop
    tab = box(CAS_L - CAS_TAB_L, 0, 0, CAS_L, CAS_W, CAS_T + CAS_TAB_H)
    for i in range(4):
        gx = CAS_L - CAS_TAB_L + 2 + i * 2
        tab = tab - box(gx, -1, CAS_T + CAS_TAB_H - 0.8, gx + 0.8, CAS_W + 1, CAS_T + CAS_TAB_H + 1)
    return c + tab


# ---------------------------------------------------------------- base body
def base_body():
    outer = rounded_block(B_L, B_W, B_H, B_R, chamfer=1.5)
    inner = rrect(B_L - 2 * WALL, B_W - 2 * WALL, B_R - WALL).extrude(B_H - WALL + 0.0) \
        .translate([WALL, WALL, -1])
    inner = inner - box(-10, -10, B_H - WALL, B_L + 10, B_W + 10, B_H + 10)
    shell = outer - inner

    # solid optics block joined to front wall and ceiling
    block = box(0.5, BLOCK_Y[0], 3.0, BLOCK_X1, BLOCK_Y[1], B_H - 0.5)
    shell = shell + (block ^ outer)

    # corner screw bosses
    for bx in (BOSS_IN, B_L - BOSS_IN):
        for by in (BOSS_IN, B_W - BOSS_IN):
            shell = shell + (cyl(BOSS_D, B_H - 1, bx, by, 0) ^ outer)
            shell = shell - cyl(2.6, 12, bx, by, -0.01)

    # cassette tunnel through the front wall into the block
    shell = shell - box(-1, OPT_Y - SLOT_W / 2, SLOT_Z, INSERT + 1.5, OPT_Y + SLOT_W / 2, SLOT_Z + SLOT_H)
    # entry flare
    flare = Manifold.batch_hull([
        box(-0.01, OPT_Y - SLOT_W / 2 - 1.2, SLOT_Z - 1.0, 0.01, OPT_Y + SLOT_W / 2 + 1.2, SLOT_Z + SLOT_H + 1.0),
        box(2.5, OPT_Y - SLOT_W / 2, SLOT_Z, 2.51, OPT_Y + SLOT_W / 2, SLOT_Z + SLOT_H)])
    shell = shell - flare

    top = SLOT_Z + SLOT_H
    # LED: 3 mm aperture, 5.2 mm bore, wire channel to rear of block
    shell = shell - cyl(3.0, 2.5, OPT_X, OPT_Y, top - 0.01)
    shell = shell - cyl(5.3, 7.6, OPT_X, OPT_Y, top + 2.5)
    shell = shell - cyl(6.2, 3.0, OPT_X, OPT_Y, top + 10.0)       # flange seat
    shell = shell - box(OPT_X - 3, OPT_Y - 3, top + 7.0, BLOCK_X1 + 1, OPT_Y + 3, top + 12.0)
    # sensor: 6 mm aperture below tunnel, pocket for TSL2591 board from below
    shell = shell - cyl(6.0, 3.0, OPT_X, OPT_Y, SLOT_Z - 2.99)
    shell = shell - box(OPT_X - 10.5, OPT_Y - 10.5, 0, OPT_X + 10.5, OPT_Y + 10.5, SLOT_Z - 3.0)

    # top: OLED window, button hole, status LED
    oled_cx, oled_cy = 70.0, B_W / 2
    shell = shell - box(oled_cx - 12.5, oled_cy - 7.5, B_H - WALL - 1, oled_cx + 12.5, oled_cy + 7.5, B_H + 1)
    shell = shell - box(oled_cx - 13.8, oled_cy - 13.8, B_H - WALL - 1, oled_cx + 13.8, oled_cy + 13.8, B_H - 1.0)
    btn_x, btn_y = OPT_X - 2, 12.5
    shell = shell - cyl(12.4, 10, btn_x, btn_y, B_H - 5)
    shell = shell - cyl(3.1, 10, OPT_X - 2, B_W - 10, B_H - 5)
    # the button + LED sit over the optics block: give them pockets inside it
    shell = shell - box(btn_x - 6.3, btn_y - 6.3, B_H - WALL - 8, btn_x + 6.3, btn_y + 6.3, B_H - WALL + 0.01)
    shell = shell - cyl(6.0, 8, OPT_X - 2, B_W - 10, B_H - WALL - 8)

    # USB-C port in rear wall
    shell = shell - box(B_L - WALL - 1, B_W / 2 - 5, 5.5, B_L + 1, B_W / 2 + 5, 9.5)
    # engraved arrow + label area next to slot on front face
    shell = shell - box(-0.01, OPT_Y - 4, SLOT_Z + 6, 0.6, OPT_Y + 4, SLOT_Z + 7)
    return shell


def base_plate():
    p = rrect(B_L, B_W, B_R).extrude(PLATE_T)
    for bx in (BOSS_IN, B_L - BOSS_IN):
        for by in (BOSS_IN, B_W - BOSS_IN):
            p = p - cyl(3.3, PLATE_T + 2, bx, by, -1)
            p = p - cyl(6.2, 1.2, bx, by, -0.01, d2=3.3)   # countersink
    # locating lip that fits inside the shell
    lip_o = rrect(B_L - 2 * WALL - 0.4, B_W - 2 * WALL - 0.4, B_R - WALL - 0.2).extrude(2.0)
    lip_i = rrect(B_L - 2 * WALL - 3.6, B_W - 2 * WALL - 3.6, B_R - WALL - 1.8).extrude(3.0)
    lip = lip_o.translate([WALL + 0.2, WALL + 0.2, PLATE_T]) - lip_i.translate([WALL + 1.8, WALL + 1.8, PLATE_T - 0.5])
    # cut the lip where the optics block and bosses are
    lip = lip - box(0, BLOCK_Y[0] - 0.5, 0, BLOCK_X1 + 0.5, BLOCK_Y[1] + 0.5, 20)
    for bx in (BOSS_IN, B_L - BOSS_IN):
        for by in (BOSS_IN, B_W - BOSS_IN):
            lip = lip - cyl(BOSS_D + 1.5, 20, bx, by, 0)
    p = p + lip
    # vent slots under the electronics
    for i in range(5):
        vx = 62 + i * 5
        p = p - box(vx, 18, -1, vx + 2, 42, PLATE_T + 1)
    return p


# ---------------------------------------------------------------- sampler
def sampler_sleeve():
    s = cyl(SL_OD, SL_H) - cyl(SL_ID, SL_H - SL_CAP, 0, 0, -0.01)
    # spring locating post under the cap
    s = s + cyl(6.0, 8.0, 0, 0, SL_H - SL_CAP - 8.0)
    # peg slot (travel limit + force indicator)
    s = s - box(-SL_SLOT_W / 2, 0, SL_SLOT_Z0, SL_SLOT_W / 2, SL_OD, SL_SLOT_Z1)
    # grip rings
    for i in range(6):
        z = 30 + i * 4.5
        ring = cyl(SL_OD + 2, 1.2, 0, 0, z) - cyl(SL_OD - 1.2, 3, 0, 0, z - 1)
        s = s - ring
    # thumb dimple on the cap
    s = s - Manifold.sphere(9, SEG).translate([0, 0, SL_H + 7.5])
    return s


def sampler_piston():
    # foot (cassette holder); foot top at z = FOOT_H, bottom at z = 0
    foot = rounded_block(FOOT_X, FOOT_Y, FOOT_H, 4.0).translate([-FOOT_X / 2, -FOOT_Y / 2, 0])
    # cassette groove, open at the bottom and both ends (along X)
    foot = foot - box(-FOOT_X, -FOOT_GROOVE_W / 2, -1, FOOT_X, FOOT_GROOVE_W / 2, FOOT_GROOVE_D)
    # small bumps that hold the cassette by friction
    for sy in (-1, 1):
        bump = cyl(0.9, 8, 0, sy * (FOOT_GROOVE_W / 2), 0, seg=24)
        foot = foot + (bump ^ box(-5, -FOOT_Y, 0, 5, FOOT_Y, FOOT_GROOVE_D))
    # backing pad: slides into the cassette fork, presses the paper flat and
    # acts as the insertion stop (cassette goes in tip-first from the +X side)
    pad = CAS_WIN - 0.6
    foot = foot + box(-pad / 2, -pad / 2, 0, pad / 2, pad / 2, FOOT_GROOVE_D + 0.01)
    # alignment mark: arrow notch showing insertion direction
    foot = foot - box(FOOT_X / 2 - 1.0, -2, FOOT_H - 0.8, FOOT_X / 2 + 1, 2, FOOT_H + 1)

    piston = cyl(PI_D, PI_L, 0, 0, FOOT_H)
    piston = piston - cyl(10.2, 20, 0, 0, FOOT_H + PI_L - 20 + 0.01)      # spring pocket
    piston = piston - cyl_y(2.6, PI_D / 2 + 1, 0, 0, FOOT_H + PI_PEG_Z)     # M3 peg (self-tapping)
    # top chamfer
    piston = piston - (cyl(PI_D + 2, 2, 0, 0, FOOT_H + PI_L - 1.2) - cyl(PI_D - 1.6, 2, 0, 0, FOOT_H + PI_L - 1.2, d2=PI_D + 1.6))
    return foot + piston


# ---------------------------------------------------------------- export
def to_trimesh(m):
    mesh = m.to_mesh()
    t = trimesh.Trimesh(vertices=np.asarray(mesh.vert_properties)[:, :3],
                        faces=np.asarray(mesh.tri_verts), process=True)
    return t


def build():
    parts = {
        "base_body": base_body(),
        "base_plate": base_plate(),
        "cassette": cassette(),
        "sampler_sleeve": sampler_sleeve(),
        "sampler_piston": sampler_piston(),
    }
    return {k: to_trimesh(v) for k, v in parts.items()}


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    # print orientation: base body upside down (top on the bed), sleeve cap-down
    flip = {"base_body": [180, 0, 0], "sampler_sleeve": [180, 0, 0]}
    for name, m in {
        "base_body": base_body(), "base_plate": base_plate(), "cassette": cassette(),
        "sampler_sleeve": sampler_sleeve(), "sampler_piston": sampler_piston(),
    }.items():
        if name in flip:
            m = m.rotate(flip[name])
        b = m.bounding_box()
        m = m.translate([-b[0], -b[1], -b[2]])
        t = to_trimesh(m)
        t.export(os.path.join(OUT, f"{name}.stl"))
        ext = t.bounds[1] - t.bounds[0]
        print(f"{name:16s} watertight={t.is_watertight} tris={len(t.faces):6d} "
              f"size={ext[0]:.1f} x {ext[1]:.1f} x {ext[2]:.1f} mm vol={t.volume/1000:.1f} cm3")
