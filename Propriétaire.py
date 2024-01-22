class Proprietaire():

    def __init__(self,nom,prenom,adresse,mail,tel):
        self.nom=nom
        self.prenom=prenom
        self.adresse=adresse
        self.mail=mail 
        self.tel=tel

    def gnom(self):
        return self.nom

    def gprenom(self):
        return self.nom_rue

    def gadresse(self):
        return self.adresse

    def gmail(self):
        return self.mail

    def gtel(self):
        return self.tel
        
    def snom(self,nnom):
        self.nom=nnom
    
    def sprenom(self,nprenom):
        self.prenom=nprenom
    
    def sadresse(self,nadresse):
        self.adresse=nadresse
    
    def smail(self,nmail):
        self.mail=nmail
    
    def stel(self,ntel):
        self.tel=ntel 

p=Proprietaire('Marco','Degibraltar','1 rue Corazon','maco@degibraltail@gmail.com','22222')

print(p.gtel())#self,nom,prenom,adresse,mail,tel 
p.stel('00000')
print(p.gtel())
