import Practicien

class Responsable_Bien_etre(Practicien):
    def __init__(self, nom, prenom, adresse, numero_telephone, id_bien_etre):
        super().__init__(nom, prenom, adresse, numero_telephone)
        self._id_bien_etre = id_bien_etre

    # Getter
    def get_id_bien_etre(self):
        return self._id_bien_etre

    # Setter
    def set_id_bien_etre(self, id_bien_etre):
        self._id_bien_etre = id_bien_etre