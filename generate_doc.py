import pandas as pd
import os
import sys

# Configuration des chemins
# On suppose que le script est à la racine et le fichier dans /Source
EXCEL_PATH = os.path.join("Source", "requirements_app_PEGS.xlsx")
OUTPUT_ADOC = "output.adoc"

def clean_text(text):
    """Nettoie le texte pour éviter de casser le format AsciiDoc"""
    if pd.isna(text):
        return ""
    return str(text).replace("\n", " + \n") # Conserve les sauts de ligne Excel

def generate_asciidoc():
    print(f"🔍 Recherche du fichier : {EXCEL_PATH}")
    
    if not os.path.exists(EXCEL_PATH):
        print(f"❌ Erreur : Le fichier {EXCEL_PATH} est introuvable.")
        sys.exit(1)

    try:
        # Lecture du fichier Excel
        df = pd.read_excel(EXCEL_PATH)
        print(f"✅ Fichier chargé : {len(df)} lignes trouvées.")
    except Exception as e:
        print(f"❌ Erreur lors de la lecture du fichier Excel : {e}")
        sys.exit(1)

    # Début du contenu AsciiDoc (Header style Book)
    adoc_content = """= Spécifications du Projet (PEGS)
:doctype: book
:toc: left
:toclevels: 3
:sectnums:
:icons: font
:source-highlighter: highlight.js

== Introduction
Ce document est généré automatiquement à partir des exigences stockées dans le fichier Excel du projet.

"""

    # 1. Regrouper par Catégorie (ex: Project, System, Hardware...)
    # On s'assure que la colonne Category existe
    if 'Category' in df.columns:
        groups = df.groupby('Category')
    else:
        # Fallback si la colonne n'existe pas
        groups = [('Exigences', df)]

    for category, items in groups:
        adoc_content += f"\n== {category}\n\n"
        
        # 2. Itérer sur chaque exigence de la catégorie
        for _, row in items.iterrows():
            req_id = clean_text(row.get('ID', 'N/A'))
            title = clean_text(row.get('Title', 'Sans titre'))
            moscow = clean_text(row.get('MoSCoW', ''))
            desc = clean_text(row.get('Description', ''))
            rationale = clean_text(row.get('Rationale', ''))
            accept_crit = clean_text(row.get('Acceptance Criteria', ''))
            
            # Construction d'un bloc pour l'exigence
            adoc_content += f"=== {req_id} - {title}\n"
            
            # Badge de priorité (MoSCoW)
            if moscow:
                adoc_content += f"**Priorité :** `{moscow}`\n\n"
            
            # Description principale
            if desc:
                adoc_content += f"==== Description\n{desc}\n\n"
            
            # Justification (Rationale)
            if rationale:
                adoc_content += f"==== Justification\n_{rationale}_\n\n"
            
            # Critères d'acceptation (si présents)
            if accept_crit:
                adoc_content += f"==== Critères d'acceptation\n[quote]\n____\n{accept_crit}\n____\n\n"
            
            adoc_content += "---\n\n"

    # Écriture du fichier final
    with open(OUTPUT_ADOC, "w", encoding="utf-8") as f:
        f.write(adoc_content)
    
    print(f"🎉 Succès : {OUTPUT_ADOC} a été généré.")

if __name__ == "__main__":
    generate_asciidoc()