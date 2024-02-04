class RegistreElevage:
    def __init__(self, nom_organisme, prenom_organisme, mail):
        self._nom_organisme = nom_organisme
        self._prenom_organisme = prenom_organisme
        self._mail = mail

    # Accesseurs
    def get_nom_organisme(self):
        return self._nom_organisme

    def get_prenom_organisme(self):
        return self._prenom_organisme

    def get_mail(self):
        return self._mail

    # Mutateurs
    def set_nom_organisme(self, nom_organisme):
        self._nom_organisme = nom_organisme

    def set_prenom_organisme(self, prenom_organisme):
        self._prenom_organisme = prenom_organisme

    def set_mail(self, mail):
        self._mail = mail

# Exemple d'utilisation
if __name__ == "__main__":
    # Création d'une instance de la classe RegistreElevage
    registre = RegistreElevage("NomOrg", "PrenomOrg", "email@exemple.com")

    # Utilisation des accesseurs
    print("Nom de l'organisme:", registre.get_nom_organisme())
    print("Prénom de l'organisme:", registre.get_prenom_organisme())
    print("Adresse e-mail:", registre.get_mail())

    # Utilisation des mutateurs
    registre.set_nom_organisme("NouveauNomOrg")
    registre.set_prenom_organisme("NouveauPrenomOrg")
    registre.set_mail("nouveau_email@exemple.com")

    # Affichage des valeurs mises à jour
    print("\nValeurs mises à jour:")
    print("Nom de l'organisme:", registre.get_nom_organisme())
    print("Prénom de l'organisme:", registre.get_prenom_organisme())
    print("Adresse e-mail:", registre.get_mail())