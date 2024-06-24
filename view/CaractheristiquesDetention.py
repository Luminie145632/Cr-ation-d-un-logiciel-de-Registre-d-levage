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

 def redimensionner_canevas(self, event):
    self.canvas.configure(scrollregion=self.canvas.bbox("all"))

 def regarder_carachersitiques_lieu_detention(self):  

 #def view_zootechnical_supervision(self):
        with open('/Creation_dun_logiciel_de_Registre_delevage/view/lieu_detention.json', 'r') as file:      

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

        btn_valider = Button(self, text="Modifier les informations", command=lambda: self.valider_encadrement_Zootechnique_animaux)
        btn_valider.grid(row=self.numberLines + 5, columnspan=len(self.col_title), sticky='nsew')       
# Redimensionner le canevas lorsque la taille de la fenêtre change
        self.bind("<Configure>", self.redimensionner_canevas) 

    #flag
 def regarder_carachersitiques_lieu_detention(self):
    import json
    from tkinter import Button

    with open('Creation_dun_logiciel_de_Registre_delevage/view/lieu_detention.json', 'r') as file:      
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

    btn_valider = Button(self, text="Modifier les informations", command=lambda: self.valider_encadrement_Zootechnique_animaux())
    btn_valider.grid(row=self.numberLines + 5, columnspan=len(self.col_title), sticky='nsew')

    # Redimensionner le canevas lorsque la taille de la fenêtre change
    self.bind("<Configure>", self.redimensionner_canevas)   
    
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


    

