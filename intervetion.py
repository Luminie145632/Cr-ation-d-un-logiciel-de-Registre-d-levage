class Intervention:
    def __init__(self, date, nom_animal, type_intervention, signature_veterinaire, type_intervention,
                 nom_medicament, voie_administration, signature_cachet_veterinaire,
                 delai_attente_competitions, delai_attente_abattage):
        self._date = date
        self._nom_animal = nom_animal
        self._type_intervention = type_intervention
        self._signature_veterinaire = signature_veterinaire
        self._type_intervention = type_intervention
        self._nom_medicament = nom_medicament
        self._voie_administration = voie_administration
        self._signature_cachet_veterinaire = signature_cachet_veterinaire
        self._delai_attente_competitions = delai_attente_competitions
        self._delai_attente_abattage = delai_attente_abattage

    # Getters
    def get_date(self):
        return self._date

    def get_nom_animal(self):
        return self._nom_animal

    def get_type_intervention(self):
        return self._type_intervention

    def get_signature_veterinaire(self):
        return self._signature_veterinaire

    def get_type_intervention(self):
        return self._type_intervention

    def get_nom_medicament(self):
        return self._nom_medicament

    def get_voie_administration(self):
        return self._voie_administration

    def get_signature_cachet_veterinaire(self):
        return self._signature_cachet_veterinaire

    def get_delai_attente_competitions(self):
        return self._delai_attente_competitions

    def get_delai_attente_abattage(self):
        return self._delai_attente_abattage

    # Setters
    def set_date(self, date):
        self._date = date

    def set_nom_animal(self, nom_animal):
        self._nom_animal = nom_animal

    def set_type_intervention(self, type_intervention):
        self._type_intervention = type_intervention

    def set_signature_veterinaire(self, signature_veterinaire):
        self._signature_veterinaire = signature_veterinaire

    def set_type_intervention(self, type_intervention):
        self._type_intervention = type_intervention

    def set_nom_medicament(self, nom_medicament):
        self._nom_medicament = nom_medicament

    def set_voie_administration(self, voie_administration):
        self._voie_administration = voie_administration

    def set_signature_cachet_veterinaire(self, signature_cachet_veterinaire):
        self._signature_cachet_veterinaire = signature_cachet_veterinaire

    def set_delai_attente_competitions(self, delai_attente_competitions):
        self._delai_attente_competitions = delai_attente_competitions

    def set_delai_attente_abattage(self, delai_attente_abattage):
        self._delai_attente_abattage = delai_attente_abattage