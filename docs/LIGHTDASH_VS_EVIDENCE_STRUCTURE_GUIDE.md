# 📐 Structure de Visualisation : Fichiers Unifiés vs Vues Dédiées (Lightdash & Evidence)

Ce document explique **techniquement et visuellement** comment s'organisent les fichiers et les tableaux de bord entre **Lightdash** et **Evidence.dev** pour chaque membre du COMEX.

---

## 🔄 1. Le Principe d'Or : Socle Code Unifié + Restitutions Personnalisées

Quelle que soit la solution choisie, la règle d'architecture BI-as-Code est stricte :

```
                        ┌──────────────────────────────────────────┐
                        │   PROJET dbt CORE (Unifié & Git)         │
                        │   • fct_placements.sql                   │
                        │   • dim_agences.sql                      │
                        │   • schema.yml (Métriques officielles)   │
                        └────────────────────┬─────────────────────┘
                                             │
                       ┌─────────────────────┴─────────────────────┐
                       ▼                                           ▼
          ┌──────────────────────────┐               ┌──────────────────────────┐
          │  RESTITUTION LIGHTDASH   │               │   RESTITUTION EVIDENCE   │
          │  (Dashboard à Onglets /  │               │   (Fichiers .md dédiés   │
          │   Spaces par Rôle)       │               │    par page métier)      │
          └──────────────────────────┘               └──────────────────────────┘
```

---

## 📊 2. Organisation dans Lightdash (Interface Web)

Dans Lightdash, vous n'avez **PAS de duplication de code**. Vous avez deux manières d'organiser la restitution :

### Option A : Le Dashboard Unifié à Onglets (Recommandé pour le COMEX)
* **Nom du Dashboard** : `GROUPE ACTUAL — PILOTAGE STRATÉGIQUE COMEX`
* **Structure à Onglets (Tabs)** :
  * 📌 **Onglet 1 : `Vue 360° (CEO)`** : 4 KPI Cards macros (CA, Marge %, Heures, Placements).
  * 💰 **Onglet 2 : `Finance & Marge (CFO)`** : Marge brute par agence, coût de la paie, rentabilité client.
  * 🏢 **Onglet 3 : `Performance Réseau (COO)`** : Classement des 22/600 agences vs Objectifs annuels.
  * 👥 **Onglet 4 : `Sourcing & RH (CHRO)`** : Volumes d'heures et effectifs d'intérimaires délégués.

### Option B : Les Espaces Sécurisés par Rôle (Spaces & RBAC)
Si la Direction souhaitait restreindre l'accès à certaines données sensibles :
* **Espace "COMEX Exécutif"** : Dashboard Global réservé à la Direction Générale et Financière.
* **Espace "Direction Réseau"** : Dashboard Agences filtré dynamiquement selon la Région du Directeur via la sécurité RLS (Row-Level Security).

---

## 📝 3. Organisation dans Evidence.dev (Fichiers Git `.md`)

Dans Evidence.dev, l'organisation est **100% basée sur l'arborescence des fichiers Markdown** dans le projet Git :

```
evidence_actual/
├── pages/
│   ├── index.md        <-- Vue Synthétique COMEX (CEO)
│   ├── finance.md      <-- Vue Finance & Marge Brute (CFO)
│   ├── reseau.md       <-- Vue Ranking Agences & Régions (COO)
│   └── rh.md           <-- Vue Sourcing & Capital Humain (CHRO)
└── evidence.plugins.yaml
```

* **Comment l'utilisateur navigue ?**  
  Evidence génère automatiquement une barre de navigation latérale/supérieure fluide permettant de passer en < 100ms de `index.md` (Vue CEO) à `finance.md` (Vue CFO).

---

## 🎯 4. Synthèse Comparative

| Critère d'Architecture | **Lightdash** | **Evidence.dev** |
| :--- | :--- | :--- |
| **Gestion du Code SQL/dbt** | 1 seul fichier `schema.yml` centralisé | 1 fichier `schema.yml` + requêtes SQL dans chaque page `.md` |
| **Organisation UI** | 1 Dashboard à 4 Onglets Métiers ou Espaces ("Spaces") | 4 Fichiers `.md` dans le dossier `pages/` |
| **Sécurité d'Accès** | RLS / RBAC natif par rôle utilisateur | Filtrage au build ou authentification globale |
| **Avantage Principal** | L'IA Aurora fonctionne sur TOUS les onglets nativement | Versionning 100% Git de chaque page individuelle |
