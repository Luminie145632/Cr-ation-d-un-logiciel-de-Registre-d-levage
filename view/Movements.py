import tkinter as tk
import glob
import os
import Methode1
import json
from tkinter import *
from tkinter import messagebox, Frame, Entry, Button, Label, BOTH, ttk, Canvas



class Movements:
    
    def view_temporary_movements(self):


        print( " c c  flag ce fichier Mouvements" )
        
        with open('/Creation_dun_logiciel_de_Registre_delevage/view/mouvements_temporaires.json', 'r') as file:
          data = json.load(file)
       

        # Parcourir les données
        for i, element in enumerate(data['mouvements_temporaires'], start=1):


            # Parcourir les clés des sous-dictionnaires
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

    # Ajouter les boutons en dehors de la boucle pour éviter la duplication
        self.bouton_ajouter_ligne = Button(self, text="Ajouter une ligne", command=self.ajouter_ligne)
        self.bouton_ajouter_ligne.grid(row=self.numberLines + 4, columnspan=len(self.col_title), sticky='nsew')

        btn_valider = Button(self, text="Modifier les informations", command= self.valider_mouvements_temporaires)
        btn_valider.grid(row=self.numberLines + 5, columnspan=len(self.col_title), sticky='nsew')       
# Redimensionner le canevas lorsque la taille de la fenêtre change
        self.bind("<Configure>", self.redimensionner_canevas)
