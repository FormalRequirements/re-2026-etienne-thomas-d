import pandas as pd
import os
import sys
import datetime

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)

EXCEL_PATH = os.path.join(PROJECT_ROOT, "source", "requirements_app_PEGS.xlsx")
OUTPUT_ADOC = os.path.join(PROJECT_ROOT, "output.adoc")

CATEGORY_ORDER = ["Goals", "Environment", "System", "Project"]

PEGS_DEFINITIONS = {
    "Goals": "Vision du projet : fournir une application mobile-first simple et stable pour le suivi de la musculation, permettant aux pratiquants de visualiser leur progression et, à terme (V2), d'interagir avec des coachs sportifs.",
    "Environment": "Contexte d'utilisation : usage principal sur smartphone en salle de sport, prenant en compte des conditions de connectivité réseau potentiellement instables (mode hors ligne) et l'environnement physique de l'entraînement.",
    "System": "Périmètre fonctionnel : couvre les fonctionnalités Cœur de la V1 (suivi de séance, historique), l'extension Coaching de la V2 et les fonctionnalités avancées de la V3 (nutrition, wearables).",
    "Project": "Cadre du projet : travail académique utilisant la méthodologie PEGS. Les exigences sont centralisées dans une source unique (Excel) et la documentation est générée automatiquement via GitHub Actions."
}

def clean_text(text):
    if pd.isna(text):
        return ""
    return str(text).strip().replace("\n", " +\n")

def generate_asciidoc():
    print(f"Recherche du fichier : {EXCEL_PATH}")
    
    if not os.path.exists(EXCEL_PATH):
        print(f"Erreur : Fichier introuvable à {EXCEL_PATH}")
        sys.exit(1)

    try:
        df = pd.read_excel(EXCEL_PATH)
        if 'Category' in df.columns:
            df['Category'] = df['Category'].str.capitalize()
    except Exception as e:
        print(f"Erreur lecture Excel : {e}")
        sys.exit(1)

    today = datetime.date.today()
    adoc_content = f"""= LIFT-TRACK Requirements Document
:author: Thomas DOUMENG & Etienne CARPENTIER
:revdate: {today}
:doctype: book
:toc: macro
:toc-title: Table des matières
:toclevels: 3
:sectnums:
:sectnumlevels: 4
:icons: font
:experimental:
:source-highlighter: highlight.js
:imagesdir: images

toc::[]

== Introduction

Ce document contient les spécifications du projet LIFT-TRACK générées automatiquement.

[TIP]
====
Dernière mise à jour : {today}.\n
Source des données : `{os.path.basename(EXCEL_PATH)}`
====
"""

    if 'Category' not in df.columns:
        df['Category'] = 'General'
        categories_to_process = ['General']
    else:
        existing_categories = df['Category'].unique().tolist()
        ordered_categories = [c for c in CATEGORY_ORDER if c in existing_categories]
        remaining_categories = [c for c in existing_categories if c not in ordered_categories]
        categories_to_process = ordered_categories + remaining_categories

    for category in categories_to_process:
        items = df[df['Category'] == category]
        if 'ID' in items.columns:
            items = items.sort_values(by='ID')

        adoc_content += f"\n== {category}\n\n"
        
        if category in PEGS_DEFINITIONS:
            adoc_content += f"{PEGS_DEFINITIONS[category]}\n\n"
        
        for _, row in items.iterrows():
            req_id = clean_text(row.get('ID', 'REQ-???'))
            title = clean_text(row.get('Title', 'Sans titre'))
            pegs_ref = clean_text(row.get('PEGS Ref', ''))
            priority = clean_text(row.get('Priority', '')) 
            desc = clean_text(row.get('Description', ''))
            rationale = clean_text(row.get('Rationale', ''))
            accept_crit = clean_text(row.get('Acceptance Criteria', ''))

            adoc_content += f"=== {req_id}: {title}\n\n"
            
            if pegs_ref:
                adoc_content += f"**Ref PEGS:** `{pegs_ref}`\n\n"

            if desc:
                adoc_content += f"[NOTE]\n.Description\n====\n{desc}\n====\n\n"

            
            if priority:
                adoc_content += f"**Priorité:** `{priority}`\n\n"
            
            if rationale:
                adoc_content += f"**Justification:** +\n{rationale}\n\n"
            
            if accept_crit:
                adoc_content += f"**Critères d'acceptation:** +\n{accept_crit}\n\n"
            
            adoc_content += "---\n\n"

    with open(OUTPUT_ADOC, "w", encoding="utf-8") as f:
        f.write(adoc_content)
    
    print(f"Succès : {OUTPUT_ADOC} généré.")

if __name__ == "__main__":
    generate_asciidoc()