import sys
sys.path.insert(1, '/Creation_dun_logiciel_de_Registre_delevage/')
import tkinter as tk
import glob     
import os
import Methode1
import json
from tkinter import ttk
from tkinter import Button  
from PIL import Image, ImageTk

class EncadrementZootechnique:

 def view_zootechnical_supervision(self):
    import json
    from tkinter import Button

    with open(r'C:\Cr-ation-d-un-logiciel-de-Registre-d-levage\view\encadrement_zootechnique.json', 'r') as file:      
        data = json.load(file)

    for i, element in enumerate(data['encadrement'],start=0):
        print("indice " + str(i))

        # Parcourir les clés des sous-dictionnaires
        for key in element:
            # Récupérer la valeur correspondante à la clé
            value = element[key]
            # Trouver l'index de la colonne correspondant à la clé
            col_index = self.col_title.index(key)

            print("indice " + str(i))
            print("data " + str(col_index))
        
            # Insérer la valeur dans le champ d'entrée correspondant
            # Ajout de lignes si nécessaire
            while i >= len(self.data):
                self.ajouter_ligne()
                print("Ligne ajoutée pour index " + str(i))
       
            entry = self.data[i][col_index]
            print(  "  data ["+ str(i)+"]["+str(col_index) +"]="+str(entry)+" value "+str(value))
            entry.delete(0, 'end')  # Supprimer le contenu précédent
            entry.insert(0, value)  # Insérer la nouvelle valeur

    # Ajouter les boutons en dehors de la boucle pour éviter la duplication
    self.bouton_ajouter_ligne = Button(self, text="Ajouter une ligne", command=self.ajouter_ligne)
    self.bouton_ajouter_ligne.grid(row=self.numberLines + 4, columnspan=len(self.col_title), sticky='nsew')

    btn_valider = Button(self, text="Modifier les informations", command= self.valider_encadrement_Zootechnique_animaux())
    btn_valider.grid(row=self.numberLines + 5, columnspan=len(self.col_title), sticky='nsew')

    # Redimensionner le canevas lorsque la taille de la fenêtre change
    self.bind("<Configure>", self.redimensionner_canevas)   
  
  










  # flag
 def redimensionner_canevas(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

 def ajouter_ligne(self):
        print("flag ajouter ligne")
        # Function to add a new row
        row_data = []
               
        for j in range(len(self.col_title)):
              
            cell = tk.Entry(self.navbar_frame, width=22)
            cell.grid(row=self.numberLines+14, column=j, sticky='nsew')
            row_data.append(cell)
        self.data.append(row_data)
        self.numberLines += 1  
                # Configurer la croissance des colonnes
        for j in range(len(self.col_title)):
            self.inner_frame.grid_columnconfigure(j, weight=1)  
