import os
import pandas as pd
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas

# -----------------------------------------------------------------------------
# Configuration des identifiants Snowflake
# -----------------------------------------------------------------------------
SNOWFLAKE_USER = os.getenv("SNOWFLAKE_USER", "LICALLMAN110")
SNOWFLAKE_PASSWORD = os.getenv("SNOWFLAKE_PASSWORD", "testSnowflake2026*")  # Entrez votre mot de passe ici ou via variable d'environnement
SNOWFLAKE_ACCOUNT = os.getenv("SNOWFLAKE_ACCOUNT", "SLPMQMD-DX08347")
SNOWFLAKE_WAREHOUSE = "COMPUTE_WH"
SNOWFLAKE_DATABASE = "BENCHMARK_DB"
SNOWFLAKE_SCHEMA = "RAW"

def upload_all_csvs():
    if not SNOWFLAKE_PASSWORD:
        print("❌ Erreur : Le mot de passe Snowflake n'est pas renseigné.")
        print("Veuillez remplir la variable SNOWFLAKE_PASSWORD dans le script ou dans votre environnement.")
        return

    print("🔌 Connexion à Snowflake...")
    conn = snowflake.connector.connect(
        user=SNOWFLAKE_USER,
        password=SNOWFLAKE_PASSWORD,
        account=SNOWFLAKE_ACCOUNT,
        warehouse=SNOWFLAKE_WAREHOUSE,
        database=SNOWFLAKE_DATABASE,
        schema=SNOWFLAKE_SCHEMA
    )

    # Répertoire contenant les fichiers CSV
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_files = [f for f in os.listdir(script_dir) if f.endswith('.csv')]

    print(f"🚀 Début de l'injection de {len(csv_files)} fichiers CSV dans Snowflake ({SNOWFLAKE_DATABASE}.{SNOWFLAKE_SCHEMA})...\n")

    for csv_file in csv_files:
        table_name = csv_file.replace('.csv', '').upper()
        file_path = os.path.join(script_dir, csv_file)
        
        print(f"📦 Traitement de {csv_file} -> Table {table_name}...")
        df = pd.read_csv(file_path)
        
        # Passer les noms de colonnes en majuscules pour Snowflake SQL
        df.columns = [col.upper() for col in df.columns]
        
        # Envoi dans Snowflake (crée la table automatiquement si elle n'existe pas)
        success, nchunks, nrows, _ = write_pandas(
            conn=conn,
            df=df,
            table_name=table_name,
            auto_create_table=True,
            overwrite=True
        )
        print(f"   ✅ Table {table_name} créée/mise à jour avec succès : {nrows} lignes insérées.")

    conn.close()
    print("\n🎉 Toutes les données ont été injectées avec succès dans Snowflake !")

if __name__ == "__main__":
    upload_all_csvs()
