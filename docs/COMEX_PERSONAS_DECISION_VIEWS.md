# 👔 Cartographie des Personnalités du COMEX & Vues Métiers Alignées

Ce document analyse avec **réalisme et pragmatisme** la maturité du Groupe Actual en 2026, la psychologie des différents membres du COMEX, et la réponse décisionnelle apportée par l'architecture **Snowflake + dbt + Lightdash / Evidence**.

---

## 🏛️ 1. Le Constat Réaliste 2026 : Où en est le Groupe Actual ?

Le Groupe Actual est un **acteur majeur du travail temporaire en France** (plus de 600 agences, des milliers de collaborateurs). Leurs équipes sont hautement qualifiées et organisées.

* **Ce qu'ils ont DEJÀ aujourd'hui** : Des tableaux de bord fonctionnels (Power BI, Tableau ou rapports consolidés mensuellement).
* **Leur VRAI défi en 2026 (La raison de la mission)** :
  1. **Les délais de consolidation** : Les rapports mensuels nécessitent du temps d'ingénierie pour agréger la paie et la facturation.
  2. **Le besoin d'instantanéité (Fast Insights)** : Les décideurs veulent interroger les données en temps réel sans attendre le rapport de fin de mois.
  3. **L'Adoption de l'IA Décisionnelle** : Permettre au COMEX de poser des questions spontanées en français (Text-to-SQL avec Lightdash Aurora) sur une couche sémantique dbt fiable.

---

## 👥 2. Matrice des Personnalités du COMEX & Attentes par Profil

Le COMEX n'est pas un bloc homogène. Chaque dirigeant aborde la donnée sous un angle spécifique :

```
┌──────────────────────────────────────────────────────────────────────────────────────────┐
│                   PERSONNAS DU COMEX & VUES DÉCISIONNELLES SUR-MESURE                     │
├───────────────────────┬──────────────────────────┬───────────────────────────────────────┤
│ DIRIGEANT / PERSONNA  │ PRIORITÉ PSYCHOLOGIQUE   │ VUE DU DASHBOARD REQUIS               │
├───────────────────────┼──────────────────────────┼───────────────────────────────────────┤
│ 1. Direction Générale │ Vision Macro 360°,      │ Vue Synthétique Groupe                │
│    (CEO / DG)         │ Croissance & Réputation  │ (CA, Marge Globale, 4 KPIs Macros)    │
├───────────────────────┼──────────────────────────┼───────────────────────────────────────┤
│ 2. Direction Financière│ Rigueur Comptable,       │ Vue Rentabilité & Marge Brute         │
│    (CFO / DAF)        │ Marge & Risque Client    │ (Marge/Secteur, Coût Paie, Encouours) │
├───────────────────────┼──────────────────────────┼───────────────────────────────────────┤
│ 3. Direction Réseau   │ Performance Terrain,     │ Vue Réseau & Ranking Agences          │
│    (COO / Dir. Ops)   │ Objectifs des Agences    │ (22/600 Agences, % Objectif Annuel)   │
├───────────────────────┼──────────────────────────┼───────────────────────────────────────┤
│ 4. Direction RH       │ Sourcing Intérimaires,   │ Vue Capital Humain & Métiers          │
│    (CHRO / DRH)       │ Placements & Heures      │ (Volume Heures, Tension Métiers)      │
├───────────────────────┼──────────────────────────┼───────────────────────────────────────┤
│ 5. Direction Data/DSI │ Sécurité, Performance    │ Vue Architecture & Gouvernance dbt    │
│    (CTO / DSI)        │ Cloud & Zéro Dette Tech  │ (Lineage dbt, RLS/RBAC, Auto-Suspend) │
└───────────────────────┴──────────────────────────┴───────────────────────────────────────┘
```

---

### 👤 1. Le Chief Executive Officer (CEO / Direction Générale)
* **Sa préoccupation majeure** : Avoir une vision synthétique claire de la santé du groupe en 1 minute.
* **Ce qu'il cherche dans le Dashboard** :
  * **La Vue Unifiée 360°** : Les 4 KPI Cards globales (CA Groupe, Marge Brute Groupe %, Total Heures, Total Placements).
  * La tendance globale d'atterrissage sur l'année.
* **Son usage de l'IA Aurora** : *"Quel est l'atterrissage du CA estimé pour le trimestre en cours ?"*

---

### 👤 2. Le Chief Financial Officer (CFO / Directeur Financier)
* **Sa préoccupation majeure** : Garantir la rentabilité opérationnelle et maîtriser la masse salariale des intérimaires.
* **Ce qu'il cherche dans le Dashboard** :
  * **La Vue Finance & Rentabilité** : La Marge Brute (€) nette après calcul de la paie (`cout_paie`).
  * Le Scatter Plot de Rentabilité Client (isoler les grands comptes à faible marge).
* **Son usage de l'IA Aurora** : *"Donne-moi le TOP 5 des clients qui génèrent moins de 12% de marge brute."*

---

### 👤 3. Le Chief Operating Officer (COO / Directeur du Réseau d'Agences)
* **Sa préoccupation majeure** : Animer et challenger les directeurs régionaux et responsables d'agences.
* **Ce qu'il cherche dans le Dashboard** :
  * **La Vue Réseau & Ranking** : Le classement des 22 agences pilotes avec leur taux de réalisation des objectifs (`objectifs_ca_annuel`).
  * La carte thermique de performance par région (Île-de-France, AURA, PACA, etc.).
* **Son usage de l'IA Aurora** : *"Quelles agences de la région PACA sont en retard sur leurs objectifs du mois ?"*

---

### 👤 4. Le Chief Human Resources Officer (CHRO / Directeur RH & Talent)
* **Sa préoccupation majeure** : Répondre à la pénurie de candidats et maximiser le volume d'heures déléguées.
* **Ce qu'il cherche dans le Dashboard** :
  * **La Vue Capital Humain** : Le nombre d'intérimaires placés et le volume d'heures travaillées par secteur (BTP, Logistique, Tertiaire).
  * L'analyse des métiers les plus demandés.
* **Son usage de l'IA Aurora** : *"Quel est le volume d'heures réalisées dans le secteur BTP ce mois-ci ?"*

---

### 👤 5. Le Chief Technology Officer / DSI (CTO / Directeur Data - Édouard Bardet / Pierre Comalada)
* **Sa préoccupation majeure** : Sécurité des données, maintenabilité du code (BI-as-Code) et maîtrise des coûts Snowflake.
* **Ce qu'il cherche dans la Solution** :
  * **Le Socle Technique dbt + Snowflake** : Des modèles dbt réutilisables, un versionning 100% Git et le contrôle des coûts Snowflake (`AUTO_SUSPEND = 60s`).
  * La gouvernance par rôle (RBAC/RLS).

---

## 🤝 3. Comment la Solution Unifiée Réconcilie Tout le Monde ?

Au lieu de créer 5 outils différents, l'architecture **Snowflake + dbt + Lightdash / Evidence** offre :

1. **Une Source Unique de Vérité (Single Source of Truth)** : Les métriques sont calculées une seule fois dans dbt (`schema.yml`).
2. **Un Dashboard Unifié avec Onglets Métiers** : Un seul tableau de bord COMEX avec 4 onglets dédiés (*Vue 360°*, *Vue Finance*, *Vue Réseau*, *Vue RH*).
3. **L'Autonomie IA pour Chaque Profil** : Chaque membre du COMEX peut interroger les données selon ses propres mots grâce à Lightdash Aurora.
