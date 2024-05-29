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
    with open(r'C:\Cr-ation-d-un-logiciel-de-Registre-d-levage\view\Soins_Courant.json', 'r') as file:
        data = json.load(file)

        for i, element in enumerate(data['interventions'], start=1):
            print("indice" + str(i))
            
            for key in element:
                print("indice key" + str(key))
                print(f"Erreur: L'indice {i} koko")
                value = element[key]

                col_index = self.col_title.index(key)

                while len(self.data) < i:
                    self.ajouter_ligne()

                entry = self.data[i - 1][col_index]
                entry.delete(0, 'end')
                entry.insert(0, value)

        self.bouton_ajouter_ligne = tk.Button(self, text="Ajouter une ligne", command=self.ajouter_ligne)
        self.bouton_ajouter_ligne.grid(row=self.numberLines + 4, columnspan=len(self.col_title), sticky='nsew')

        btn_valider = tk.Button(self, text="Modifier les informations", command=lambda: self.valider_informations_controle())
        btn_valider.grid(row=self.numberLines + 5, columnspan=len(self.col_title), sticky='nsew')

    # def view_informations_intervention(self):
    #   with open(r'C:\Cr-ation-d-un-logiciel-de-Registre-d-levage\view\Soins_Courant.json', 'r') as file:
    #     data = json.load(file)

    #     for i, element in enumerate(data['interventions'], start=1):
    #         print("indice" + str(i))
            
    #         for key in element:
    #             print("indice key" + str(key))
    #             print(f"Erreur: L'indice {i} koko")
    #             value = element[key]

    #             col_index = self.col_title.index(key)

    #             if i > len(self.data):
    #                 self.ajouter_ligne()

    #             if i <= len(self.data):
    #                 entry = self.data[i - 1][col_index]
    #                 entry.delete(0, 'end')
    #                 entry.insert(0, value)
    #             else:
    #                 print(f"Erreur: L'indice {i} dépasse la taille de self.data. numéro " + str(len(self.data)))

    #     self.bouton_ajouter_ligne = Button(self, text="Ajouter une ligne", command=self.ajouter_ligne)
    #     self.bouton_ajouter_ligne.grid(row=self.numberLines + 4, columnspan=len(self.col_title), sticky='nsew')

    #     btn_valider = Button(self, text="Modifier les informations", command=lambda: self.valider_informations_controle())
    #     btn_valider.grid(row=self.numberLines + 5, columnspan=len(self.col_title), sticky='nsew')


