import extract
import save
import process

if __name__ == "__main__":
    # extraction des données
    Drugs = extract.extract_drugs("./data/drugs.csv")
    Pubmed = extract.extract_publications("./data/pubmed.csv")
    Pubmed.pop("\t")
    Clinals = extract.extract_clinical_trials("./data/clinical_trials.csv")

    # Generation du JSON de liaison
    result = {}
    for drug in Drugs:
        result[drug] = {
            "journal": process.find_in_journal(drug, Drugs, Pubmed, Clinals),
            "pubmed": process.find_in_source(drug, Drugs, Pubmed),
            "scientific_title": process.find_in_source(drug, Drugs, Clinals),
        }

    # Stockage du fichier JSON
    save.ecrire(result)
