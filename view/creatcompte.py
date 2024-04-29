import json

def checkfile(id,password):
 with open("comptes.json") as comptes:
    data=json.load(comptes)
    for compte in enumerate( data['comptes']  ):#, start=15):
      if( (id==compte["nom_user"])&&(id==compte["password"])   ):  
        return True
      else:
        return false


      