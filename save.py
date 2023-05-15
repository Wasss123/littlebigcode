import json
def write(result):

    """
    write saves the json file

    result : dict representing the graph

    return: None
    """
    with open("graph.json", "w") as mon_fichier:
        json.dump(result, mon_fichier)
