import pandas as pd
import os
import sys

# Configuration
EXCEL_PATH = os.path.join("source", "requirements_app_PEGS.xlsx")
REQUIRED_COLUMNS = ["ID", "Category", "Title", "PEGS Ref", "Priority", "Description"]

def check_excel_structure():
    print(f"DÉBUT DU TEST : Vérification du fichier {EXCEL_PATH}...")

    # 1. Vérifier si le fichier existe
    if not os.path.exists(EXCEL_PATH):
        print(f"ERREUR FATALE : Le fichier Excel est introuvable à : {EXCEL_PATH}")
        sys.exit(1)

    try:
        # 2. Charger le fichier
        df = pd.read_excel(EXCEL_PATH)
        print(f"Fichier chargé. {len(df)} lignes trouvées.")

        # 3. Vérifier les colonnes
        missing_columns = [col for col in REQUIRED_COLUMNS if col not in df.columns]
        
        if missing_columns:
            print(f"ERREUR DE STRUCTURE : Il manque ces colonnes dans l'Excel : {missing_columns}")
            print(f"Colonnes trouvées : {list(df.columns)}")
            sys.exit(1)
        else:
            print("Structure des colonnes : VALIDE")

        # 4. Vérifier qu'il n'est pas vide
        if df.empty:
            print("ATTENTION : Le fichier Excel est vide (aucune ligne de données).")
            # On ne bloque pas forcément, mais c'est louche.
        
    except Exception as e:
        print(f"ERREUR CRITIQUE lors de la lecture : {e}")
        sys.exit(1)

    print("TEST RÉUSSI : Les données semblent correctes.")
    sys.exit(0)

if __name__ == "__main__":
    check_excel_structure()