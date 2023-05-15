import extract
import save
import process

if __name__ == "__main__":
    # data extraction
    drugs = extract.extract_drugs("./data/drugs.csv")
    pubmed = extract.extract_publication("./data/pubmed.csv")
    pubmed.pop("\t")
    clinals = extract.extract_clinical_trials("./data/clinical_trials.csv")

    # JSON generation
    result = {}
    for drug in drugs:
        result[drug] = {
            "journal": process.find_in_journal(drug, drugs, pubmed, clinals),
            "pubmed": process.find_in_source(drug, drugs, pubmed),
            "scientific_title": process.find_in_source(drug, drugs, clinals),
        }

    # saving JSON file
    save.write(result)
