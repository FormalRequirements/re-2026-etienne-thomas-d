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
    "Goals": "Project vision: provide a simple and stable mobile-first application for tracking weight training, allowing users to visualize their progress and, in the future (V2), interact with sports coaches.",
    "Environment": "Usage context: mainly used on smartphones in gyms, taking into account potentially unstable network connectivity (offline mode) and the physical environment of training.",
    "System": "Functional scope: covers the Core features of V1 (session tracking, history), the Coaching extension of V2, and the advanced features of V3 (nutrition, wearables).",
    "Project": "Project framework: academic work using the PEGS methodology. Requirements are centralized in a single source (Excel) and documentation is generated automatically via GitHub Actions."
}

def clean_text(text):
    if pd.isna(text):
        return ""
    return str(text).strip().replace("\n", " +\n")

def generate_asciidoc():
    print(f"Looking for file: {EXCEL_PATH}")
    
    if not os.path.exists(EXCEL_PATH):
        print(f"Error: File not found at {EXCEL_PATH}")
        sys.exit(1)

    try:
        df = pd.read_excel(EXCEL_PATH)
        if 'Category' in df.columns:
            df['Category'] = df['Category'].str.capitalize()
    except Exception as e:
        print(f"Excel read error: {e}")
        sys.exit(1)

    today = datetime.date.today()
    adoc_content = f"""= LIFT-TRACK Requirements Document
:author: Thomas DOUMENG & Etienne CARPENTIER
:revdate: {today}
:doctype: book
:toc: macro
:toc-title: Table of Contents
:toclevels: 3
:sectnums:
:sectnumlevels: 2
:icons: font
:experimental:
:source-highlighter: highlight.js
:imagesdir: images

toc::[]

== Introduction

This document contains the specifications of the LIFT-TRACK project generated automatically.

[TIP]
====
Last update: {today}.\n
Data source: `{os.path.basename(EXCEL_PATH)}`
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
            title = clean_text(row.get('Title', 'Untitled'))
            pegs_ref = clean_text(row.get('PEGS Ref', ''))
            priority = clean_text(row.get('Priority', '')) 
            desc = clean_text(row.get('Description', ''))
            rationale = clean_text(row.get('Rationale', ''))
            accept_crit = clean_text(row.get('Acceptance Criteria', ''))

            adoc_content += f"=== {req_id}: {title}\n\n"
            
            if pegs_ref:
                adoc_content += f"**PEGS Ref:** `{pegs_ref}`\n\n"

            if desc:
                adoc_content += f"[NOTE]\n.Description\n====\n{desc}\n====\n\n"

            
            if priority:
                adoc_content += f"**Priority:** `{priority}`\n\n"
            
            if rationale:
                adoc_content += f"**Rationale:** +\n{rationale}\n\n"
            
            if accept_crit:
                adoc_content += f"**Acceptance Criteria:** +\n{accept_crit}\n\n"
            
            adoc_content += "---\n\n"

    with open(OUTPUT_ADOC, "w", encoding="utf-8") as f:
        f.write(adoc_content)
    
    print(f"Success: {OUTPUT_ADOC} generated.")

if __name__ == "__main__":
    generate_asciidoc()