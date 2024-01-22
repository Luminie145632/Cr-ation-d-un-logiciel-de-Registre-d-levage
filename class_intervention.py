# Définition de la classe intervention
class Intervention:
    # Constructeur de la classe intervention
    def __init__(self, date, nom_animal, type_intervention, signature_cachet_veterinaire, nom_medicaments, voie_administration_dose, date_debut_traitement, date_fin_traitement, numero_ordonnance, delai_attente_competition, delai_attente_abattage_eclusion_abattage):
        # Attributs de la classe
        self.date = date
        self.nom_animal = nom_animal
        self.type_intervention = type_intervention
        self.signature_cachet_veterinaire = signature_cachet_veterinaire
        self.nom_medicaments = nom_medicaments
        self.voie_administration_dose = voie_administration_dose
        self.date_debut_traitement = date_debut_traitement
        self.date_fin_traitement = date_fin_traitement
        self.numero_ordonnance = numero_ordonnance
        self.delai_attente_competition = delai_attente_competition
        self.delai_attente_abattage_eclusion_abattage = delai_attente_abattage_eclusion_abattage

        # Phrase qui décrit l'intervention vétérinaire.
        print(f"Le {self.date}, une intervention a été réalisée sur l'animal nommé {self.nom_animal}. Cette intervention de type {self.type_intervention} a été effectuée par le vétérinaire dont la signature et le cachet sont {self.signature_cachet_veterinaire}. Les médicaments prescrits sont {self.nom_medicaments} et doivent être administrés par voie {self.voie_administration_dose}. Le traitement a débuté le {self.date_debut_traitement} et se termine le {self.date_fin_traitement}. Le numéro d'ordonnance associé à cette intervention est {self.numero_ordonnance}. Un délai d'attente de {self.delai_attente_competition} jours est requis avant toute participation à une compétition, et un délai d'attente de {self.delai_attente_abattage_eclusion_abattage} jours est nécessaire avant tout abattage ou exclusion d'abattage.")

# Exemple d'utilisation de la classe
intervention_animal = Intervention("01/02/2022", "Cheval A", "Vaccination", "Dr. Vétérinaire", "Vaccin XYZ", "intramusculaire", "01/02/2022", "15/02/2022", "12345", 7, 14)
