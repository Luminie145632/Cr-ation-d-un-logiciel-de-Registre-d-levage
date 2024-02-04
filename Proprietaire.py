import Practicien

class Proprietaire(Practicien):
    def __init__(self, nom, prenom, adresse, numero_telephone, mail):
        super().__init__(nom, prenom, adresse, numero_telephone)
        self._mail = mail

    # Getter
    def get_mail(self):
        return self._mail

    # Setter
    def set_mail(self, mail):
        self._mail = mail