import Practicien

class Dentiste(Practicien):
    def __init__(self, nom, prenom, adresse, numero_telephone, _dentiste):
        super().__init__(nom, prenom, adresse, numero_telephone)
        self._dentsite = _dentiste

    # Getter
    def get_Dentiste(self):
        return self._marechal_ferrand

    # Setter
    def set_Dentiste(self, _dentiste):
        self._dentiste = _dentiste    

