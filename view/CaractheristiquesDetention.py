# Accueil.py  
import sys
sys.path.insert(1, '/Creation_dun_logiciel_de_Registre_delevage/')
import tkinter as tk
from tkinter import ttk
from tkinter import Button  
from PIL import Image, ImageTk
import glob
import os
import Methode1
import json
from tkinter import *
from tkinter import messagebox, Frame, Entry, Button, Label, BOTH, ttk, Canvas

class CaratheristiquesDetention:
 
 def __init__(self, width, col_titles, height):
        super().__init__()

        self.numberColumns = width 
        self.numberLines = height
        self.col_title = col_titles
        self.data = []  

        self.title("Accueil")
        self.geometry("1920x1080")

        # Création du canevas pour le panneau
        self.navbar_canvas = tk.Canvas(self, bd=2, relief=tk.GROOVE)
        self.navbar_canvas.grid(row=10, columnspan=len(self.col_title), sticky="ew")

        # Création du cadre à l'intérieur du canevas
        self.navbar_frame = tk.Frame(self.navbar_canvas)
        self.navbar_canvas.create_window((0, 0), window=self.navbar_frame, anchor='nw')

        # Ajoutez les éléments (champs d'entrée) au cadre
        self.ajouter_champs_entree()

      # Redimensionner le canevas lorsque la taille de la fenêtre change
        self.bind("<Configure>", self.redimensionner_canevas)
 def ouvrir_caracteristiques_lieu_detention(self, width):
    self.navbar_frame = tk.Frame(self.navbar_canvas)
    self.navbar_canvas.create_window((0, 0), window=self.navbar_frame, anchor='nw')
    self.col_title = ["Date", "Organisme de controle", "Motif de controle", "Nom du controleur", "Cachet","Signature"]

    for j in range(len(self.col_title)):
        col_tmp = self.col_title[j]
        col_title = tk.Label(self.navbar_frame, text=col_tmp, width=15, relief="solid", bg="lightgray", anchor="w")
        col_title.grid(row=13, column=j, sticky='nsew')

    for i in range(20):
        row_data = []
        for j in range(len(self.col_title)):
            cell = tk.Entry(self.navbar_frame, width=22)
            cell.grid(row=i+14, column=j, sticky='nsew')
            row_data.append(cell)
        self.data.append(row_data)

    for j in range(len(self.col_title)):
        self.navbar_frame.grid_columnconfigure(j, weight=1)

    self.bind("<Configure>", self.redimensionner_canevas)
#  def regarder_carachersitiques_lieu_detention(self):

#      with open('caracteristiques_lieu_detention.json', 'r') as file:
#         data = json.load(file)

#         # Parcourir les données
#         for i, element in enumerate(data['caracteristiques_lieu_detention'], start=15):
#             text_fields = []

#             # Parcourir les clés des sous-dictionnaires
#             for key in element:
#                 # Récupérer le sous-dictionnaire correspondant à la clé
#                 sub_dict = element[key]

#                 # Parcourir les clés et valeurs du sous-dictionnaire
#                 for j, sub_key in enumerate(sub_dict, start=1):
#                     value = sub_dict[sub_key]

#                     # Trouver l'index de la colonne correspondant à la clé
#                     col_index = self.col_title.index(sub_key)

#                     # Insérer la valeur dans le champ d'entrée correspondant
#                     entry = self.data[i-15][col_index]
#                     entry.delete(0, 'end')  # Supprimer le contenu précédent
#                     entry.insert(0, value)  # Insérer la nouvelle valeur
#                     # text_field.insert(END, f"{key}: {value}\n")
#                     # text_fields.append(text_field)

#     # Ajouter les boutons en dehors de la boucle pour éviter la duplication
#         self.bouton_ajouter_ligne = Button(self, text="Ajouter une ligne", command=self.ajouter_ligne)
#         self.bouton_ajouter_ligne.grid(row=self.numberLines + 4, columnspan=len(self.col_title), sticky='nsew')

