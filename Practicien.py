class Practicien:
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