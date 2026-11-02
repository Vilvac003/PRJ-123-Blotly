---
# 🧩 Versioning – systém dopĺňa automaticky
fm_version: "1.0.1"

# Dátum buildu – generuje skript
fm_build: "2026-11-02T15:50:53.603472+00:00"

# Poznámka k verzii – voliteľné
fm_version_comment: ""


# 🆔 IDENTITY --------------------------------------------------------

# ID generuje CLI / skript

# Unikátne UUID – generuje skript
guid: "6d8a3f49-520f-4139-a2b7-3708d33e7091"


# 🧭 CONTEXT ---------------------------------------------------------

# DAO / doména (knife, sdlc, q12, 7ds...) dopĺňa skript
dao: "sthdf"

# Názov zápisu – dopĺňa používateľ
title: "knowledge contribution"

# Krátky popis – dopĺňa používateľ (voliteľné)
description: "Optické meranie mastnoty vlasov cez presvitanie papierika (KNIFE)"


# 👥 AUTHORSHIP ------------------------------------------------------

# Hlavný autor – z globálneho configu
author: "Viliam Vachan"

# Zoznam autorov – generuje skript
authors:
  - "Viliam Vachan"


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
tags: ["knife","optical-sensing","esp32","3d-printing","intermediate"]


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

# 📚 Knowledge Contribution

Toto deliverable je v systéme reprezentované ako **KNIFE** — samostatný
príspevok so štandardnou KNIFE štruktúrou (účel, princíp, aplikácia,
detailný článok, tipy, hodnota).

## 🔖 Názov a stručný popis
- **Téma:** Optické meranie mastnoty vlasov cez presvitanie zmatňujúceho papierika.
- **Prečo je dôležitá:** Mastnotu vlasov a pokožky hlavy dnes ľudia posudzujú „od oka“. Profesionálne prístroje (napr. Sebumeter SM 815) sú pre bežného človeka drahé. Rovnaký princíp sa dá postaviť lacno z bežných súčiastok.

## 🎯 Čo rieši (účel, cieľ)
Ukázať, ako z lacného svetelného senzora, LED a zmatňujúceho papierika vyrobiť merač, ktorý číselne vyjadrí, koľko mazu (sebum) sa odobralo z vlasov alebo pokožky.

## 🧩 Ako to rieši (princíp)
Čistý zmatňujúci papierik je takmer nepriehľadný. Keď nasaje maz, stane sa **priesvitným**. Ak ho presvietime LED a za ním meriame intenzitu svetla, platí: **viac mazu = viac prejdeného svetla**. Zmeraná hodnota sa prepočíta na úroveň mastnoty.

## 🧪 Ako to použiť (aplikácia)
1. Zmerať **referenčnú hodnotu** čistého papierika (nulová mastnota).
2. Papierik v kazete pritlačiť na vlasy/pokožku hlavy (pružinový odberník zabezpečí vždy rovnaký tlak).
3. Kazetu vsunúť do meracieho tunela a zmerať prejdené svetlo.
4. Rozdiel oproti referencii prepočítať na úroveň (suché / normálne / mastné).

---

## ⚡ Rýchly návod (Top)
- Biela LED nad papierikom, svetelný senzor pod ním, všetko v **svetlotesnej** (čiernej) skrinke.
- Meraj vždy pri rovnakom prúde LED a rovnakej vzdialenosti.
- Pred každým meraním odpočítaj referenciu čistého papierika.

## 📜 Detailný článok
**Súčiastky prototypu Blotly:** ESP32-C3 SuperMini, digitálny svetelný senzor (I²C), biela LED spínaná tranzistorom 2N2222, OLED displej 0,96″ (I²C), tlačidlo, kazeta a pružinový odberník z 3D tlače.

**Prečo svetlotesná skrinka:** Okolité svetlo by zmenilo meranie. Skrinka a kazeta sa preto tlačia z čierneho filamentu a papierik sa presvecuje v úzkom tuneli, aby do senzora išlo len svetlo z vlastnej LED.

**Prečo pružina:** Hodnota závisí od toho, koľko mazu papierik nasaje. Konštantný tlak pri odbere robí merania porovnateľné.

**Alternatívy, ktoré sme zvažovali:** kapacitné/odporové meranie priamo na pokožke (rušia ho pot a vlhkosť) a kamera s mikroskopom a spracovaním obrazu (náročnejší softvér). Optická metóda s papierikom bola vybraná ako najspoľahlivejšia na samotný tuk.

## 💡 Tipy a poznámky
- Pri stabilnom meraní pomáha spriemerovať viac odčítaní senzora.
- Prototyp je učebný nástroj, **nenahrádza klinický prístroj**.
- Zatiaľ nie je overená presnosť ani kalibrácia voči referenčnému prístroju (pozri Project Outcomes).

## ✅ Hodnota / Zhrnutie
Princíp profesionálneho sebumetra sa dá zopakovať lacno a otvorene. Čitateľ získa princíp, zoznam súčiastok a 3D model skrinky.

## 🗂️ Taxonómia KNIFE
- **Kategória:** Hardvér, meranie, DIY
- **Typ:** návod / prípadová štúdia
- **Tagy:** optické meranie, sebum, ESP32, 3D tlač, open-source

## 🌍 Referencie
- Sebumeter SM 815 (Courage + Khazaka) – profesionálny prístroj s rovnakým princípom
- Delfin Technologies – SebumScale
- Repozitár projektu: [https://github.com/Vilvac003/PRJ-123-Blotly](https://github.com/Vilvac003/PRJ-123-Blotly)

## Navigácia
- [↩️ Späť](../index.md)
