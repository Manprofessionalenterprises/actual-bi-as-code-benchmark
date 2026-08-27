# 📊 Spécification du Dashboard Exécutif COMEX (Rendu Lightdash)

Ce document décrit le **Maquettage et le Rendu Visuel Exact** du Tableau de Bord de Pilotage Exécutif destiné au COMEX / CODIR du Groupe Actual sur **Lightdash**, connecté à Snowflake.

---

## 🎯 Ce que le COMEX veut voir en priorité (Vision 360°)

Le COMEX d'un groupe d'intérim gère la performance de **22 agences régionales** (ou 600+ en cible) autour de **4 indicateurs clés de rentabilité** :

1. **Le Chiffre d'Affaires Groupe (€)** : Mesure de la croissance brute.
2. **La Marge Brute (€ et %)** : Rentabilité nette après paie des intérimaires.
3. **Le Volume d'Heures Facturées** : Mesure de l'activité réelle sur le terrain.
4. **Le Nombre de Placements Actifs** : Volume d'intérimaires délégués chez les clients.

---

## 📐 Layout & Agencement Visuel du Dashboard Lightdash

```
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│ 🏢 GROUPE ACTUAL — DASHBOARD DE PILOTAGE STRATÉGIQUE COMEX                             │
├───────────────┬─────────────────┬──────────────────┬──────────────────┬─────────────────┤
│ CA Total      │ Marge Brute     │ Taux de Marge    │ Total Heures     │ Placements      │
│ 1 450 000 €   │   320 500 €     │     22,1 %       │   65 400 hrs     │    3 500        │
├───────────────┴─────────────────┴──────────────────┴──────────────────┴─────────────────┤
│                                                                                         │
│  [ GRAPHIQUE 1 : Bar Chart ]                                                           │
│  Chiffre d'Affaires & Marge Brute par Agence (Top 22 Agences du Réseau)                │
│  ┌───────────────────────────────────────────────────────────────────────────────────┐  │
│  │ Agence Paris Ouest  ██████████████████████████████ (240k€ | Marge: 52k€)         │  │
│  │ Agence Lyon Centre  ██████████████████████ (180k€ | Marge: 41k€)                 │  │
│  │ Agence Marseille    ██████████████████ (150k€ | Marge: 33k€)                     │  │
│  │ Agence Bordeaux     ███████████████ (120k€ | Marge: 27k€)                         │  │
│  └───────────────────────────────────────────────────────────────────────────────────┘  │
│                                                                                         │
├───────────────────────────────────────────┬─────────────────────────────────────────────┤
│  [ GRAPHIQUE 2 : Donut Chart ]            │  [ GRAPHIQUE 3 : Scatter Plot ]             │
│  Répartition du CA par Secteur Client     │  Analyse Rentabilité Clients (Marge vs CA)  │
│  • BTP / Bâtiment (35%)                   │  (Repérer les clients à forte marge vs      │
│  • Logistique / Transport (25%)           │   les grands comptes à faible marge)        │
│  • Industrie / Agro (20%)                 │                                             │
│  • Tertiaire & Services (15%)             │                                             │
│  • Santé & Médical (5%)                   │                                             │
├───────────────────────────────────────────┴─────────────────────────────────────────────┤
│  [ TABLEAU 4 : Top 10 Agences Performantes & Taux d'Objectif ]                           │
│  ┌────────────────────┬──────────────┬──────────────┬───────────────┬────────────────┐  │
│  │ Agence             │ Région       │ CA Réalisé   │ Objectif CA   │ % Réalisation  │  │
│  ├────────────────────┼──────────────┼──────────────┼───────────────┼────────────────┤  │
│  │ Agence Paris Ouest │ Île-de-France│   240 000 €  │   220 000 €   │    109 % 🟢    │  │
│  │ Agence Lyon Centre │ AURA         │   180 000 €  │   175 000 €   │    103 % 🟢    │  │
│  │ Agence Marseille   │ PACA         │   150 000 €  │   160 000 €   │     94 % 🟡    │  │
│  └────────────────────┴──────────────┴──────────────┴───────────────┴────────────────┘  │
└─────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 🛠️ Configuration des 4 Widgets clés dans Lightdash

### Widget 1 : Les 4 KPI Cards (En-tête)
* **Source dbt** : `BENCHMARK_DB.ANALYTICS.FCT_PLACEMENTS`
* **Métriques configurées dans `schema.yml`** :
  * `total_chiffre_affaires` (format: EUR, couleur: Bleu)
  * `total_marge_brute` (format: EUR, couleur: Vert)
  * `total_heures` (format: Number)
  * `nombre_placements` (format: Count)

### Widget 2 : Performance des 22 Agences du Réseau (Bar Chart)
* **Dimension X** : `nom_agence`
* **Métriques Y** : `total_chiffre_affaires` (Stacked ou Side-by-side avec `total_marge_brute`)
* **Tris** : Ordonné par `total_chiffre_affaires` décroissant.
* **Agences représentées** : Les **22 agences** réparties sur 5 régions (Île-de-France, AURA, PACA, Nouvelle-Aquitaine, Occitanie).

### Widget 3 : Répartition par Secteur Client (Donut Chart)
* **Dimension** : `client_secteur` (BTP, Logistique, Industrie, Tertiaire, Santé)
* **Métrique** : `total_chiffre_affaires`
* **Légende** : Pourcentage du CA global Groupe.

### Widget 4 : Tableau d'Arbitrage Comex (DataTable)
* **Dimensions** : `nom_agence`, `agence_region`, `directeur`
* **Métriques** : `chiffre_affaires_total`, `objectifs_ca_annuel`, `% réalisation`
* **Formatage conditionnel** :
  * 🟢 Vert si % Réalisation ≥ 100%
  * 🟡 Jaune si % Réalisation entre 90% et 99%
  * 🔴 Rouge si % Réalisation < 90%

---

## 🤖 Interaction avec l'IA Lightdash (Aurora)

Lorsque le COMEX consulte ce tableau de bord, il peut utiliser **Aurora AI** avec des questions naturelles :

1. *"Affiche-moi le Top 3 des agences les plus rentables en région Île-de-France."*
2. *"Quelle est la marge brute moyenne sur le secteur BTP par rapport au secteur Logistique ?"*
3. *"Quelles agences sont en dessous de 90% de leur objectif annuel ?"*

Aurora lit directement les définitions du fichier `schema.yml` de dbt et génère la visualisation sous 2 secondes.
