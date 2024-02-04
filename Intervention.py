from datetime import date
import _json

class Intervention:
    def __init__(self, intervention_date, nom_animal, type_intervention, signature_cachet_veterinaire,
                 nom_medicaments, voie_administration, delai_attentes_competitions, delai_attentes_abattage):
        self._intervention_date = intervention_date
        self._nom_animal = nom_animal
        self._type_intervention = type_intervention
        self._signature_cachet_veterinaire = signature_cachet_veterinaire
        self._nom_medicaments = nom_medicaments
        self._voie_administration = voie_administration
        self._delai_attentes_competitions = delai_attentes_competitions
        self._delai_attentes_abattage = delai_attentes_abattage

    # Accesseurs
    def get_intervention_date(self):
        return self._intervention_date

    def get_nom_animal(self):
        return self._nom_animal

    def get_type_intervention(self):
        return self._type_intervention

    def get_signature_cachet_veterinaire(self):
        return self._signature_cachet_veterinaire

    def get_nom_medicaments(self):
        return self._nom_medicaments

    def get_voie_administration(self):
        return self._voie_administration

    def get_delai_attentes_competitions(self):
        return self._delai_attentes_competitions

    def get_delai_attentes_abattage(self):
        return self._delai_attentes_abattage

    # Mutateurs
    def set_intervention_date(self, intervention_date):
        self._intervention_date = intervention_date

    def set_nom_animal(self, nom_animal):
        self._nom_animal = nom_animal

    def set_type_intervention(self, type_intervention):
        self._type_intervention = type_intervention

    def set_signature_cachet_veterinaire(self, signature_cachet_veterinaire):
        self._signature_cachet_veterinaire = signature_cachet_veterinaire

    def set_nom_medicaments(self, nom_medicaments):
        self._nom_medicaments = nom_medicaments

    def set_voie_administration(self, voie_administration):
        self._voie_administration = voie_administration

    def set_delai_attentes_competitions(self, delai_attentes_competitions):
        self._delai_attentes_competitions = delai_attentes_competitions

    def set_delai_attentes_abattage(self, delai_attentes_abattage):
        self._delai_attentes_abattage = delai_attentes_abattage







def addIntervention(interventions_list,date, NomAnimal, TypeIntervention, Signature_cachet,NomMedicament, VoieAdministration, number):
 i=Intervention(date(2024, 1, 28), NomAnimal, TypeIntervention, Signature_cachet,NomMedicament, VoieAdministration, 7, date(2024, 2, 4))  
 interventions_list.append(i) 
 
# Conversion en JSON et écriture dans un fichier
 with open('interventions.json', 'w') as json_file:
    _json.dump({"interventions": interventions_list}, json_file, indent=2)



# Exemple d'utilisation
if __name__ == "__main__":
    # Création d'une instance de la classe Intervention
    intervention = Intervention(date(2024, 1, 28), "NomAnimal", "TypeIntervention", "SignatureCachetVet",
                                "NomMedicaments", "VoieAdministration", 7, date(2024, 2, 4))

    # Utilisation des accesseurs
    print("Date de l'intervention:", intervention.get_intervention_date())
    print("Nom de l'animal:", intervention.get_nom_animal())
    print("Type d'intervention:", intervention.get_type_intervention())
    print("Signature/cachet vétérinaire:", intervention.get_signature_cachet_veterinaire())
    print("Nom des médicaments:", intervention.get_nom_medicaments())
    print("Voie d'administration:", intervention.get_voie_administration())
    print("Délai d'attente pour compétitions:", intervention.get_delai_attentes_competitions())
    print("Délai d'attente pour abattage:", intervention.get_delai_attentes_abattage())

    # Utilisation des mutateurs
    intervention.set_intervention_date(date(2024, 2, 1))
    intervention.set_nom_animal("NouveauNomAnimal")
    intervention.set_type_intervention("NouveauTypeIntervention")
    intervention.set_signature_cachet_veterinaire("NouvelleSignatureCachetVet")
    intervention.set_nom_medicaments("NouveauNomMedicaments")
    intervention.set_voie_administration("NouvelleVoieAdministration")
    intervention.set_delai_attentes_competitions(14)
    intervention.set_delai_attentes_abattage(date(2024, 2, 18))

    # Affichage des valeurs mises à jour
    print("\nValeurs mises à jour:")
    print("Date de l'intervention:", intervention.get_intervention_date())
    print("Nom de l'animal:", intervention.get_nom_animal())
    print("Type d'intervention:", intervention.get_type_intervention())
    print("Signature/cachet vétérinaire:", intervention.get_signature_cachet_veterinaire())
    print("Nom des médicaments:", intervention.get_nom_medicaments())
    print("Voie d'administration:", intervention.get_voie_administration())
    print("Délai d'attente pour compétitions:", intervention.get_delai_attentes_competitions())
    print("Délai d'attente pour abattage:", intervention.get_delai_attentes_abattage())
    

    


