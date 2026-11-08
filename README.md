# Analyse des ventes avec Python et SQL

## Présentation du projet

Ce projet a été réalisé dans le cadre d'un exercice de formation Simplon.

L'objectif est d'analyser les ventes d'une entreprise sur une période de 20 jours afin de calculer le chiffre d'affaires, d'étudier les quantités vendues par produit et de comparer les résultats entre les régions.

Les données sont traitées avec SQL et Python, puis représentées sous forme de graphiques interactifs.

## Technologies utilisées

- **Python** : traitement et analyse des données.
- **Pandas** : manipulation et regroupement des données.
- **Plotly Express** : création des graphiques interactifs.
- **SQL** : calcul des ventes et du chiffre d'affaires.
- **Git et GitHub** : gestion des versions et publication du projet.

## Analyses réalisées

- Calcul du chiffre d'affaires total.
- Calcul des quantités vendues par produit.
- Calcul du chiffre d'affaires par produit.
- Analyse des ventes par région.

## Résultats obtenus

Sur les 20 jours étudiés, l'entreprise a réalisé un chiffre d'affaires total de **44 825 €**, pour **3 380 unités vendues**.

| Produit | Quantités vendues | Chiffre d'affaires |
|---|---:|---:|
| Produit A | 1 750 | 17 500 € |
| Produit B | 1 055 | 15 825 € |
| Produit C | 575 | 11 500 € |
| **Total** | **3 380** | **44 825 €** |

Le produit A est le plus vendu et génère le chiffre d'affaires le plus important. Le produit C se vend moins, mais possède le prix unitaire le plus élevé.

## Visualisations

Le projet contient trois graphiques HTML interactifs :

- [Chiffre d'affaires par produit](ca-par-produit.html)
- [Quantités vendues par produit](quantite-par-produit.html)
- [Quantités vendues par région](ventes-par-region.html)

Ces fichiers peuvent être téléchargés puis ouverts dans un navigateur pour consulter les graphiques.

## Organisation du projet

- `script.py` : programme Python réalisant les calculs et les graphiques.
- `requetes.sql` : requêtes SQL utilisées pour l'analyse.
- `synthese.md` : synthèse des résultats obtenus.
- `requirements.txt` : bibliothèques Python nécessaires.
- `ca-par-produit.html` : graphique du chiffre d'affaires par produit.
- `quantite-par-produit.html` : graphique des quantités par produit.
- `ventes-par-region.html` : graphique des ventes par région.

## Exécution du projet

Installer les bibliothèques nécessaires :

```bash
python -m pip install -r requirements.txt
```

Exécuter ensuite le programme :

```bash
python script.py
```

Le programme récupère les données depuis un fichier CSV publié sur Google Sheets. Une connexion Internet est donc nécessaire.

Les graphiques HTML sont générés dans le dossier du projet.

## Auteur

**max43700**

Projet réalisé dans le cadre d'une formation Simplon.