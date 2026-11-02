---
# 🧩 Versioning – systém dopĺňa automaticky
fm_version: "1.0.1"

# Dátum buildu – generuje skript
fm_build: "2026-11-02T15:50:53.700639+00:00"

# Poznámka k verzii – voliteľné
fm_version_comment: ""


# 🆔 IDENTITY --------------------------------------------------------

# ID generuje CLI / skript

# Unikátne UUID – generuje skript
guid: "1cb3eba0-e6fa-44ea-8cd5-3ad23a8c5601"


# 🧭 CONTEXT ---------------------------------------------------------

# DAO / doména (knife, sdlc, q12, 7ds...) dopĺňa skript
dao: "sthdf"

# Názov zápisu – dopĺňa používateľ
title: "project summary"

# Krátky popis – dopĺňa používateľ (voliteľné)
description: "Blotly – otvorený merač mastnoty vlasov a pokožky hlavy"


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
tags: ["sthdf","blotly","esp32","3d-printing"]


# 🌍 LOCALIZATION -----------------------------------------------------

# Jazyk dokumentu – doplní skript podľa štruktúry
locale: "sk"


# 🕒 LIFECYCLE --------------------------------------------------------

# Dátum vytvorenia – generuje skript
created: "2026-11-02 16:50"

# Dátum poslednej úpravy – dopĺňa človek
modified: "2026-11-02 17:30"

# Stav dokumentu – default "backlog"
status: "in-progress"

# Viditeľnosť – default "public"
privacy: "public"


# ⚖ INTELLECTUAL PROPERTY -------------------------------------------

# Držiteľ práv k obsahu – dopĺňa skript
rights_holder_content: "Viliam Vachan"

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

# 📝 Project Summary

## 🔖 Identifikácia
## 1️⃣ Názov projektu
- **Názov projektu:** `PRJ_123_Blotly_ST039_ST048`
- **Stručný popis:** **Blotly** je otvorený merač mastnoty vlasov a pokožky hlavy. Zmatňujúci papierik nasaje maz, LED ho presvieti a svetelný senzor zmeria, koľko svetla prešlo. Výsledok sa zobrazí na OLED displeji. Skrinku a odberník si používateľ vytlačí na 3D tlačiarni.

## 2️⃣ Členovia tímu

| ST ID | Meno | Rola v tíme | Kompetencie |
|-------|------|-------------|-------------|
| ST039 | Tomáš Majerník | TODO – rola | TODO |
| ST048 | Viliam Vachan | TODO – rola (vývoj, 3D model, hardvér) | 3D modelovanie, hardvér, dokumentácia |

*(Rozdelenie rolí a kompetencií doplniť spolu s Tomášom.)*

## 3️⃣ Motivácia tímu
- Mastnotu vlasov dnes posudzujeme od oka, čo vedie k zbytočnému častému umývaniu alebo k nevhodnej starostlivosti.
- Profesionálne prístroje sú pre bežného človeka drahé a nedostupné.
- Projekt spája elektroniku, 3D tlač a návrh produktu, takže je vhodný na učenie.
- TODO – doplniť osobnú motiváciu

## 4️⃣ Cieľ a pridaná hodnota projektu
- **Finálny cieľ:** funkčný prototyp, ktorý zmeria úroveň mastnoty, a otvorený návod s 3D modelmi a kódom.
- **Úspech spoznáme, keď:** zariadenie dáva opakovateľné hodnoty pre čistý a mastný papierik a dá sa podľa návodu postaviť z bežne dostupných súčiastok.
- **Pridaná hodnota:** výrazne nižšia cena než profesionálne prístroje (orientačne ~30 € za diely).

## 5️⃣ Popis riešenia
- **Riadenie:** ESP32-C3 SuperMini
- **Meranie:** biela LED (spínaná tranzistorom 2N2222) a digitálny svetelný senzor (I²C) pod meraným papierikom
- **Zobrazenie:** OLED 0,96″ 128×64, tlačidlo na spustenie merania
- **Mechanika:** skrinka s optickým tunelom (95×60×34 mm), kazeta s papierikom, pružinový odberník vzorky; všetko z 3D tlače (čierny PLA/PETG)
- **Model:** parametrický Python skript [`hardware/model.py`](https://github.com/Vilvac003/PRJ-123-Blotly/blob/main/hardware/model.py)

## 6️⃣ Projektový plán
- Odhadovaný čas na prácu: TODO x hodín / týždeň
- Predpokladaný stav v čase prezentácie: **funkčný prototyp**
- Hlavné míľniky:
  - [x] Príprava (výber princípu, 3D model, zoznam súčiastok)
  - [ ] Implementácia (objednanie dielov, tlač, zostavenie, firmvér)
  - [ ] Testovanie (referencia, kalibrácia, opakovateľnosť)
  - [ ] Prezentácia

### 📅 Míľniky a výstupy
- **Do januára dodáme:**
  - [ ] prototyp
  - [ ] prezentáciu
  - [ ] dokumentáciu

## 7️⃣ Zákazník a hodnoty
- **Používatelia:** ľudia, ktorí chcú vedieť, kedy vlasy naozaj potrebujú umyť; ľudia s mastnou alebo citlivou pokožkou hlavy; kaderníctva a štúdiá; kutilovia a študenti.
- **Prínos:** jasný číselný údaj namiesto odhadu, za zlomok ceny profesionálneho prístroja.

## 8️⃣ Očakávané výstupy
- **Dokumentácia:** README, KNIFE článok (Knowledge Contribution), návod na zostavenie
- **Artefakty:** funkčný prototyp, 3D modely (STL/GLB), firmvér, produktový plagát ([`poster/blotly.pdf`](https://github.com/Vilvac003/PRJ-123-Blotly/blob/main/poster/blotly.pdf))

## 📚 Kontext
- Sebumeter SM 815 (Courage + Khazaka), SebumScale (Delfin Technologies)
- Zmatňujúce papieriky (oil blotting papers) ako spotrebný materiál

## 🧭 Riziká a závislosti
- Meranie je citlivé na rozptýlené svetlo a nestálosť LED (riešenie: svetlotesná skrinka, stabilný prúd).
- Presnosť bez kalibrácie voči referenčnému prístroju nie je známa.
- Rôzne papieriky môžu mať rôznu priepustnosť (nutná referencia pre konkrétny typ).
- Dostupnosť súčiastok (niektoré položky boli vypredané, napr. OLED v Techfune).
- Presný typ senzora (TSL2591 / BH1750) treba zjednotiť s modelom.

## 9️⃣ Reflexia a ďalšie kroky
- Očakávame, že sa naučíme návrh optického merania, prácu s I²C senzormi a návrh dielov pre 3D tlač.
- Ďalší rozvoj: kalibrácia, ukladanie meraní, mobilná aplikácia, porovnanie s profesionálnym prístrojom.

---

## Navigácia
- [↩️ Späť](../index.md)
