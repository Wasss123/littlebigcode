import os
import csv
import json


def extract_drugs(filename):
    """
    extract_drugs: extracts drug data from drugs.csv

    filename : path of drugs.csv file

    return: dict containing id and name of drugs
    """
    drugs = {}
    with open(filename, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            drug_id = row["atccode"]
            drug_name = row["drug"]
            drugs[drug_id] = drug_name
    return drugs


def extract_publication(filename):
    # extraction des publication du fichier pubmed csv
    # Stocker les données dans un fichier json
    """
    extract_publications: extracts publication data from pubmed.csv

    filename : path of pubmed.csv csv pubmed.csv

    return: dict containing id as key and title date and journal as value
    """
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
    """
    extract_publications: extracts publication data from clinical_trials.csv

    filename : path of clinical_trials.csv

    return: dict containing id as key and title date and journal as value
    """
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
    """
    extract_publications: extracts publication data from pubmed.json

    filename : path of pubmed.json

    return: dict containing id as key and title date and journal as value
    """
    with open(filename, "r") as my_file:
        publications = json.load(my_file)
    return publications
