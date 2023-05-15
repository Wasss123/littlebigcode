def find_in_source(drug, Drugs, source):
    # Recherche de drug dans les publication
    # retourner une list de toutes les publications et leurs dates
    # dans lesquelles figures le mot du médicament
    list = []
    for pub in source:
        if Drugs[drug].lower() in source[pub]["title"].lower():
            list.append({pub: source[pub]["date"]})
    return list


def find_in_journal(drug, Drugs, Pubmed, Clinals):
    # Recherche de drug dans les journaux
    # retourner une list de toutes les publications et leurs dates
    # dans lesquelles figures le mot du médicament
    list = []
    for pub in Pubmed:
        if (
            Drugs[drug].lower() in Pubmed[pub]["title"].lower()
            and {Pubmed[pub]["journal"]: Pubmed[pub]["date"]} not in list
        ):
            list.append({Pubmed[pub]["journal"]: Pubmed[pub]["date"]})
    for pub in Clinals:
        if (
            Drugs[drug].lower() in Clinals[pub]["title"].lower()
            and {Clinals[pub]["journal"]: Clinals[pub]["date"]} not in list
        ):
            list.append({Clinals[pub]["journal"]: Clinals[pub]["date"]})
    return list