#         btn_valider = Button(self, text="Modifier les informations", command=self.valider_carathersitiques_lieu)
#         btn_valider.grid(row=self.numberLines + 5, columnspan=len(self.col_title), sticky='nsew')         
#         #Barre de défilement verticale pour le Canvas

#         # Barre de défilement verticale pour le Canvas
#                 # Création du cadre à l'intérieur du canevas
#         self.navbar_frame = tk.Frame(self.navbar_canvas)
#         self.navbar_canvas.create_window((0, 0), window=self.navbar_frame, anchor='nw')
#         scrollbar = tk.Scrollbar(self, orient="vertical", command=self.navbar_canvas.yview)  

#         # Configuration du Canvas pour le défilement
#         self.navbar_canvas.create_window((0, 0), window=self.navbar_frame, anchor='nw')
#       #  self.navbar_canvas.config(yscrollcommand=scrollbar)
       
#         scrollbar.grid(row=10, column=len(self.col_title) + 1, sticky='ns')
#         self.navbar_canvas.config(yscrollcommand=scrollbar.set)

#         self.bind("<Configure>", self.redimensionner_canevas)    

 def redimensionner_canevas(self, event):
    self.canvas.configure(scrollregion=self.canvas.bbox("all"))

 def ouvrir_caracteristiques_lieu_detention(self,width):
    # Assurez-vous que les données précédentes sont effacées si nécessaire
     self.supprimer_widgets()  # Assurez-vous que cette méthode est correctement implémentée
     self.numberLines = width
     self.numberColumns = width
    # Calcul de la longueur de la phrase "Caractéristiques lieu de détention"
    # Définition des titres des colonnes
     self.col_title = ["Sire", "Statut Juridique", "Denomination", "Adresse", "numero de Telephone", "Portable", "Mail",
                      "prenom", "nom_usage", "Adresse", "portable", "mail", "Telephone", "Tel", "tel"]
                     
    # Ajout de l'espace entre le menu de navigation et "Sire"
     for j in range(15):
      print("nombres " +str(self.numberColumns))
      col_tmp = self.col_title[j]
      col_title = tk.Label(self, text=col_tmp, width=15, relief="solid", bg="lightgray", anchor="w")
      col_title.grid(row=13, column=j, sticky='nsew')  # Utilise sticky pour que la colonne s'adapte
      # Ajout des données du tableau
      self.data = [] 

    # Création des champs d'entrée
     for i in range(5):
        row_data = []
        for j in range(len(self.col_title)):
            cell = tk.Entry(self, width=22)
            cell.grid(row=i+14, column=j, sticky='nsew')  # Commencer à la ligne 12
            row_data.append(cell)
        self.data.append(row_data)

     # Configurer la gestion des colonnes pour qu'elles s'adaptent au contenu
     for j in range(self.numberColumns):
        self.grid_columnconfigure(j, weight=1) 

     # Bouton de validation
     self.bouton_ajouter_ligne = Button(self, text="Ajouter une ligne", command=self.ajouter_ligne)
     self.bouton_ajouter_ligne.grid(row=self.numberLines + 4, column=0, columnspan=len(self.col_title), sticky='nsew')
     
     btn_valider = tk.Button(self, text="Valider", command=self.valider_carathersitiques_lieu)
     btn_valider.grid(row=self.numberLines + 5, column=0, columnspan=len(self.col_title), sticky='nsew')
     
     btn_valider = tk.Button(self, text="Afficher mes lieux de détention", command=self.regarder_carachersitiques_lieu_detention)
     btn_valider.grid(row=self.numberLines + 6, column=0, columnspan=len(self.col_title), sticky='nsew')  
     # Gestionnaire d'événements pour détecter les changements de taille de fenêtre
     self.bind("<Configure>", self.redimensionner_image) 
 def redimensionner_canevas(self, event):
    self.canvas.configure(scrollregion=self.canvas.bbox("all"))


    
