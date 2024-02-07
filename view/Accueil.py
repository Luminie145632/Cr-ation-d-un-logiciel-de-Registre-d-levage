# Accueil.py
import sys
sys.path.insert(1, '/Creation_dun_logiciel_de_Registre_delevage/')
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import glob
import os
from controller.Methode_1 import ouvrir_fichier, fermer_fichier

class FenetrePrincipale(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Accueil")
        self.geometry("1920x1080")
        self.iconbitmap("/Creation_dun_logiciel_de_Registre_delevage/images/horse_sans_fond.ico")

        # Ajout de la phrase "Bienvenue sur notre application." au centre
        etiquette_bienvenue = tk.Label(self, text="Bienvenue sur la page d'accueil de notre application.", font=("Helvetica", 16, "bold"))
        etiquette_bienvenue.pack(side="top", pady=20)

        # Création de la barre de navigation
        navbar = tk.Frame(self, bd=2, relief=tk.GROOVE)
        navbar.pack(side="top", fill="x")

        # Création des boutons de la barre de navigation
        btn_caracteristiques_lieu = tk.Button(navbar, text="Caractéristiques du Lieu de Détention", command=self.ouvrir_caracteristiques_lieu)
        btn_caracteristiques_lieu.pack(side="left", expand=True, fill='both')

        btn_mouvement_temporaire = tk.Button(navbar, text="Encadrement Zootechnique, Sanitaire et Medical des Animaux", command=self.ouvrir_nouvelle_fenetre)
        btn_mouvement_temporaire.pack(side="left", expand=True, fill='both')

        btn_mouvement_temporaire = tk.Button(navbar, text="Présence et Caractéristiques des Animaux", command=self.ouvrir_nouvelle_fenetre)
        btn_mouvement_temporaire.pack(side="left", expand=True, fill='both')

        btn_mouvement_temporaire = tk.Button(navbar, text="Mouvement Temporaire des Animaux", command=self.ouvrir_nouvelle_fenetre)
        btn_mouvement_temporaire.pack(side="left", expand=True, fill='both')

        btn_mouvement_temporaire = tk.Button(navbar, text="Intervents et Soins Courants", command=self.ouvrir_nouvelle_fenetre)
        btn_mouvement_temporaire.pack(side="left", expand=True, fill='both')

        btn_mouvement_temporaire = tk.Button(navbar, text="Contrôle du Registre d'élevage", command=self.ouvrir_nouvelle_fenetre)
        btn_mouvement_temporaire.pack(side="left", expand=True, fill='both')

        #btn_mouvement_temporaire = tk.Button(navbar, text="Mouvement Temporaire", command=self.ouvrir_nouvelle_fenetre)
        #btn_mouvement_temporaire.pack(side="left", expand=True, fill='both')

        #btn_lieux_detention = tk.Button(navbar, text="Lieux de Détention", command=self.ouvrir_fenetre_Lieu_detention)
        #btn_lieux_detention.pack(side="left", expand=True, fill='both')

        #btn_presence_caracteristiques = tk.Button(navbar, text="Présence et Caractéristiques", command=self.renseigner_presence_caracteristiques)
        #btn_presence_caracteristiques.pack(side="left", expand=True, fill='both')

        #btn_interventions = tk.Button(navbar, text="Interventions", command=self.ouvrir_fenetre_Lieu_caratheristiques)
        #btn_interventions.pack(side="left", expand=True, fill='both')

        # Ajoutez d'autres boutons de la barre de navigation si nécessaire

        # Création du Label pour afficher les images
        self.label_image = tk.Label(self, bd=0, highlightthickness=0)
        self.label_image.pack(side="bottom", fill="both", expand=True)

        # Gestionnaire d'événements pour détecter les changements de taille de fenêtre
        self.bind("<Configure>", self.redimensionner_image)

        # Appel à la méthode pour gérer le fond d'image changeant
        self.setup_background_animation()

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

        for child in self.label_image.winfo_children():
            child.lift()

        self.after(2000, self.load_image)

    def redimensionner_image(self, event):
        image_path = self.image_paths[self.current_image_index]
        image = Image.open(image_path)
        image = image.resize((self.winfo_width(), self.winfo_height()))
        photo = ImageTk.PhotoImage(image)
        self.label_image.configure(image=photo)
        self.label_image.image = photo

    def ouvrir_caracteristiques_lieu(self):
        chemin_fichier = "/Creation_dun_logiciel_de_Registre_delevage/view/Page_caractéristique_du_lieu_de_detention.py"
        fichier = ouvrir_fichier(chemin_fichier)
        #fermer_fichier(fichier)
        # Ajoutez ici le code pour traiter le contenu du fichier si nécessaire

    def ouvrir_nouvelle_fenetre(self):
        self.destroy()
        os.system("python Page_1_mouvements_temporaires_des_animaux.py")

# ... (autres méthodes)

if __name__ == "__main__":
    fenetre_principale = FenetrePrincipale()
    fenetre_principale.mainloop()
