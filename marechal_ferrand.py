import MarechalFerrand
import Dentiste

class RegistreElevage:
    def __init__(self, nom_organisme, prenom_organisme, tel, mail, marechal_ferrand, dentiste):
        self._nom_organisme = nom_organisme
        self._prenom_organisme = prenom_organisme
        self._tel = tel
        self._mail = mail
        self._marechal_ferrand = marechal_ferrand
        self._dentiste = dentiste

    # Getters
    def get_nom_organisme(self):
        return self._nom_organisme

    def get_prenom_organisme(self):
        return self._prenom_organisme

    def get_tel(self):
        return self._tel

    def get_mail(self):
        return self._mail

    def get_marechal_ferrand(self):
        return self._marechal_ferrand

    def get_dentiste(self):
        return self._dentiste

    # Setters
    def set_nom_organisme(self, nom_organisme):
        self._nom_organisme = nom_organisme

    def set_prenom_organisme(self, prenom_organisme):
        self._prenom_organisme = prenom_organisme

    def set_tel(self, tel):
        self._tel = tel

    def set_mail(self, mail):
        self._mail = mail

    def set_marechal_ferrand(self, marechal_ferrand):
        self._marechal_ferrand = marechal_ferrand

    def set_dentiste(self, dentiste):
        self._dentiste = dentiste

# Exemple d'utilisation
if __name__ == "__main__":
    # Création d'objets MarechalFerrand et Dentiste
    marechal_ferrand = MarechalFerrand("NomMarechal", "PrenomMarechal", "AdresseMarechal", "123456789", "SpecialiteMarechal")
    dentiste = Dentiste("NomDentiste", "PrenomDentiste", "AdresseDentiste", "987654321", "SpecialiteDentiste")

    # Création d'une instance de la classe RegistreElevage
    registre_elevage = RegistreElevage("NomOrganisme", "PrenomOrganisme", 123456789, "mail@organisme.com", marechal_ferrand, dentiste)

    # Utilisation des accesseurs
    print("Nom de l'organisme:", registre_elevage.get_nom_organisme())
    print("Prénom de l'organisme:", registre_elevage.get_prenom_organisme())
    print("Téléphone de l'organisme:", registre_elevage.get_tel())
    print("Mail de l'organisme:", registre_elevage.get_mail())
    print("Marechal Ferrand:", registre_elevage.get_marechal_ferrand().get_nom(), registre_elevage.get_marechal_ferrand().get_prenom())
    print("Dentiste:", registre_elevage.get_dentiste().get_nom(), registre_elevage.get_dentiste().get_prenom())

