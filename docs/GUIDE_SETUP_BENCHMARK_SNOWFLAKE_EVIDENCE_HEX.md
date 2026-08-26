# 🚀 Guide Complet d'Installation & Configuration : Snowflake, dbt, Evidence.dev & Hex.tech

Ce document récapitule l'ensemble de la procédure pas-à-pas pour monter et exécuter le **Benchmark BI-as-Code** (`actual_bi_as_code_benchmark`).

---

## 🏗️ Architecture Globale du Projet

```
[ Données CSV (data/*.csv) ]
          │
          ▼  (upload_to_snowflake.py)
[ Snowflake : BENCHMARK_DB.RAW ]
          │
          ▼  (dbt_project)
[ Snowflake : BENCHMARK_DB.ANALYTICS ]
          │
  ┌───────┴───────────────────────┐
  ▼                               ▼
[ Evidence.dev ]              [ Hex.tech ]
(BI-as-Code Local, .md)     (Cloud Notebook & App)
```

---

## Étape 1 : Inscription & Configuration du Compte Snowflake

### 1.1 Inscription à l'Essai Gratuit (Free Trial 400$)
Rendez-vous sur [signup.snowflake.com](https://signup.snowflake.com/) et sélectionnez **exactement** les options suivantes :

* **Formulaire d'inscription** : Renseignez vos informations personnelles.
* **Édition Snowflake** : **Enterprise** 
  > *Raison : Débloque toutes les fonctionnalités avancées (Time Travel 90j, rôles avancés) tout en étant couvert à 100% par les 400$ de crédits gratuits.*
* **Cloud Provider** : **AWS (Amazon Web Services)**
  > *Raison : Standard le plus performant et le mieux supporté par dbt et les connecteurs Python.*
* **Région Cloud** : **Europe (Paris) `eu-west-3`** ou **Europe (Frankfurt) `eu-central-1`**.
* **Rôle / Use-Case** : **Co-Developer** (ou `Data Engineering & Analytics`).
* **Carte bancaire** : Aucune carte bancaire requise.

### 1.2 Récupération de l'Account Identifier
Dans l'interface Snowsight (en bas à gauche > Profil > Account > Copy Account Identifier) :
* Format recommandé : `ORGNAME-ACCOUNTNAME` (ex: `MYCOMPANY-BENCHMARK`)
* Format alternatif : `xy12345.eu-west-3.aws`

### 1.3 Script SQL Initial dans Snowflake (Snowsight Worksheet)
Exécutez ce script SQL pour préparer la base de données et minimiser la consommation de crédits :

```sql
-- 1. Base de données du benchmark
CREATE DATABASE IF NOT EXISTS BENCHMARK_DB;

-- 2. Schémas
CREATE SCHEMA IF NOT EXISTS BENCHMARK_DB.RAW;        -- Pour l'ingestion des CSV
CREATE SCHEMA IF NOT EXISTS BENCHMARK_DB.ANALYTICS;  -- Pour les modèles dbt

-- 3. Warehouse (Moteur de calcul) optimisé pour le coût
CREATE WAREHOUSE IF NOT EXISTS COMPUTE_WH 
WITH 
    WAREHOUSE_SIZE = 'X-SMALL'
    AUTO_SUSPEND = 60          -- Suspend après 60s d'inactivité
    AUTO_RESUME = TRUE          -- Redémarre automatiquement à la première requête
    INITIALLY_SUSPENDED = TRUE;
```

---

## Étape 2 : Ingestion des Données CSV (`upload_to_snowflake.py`)

Installez les dépendances Python nécessaires :
```bash
pip install snowflake-connector-python pandas pyarrow
```

Le script `data/upload_to_snowflake.py` lit tous les fichiers CSV du dossier `data/` et les injecte automatiquement dans `BENCHMARK_DB.RAW` :

```python
import os
import pandas as pd
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas

# Connexion Snowflake
conn = snowflake.connector.connect(
    user='VOTRE_UTILISATEUR',
    password='VOTRE_MOT_DE_PASSE',
    account='VOTRE_ACCOUNT_IDENTIFIER',
    warehouse='COMPUTE_WH',
    database='BENCHMARK_DB',
    schema='RAW'
)

data_dir = "./data"
csv_files = [f for f in os.listdir(data_dir) if f.endswith('.csv')]

print(f"🚀 Injection de {len(csv_files)} fichiers CSV...")

for csv_file in csv_files:
    table_name = csv_file.replace('.csv', '').upper()
    file_path = os.path.join(data_dir, csv_file)
    
    df = pd.read_csv(file_path)
    df.columns = [col.upper() for col in df.columns]
    
    success, nchunks, nrows, _ = write_pandas(
        conn=conn,
        df=df,
        table_name=table_name,
        auto_create_table=True,
        overwrite=True
    )
    print(f"✅ Table {table_name} injectée ({nrows} lignes).")

conn.close()
```

---

## Étape 3 : Transformation des Données avec dbt

Configurez le fichier `~/.dbt/profiles.yml` :

```yaml
actual_bi_as_code_benchmark:
  target: dev
  outputs:
    dev:
      type: snowflake
      account: VOTRE_ACCOUNT_IDENTIFIER
      user: VOTRE_UTILISATEUR
      password: VOTRE_MOT_DE_PASSE
      role: ACCOUNTADMIN
      warehouse: COMPUTE_WH
      database: BENCHMARK_DB
      schema: ANALYTICS
      threads: 4
      client_session_keep_alive: False
```

Exécutez vos transformations dbt :
```bash
cd dbt_project
dbt debug
dbt run
```

---

## Étape 4 : Intégration d'Evidence.dev (BI-as-Code Local)

### 4.1 Caractéristiques d'Evidence
* **Compte requis ?** ❌ **NON (100% Local & Open Source)**.
* **Emplacement dans le projet** : Dossier [`evidence_actual/`](file:///Users/mohammedamine/AI%20engineer%20projects%20%28freelance%20Bicode%29/actual_bi_as_code_benchmark/evidence_actual).

### 4.2 Installation & Démarrage
Dans le dossier `evidence_actual` :

```bash
cd evidence_actual

# 1. Installation des dépendances
npm install
npm install @evidence-dev/snowflake

# 2. Lancement du serveur local
npm run dev
```

### 4.3 Configuration de la Connexion Snowflake
1. Accédez à `http://localhost:3000/settings`.
2. Choisissez le connecteur **Snowflake**.
3. Renseignez :
   * **Account** : `VOTRE_ACCOUNT_IDENTIFIER`
   * **Database** : `BENCHMARK_DB`
   * **Warehouse** : `COMPUTE_WH`
   * **Schema** : `ANALYTICS`
   * **User / Password** : Vos identifiants Snowflake.

### 4.4 Exemple de Tableau de Bord (`pages/index.md`)
```markdown
# 📈 Dashboard Placements Agences

```sql placements
select 
    nom_agence,
    sum(chiffre_affaires) as total_ca
from BENCHMARK_DB.ANALYTICS.FCT_PLACEMENTS
group by 1
order by total_ca desc
```

<BarChart 
    data={placements} 
    x=nom_agence 
    y=total_ca 
    title="Chiffre d'Affaires par Agence (€)"
/>
```

---

## Étape 5 : Intégration de Hex.tech (Cloud Notebook & App)

### 5.1 Caractéristiques de Hex
* **Compte requis ?** ✅ **OUI (Compte Cloud SaaS)**.
* **Prix** : Essai gratuit 14 jours (puis plan gratuit Community).

### 5.2 Création du Compte & Configuration
1. Inscrivez-vous sur [hex.tech](https://hex.tech/).
2. Allez dans **Settings** > **Data connections** > **+ New connection**.
3. Sélectionnez **Snowflake** et entrez les paramètres :
   * **Account** : `VOTRE_ACCOUNT_IDENTIFIER`
   * **Database** : `BENCHMARK_DB`
   * **Warehouse** : `COMPUTE_WH`
   * **Authentication** : User / Password Snowflake.
4. Testez la connexion et enregistrez.

### 5.3 Création d'une Application / Notebook
1. Cliquez sur **+ New project**.
2. Écrivez des requêtes SQL directement sur `BENCHMARK_DB.ANALYTICS.FCT_PLACEMENTS`.
3. Ajoutez des cellules Python ou des composants graphiques interactifs (Bar Chart, Selectors, Inputs).
4. Cliquez sur **Publish** pour rendre l'application accessible.

---

## 📊 Matrice de Comparaison Evidence vs Hex

| Fonctionnalité | **Evidence.dev** | **Hex.tech** |
| :--- | :--- | :--- |
| **Paradigme** | BI-as-Code (Markdown + SQL + Svelte) | Data Notebook & App Builder (SQL + Python + UI) |
| **Hébergement** | Local (`localhost:3000`) ou Git/Vercel | Cloud SaaS (sur hex.tech) |
| **Versionning Git** | Nativement dans votre repo Git | Intégré à la plateforme Cloud |
| **Profil utilisateur ciblé** | Développeurs Analytics, Data Engineers | Data Analysts, Data Scientists, Métier |
