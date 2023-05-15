import os
import csv
import json


def extract_drugs(filename):
    # extraction des medicament du fichier drug csv
    # Stocker les données dans un fichier json
    drugs = {}
    with open(filename, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            drug_id = row["atccode"]
            drug_name = row["drug"]
            drugs[drug_id] = drug_name
    return drugs


def extract_publications(filename):
    # extraction des publication du fichier pubmed csv
    # Stocker les données dans un fichier json
    publications = {}
    with open(filename, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            publication_id = row["id"]
            title = row["title"]
            journal = row["journal"]
            date = row["date"]
            publications[publication_id] = {
                "title": title,
                "journal": journal,
                "date": date,
            }
    return publications


def extract_clinical_trials(filename):
    # extraction des medicament du fichier clinal trial csv
    # Stocker les données dans un fichier json
    clinical_trials = {}
    with open(filename, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            trial_id = row["id"]
            title = row["scientific_title"]
            journal = row["journal"]
            date = row["date"]
            clinical_trials[trial_id] = {
                "title": title,
                "journal": journal,
                "date": date,
            }
    return clinical_trials


def extract_publications_json(filename):
    with open(filename, "r") as mon_fichier:
        publications = json.load(mon_fichier)
    return publications
