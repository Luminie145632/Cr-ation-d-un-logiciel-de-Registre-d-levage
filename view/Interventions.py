# Accueil.py  
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
        
class Interventions:

  def view_informations_intervention(self):
    with open('/Creation_dun_logiciel_de_Registre_delevage/view/Soins_Courant.json', 'r') as file:
        data = json.load(file)

        for i, element in enumerate(data['interventions'], start=1):
            print("indice" + str(i))

            for key in element:
                # Récupérer la valeur correspondante à la clé
                value = element[key]

                # Trouver l'index de la colonne correspondant à la clé
                col_index = self.col_title.index(key)
                print("indice "+str(i)+" < "+str(len(self.data))+ " ")   
                if i > len(self.data):
                    self.ajouter_ligne()

                # Vérifier si l'indice i est valide pour self.data
                if i <= len(self.data):
                    # Insérer la valeur dans le champ d'entrée correspondant
                    entry = self.data[i - 1][col_index]
                    entry.delete(0, 'end')  # Supprimer le contenu précédent
                    entry.insert(0, value)  # Insérer la nouvelle valeur
                else:
              #      self.ajouter_ligne
                    print(f"Erreur: L'indice {i} dépasse la taille de self.data.")
            
        self.bouton_ajouter_ligne = tk.Button(self, text="Ajouter une ligne", command=self.ajouter_ligne)
        self.bouton_ajouter_ligne.grid(row=self.numberLines + 4, columnspan=len(self.col_title), sticky='nsew')

        btn_valider = tk.Button(self, text="Modifier les informations", command=lambda: self.valider_informations_intervention())
        btn_valider.grid(row=self.numberLines + 5, columnspan=len(self.col_title), sticky='nsew')

        # Redimensionner le canevas lorsque la taille de la fenêtre change
        self.bind("<Configure>", self.redimensionner_canevas)
    
  def redimensionner_canevas(self, event):
     self.canvas.configure(scrollregion=self.canvas.bbox("all"))



