import pandas as pd
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
EXCEL_PATH = os.path.join(PROJECT_ROOT, "source", "requirements_app_PEGS.xlsx")

REQUIRED_COLUMNS = ["ID", "Category", "Title", "PEGS Ref", "Priority", "Description"]

def check_excel_structure():
    print(f"DÉBUT DU TEST : Vérification du fichier {EXCEL_PATH}...")

    if not os.path.exists(EXCEL_PATH):
        print(f"ERREUR FATALE : Le fichier Excel est introuvable à : {EXCEL_PATH}")
        sys.exit(1)

    try:
        df = pd.read_excel(EXCEL_PATH)
        print(f"Fichier chargé. {len(df)} lignes trouvées.")

        missing_columns = [col for col in REQUIRED_COLUMNS if col not in df.columns]
        
        if missing_columns:
            print(f"ERREUR DE STRUCTURE : Il manque ces colonnes : {missing_columns}")
            sys.exit(1)
        else:
            print("Structure des colonnes : VALIDE")

        if df.empty:
            print("ATTENTION : Le fichier Excel est vide.")
        
    except Exception as e:
        print(f"ERREUR CRITIQUE lors de la lecture : {e}")
        sys.exit(1)

    print("TEST RÉUSSI.")
    sys.exit(0)
    

if __name__ == "__main__":
    check_excel_structure()