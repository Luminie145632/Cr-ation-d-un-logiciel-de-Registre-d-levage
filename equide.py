from marechal_ferrand import Marechal_Ferrand
from veterinaire_sanitaire import Veterinaire_sanitaire
from veterinaire_traitant import Veterinaire_traitant
from marechal_ferrand import Marechal_Ferrand
from dentiste import Dentiste
from referent_bien_etre import Referent_bien_etre
from organisme_sanitaire import Organisme_sanitaire

class Equide():
    def __init__(self,lieu_habituel_detention,duree_detention,veterinaire_traitant)#poids,race,taille,nom):
     self.lieu_habituel_detention=lieu_habituel_detention
     self.duree_detention=duree_detention
     self.veterinaire_traitant=[]
     self.veteriaire_sanitaire=[]
     self.ref_bien_etre=[]
     self.Marechal_Ferrand=[]
     self.Dentiste=[]
     self.Organisme_sanitaire=[]
     
m=Marechal_Ferrand('zzzz','yyyy','06890912') 
vs=Veterinaire_sanitaire('Abul','Karl','22','Abul.karl@proton.me')
vt=Veterinaire_traitant('Abul','Karl','22','Abul.karl@proton.me')
d=Dentiste('Kill','4 rue de la gloire','06890912')     
e=Equide('Paris','3')
o=Organisme_sanitaire('Abul','Karl','22','Abul.karl@proton.me',' 5 rue station')
referent_bien_etre=Referent_bien_etre('Abul','Karl','06 77 91 56 21','Abul.karl@proton.me')

e.append(m)
e.append(vs)
e.append(vt)
e.append(d)
e.append(o)
e.append(referent_bien_etre)




