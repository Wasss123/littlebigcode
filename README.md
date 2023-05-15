# littlebigcode
Ce projet est réalisé par Wassim KHELIL dans le cadre de son entretien technique avec l'entreprise LITTLEBIGCODE
Ce project contient :
## Le dossier data 
Ce dossier contients les données drugs.csv, pubmed.csv, pubmed.json et clinal_trials.csv
## Extract.py
Comporte 4 fonctions qui permmettent d'extraire les données des fichies à partir de leurs chemins
## process.py
comporte 2 functions qui permettent de chercher si un médicaments et mentionné dans une publication ou journal 
## save.py
comporte une fonction qui permet de sauvegarder dictionnaire qui représente le graph de liaison sous format de JSON
## main.py
La fonction principale qui fait appele au autre fonction pour extraire traiter, générer le graph de liasion et le sauvegarder 
## Le dossier test
Ce dossier comporte un sous dossier resources qui test.py afin de réaliser les test unitaires
