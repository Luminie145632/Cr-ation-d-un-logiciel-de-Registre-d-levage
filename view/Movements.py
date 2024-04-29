import tkinter as tk
import glob
import os
import Methode1
import json
from tkinter import *
from tkinter import messagebox, Frame, Entry, Button, Label, BOTH, ttk, Canvas



class Movements:
    
    def view_temporary_movements(self):




     with open('mouvements_temporaires.json', 'r') as file:
        data = json.load(file)

        # Parcourir les données
        for i, element in enumerate(data['mouvements'], start=1):
            text_fields = []

            # Parcourir les clés des sous-dictionnaires
            for key in element:
                # Récupérer la valeur correspondante à la clé
                value = element[key]

                # Trouver l'index de la colonne correspondant à la clé
                col_index = self.col_title.index(key)

                # Vérifier si l'indice i est valide pour self.data
                if i < len(self.data):
                    # Insérer la valeur dans le champ d'entrée correspondant
                    entry = self.data[i - 1][col_index]
                    entry.delete(0, 'end')  # Supprimer le contenu précédent
                    entry.insert(0, value)  # Insérer la nouvelle valeur
                else:
                    print(f"Erreur: L'indice {i} dépasse la taille de self.data.")

    # Ajouter les boutons en dehors de la boucle pour éviter la duplication
     self.bouton_ajouter_ligne = Button(self, text="Ajouter une ligne", command=self.ajouter_ligne)
     self.bouton_ajouter_ligne.grid(row=self.numberLines + 4, columnspan=len(self.col_title), sticky='nsew')

     btn_valider = Button(self, text="Modifier les informations", command=lambda: self.valider_informations_controle())
     btn_valider.grid(row=self.numberLines + 5, columnspan=len(self.col_title), sticky='nsew')       
# Redimensionner le canevas lorsque la taille de la fenêtre change
     self.bind("<Configure>", self.redimensionner_canevas)







      #   print("appel view animal")
      # #  self.navbar_canvas.create_window((0, 0), window=animal_frame, anchor='nw')
      #   with open('mouvements_temporaires.json', 'r') as file:
      #       data = json.load(file)

      #   for i, animal in enumerate( data['mouvements']  ):#, start=15):
      #       text_fields = []
      #       for j, key in enumerate(self.col_title):
      #           text_field = tk.Entry(self.inner_frame, width=3)
      #           text_field.grid(row=i, column=j, sticky='nsew')
      #           value = animal.get(key, '')
      #           text_field.insert(tk.END,  value)#  f"{key}: {value}\n")
      #           text_fields.append(text_field)
      #       self.data.append(text_fields)

      #   for j in range(len(self.col_title)):
      #     self.inner_frame.grid_columnconfigure(j, weight=1)
      #   self.inner_frame.update_idletasks()
      #   self.navbar_canvas.configure(scrollregion=self.navbar_canvas.bbox("all"))      





      #   print("appel view animal")
      # #  self.navbar_canvas.create_window((0, 0), window=animal_frame, anchor='nw')
      #   with open('mouvements_temporaires.json', 'r') as file:
      #       data = json.load(file)

      #   for i, animal in enumerate( data['mouvements']  ):#, start=15):
      #       text_fields = []
      #       for j, key in enumerate(self.col_title):
      #           text_field = tk.Entry(self.inner_frame, width=3)
      #           text_field.grid(row=i, column=j, sticky='nsew')
      #           value = animal.get(key, '')
      #           text_field.insert(tk.END,  value)#  f"{key}: {value}\n")
      #           text_fields.append(text_field)
      #       self.data.append(text_fields)

      #   for j in range(len(self.col_title)):
      #     self.inner_frame.grid_columnconfigure(j, weight=1)
      #   self.inner_frame.update_idletasks()
      #   self.navbar_canvas.configure(scrollregion=self.navbar_canvas.bbox("all"))      
