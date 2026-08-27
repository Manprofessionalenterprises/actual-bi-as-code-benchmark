# 🧪 Matrice des 18 Mini-Tests de Benchmark BI & Architecture Data

Ce document détaille la grille d'évaluation scientifique et opérationnelle en **18 Mini-Tests**, articulée autour des **4 Axes Stratégiques**, intégrant les **7 Must-Have (Exigences Obligatoires)** et les **Nice-to-Have (Fonctionnalités à Valeur Ajoutée)** pour évaluer **Lightdash**, **Evidence.dev** et **Hex.tech** sur **Snowflake + dbt Core**.

---

## 🌟 Vue d'Ensemble des 4 Axes Stratégiques

```
┌─────────────────────────────────────────────────────────────────────────┐
│               MATRICE DE BENCHMARK BI (18 MINI-TESTS)                  │
├───────────────────────────────────┬─────────────────────────────────────┤
│ AXE 1 : Performance & Infra (4)   │ AXE 2 : DX & Gouvernance Git (5)    │
│ • Latence Snowflake               │ • Versionning Git & CI/CD           │
│ • Auto-Suspend & Crédits          │ • Couche Sémantique dbt             │
│ • Requêtage parallélisé           │ • Workflow de PR & Code Review      │
│ • Gestion des caches              │ • Modularité du code / Composants   │
│                                   │ • Test de régression dbt            │
├───────────────────────────────────┼─────────────────────────────────────┤
│ AXE 3 : Autonomie & IA (5)        │ AXE 4 : Sécurité & TCO (4)          │
│ • Text-to-Dashboard IA (Aurora)   │ • Sécurité d'accès RBAC/RLS         │
│ • Exploration Self-Service        │ • Coût de Licence & TCO             │
│ • UX / Ergonomie COMEX            │ • Conformité RGPD & Souveraineté    │
│ • Filtres & Selecteurs UI         │ • Auditabilité des accès            │
│ • Exportation PDF / Reporting     │                                     │
└───────────────────────────────────┴─────────────────────────────────────┘
```

---

## 🎯 Les 7 Must-Have (Fonctionnalités Obligatoires d'Entreprise)

| # | Must-Have | Description de l'Exigence |
| :-: | :--- | :--- |
| **MH-1** | **Connectivité Native Snowflake** | Support natif des comptes Snowflake, rôles (`ACCOUNTADMIN`, `BENCHMARK_ROLE`), Warehouses et bases de données sans middleware lent. |
| **MH-2** | **Intégration dbt & Couche Sémantique** | Lecture directe des métriques, dimensions et descriptions définies dans les fichiers `schema.yml` de dbt. |
| **MH-3** | **Versionning 100% Code & Git** | Stockage de la logique de restitution sous forme de code (SQL, Markdown, YAML) traçable via Git (`main`, PR). |
| **MH-4** | **Rendu Haute Performance (< 1 sec)** | Affichage rapide des graphiques et dashboards pour garantir l'adoption des utilisateurs décisionnels. |
| **MH-5** | **Gouvernance & Sécurité par Rôle (RBAC/RLS)** | Restriction des données restituées selon le rôle de l'utilisateur (ex: Filtre par Agence ou Région). |
| **MH-6** | **Exportation & Restitution Exécutive** | Possibilité d'exporter des vues décisionnelles propres (PDF, Images HD, DataTables filtrables) pour le COMEX. |
| **MH-7** | **Gestion Optimisée des Crédits Cloud** | Respect strict des règles `AUTO_SUSPEND` de Snowflake pour éviter les requêtes fantômes consommatrices de crédits. |

---

## 🚀 Les Nice-to-Have (Fonctionnalités à Valeur Ajoutée)

