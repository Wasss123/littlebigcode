import json

def ecrire(Resultat):
    #Stockage du fichier JSON
    with open('sortie.json', 'w') as mon_fichier:
	    json.dump(Resultat, mon_fichier)

