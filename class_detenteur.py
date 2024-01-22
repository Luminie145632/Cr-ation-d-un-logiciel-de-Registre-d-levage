# Définition de la classe détenteur
class Detenteur:
    # Constructeur de la classe détenteur
    def __init__(self, Nom_du_proprietaire, Prenom_du_proprietaire, date_ouverture_elevage):
        # Attributs de la classe
        self.Nom_du_proprietaire = Nom_du_proprietaire
        self.Prenom_du_proprietaire = Prenom_du_proprietaire
        self.date_ouverture_elevage = date_ouverture_elevage

        # Phrase qui donne le prénom et le nom du propriétaire du cheval.
        print(f"Le propriétaire de ce cheval s'appelle {self.Nom_du_proprietaire} {self.Prenom_du_proprietaire} et son élevage de chevaux a ouvert le {self.date_ouverture_elevage}.")

# Exemple d'utilisation de la classe
proprietaire_cheval = Detenteur("Dupont", "Jean", "18/06/2003")
