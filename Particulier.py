class Detenteur:
    def __init__(self, nom, prenom, adresse, numero_telephone):
        self._nom = nom
        self._prenom = prenom
        self._adresse = adresse
        self._numero_telephone = numero_telephone

    # Getters
    def get_nom(self):
        return self._nom

    def get_prenom(self):
        return self._prenom

    def get_adresse(self):
        return self._adresse

    def get_numero_telephone(self):
        return self._numero_telephone

    # Setters
    def set_nom(self, nom):
        self._nom = nom

    def set_prenom(self, prenom):
        self._prenom = prenom

    def set_adresse(self, adresse):
        self._adresse = adresse

    def set_numero_telephone(self, numero_telephone):
        self._numero_telephone = numero_telephone

# Particulier.py
class Particulier(Detenteur):
    def __init__(self, nom, prenom, adresse, numero_telephone, num_agrit):
        super().__init__(nom, prenom, adresse, numero_telephone)
        self._num_agrit = num_agrit

    # Getter
    def get_num_agrit(self):
        return self._num_agrit

    # Setter
    def set_num_agrit(self, num_agrit):
        self._num_agrit = num_agrit

# Exemple d'utilisation
if __name__ == "__main__":
    # Création d'une instance de la classe Particulier
    particulier = Particulier("NomParticulier", "PrenomParticulier", "AdresseParticulier", "123456789", "123ABC")

    # Utilisation des accesseurs
    print("Nom du particulier:", particulier.get_nom())
    print("Prénom du particulier:", particulier.get_prenom())
    print("Adresse du particulier:", particulier.get_adresse())
    print("Numéro de téléphone du particulier:", particulier.get_numero_telephone())
    print("Numéro agrit du particulier:", particulier.get_num_agrit())

    # Utilisation des mutateurs
    particulier.set_nom("NouveauNomParticulier")
    particulier.set_prenom("NouveauPrenomParticulier")
    particulier.set_adresse("NouvelleAdresseParticulier")
    particulier.set_numero_telephone("987654321")
    particulier.set_num_agrit("456XYZ")

    # Affichage des valeurs mises à jour
    print("\nValeurs mises à jour:")
    print("Nom du particulier:", particulier.get_nom())
    print("Prénom du particulier:", particulier.get_prenom())
    print("Adresse du particulier:", particulier.get_adresse())
    print("Numéro de téléphone du particulier:", particulier.get_numero_telephone())
    print("Numéro agrit du particulier:", particulier.get_num_agrit())