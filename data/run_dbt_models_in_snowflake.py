import os
import snowflake.connector

conn = snowflake.connector.connect(
    user=os.getenv("SNOWFLAKE_USER", "LICALLMAN110"),
    password=os.getenv("SNOWFLAKE_PASSWORD", "testSnowflake2026*"),
    account=os.getenv("SNOWFLAKE_ACCOUNT", "SLPMQMD-DX08347"),
    warehouse="COMPUTE_WH",
    database="BENCHMARK_DB",
    schema="ANALYTICS"
)

cursor = conn.cursor()

print("🚀 Exécution des transformations dbt/SQL dans BENCHMARK_DB.ANALYTICS...")

# 1. Table DIM_AGENCES
print("  🔨 Création de la table DIM_AGENCES...")
cursor.execute("""
CREATE OR REPLACE TABLE BENCHMARK_DB.ANALYTICS.DIM_AGENCES AS
SELECT
    a.agence_id,
    a.nom_agence,
    a.region,
    a.directeur,
    a.objectifs_ca_annuel,
    COUNT(DISTINCT m.mission_id) AS total_missions,
    COALESCE(SUM(m.chiffre_affaires), 0) AS chiffre_affaires_total
FROM BENCHMARK_DB.RAW.RAW_AGENCES a
LEFT JOIN BENCHMARK_DB.RAW.RAW_MISSIONS m ON a.agence_id = m.agence_id
GROUP BY 1, 2, 3, 4, 5;
""")
print("  ✅ DIM_AGENCES créée !")

# 2. Table DIM_CLIENTS
print("  🔨 Création de la table DIM_CLIENTS...")
cursor.execute("""
CREATE OR REPLACE TABLE BENCHMARK_DB.ANALYTICS.DIM_CLIENTS AS
SELECT
    c.client_id,
    c.nom_entreprise,
    c.secteur AS secteur_activite,
    c.ville,
    COUNT(DISTINCT m.mission_id) AS total_missions_commandees,
    COALESCE(SUM(m.chiffre_affaires), 0) AS total_facture
FROM BENCHMARK_DB.RAW.RAW_CLIENTS c
LEFT JOIN BENCHMARK_DB.RAW.RAW_MISSIONS m ON c.client_id = m.client_id
GROUP BY 1, 2, 3, 4;
""")
print("  ✅ DIM_CLIENTS créée !")

# 3. Table FCT_PLACEMENTS
print("  🔨 Création de la table FCT_PLACEMENTS...")
cursor.execute("""
CREATE OR REPLACE TABLE BENCHMARK_DB.ANALYTICS.FCT_PLACEMENTS AS
SELECT
    m.mission_id,
    m.type_contrat,
    m.statut_mission AS statut,
    m.date_debut,
    m.date_fin,
    
    a.agence_id,
    a.nom_agence,
    a.region AS agence_region,
    
    c.client_id,
    c.nom_entreprise AS client_nom,
    c.secteur AS client_secteur,
    
    cand.candidat_id,
    cand.nom_prenom AS candidat_nom_complet,
    cand.metier_principal AS candidat_metier,
    
    m.heures_travaillees AS heures_effectuees,
    m.taux_horaire_facture,
    m.taux_horaire_paye,
    
    m.chiffre_affaires,
    m.cout_salarial AS cout_paie,
    m.marge_brute

FROM BENCHMARK_DB.RAW.RAW_MISSIONS m
LEFT JOIN BENCHMARK_DB.RAW.RAW_AGENCES a ON m.agence_id = a.agence_id
LEFT JOIN BENCHMARK_DB.RAW.RAW_CLIENTS c ON m.client_id = c.client_id
LEFT JOIN BENCHMARK_DB.RAW.RAW_CANDIDATS cand ON m.candidat_id = cand.candidat_id;
""")
print("  ✅ FCT_PLACEMENTS créée !")

cursor.close()
conn.close()
print("🎉 Toutes les tables mart sont prêtes et remplies dans BENCHMARK_DB.ANALYTICS !")
