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
        with open(r'C:\Cr-ation-d-un-logiciel-de-Registre-d-levage\view\encadrement_zootechnique.json', 'r') as file:      

            data = json.load(file)



            for i, element in enumerate(data['encadrement'], start=1):

                print("indice "+str(i))
                while i > len(self.data):
                    self.ajouter_ligne()


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
                    elif i>=len(self.data):
                      while i >=len(self.data):
                       self.ajouter_ligne()
                       print(f"Erreur: L'indice {i} dépasse la taille de self.data.")

    # Ajouter les boutons en dehors de la boucle pour éviter la duplication
        self.bouton_ajouter_ligne = Button(self, text="Ajouter une ligne", command=self.ajouter_ligne)
        self.bouton_ajouter_ligne.grid(row=self.numberLines + 4, columnspan=len(self.col_title), sticky='nsew')

        btn_valider = Button(self, text="Modifier les informations", command=lambda: self.valider_encadrement_Zootechnique_animaux)
        btn_valider.grid(row=self.numberLines + 5, columnspan=len(self.col_title), sticky='nsew')       
# Redimensionner le canevas lorsque la taille de la fenêtre change
        self.bind("<Configure>", self.redimensionner_canevas)


    def redimensionner_canevas(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

