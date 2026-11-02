# Blotly – hardvér (3D model)

Parametrický model merača mastnoty vlasov **Blotly** (všetky rozmery v mm).

| Súbor | Obsah |
|---|---|
| `model.py` | parametrický model (Python: `manifold3d`, `trimesh`, `numpy`) |
| `stl/` | diely pripravené na 3D tlač (základ a kazeta v čiernom filamente) |
| `glb/` | 3D náhľady: `blotly-assembled.glb` (zostava), `blotly-exploded.glb` (rozloženie) |

## Generovanie STL
```bash
pip install manifold3d trimesh numpy
python model.py
```
Výstup sa uloží do `stl/`.

## Známe úpravy (TODO)
- Model počíta s TSL2591, nákupný zoznam s BH1750 (21×16 mm) – rozšíriť vrecko pre senzor.
- Doplniť čiapočku tlačidla.
- Prispôsobiť dĺžku pružiny (0,8×8,3×60 mm).
