class Lieu:

    def __init__(self,adresse,nom_rue_ville,code_postal,domaine_activite):
        self.adresse=adresse
        self.nom_rue_ville=nom_rue_ville
        self.code_postal=code_postal
        self.domaine_activite=domaine_activite


    def adresse(self):
        return self.adresse
    def gnom_rue(self):
        return self.nom_rue
    def gcode_postal(self):
        return self.code_postal
    def gdomaine_activite(self):
        return self.domaine_activite
    
    def sadresse(self,nadresse):
        self.adresse=nadresse
    def snom_rue(self,nnom_rue):
        self.nom_rue=nnom_rue
    def scode_postal(self,ncode_postal):
        self.code_postal=ncode_postal
    def sdomaine_activite(self,ndomaine_activite):
        self.domaine_activite=ndomaine_activite  


l= Lieu('4 rue du coq','rue du coq','778','YYY')
print(l.gcode_postal()) 
l.scode_postal('99999')
print(l.gcode_postal())
