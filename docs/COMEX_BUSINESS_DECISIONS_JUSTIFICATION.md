# 🎯 Décodage Stratégique : Décisions du COMEX & Justification des Chiffres Clés

Ce document décrypte le **mode de fonctionnement réel du COMEX / CODIR du Groupe Actual**, la souffrance quotidienne qu'ils cherchent à résoudre, et la **justification décisionnelle de chaque chiffre clé**.

---

## 🛑 1. Ce que le COMEX fait aujourd'hui à 90% (La Souffrance Actuelle)

Aujourd'hui, sans outil sémantique unifié (BI-as-Code) :

1. **La Guerre des Fichiers Excel** :
   * La Direction Financière arrive en réunion avec un fichier Excel basés sur les factures comptables.
   * La Direction du Réseau d'Agences arrive avec un autre Excel basé sur les relevés d'heures d'intérimaires.
   * La Direction RH a un 3ème fichier basé sur les contrats signés.

2. **Le Résultat en Réunion COMEX** :
   * Ils passent **45 minutes à débattre de "qui a le bon chiffre de CA"** au lieu de prendre des décisions d'entreprise.
   * **Le besoin n°1 d'Actual** : Une **Source Unique de Vérité (Single Source of Truth)** garantie par Snowflake + dbt où la définition de la Marge Brute et du CA est la même pour tout le monde.

---

## 💡 2. Les 4 Grandes Décisions du COMEX & Justification des Chiffres

```
┌──────────────────────────────────────────────────────────────────────────────────────────┐
│                   LES 4 DÉCISIONS STRATÉGIQUES DU COMEX GROUPE ACTUAL                     │
├──────────────────────────┬──────────────────────────┬────────────────────────────────────┤
│ DÉCISION                 │ CHIFFRE CLÉ REQUIS       │ JUSTIFICATION STRATÉGIQUE          │
├──────────────────────────┼──────────────────────────┼────────────────────────────────────┤
│ 1. Rentabilité du Réseau │ Marge Brute (€ et %)     │ Ne pas confondre le CA (volume) et │
│                          │ par Agence et Secteur    │ le bénéfice net de chaque agence.  │
├──────────────────────────┼──────────────────────────┼────────────────────────────────────┤
│ 2. Arbitrage Réseau      │ Taux de Réalisation des  │ Décider de fermer/fusionner ou     │
│    (Implantation/Fermeture)│ Objectifs par Agence     │ d'investir dans une nouvelle zone. │
├──────────────────────────┼──────────────────────────┼────────────────────────────────────┤
│ 3. Risque Grand Compte   │ Concentration du CA      │ Détecter les gros clients qui font │
│                          │ vs Marge par Client      │ du volume mais zéro marge brute.   │
├──────────────────────────┼──────────────────────────┼────────────────────────────────────┤
│ 4. Tension RH & Métiers  │ Ratio Placements Actifs  │ Réallouer le budget d'acquisition  │
│                          │ / Heures Travaillées     │ candidats sur les métiers rares.   │
└──────────────────────────┴──────────────────────────┴────────────────────────────────────┘
```

---

### 📊 Décision 1 : Arbitrage de la Marge Brute vs Chiffre d'Affaires
* **Le Chiffre requis** : Marge Brute (€) & Taux de Marge (%) ventilés par Agence et Secteur.
* **La Justification Métier** : 
  Dans le travail temporaire, le Chiffre d'Affaires est un "trompe-l'œil". Une agence qui génère **2 M€ de CA avec 8% de marge brute** coûte de l'argent au groupe (frais de structure). Une agence qui génère **800 k€ de CA à 22% de marge** dégagera une forte rentabilité.
* **La Décision COMEX** : 
  Imposer une revalorisation du coefficient de facturation aux clients à faible marge ou réorienter l'effort commercial vers les secteurs plus rentables (ex: Tertiaire/IT plutôt que BTP).

---

### 🏢 Décision 2 : Équilibre & Expansion du Réseau d'Agences
* **Le Chiffre requis** : Taux de Réalisation de l'Objectif Annuel par Agence (22 agences pilotes / 600 agences réseau).
* **La Justification Métier** :
  Le COMEX a besoin d'isoler en un coup d'œil les agences en sous-performance (< 90% de leur objectif) et celles en sur-performance (> 105%).
* **La Décision COMEX** :
  * **Pour les agences rouges (< 90%)** : Déclencher un audit de secteur, envoyer un renfort commercial ou restructurer.
  * **Pour les agences vertes (> 105%)** : Débloquer du budget d'embauche pour ajouter un permanent ou ouvrir une succursale dans la ville voisine.

---

### ⚠️ Décision 3 : Gestion du Risque Clients & Grands Comptes
* **Le Chiffre requis** : Matrice Marge Brute (€) vs CA (€) par Client (Scatter Plot).
* **La Justification Métier** :
  Si les 3 plus gros clients du groupe représentent 40% du volume total d'heures mais seulement 10% de la marge brute globale, le groupe s'expose à un **risque de concentration majeur** (dépendance vis-à-vis d'un donneur d'ordre exigeant).
* **La Décision COMEX** :
  Renégocier les conditions contractuelles lors du renouvellement des accords-cadres ou diversifier le portefeuille sur des ETI locales.

---

### 👥 Décision 4 : Pilotage de la Force de Recrutement
* **Le Chiffre requis** : Volume d'Heures Intérimaires Travaillées & Taux de Remplissage par Métier.
* **La Justification Métier** :
  Le secteur de l'intérim souffre de pénurie de candidats qualifiés. Si les commandes clients augmentent mais que le volume d'heures stagne, le problème vient du sourcing candidat.
* **La Décision COMEX** :
  Réallouer les budgets marketing RH (jobboards, formations financées) vers les agences et régions connaissant le plus fort taux de missions non pourvues.

---

## 🚫 3. Ce dont le COMEX N'A PAS BESOIN (Ce qu'il faut filtrer)

Pour garder un dashboard exécutif d'une clarté absolue, nous éliminons :
* ❌ **Le détail individuel des factures ou des fiches de paie** (niveaux opérationnels).
* ❌ **Les métriques techniques IT** (temps de rafraîchissement dbt, schémas bruts Snowflake).
* ❌ **Les données non agrégées sans indicateur de comparaison** (ex: afficher le CA sans l'objectif annuel associé n'a aucune valeur décisionnelle).
