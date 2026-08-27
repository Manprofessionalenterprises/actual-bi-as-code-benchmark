# PROGRESS — GROUPE ACTUAL BI AS CODE BENCHMARK

## 📅 Statut du Projet au 27 Août 2026

### 🚀 Dernières Actions Exécutées (Résolution Affichage Lightdash Cloud)

1. **Déploiement du Dashboard & Graphiques via CLI & API Lightdash Cloud** :
   - Génération des définitions YAML pour les 4 graphiques et le tableau de bord exécutif (`GROUPE ACTUAL — PILOTAGE STRATÉGIQUE COMEX`).
   - Déploiement automatisé via `lightdash upload --project c9e5a221-4b16-435b-97b3-c657eed1a28d --force`.

2. **Résolution de l'Erreur `Invalid cartesian chart config - no eCharts config` (Tuiles 1 & 3)** :
   - **Problème identifié** : L'interface React de Lightdash Cloud exigeait la structure complète `eChartsConfig.series` (avec encodage `xRef` et `yRef`) pour les cartes cartésiennes en histogramme (Bar Charts).
   - **Correction appliquée dans les fichiers YAML** :
     - `dbt_project/lightdash/spaces/shared/performance-par-agence.chart.yml`
     - `dbt_project/lightdash/spaces/shared/ca-par-region.chart.yml`
   - **Liaison des tuiles du Dashboard** :
     - Liaison des UUIDs réels du serveur via l'API REST (`data/fix_and_build_lightdash_dashboard.py`).

3. **Vérification Empirique Effectuée** :
   - Exécution du script de contrôle API (`data/verify_echarts_presence.py`) confirmant que le serveur Lightdash Cloud renvoie `HTTP 200 OK` avec les objets `eChartsConfig` validés.

---

### 📂 Fichiers Modifiés & Créés
- `dbt_project/lightdash/spaces/shared/performance-par-agence.chart.yml` : Ajout de la structure `eChartsConfig.series` pour l'agence.
- `dbt_project/lightdash/spaces/shared/ca-par-region.chart.yml` : Ajout de la structure `eChartsConfig.series` pour la région.
- `dbt_project/lightdash/spaces/shared/groupe-actual-pilotage-comex.dashboard.yml` : Configuration des tuiles avec liaisons des graphiques.
- `data/create_lightdash_as_code.py` : Script de création initiale du code Lightdash.
- `data/fix_and_build_lightdash_dashboard.py` : Script de liaison des UUIDs de tuiles via l'API REST.
- `data/upload_with_echarts_yml.py` : Script de régénération YAML avec `eChartsConfig`.
- `data/verify_echarts_presence.py` : Script de vérification de l'intégrité API.

---

### 🎯 Décisions Prises & Justifications Business
1. **Architecture Dashboard-as-Code** : Tout le contenu visuel Lightdash est versionné dans Git sous `dbt_project/lightdash/` pour assurer la reproductibilité sans clic manuel.
2. **Double Niveau d'Analyse (Agences vs Régions)** : Présentation des 22 agences pilotes croisées avec les 12 régions administratives pour répondre simultanément aux besoins du Comex et des directeurs régionaux.
3. **Sécurité RLS (Row-Level Security)** : Option B retenue pour le déploiement général, Option A (vue globale) pour le COMEX.

---

### ⏭️ Prochaines Étapes
1. **Enregistrement de la démo vidéo Loom (90s)** : Présentation de l'environnement Snowflake + Lightdash + Evidence.
2. **Envoi du courriel d'Outreach** à Kinga Ibanez (`kinga.ibanez@actualgroup.com`) et Pierre Comalada (`pierre.comalada@actualgroup.com`).
