import Practicien

class Detenteur(Practicien):
    def __init__(self, nom, prenom, adresse, numero_telephone, SIRE):
        super().__init__(nom, prenom, adresse, numero_telephone)
        self.SIRE = SIRE

    # Getter
    def get_SIRE(self):
        return self.SIRE

    # Setter
    def set_SIRE(self, SIRE):
        self.SIRE = SIRE   

