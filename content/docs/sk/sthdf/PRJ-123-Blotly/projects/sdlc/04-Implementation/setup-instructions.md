---
# 🧩 Versioning – systém dopĺňa automaticky
fm_version: "1.0.1"

# Dátum buildu – generuje skript
fm_build: "2026-11-02T15:50:52.787470+00:00"

# Poznámka k verzii – voliteľné
fm_version_comment: ""


# 🆔 IDENTITY --------------------------------------------------------

# ID generuje CLI / skript

# Unikátne UUID – generuje skript
guid: "bee914cd-4633-4d0e-bddf-accf1115757f"


# 🧭 CONTEXT ---------------------------------------------------------

# DAO / doména (knife, sdlc, q12, 7ds...) dopĺňa skript
dao: "sthdf"

# Názov zápisu – dopĺňa používateľ
title: "setup instructions"

# Krátky popis – dopĺňa používateľ (voliteľné)
description: "Postup zostavenia Blotly"


# 👥 AUTHORSHIP ------------------------------------------------------

# Hlavný autor – z globálneho configu
author: "Viliam Vachan"

# Zoznam autorov – generuje skript
authors:
  - "Viliam Vachan"
  - "Tomáš Majerník"


# 🗂 CLASSIFICATION ---------------------------------------------------

# Nadradená kategória – môže doplniť používateľ
category: ""

# Typ dokumentu (guide, case, tutorial...) – používateľ (voliteľné)
type: ""

# Priorita (low/medium/high) – voliteľné
priority: ""

# Tagy – odporúča sa 2–6 tagov.
# Typy tagov:
#   - rámce: knife, 7ds, sdlc, q12
#   - účel: tutorial, guide, pattern, case-study
#   - téma: git, backup, ai, communication
#   - úroveň: beginner, intermediate, advanced
tags: []


# 🌍 LOCALIZATION -----------------------------------------------------

# Jazyk dokumentu – doplní skript podľa štruktúry
locale: "sk"


# 🕒 LIFECYCLE --------------------------------------------------------

# Dátum vytvorenia – generuje skript
created: "2026-11-02 16:50"

# Dátum poslednej úpravy – dopĺňa človek
modified: "2026-11-02 18:30"

# Stav dokumentu – default "backlog"
status: "in-progress"

# Viditeľnosť – default "public"
privacy: "public"


# ⚖ INTELLECTUAL PROPERTY -------------------------------------------

# Držiteľ práv k obsahu – dopĺňa skript
rights_holder_content: "Viliam Vachan, Tomáš Majerník"

# Systémový vlastník práv
rights_holder_system: "CAA / KNIFE / LetItGrow"

# Licencia
license: "CC-BY-NC-SA-4.0"

# Disclaimer
disclaimer: "Use at your own risk. Methods provided as-is; participation is voluntary and context-aware."

# Copyright
copyright: "© 2025 Roman Kazicka"


# 🔗 ORIGIN / PROVENANCE ---------------------------------------------

# Repozitár pôvodu
origin_repo: ""

# URL pôvodného repozitára
origin_repo_url: ""

# Commit pôvodu
origin_commit: ""

# Branch pôvodu
origin_branch: ""

# Systém pôvodu (CAA/KNIFE/STHDF…)
origin_system: "CAA"

# Pôvodný autor
origin_author: "Roman Kazicka"

# Importovaný zdroj
origin_imported_from: ""

# Dátum importu
origin_import_date: ""


# 🧱 RESERVED ---------------------------------------------------------

fm_reserved1: ""
fm_reserved2: ""
---

<!-- SDLC_INSTANCE_ID: PRJ-123-Blotly -->

# ⚙️ Setup Instructions

## 1. Vygenerovanie modelov (voliteľné)
```bash
pip install manifold3d trimesh numpy
python hardware/model.py
```
Hotové STL sú aj priamo v [`hardware/stl`](https://github.com/Vilvac003/PRJ-123-Blotly/tree/main/hardware/stl).

## 2. Tlač
- Materiál PLA alebo PETG, vrstva 0,2 mm.
- `base_body` a `cassette` tlačte **čiernym** filamentom.
- `base_body` tlačte hore nohami, `sampler_sleeve` čiapočkou nadol a `sampler_piston` pätou nadol.

## 3. Zostavenie
1. Vložte svetelný senzor do vrecka pod optickým tunelom a LED do vývrtu nad tunelom.
2. Zapojte LED cez tranzistor podľa [schémy](../03-Design/architecture-diagram.md).
3. Pripojte OLED a senzor na spoločnú I²C zbernicu.
4. Osaďte tlačidlo a stavovú LED.
5. Uzatvorte veko 4 skrutkami M3×8.
6. Do odberníka vložte pružinu a zaistite piest čapom (skrutka M3).

## 4. Firmvér
TODO

---
**Navigation:** [⬆️ Up](./index.md) · [🏠 Home](../index.md)
