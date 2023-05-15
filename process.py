def find_in_source(drug, Drugs, source):
    """
    find_in_source does Recherche de drug dans les publication

    drug : id of the drug
    Drugs: dict of all drugs
    source: either Pubmed dict or Cinals dict

    return: une list de toutes les publications et leurs dates dans lesquelles figures le mot du medicament
    """
    assert isinstance(drug, dict)
    list = []
    for pub in source:
        if Drugs[drug].lower() in source[pub]["title"].lower():
            list.append({pub: source[pub]["date"]})
    return list


def find_in_journal(drug : dict, Drugs : dict, Pubmed, Clinals) -> list:
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
