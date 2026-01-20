import pandas as pd

def generate_asciidoc():
    # 1. Lecture du fichier Excel (à configurer plus tard avec ton fichier)
    # df = pd.read_excel('data.xlsx') 
    
    # 2. Création du contenu AsciiDoc
    # L'en-tête standard pour ressembler au template
    adoc_content = """
= Titre du Document
:doctype: book
:toc: left
:sectnums:
:toclevels: 3

== Introduction
Ceci est un texte généré automatiquement depuis Python.

== Section depuis Excel
"""
    
    # Simulation d'une boucle sur des données
    items = ["Donnée A", "Donnée B", "Donnée C"]
    for item in items:
        adoc_content += f"\n=== {item}\nDescription pour {item}...\n"

    # 3. Écriture du fichier .adoc
    with open("output.adoc", "w", encoding="utf-8") as f:
        f.write(adoc_content)
    
    print("Succès : Fichier output.adoc généré.")

if __name__ == "__main__":
    generate_asciidoc()