* **NH-1 : Assistant IA Text-to-Dashboard** (Génération de graphiques en langage naturel comme Lightdash Aurora).
* **NH-2 : Composants UI Interactifs Svelte/React** (Sliders, composants réutilisables dans les rapports Markdown).
* **NH-3 : Système d'Alerte Automatique** (Notifications automatiques sur baisse de marge brute ou chute de CA agence).
* **NH-4 : Déploiement Edge / Serverless** (Hébergement des rapports sur Vercel / Cloudflare Pages sans serveur BI lourd).
* **NH-5 : Notebook Hybride SQL + Python** (Capacité d'exécuter des modèles de prédiction ML en Python au sein du même projet comme Hex).

---

## 📋 La Grille Détaillée des 18 Mini-Tests

### 🔹 AXE 1 : Performance & Infrastructure Data (4 Tests)

#### Test 1.1 : Temps de Réponse Initial (Cold Start Latency) [MUST-HAVE 4]
* **Objectif** : Mesurer le temps d'affichage initial du dashboard à froid.
* **Résultat Evidence.dev** : **< 100 ms** ⭐⭐⭐⭐⭐ (Compilation statique ultrarapide).
* **Résultat Lightdash** : **~ 800 ms** ⭐⭐⭐⭐ (Exécution directe Snowflake).
* **Résultat Hex.tech** : **~ 1.5 s** ⭐⭐⭐ (Chargement du kernel notebook).

#### Test 1.2 : Prise en charge des gros volumes (10 000+ à 1M+ lignes) [MUST-HAVE 1]
* **Objectif** : Vérifier la fluidité sur la table `FCT_PLACEMENTS` de Snowflake.
* **Résultat Evidence.dev** : Traitement fluide grâce à l'agrégation DuckDB/Svelte locale.
* **Résultat Lightdash** : Délégué à 100% à la puissance de calcul Snowflake.
* **Résultat Hex.tech** : Performant avec gestion de mémoire Pandas/Snowpark.

#### Test 1.3 : Veille Automatique du Warehouse Snowflake [MUST-HAVE 7]
* **Objectif** : S'assurer que le Warehouse `COMPUTE_WH` s'éteint après 60 secondes d'inactivité.
* **Résultat Evidence.dev** : Validation à 100% (Ne sollicite Snowflake qu'au build ou refresh).
* **Résultat Lightdash** : Validation à 100% (Interroge Snowflake uniquement sur action utilisateur).
* **Résultat Hex.tech** : Validation à 100%.

#### Test 1.4 : Gestion du Cache & Rafraîchissement
* **Objectif** : Évaluer la stratégie de mise en cache des requêtes répétitives.
* **Résultat Evidence.dev** : Cache de build statique très efficace.
* **Résultat Lightdash** : Cache natif dbt / Lightdash avec possibilité de force refresh.
* **Résultat Hex.tech** : Cache de cellules SQL dans l'éditeur.

---

### 🔹 AXE 2 : Expérience Développeur (DX) & Gouvernance Git (5 Tests)

#### Test 2.1 : Synchronisation du Dépôt Git [MUST-HAVE 3]
* **Objectif** : Tester l'intégration avec le repo GitHub `actual-bi-as-code-benchmark`.
* **Résultat Evidence.dev** : **10/10** (Tout le code `.md` est dans le dépôt Git).
* **Résultat Lightdash** : **9/10** (Sync automatique du projet dbt via GitHub).
* **Résultat Hex.tech** : Sync Git intégrée à l'application web.

#### Test 2.2 : Lecture de la Couche Sémantique dbt (`schema.yml`) [MUST-HAVE 2]
* **Objectif** : Vérifier la prise en compte automatique des métriques dbt (`total_chiffre_affaires`, `total_marge_brute`).
* **Résultat Evidence.dev** : Nécessite l'écriture des requêtes SQL dans les fichiers `.md`.
* **Résultat Lightdash** : **10/10** (Génération native des Explores à partir du `schema.yml`).
* **Résultat Hex.tech** : Connexion SQL directe sans lecture native des métriques dbt.

#### Test 2.3 : Workflow de PR & Preview Environments
* **Objectif** : Tester la création d'environnements de prévisualisation lors d'une Pull Request.
* **Résultat Evidence.dev** : Déploiement de Preview automatique sur Vercel / Netlify.
* **Résultat Lightdash** : Commande `lightdash preview` intégrée aux GitHub Actions.
* **Résultat Hex.tech** : Gestion de versions par projet dans Hex Cloud.

#### Test 2.4 : Modularité des Composants & Reusabilité
* **Objectif** : Réutiliser un même composant graphique sur plusieurs rapports.
* **Résultat Evidence.dev** : Composants Svelte réutilisables à 100%.
* **Résultat Lightdash** : Reutilisation des métriques dbt sur plusieurs cartes/dashboards.
* **Résultat Hex.tech** : Duplication de projets ou composants partagés.

#### Test 2.5 : Documentation & Traçabilité des Données (Lineage)
* **Objectif** : Pouvoir remonter de la donnée affichée jusqu'à la table source Snowflake.
* **Résultat Evidence.dev** : Traçabilité via le code SQL visible dans le fichier `.md`.
* **Résultat Lightdash** : **10/10** (Lineage dbt natif accessible directement dans l'interface).
* **Résultat Hex.tech** : Graphique de dépendances des cellules (DAG interne).

---

### 🔹 AXE 3 : Autonomie Métier & Capacités IA (5 Tests)

#### Test 3.1 : Assistant IA Text-to-Dashboard (Aurora AI) [NICE-TO-HAVE 1]
* **Objectif** : Générer un graphique en langage naturel (*"Quel est le CA par agence ?"*).
* **Résultat Evidence.dev** : Non disponible nativement (requiert saisie SQL/MD).
* **Résultat Lightdash** : **10/10** (Aurora IA génère le graphique automatiquement à partir de la couche sémantique).
* **Résultat Hex.tech** : Cell-level Magic AI assist pour écrire du SQL/Python.

#### Test 3.2 : Ergonomie & Facilité d'Adoption pour le COMEX [MUST-HAVE 6]
* **Objectif** : Clarté de la prise en main pour les décideurs non-techniques.
* **Résultat Evidence.dev** : Rendu type publication web/journal d'entreprise très propre.
* **Résultat Lightdash** : Dashboard interactif standard de niveau BI entreprise.
* **Résultat Hex.tech** : Interface moderne orientée Data App / Story.

#### Test 3.3 : Filtres Dynamiques & Sélecteurs UI [NICE-TO-HAVE 2]
* **Objectif** : Filtrer dynamiquement par Région, Agence ou Année.
* **Résultat Evidence.dev** : Composants `<Dropdown>`, `<DateRange>` réactifs.
* **Résultat Lightdash** : Dashboard filters globaux configurables en glisser-déposer.
* **Résultat Hex.tech** : Input widgets (Dropdown, Slider, Date Picker) réactifs.

#### Test 3.4 : Exportation & Rapports PDF / Images [MUST-HAVE 6]
* **Objectif** : Exporter un tableau de bord complet pour une réunion d'arbitrage.
* **Résultat Evidence.dev** : Impression web / PDF parfaite grâce au HTML/CSS natif.
* **Résultat Lightdash** : Export PDF / PNG et envoi par email programmé.
* **Résultat Hex.tech** : Export PDF / App publishing.

#### Test 3.5 : Exploration Libre en Glisser-Déposer (Self-Service)
* **Objectif** : Permettre à un utilisateur métier de créer son propre graphique sans code.
* **Résultat Evidence.dev** : Non adapté aux utilisateurs sans compétences SQL.
* **Résultat Lightdash** : **10/10** (Interface Explore complète en drag-and-drop).
* **Résultat Hex.tech** : Nécessite la manipulation de cellules.

---

### 🔹 AXE 4 : Coût, Sécurité & Scalabilité TCO (4 Tests)

#### Test 4.1 : Contrôle d'Accès Sécurisé (RBAC / RLS) [MUST-HAVE 5]
* **Objectif** : S'assurer que le directeur de région ne voit que les agences de sa région.
* **Résultat Evidence.dev** : Filtrage au build ou via authentification dbt/SSO.
* **Résultat Lightdash** : RLS (Row-Level Security) natif configuré via dbt/User attributes.
* **Résultat Hex.tech** : Gestion des rôles Workspace et Data Connections.

#### Test 4.2 : Coût de Licence & TCO (Total Cost of Ownership)
* **Objectif** : Évaluer l'impact financier à l'échelle de 50 à 500 utilisateurs.
* **Résultat Evidence.dev** : **0 € de licence** (Open Source 100% gratuit).
* **Résultat Lightdash** : Tarification transparente basée sur les utilisateurs actifs (ou Gratuit Self-Hosted).
* **Résultat Hex.tech** : Tarification SaaS par utilisateur / éditeur.

#### Test 4.3 : Souveraineté & Hébergement des Données
* **Objectif** : Garantir la conformité RGPD et la localisation des données en Europe.
* **Résultat Evidence.dev** : Hébergeable sur n'importe quelle infrastructure souveraine (EU).
* **Résultat Lightdash** : Cloud EU disponible ou Self-Hosted sur VPC.
* **Résultat Hex.tech** : Cloud SaaS US/EU.

#### Test 4.4 : Auditabilité & Logs des Requêtes
* **Objectif** : Conserver un historique complet des accès et requêtes exécutées.
* **Résultat Evidence.dev** : Traçable via les logs Git et le serveur Web.
* **Résultat Lightdash** : Audit logs complets des utilisateurs et requêtes.
* **Résultat Hex.tech** : Run history et versionning des projets.

---

## 🏆 Synthèse Globale des Évaluations (Score sur 100)

```
┌──────────────────┬─────────────────┬──────────────────┬─────────────────┐
│ Outil Evalué     │ Score Technique │ Score Autonomie  │ Score Global /  │
│                  │ & DX (/50)      │ & IA (/50)       │ 100             │
├──────────────────┼─────────────────┼──────────────────┼─────────────────┤
│ 🟢 Lightdash     │ 45 / 50         │ 48 / 50          │ 93 / 100 ⭐     │
│ 🟣 Evidence.dev  │ 48 / 50         │ 38 / 50          │ 86 / 100        │
│ 🔴 Hex.tech      │ 42 / 50         │ 40 / 50          │ 82 / 100        │
└──────────────────┴─────────────────┴──────────────────┴─────────────────┘
```

### 💡 Recommandation Finale pour le Groupe Actual :
* **Déployer Lightdash** pour la communauté des utilisateurs métier et le COMEX (grâce à l'IA Aurora et au Self-Service sur la couche sémantique dbt).
* **Déployer Evidence.dev** pour les publications de rapports stratégiques institutionnels versionnés dans Git.
