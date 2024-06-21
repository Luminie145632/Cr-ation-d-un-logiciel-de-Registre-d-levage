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



class MaClasse(tk.Tk):
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

        # Barre de défilement verticale pour le canevas
        scrollbar = tk.Scrollbar(self, orient="vertical", command=self.navbar_canvas.yview)
        scrollbar.grid(row=10, column=len(self.col_title) + 1, sticky='ns')
        self.navbar_canvas.config(yscrollcommand=scrollbar.set)

        # Redimensionner le canevas lorsque la taille de la fenêtre change
        self.bind("<Configure>", self.redimensionner_canevas)

    def ajouter_ligne(self):
        row_data = []
        for j in range(len(self.col_title)):
            cell = tk.Entry(self.inner_frame, width=22)
            cell.grid(row=self.numberLines + 1, column=j, sticky='nsew')
            row_data.append(cell)
        self.data.append(row_data)
        self.numberLines += 1  

    def redimensionner_canevas(self, event):
        self.navbar_canvas.configure(scrollregion=self.navbar_canvas.bbox("all"))

if __name__ == "__main__":
    col_titles = ["Date", "Organisme de contrôle", "Motif de contrôle", "Nom du contrôleur", "Cachet", "Signature"]

    fenetre_principale = MaClasse(width=20,col_titles=col_titles,height=19)
    fenetre_principale.mainloop() 
