# mes_methodes.py

def ouvrir_fichier(Page_caractéristique_du_lieu_de_detention):
    try:
        fichier = open(Page_caractéristique_du_lieu_de_detention, 'r')
        contenu = Page_caractéristique_du_lieu_de_detention.read()
        print("Contenu du fichier :")
        print(contenu)
        return fichier  # Retourne le fichier ouvert
    except FileNotFoundError:
        print(f"Le fichier {Page_caractéristique_du_lieu_de_detention} n'a pas été trouvé.")
        return None

def fermer_fichier(accueil):
    if accueil:
        accueil.close()
        print("Fichier fermé.")
    else:
        print("Aucun fichier à fermer.")
