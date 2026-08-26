# 🛡️ Guide de Sécurité Anti-Coûts et Protection Snowflake (Free Trial)

Ce document récapitule toutes les garanties et configurations pour vous assurer qu'**aucun frais non désiré ne sera prélevé**, et que vos 400$ de crédits d'essai restent protégés.

---

## 1. 🛑 Garantie Technique N°1 : Aucune Carte Bancaire Enregistrée

* **Absence de Moyen de Paiement** : Lors de la création de votre compte d'essai gratuit sur Snowflake (Free Trial 30 jours / 400$), **aucune carte bancaire n'est demandée**.
* **Impossibilité de Prélèvement** : Sans carte enregistrée, il est **techniquement impossible** pour Snowflake de vous facturer un centime.
* **Expiration sans engagement** : Lorsque l'essai gratuit arrive à 30 jours ou que les 400$ sont épuisés, le compte passe automatiquement en statut `Suspended`. Il ne bascule **jamais** en mode payant automatique.

---

## 2. ⚡ Garantie N°2 : La veille automatique du Warehouse (`AUTO_SUSPEND = 60`)

Dans Snowflake, seul le calcul (*Warehouse*) consomme des crédits. Le stockage de vos CSV ne coûte que quelques centimes par mois.

Dans le script SQL que vous avez exécuté dans Snowsight, nous avons configuré :
```sql
CREATE WAREHOUSE IF NOT EXISTS COMPUTE_WH 
WITH 
    WAREHOUSE_SIZE = 'X-SMALL' -- 1 crédit / heure max
    AUTO_SUSPEND = 60          -- S'éteint après 60 SECONDES d'inactivité
    AUTO_RESUME = TRUE;
```

### Ce que ça garantit :
* Dès que votre script Python ou dbt a fini de travailler, le serveur attend 60 secondes puis **s'éteint complètement**.
* **Consommation moyenne par execution** : Moins de 0,02 crédit (soit ~0,03 €).

---

## 3. 🔒 Garantie N°3 : Garde-Fou Ultime (Resource Monitor)

Si vous voulez fixer un plafond absolu (par exemple : **Bloquer le compte s'il consomme plus de 10 crédits sur vos 400$ gratuits**), exécutez ce script SQL dans votre Worksheet Snowsight :

```sql
-- 1. Création d'un moniteur de ressources plafonné à 10 crédits
CREATE OR REPLACE RESOURCE MONITOR LIMIT_BENCHMARK_CREDITS
WITH 
    CREDIT_QUOTA = 10                  -- Plafond de 10 crédits
    FREQUENCY = MONTHLY
    START_TIMESTAMP = IMMEDIATELY
    NOTIFY_USERS = (CURRENT_USER())
    TRIGGERS 
        ON 80 PERCENT DO NOTIFY         -- Alerte à 8 crédits
        ON 100 PERCENT DO SUSPEND;      -- Suspend immédiatement les calculs à 10 crédits

-- 2. Attacher le moniteur au warehouse COMPUTE_WH
ALTER WAREHOUSE COMPUTE_WH SET RESOURCE_MONITOR = LIMIT_BENCHMARK_CREDITS;
```

---

## 📋 Récapitulatif Sécurité

| Risque potentiel | Réalité Snowflake | Protection active |
| :--- | :--- | :--- |
| **Prélèvement bancaire surprise** | Impossible (pas de carte enregistrée) | ✅ Essai gratuit 100% sans carte |
| **Serveur qui tourne indéfiniment** | Bloqué par l'Auto-suspend | ✅ S'éteint après 60 secondes |
| **Dépassement de consommation** | Bloqué par le Resource Monitor | ✅ Plafond fixé sur les crédits |
