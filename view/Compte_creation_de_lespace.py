import tkinter as tk
import sys
from PIL import Image, ImageTk
import glob
from tkinter import ttk

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

        # Création du canvas pour afficher les images
        self.canvas = tk.Canvas(self, width=1920, height=800)
        self.canvas.grid(row=0, column=0, sticky="nsew")

        # Création du label pour afficher l'image
        self.label_image = tk.Label(self.canvas)
        self.label_image.pack(fill=tk.BOTH, expand=tk.YES)

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

        # Création de la fenêtre DemoWidget
        demo_widget = DemoWidget(self)
        # Placer DemoWidget directement sur l'image du canvas
        self.canvas.create_window(950, 320, window=demo_widget, anchor='center')

    def setup_background_animation(self):
        self.image_paths = glob.glob("/Creation_dun_logiciel_de_Registre_delevage/images/*.png")
        self.current_image_index = 0
        self.load_image()

    def load_image(self):
        image_path = self.image_paths[self.current_image_index]
        image = Image.open(image_path)
        image = image.resize((self.winfo_width(), self.winfo_height()))
        photo = ImageTk.PhotoImage(image)
        self.label_image.configure(image=photo)
        self.label_image.image = photo
        self.current_image_index = (self.current_image_index + 1) % len(self.image_paths)

        self.after(2000, self.load_image)

    def redimensionner_image(self, event):
        image_path = self.image_paths[self.current_image_index]
        image = Image.open(image_path)
        image = image.resize((self.winfo_width(), self.winfo_height()))
        photo = ImageTk.PhotoImage(image)
        self.label_image.configure(image=photo)
        self.label_image.image = photo


class DemoWidget(tk.Frame):
    CHOIX = ["Particulier", "Professionnel"]

    def __init__(self, root):
        super().__init__(root)
        self.pack()

        # Variable commune pour les boutons radio
        self.var_choix = tk.StringVar()

        # Création du style personnalisé
        style = ttk.Style()
        style.configure("TRadiobutton", background=root.cget("bg"), foreground="black", borderwidth=0)

        for i, rb_label in enumerate(self.CHOIX):
            rb = ttk.Radiobutton(self, text=rb_label, value=rb_label, variable=self.var_choix,
                                 compound='center', style='TRadiobutton')
            rb.grid(column=i, row=2, padx=20)  # Ajout de l'espacement entre les boutons


if __name__ == "__main__":
    # Définition des titres de colonnes
    col_titles = ["Colonne 1", "Colonne 2", "Colonne 3", "Colonne 4", "Colonne 5", "Colonne 6"]

    # Création de la fenêtre principale en fournissant les arguments requis
    fenetre_principale = FenetrePrincipale(width=6, col_titles=col_titles, height=3)
    fenetre_principale.mainloop()
