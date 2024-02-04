class Mouvement:
    def __init__(self, date_entree, motif, etape_eventuelle, lieu_de_destination, date_de_retour):
        self._date_entree = date_entree
        self._motif = motif
        self._etape_eventuelle = etape_eventuelle
        self._lieu_de_destination = lieu_de_destination
        self._date_de_retour = date_de_retour

    # Accesseurs (getters)
    @property
    def date_entree(self):
        return self._date_entree

    @property
    def motif(self):
        return self._motif

    @property
    def etape_eventuelle(self):
        return self._etape_eventuelle

    @property
    def lieu_de_destination(self):
        return self._lieu_de_destination

    @property
    def date_de_retour(self):
        return self._date_de_retour

    # Mutateurs (setters)
    @date_entree.setter
    def date_entree(self, value):
        self._date_entree = value

    @motif.setter
    def motif(self, value):
        self._motif = value

    @etape_eventuelle.setter
    def etape_eventuelle(self, value):
        self._etape_eventuelle = value

    @lieu_de_destination.setter
    def lieu_de_destination(self, value):
        self._lieu_de_destination = value

    @date_de_retour.setter
    def date_de_retour(self, value):
        self._date_de_retour = value