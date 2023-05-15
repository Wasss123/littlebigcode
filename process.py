def find_in_source(drug : dict, drugs : dict, source : dict) -> list:
    """
    find_in_source searches if the given drug is present in the source

    drug : id of the drug
    drugs: dict of all drugs
    source: either pubmed dict or Cinals dict

    return: a list of all publications and date in which the drug is mentionned
    """
    list = []
    for pub in source:
        if drugs[drug].lower() in source[pub]["title"].lower():
            list.append({pub: source[pub]["date"]})
    return list


def find_in_journal(drug : dict, drugs : dict, pubmed : dict, clinals : dict) -> list:
    """
    find_in_source searches if the given drug is present in the source

    drug : id of the drug
    drugs: dict of all drugs
    pubmed: dict of all medical publications
    clinals: dict of all clinal trials

    return: a list of all journals and date in which the drug is mentionned
    """
    list = []
    for pub in pubmed:
        if (
            drugs[drug].lower() in pubmed[pub]["title"].lower()
            and {pubmed[pub]["journal"]: pubmed[pub]["date"]} not in list
        ):
            list.append({pubmed[pub]["journal"]: pubmed[pub]["date"]})
    for pub in clinals:
        if (
            drugs[drug].lower() in clinals[pub]["title"].lower()
            and {clinals[pub]["journal"]: clinals[pub]["date"]} not in list
        ):
            list.append({clinals[pub]["journal"]: clinals[pub]["date"]})
    return list
