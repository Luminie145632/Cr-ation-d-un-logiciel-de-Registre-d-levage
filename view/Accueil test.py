import tkinter as tk
from PIL import Image, ImageTk
import glob
import sys
from tkinter import ttk
from tkinter import Button  
import os
import Methode1
from Page_caracteristique_du_lieu_de_detention import FenetrePrincipaleCaracth
from Soins_CourantGUI import Soins_cournat
from Presence_et_Caratheristiques_animauxGUI import Presence_CaratherisisGUI
#from Page_controle_du_registre_delevage import FenetrePrincipale
import json
#from tkinter import * (Cause des problèmes si décommenté)
from tkinter import messagebox, Frame, Entry, Button, Label, BOTH, ttk, Canvas
#from controller.Methode_1 import ouvrir_fichier, fermer_fichier

#####################################################################################################################

class FenetrePrincipale(tk.Tk):
    def __init__(self, width, col_titles, height):
        super().__init__()

        self.width = width
        self.height = height
        self.numberColumns = width
        self.numberLines = height
        self.col_title = col_titles
        self.data = []

        self.title("Page de l'application")
        self.geometry("1920x1080")  
        self.iconbitmap("/Creation_dun_logiciel_de_Registre_delevage/images/horse_sans_fond.ico")

        self.setup_background_animation()
        self.setup_navigation_bar()

        self.bind("<Configure>", self.redimensionner_image)

    def setup_navigation_bar(self):
        navbar = tk.Frame(self, bd=2, relief=tk.GROOVE)
        navbar.grid(row=1, column=0, columnspan=self.numberColumns, sticky="ew")

        btn_caracteristiques_lieu = tk.Button(navbar, text="Caractéristiques du Lieu de Détention", command=self.ouvrir_caracteristiques_lieu_detention)
        btn_caracteristiques_lieu.grid(row=0, column=1, sticky="ew")

        btn_mouvement_temporaire = tk.Button(navbar, text="Encadrement Zootechnique, Sanitaire et Médical des Animaux", command=self.open_encadrement_zootechnique)
        btn_mouvement_temporaire.grid(row=0, column=2, sticky="ew")

        btn_mouvement_temporaire = tk.Button(navbar, text="Présence et Caractéristiques des Animaux", command=self.ouvrir_caractheristiques_animaux)
        btn_mouvement_temporaire.grid(row=0, column=3, sticky="ew")

        btn_mouvement_temporaire_mvt = tk.Button(navbar, text="Mouvements Temporaires des Animaux", command=lambda: self.ouvrir_mouvement_temporaires(self.numberColumns))
        btn_mouvement_temporaire_mvt.grid(row=0, column=4, sticky="ew")

        btn_mouvement_temporaire = tk.Button(navbar, text="Interventions et Soins Courants", command=lambda: self.ouvrir_interventions(self.numberColumns))
        btn_mouvement_temporaire.grid(row=0, column=5, sticky="ew")

        btn_mouvement_temporaire = tk.Button(navbar, text="Contrôle du Registre d'élevage", command=lambda: self.ouvrir_controle_registre_elevage(self.numberColumns))
        btn_mouvement_temporaire.grid(row=0, column=6, sticky="ew")

        # Texte additionnel
        texte_instruction = "Pour générer le document PDF qui va regrouper toutes les informations que vous avez entrées dans les différentes parties de l'application."
        etiquette_instruction = tk.Label(self, text=texte_instruction, font=("Helvetica", 12))
        etiquette_instruction.grid(row=2, column=0, columnspan=self.numberColumns, sticky="nsew")

        # Texte additionnel2
        texte_instruction2 = "Veuillez cliquer sur le bouton suivant :"
        etiquette_instruction2 = tk.Label(self, text=texte_instruction2, font=("Helvetica", 12))
        etiquette_instruction2.grid(row=3, column=0, columnspan=self.numberColumns, sticky="nsew")

        # Bouton pour générer le document PDF
        btn_generer_pdf = tk.Button(self, text="Générer le document PDF", command=self.generer_document_pdf, font=("Helvetica", 14, "bold"))
        btn_generer_pdf.place(relx=0.5, rely=0.5, anchor="center")

    def setup_background_animation(self):
        self.image_paths = glob.glob("/Creation_dun_logiciel_de_Registre_delevage/images/*.png")
        self.current_image_index = 0
        self.load_image()

        etiquette_bienvenue = tk.Label(self, text="Bienvenue sur la page d'accueil de notre application.", font=("Helvetica", 16, "bold"))
        etiquette_bienvenue.grid(row=0, column=0, columnspan=self.numberColumns, sticky="nsew")  

        self.label_image = tk.Label(self, bd=0, highlightthickness=0)
        self.label_image.grid(row=5, column=0, columnspan=self.numberColumns, sticky='nsew')  

        self.grid_rowconfigure(1, weight=0)  
        self.grid_rowconfigure(2, weight=0)  
        self.grid_rowconfigure(3, weight=0)  
        self.grid_rowconfigure(4, weight=0)  
        self.grid_rowconfigure(5, weight=1)  
        self.grid_columnconfigure(0, weight=1)

    def load_image(self):
        image_path = self.image_paths[self.current_image_index]
        original_image = Image.open(image_path)
        original_image = original_image.resize((self.width, self.height))
        self.photo = ImageTk.PhotoImage(original_image)

        if hasattr(self, 'label_image'):
            self.label_image.configure(image=self.photo)
            self.label_image.image = self.photo
        else:
            self.label_image = tk.Label(self, bd=0, highlightthickness=0, image=self.photo)
            self.label_image.grid(row=5, column=0, columnspan=self.numberColumns, sticky="nsew")

        for child in self.label_image.winfo_children():
            child.lift()

        self.current_image_index = (self.current_image_index + 1) % len(self.image_paths)
        self.after(2000, self.load_image)

    def redimensionner_image(self, event):
        if self.photo:
            resized_image = Image.open(self.image_paths[self.current_image_index])
            resized_image = resized_image.resize((self.winfo_width(), self.winfo_height()))
            self.photo = ImageTk.PhotoImage(resized_image)
            self.label_image.configure(image=self.photo)
            self.label_image.image = self.photo

    def ouvrir_caracteristiques_lieu_detention(self):
        pass

    def open_encadrement_zootechnique(self):
        pass

    def ouvrir_caractheristiques_animaux(self):
        pass

    def ouvrir_mouvement_temporaires(self, width):
        pass

    def ouvrir_interventions(self, width):
        pass

    def ouvrir_controle_registre_elevage(self, width):
        pass

    def generer_document_pdf(self):
        # Ajoutez ici la logique pour générer le document PDF avec les informations de l'application
        pass

if __name__ == "__main__":
    col_titles = ["Date", "Organisme de contrôle", "Motif de contrôle", "Nom du contrôleur", "Cachet", "Signature"]
    fenetre_principale = FenetrePrincipale(width=1920, col_titles=col_titles, height=1080)
    fenetre_principale.mainloop()
