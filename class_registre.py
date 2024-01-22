# Définition de la classe registre
class Registre:
    # Constructeur de la classe registre
    def __init__(self, date, organisme_controle, nom_controle, cachet, signature):
        # Attributs de la classe
        self.date = date
        self.organisme_controle = organisme_controle
        self.nom_controle = nom_controle
        self.cachet = cachet
        self.signature = signature

        # Phrase qui donne des informations sur le contrôle du cheval
        print(f"L'{self.organisme_controle} a effectué un contrôle le {self.date}. Le contrôle a été effectué par {self.nom_controle}. Cachet : {self.cachet}, Signature : {self.signature}.")

# Exemple d'utilisation de la classe Registre
controle_cheval = Registre("01/02/2022", "OrganismeXYZ", "Inspecteur ABC", "CachetXYZ", "SignatureXYZ")
