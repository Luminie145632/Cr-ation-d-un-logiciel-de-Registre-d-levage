import Lieu
import tkinter

class LieuDetention(Lieu):
    def __init__(self, adresse, nom_rue_ville, code_postal, domaine_activite, types_activites):
        super().__init__(adresse, nom_rue_ville, code_postal, domaine_activite)
        self.types_activites = types_activites

    def gtypes_activites(self):
        return self.types_activites

    def stypes_activites(self, ntypes_activites):
        self.types_activites = ntypes_activites


# Exemple d'utilisation
ld = LieuDetention('5 rue de la prison', 'rue de la prison', '12345', 'Correctionnel', 'Prison')
print(ld.gcode_postal())  # Affiche le code postal initial
ld.scode_postal('54321')   # Change le code postal
print(ld.gcode_postal())  # Affiche le nouveau code postal
print(ld.gtypes_activites())  # Affiche le type d'activités initial
ld.stypes_activites('Centre de détention')  # Change le type d'activités
print(ld.gtypes_activites())  # Affiche le nouveau type d'activités