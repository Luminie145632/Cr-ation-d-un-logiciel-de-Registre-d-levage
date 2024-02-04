import Practicien

class Veterinaire(Practicien):
    def __init__(self, nom, prenom, adresse, numero_telephone, _Veterinaire):
        super().__init__(nom, prenom, adresse, numero_telephone)
        self._Veteriaire = _Veterinaire

    # Getter
    def get_Veterinaire(self):
        return self._marechal_ferrand

    # Setter
    def set_Veterinaire(self, _Veterinaire):
        self._Veterinaire = _Veterinaire    

