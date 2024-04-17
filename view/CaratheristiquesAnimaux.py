#sys.path.insert(1, '/Creation_dun_logiciel_de_Registre_delevage/')
import tkinter as tk
import glob
import os
import Methode1
import json

from tkinter import ttk
from tkinter import Button  
from PIL import Image, ImageTk
from tkinter import *
from tkinter import messagebox, Frame, Entry, Button, Label, BOTH, ttk, Canvas
from tkinter import scrolledtext



class CaractheristiquesAnimaux:

    def view_animals(self):
        print("koko")
        with open('caratheristiques_animaux.json', 'r') as file:
            data = json.load(file)

        # Affichage des animaux dans les zones de texte
        for i, animal in enumerate(data['caractheristiques'], start=15):
            text_fields = []

            for j, key in enumerate(self.col_title):
                # Utilisation de ScrolledText à la place de Entry
                text_field = scrolledtext.ScrolledText(self, width=30, height=1)
                text_field.grid(row=i, column=j, sticky='nsew')
                # Récupérer la valeur de la clé si elle existe, sinon utiliser une chaîne vide
                value = animal.get(key, '')
                text_field.insert(END, f"{key}: {value}\n")
                text_fields.append(text_field)

            self.data.append(text_fields)

        self.bouton_ajouter_ligne = Button(self, text="Ajouter une ligne", command=self.ajouter_ligne)
        self.bouton_ajouter_ligne.grid(row=self.numberLines + 4, columnspan=len(self.col_title), sticky='nsew')

        btn_valider = Button(self, text="Modifier les informations", command=self.valider_caratheristiques_animaux)
        btn_valider.grid(row=self.numberLines + 5, columnspan=len(self.col_title), sticky='nsew')

        # Redimensionner le canevas lorsque la taille de la fenêtre change
        self.bind("<Configure>", self.redimensionner_canevas)

    def redimensionner_canevas(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

      # text_field.grid(row=i, column=j, sticky='nsew')
        #     # Récupérer la valeur de la clé si elle existe, sinon utiliser une chaîne vide
        # value = animal.get(key, '')
        # text_field.insert(END, f"{key}: {value}\n")
        # text_fields.append(text_field) #meme si les text fields descendent jusqy'en bas de la fenetre, je puissent descendre pour les voir via une barre de navigation



# import sys
# sys.path.insert(1, '/Creation_dun_logiciel_de_Registre_delevage/')
# import tkinter as tk
# import glob
# import os
# import Methode1
# import json

# from tkinter import ttk
# from tkinter import Button  
# from PIL import Image, ImageTk
# from tkinter import *
# from tkinter import messagebox, Frame, Entry, Button, Label, BOTH, ttk, Canvas

# class CaractheristiquesAnimaux:
#     def view_animals(self):
#         print("koko")
#         with open('caratheristiques_animaux.json', 'r') as file:
#             data = json.load(file)

#         # Création d'un canevas avec une barre de défilement verticale
#         self.canvas = tk.Canvas(self)
#         scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
#         scrollbar.grid(row=0, column=len(self.col_title), sticky='ns')
#         self.canvas.config(yscrollcommand=scrollbar.set)
#         self.canvas.grid(row=15, column=0, columnspan=len(self.col_title), sticky='nsew')

#         # Conteneur pour les champs de texte
#         self.frame = tk.Frame(self.canvas)
#         self.canvas.create_window((0, 0), window=self.frame, anchor='nw')

#         # Affichage des animaux dans les champs de texte
#         for i, animal in enumerate(data['caractheristiques'], start=15):
#             text_fields = []
#             for j, key in enumerate(self.col_title):
#                 text_field = Entry(self.frame, width=3)
#                 text_field.grid(row=i, column=j, sticky='nsew')
#                 value = animal.get(key, '')
#                 text_field.insert(END, f"{key}: {value}\n")
#                 text_fields.append(text_field)
#             self.data.append(text_fields)

#         # Bouton pour ajouter une ligne
#         self.bouton_ajouter_ligne = Button(self.frame, text="Ajouter une ligne", command=self.ajouter_ligne)
#         self.bouton_ajouter_ligne.grid(row=self.numberLines + 4, columnspan=len(self.col_title), sticky='nsew')

#         # Bouton pour modifier les informations
#         btn_valider = Button(self.frame, text="Modifier les informations", command=self.valider_caratheristiques_animaux)
#         btn_valider.grid(row=self.numberLines + 5, columnspan=len(self.col_title), sticky='nsew')

#         # Redimensionner le canevas lorsque la taille de la fenêtre change
#         self.bind("<Configure>", self.redimensionner_canevas)

#     def redimensionner_canevas(self, event):
#         self.canvas.configure(scrollregion=self.canvas.bbox("all"))