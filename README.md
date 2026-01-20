# Implémentation de la méthode PEGS – LIFT-TRACK (2026)

## 📌 Présentation du projet

Ce dépôt contient les exigences relative a *LIFT-TRACK*, une application **mobile-first** de suivi sportif destinée aux pratiquants de fitness et de musculation en cours de développement.

L’application est pensée pour une utilisation principale sur smartphone, en conditions réelles d’entraînement, avec une extension ultérieure vers des usages desktop, notamment pour des coachs sportifs.

---

## 🎯 Objectifs du dépôt

Ce dépôt a pour objectifs de :

- Mettre en œuvre la **méthodologie PEGS** sur un cas d’étude concret.
- Définir une **base d’exigences claire, cohérente et structurée** pour l’application.
- Centraliser toutes les exigences dans une **source unique de vérité**.

⚠️ Ce dépôt décrit **l’application dans sa globalité** (produit, usages, contraintes, évolution)  
et **ne se concentre pas sur les détails d’implémentation technique ou d’API**.

---

## 🧩 Périmètre fonctionnel de l’application

### Version 1 – Fonctionnalités cœur (Pratiquants)

La V1 vise à fournir une application **simple, stable et utilisable**, permettant aux pratiquants de :

- Renseigner les exercices réalisés lors d’une séance (charges, répétitions, séries).
- Consulter l’historique des séances et des performances par exercice.
- Créer et réutiliser des programmes d’entraînement.
- Visualiser leur progression dans le temps.
- Utiliser l’application en salle, dans un contexte mobile et avec une connectivité réseau potentiellement instable.

Cette version est volontairement limitée afin de favoriser une sortie rapide et une validation par l’usage réel.

---

### Version 2 – Coaching sportif

La V2 introduit un nouveau type d’utilisateur : le **coach sportif**, avec notamment :

- Des comptes distincts pratiquant / coach.
- L’association coach ↔ pratiquants.
- L’accès du coach aux données de suivi de ses coachés.
- La gestion et l’adaptation des programmes.
- Des outils de suivi simplifiés pour les coachs.

---

### Version 3 – Fonctionnalités avancées

La V3 prévoit des extensions à plus forte valeur ajoutée, telles que :

- Le suivi alimentaire.
- L’intégration de données issues de plateformes de santé ou de wearables.
- Des outils d’assistance à l’analyse (règles métier ou IA légère).
- Un mode de suivi de séance via montre connectée.

Ces fonctionnalités sont volontairement exclues des premières versions afin de maîtriser la complexité.

---

## 📐 Démarche d’ingénierie des exigences (PEGS)

Toutes les exigences sont structurées selon la méthode **PEGS** :

- **P – Project**  
  Rôles, livrables, processus, risques et contraintes organisationnelles.

- **E – Environment**  
  Contexte d’utilisation, hypothèses, contraintes terrain, invariants et glossaire.

- **G – Goals**  
  Objectifs, bénéfices attendus, scénarios d’usage, exclusions et parties prenantes.

- **S – System**  
  Composants, fonctionnalités, interfaces, priorisation et critères d’acceptation.

Chaque exigence est :
- identifiée de manière unique,
- classée selon PEGS,
- associée à des critères d’acceptation et de vérification.

---

## 📂 Structure du dépôt

- `\index.html`  
Rapport HTML généré par le script, permettant de consulter le rapport depuis un navigateur.

- `\README.md`  
Fichier markdown de présentation du projet et de la démarche méthodologique.

- \scripts :

    - `generate_doc.py`
    Script python permettant de générer le fichier .html à partir du fichier source contenant les exigences.

- \source :

    - `requirements_app_PEGS.xlsx`
    Tableau excel contenant l'intégralité des exigences exprimées pour le projet, 


---

## 🛠️ Génération automatique de la documentation

La génération de la documentation est **entièrement automatisée** via **GitHub Actions**.

### 🔄 Génération automatique
- Toute modification du fichier source **Excel contenant les exigences**
- suivie d’un **push sur le dépôt**
- déclenche automatiquement un workflow de génération de documentation.

👉 Cela garantit que les documents générés sont **toujours à jour** et strictement alignés avec la source des exigences.

### ▶️ Génération manuelle
Il est également possible de lancer manuellement la génération de la documentation :

1. Aller dans **Actions**
2. Sélectionner **All workflows**
3. Choisir **Generate Documentation**
4. Cliquer sur **Run workflow**

Cette option permet de rejouer la génération sans modifier les sources.

---

## 👥 Parties prenantes (Stakeholders)

Les principales parties prenantes identifiées sont :

- **Pratiquants** : utilisateurs finaux de l’application.
- **Coachs sportifs** : utilisateurs professionnels ciblés à partir de la V2.
- **Développeur** : responsable de la conception, du développement et de la maintenance.

L’identification explicite des parties prenantes permet de justifier les exigences et leur priorisation.

---

## ✍️ Auteurs

- **Étienne CARPENTIER**
- **Thomas DOUMENG**

---

## 📚 Contexte académique

Ce dépôt est réalisé dans le cadre d’un **travail académique en ingénierie des exigences**.  
Il vise à démontrer :

- la bonne application de la méthode PEGS,
- la cohérence et la qualité des exigences,
- une approche réaliste orientée produit et usage réel.

Le projet s’appuie volontairement sur un cas concret afin d’éviter une approche purement théorique.
