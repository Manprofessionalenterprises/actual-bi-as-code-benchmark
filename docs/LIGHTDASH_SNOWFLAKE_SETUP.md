# ⚡ Guide d'Intégration Lightdash + Snowflake + dbt

Ce guide explique étape par étape comment connecter **Lightdash** (la solution BI nativement intégrée à dbt) avec votre Data Warehouse **Snowflake**.

---

## 🏗️ Architecture Lightdash & dbt

Lightdash utilise directement les métadonnées et la couche sémantique de **dbt** (fichiers `schema.yml` et modèles `.sql`) pour générer automatiquement l'interface d'exploration BI sans dupliquer la modélisation.

```
[ Snowflake (BENCHMARK_DB.ANALYTICS) ]
                   │
                   ▼
       [ dbt Core / schema.yml ]
                   │
                   ▼
             [ Lightdash ]
 (BI native dbt, Dashboards, Exploration)
```

---

## Étape 1 : Inscription à Lightdash Cloud (ou Self-Hosted)

1. Rendez-vous sur [app.lightdash.cloud](https://app.lightdash.cloud/) (ou votre instance locale Lightdash Docker).
2. Créez votre compte ou connectez-vous.
3. Lors de la création d'un nouveau projet, sélectionnez **Snowflake** comme Data Warehouse.

---

## Étape 2 : Configuration de la Connexion Snowflake dans Lightdash

Remplissez le formulaire de connexion de Lightdash avec vos paramètres Snowflake :

* **Type** : `Snowflake`
* **Account** : `SLPMQMD-DX08347`
* **User** : `LICALLMAN110` (ou `BENCHMARK_USER`)
* **Password** : `testSnowflake2026*`
* **Warehouse** : `COMPUTE_WH`
* **Database** : `BENCHMARK_DB`
* **Schema** : `ANALYTICS`
* **Role** : `ACCOUNTADMIN` (ou `BENCHMARK_ROLE`)

Cliquez sur **Test Connection** pour valider la connexion réseau.

---

## Étape 3 : Connexion au Projet dbt (GitHub / GitLab)

Pour que Lightdash génère vos vues d'exploration BI :

1. Dans la section **dbt Connection**, choisissez **GitHub**.
2. Sélectionnez votre dépôt GitHub : `Manprofessionalenterprises/Meta-Agent-full-architect`.
3. Indiquez le chemin vers votre projet dbt : `actual_bi_as_code_benchmark/dbt_project`.
4. Indiquez la branche : `main`.

Lightdash va lire automatiquement le fichier `dbt_project.yml` et les fichiers `schema.yml` dans `models/marts/` pour construire votre catalogue de métriques.

---

## Étape 4 : Déploiement via CLI Lightdash (Alternative Locale)

Si vous préférez tester Lightdash directement en ligne de commande depuis votre Mac :

```bash
# 1. Installer le CLI Lightdash
npm install -g @lightdash/cli

# 2. Se connecter à votre instance Lightdash
lightdash login https://app.lightdash.cloud

# 3. Prévisualiser vos tableaux de bord dbt
cd actual_bi_as_code_benchmark/dbt_project
lightdash start
```

---

## 📊 Exploration dans Lightdash

Une fois la connexion établie :
1. Les modèles marts (ex: `fct_placements`, `dim_agences`, `dim_clients`) apparaissent automatiquement sous forme d'**Explores**.
2. Vous pouvez créer des graphiques en glisser-déposer basés sur les colonnes et métriques définies dans vos `schema.yml`.
3. Sauvegardez vos graphiques dans un **Dashboard BI**.
