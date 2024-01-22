# Définition de la classe lieu_de_detention
class LieuDeDetention:
    # Constructeur de la classe lieu_de_detention
    def __init__(self, denomination, adresse, type_activite, plan_du_lieu_de_detention):
        # Attributs de la classe
        self.denomination = denomination
        self.adresse = adresse
        self.type_activite = type_activite
        self.plan_du_lieu_de_detention = plan_du_lieu_de_detention
  
        # Phrase qui donne les caractéristiques du lieu de détention où se trouve le cheval du propriétaire.
        print(f"Le lieu où est gardé le cheval du propriétaire est {self.denomination}, situé à {self.adresse}. Pour vous y rendre, suivez le plan du lieu de détention : {self.plan_du_lieu_de_detention}. Cet endroit propose des activités liées aux {self.type_activite}.")

# Exemple d'utilisation de la classe
lieu_detention_cheval = LieuDeDetention("Stable de l'Étoile", "123 Rue des Écuries", "cours d'équitation", "chemin.pdf")
