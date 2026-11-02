---
# 🧩 Versioning – systém dopĺňa automaticky
fm_version: "1.0.1"

# Dátum buildu – generuje skript
fm_build: "2026-11-02T15:50:52.521783+00:00"

# Poznámka k verzii – voliteľné
fm_version_comment: ""


# 🆔 IDENTITY --------------------------------------------------------

# ID generuje CLI / skript

# Unikátne UUID – generuje skript
guid: "5846621d-f557-4001-977e-8ff1a3f78bd3"


# 🧭 CONTEXT ---------------------------------------------------------

# DAO / doména (knife, sdlc, q12, 7ds...) dopĺňa skript
dao: "sthdf"

# Názov zápisu – dopĺňa používateľ
title: "feasibility study"

# Krátky popis – dopĺňa používateľ (voliteľné)
description: "Štúdia uskutočniteľnosti Blotly"


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

# 🧪 Feasibility Study

## Porovnanie princípov

| Princíp | Náročnosť | Presnosť | Spotrebný materiál |
|---------|-----------|----------|--------------------|
| **Optický** (papierik + LED + senzor) | stredná | vysoká | áno |
| Kapacitný / odporový | nízka | nízka až stredná, ruší ho pot | nie |
| Kamerový + softvér | vysoká | stredná | nie |

**Rozhodnutie:** optický princíp, rovnaký ako pri profesionálnom Sebumetri.

## Orientačné náklady
Optická verzia vychádza podľa prieskumu na približne 12 až 15 € za základné diely. S 3D tlačou, OLED displejom a ďalšími položkami spolu okolo ~30 €.

## Riziká

| Riziko | Dopad | Riešenie |
|--------|-------|----------|
| rozptýlené svetlo | skreslené meranie | čierna svetlotesná skrinka |
| nestabilná LED | nepresné hodnoty | spínanie tranzistorom, rezistory |
| rôzne papieriky | rôzna priepustnosť | referencia pre konkrétny typ |
| nedostupnosť dielov | oneskorenie | náhradné zdroje, záložný ESP32 |
| neznáma presnosť | nízka dôveryhodnosť | kalibrácia, porovnanie s referenciou |

---
**Navigation:** [⬆️ Up](./index.md) · [🏠 Home](../index.md)
