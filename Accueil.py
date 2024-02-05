import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import glob
import os

class FenetrePrincipale(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Accueil")
        self.geometry("1920x1080")  # Définir la taille initiale de la fenêtre
        self.iconbitmap("horse_sans_fond.ico")

        # Ajout de la phrase "Bienvenue sur notre application." au centre
        etiquette_bienvenue = tk.Label(self, text="Bienvenue sur notre application.", font=("Helvetica", 16, "bold"))
        etiquette_bienvenue.pack(side="top", pady=20)

        # Création de la barre de navigation
        navbar = tk.Frame(self, bd=2, relief=tk.GROOVE)
        navbar.pack(side="top", fill="x")

        # Création des boutons de la barre de navigation
        btn_mouvement_temporaire = tk.Button(navbar, text="Mouvement Temporaire", command=self.ouvrir_nouvelle_fenetre)
        btn_mouvement_temporaire.pack(side="left", expand=True, fill='both')

        btn_lieux_detention = tk.Button(navbar, text="Lieux de Détention", command=self.ouvrir_fenetre_Lieu_detention)
        btn_lieux_detention.pack(side="left", expand=True, fill='both')

        btn_presence_caracteristiques = tk.Button(navbar, text="Présence et Caractéristiques", command=self.renseigner_presence_caracteristiques)
        btn_presence_caracteristiques.pack(side="left", expand=True, fill='both')

        btn_interventions = tk.Button(navbar, text="Interventions", command=self.ouvrir_fenetre_Lieu_caratheristiques)
        btn_interventions.pack(side="left", expand=True, fill='both')

        # Ajout d'un séparateur pour plus de clarté
        ttk.Separator(navbar, orient="vertical").pack(side="left", padx=5)

        # Ajoutez d'autres boutons de la barre de navigation si nécessaire

        # Création du Label pour afficher les images
        self.label_image = tk.Label(self, bd=0, highlightthickness=0)
        self.label_image.pack(side="bottom", fill="both", expand=True)

        # Gestionnaire d'événements pour détecter les changements de taille de fenêtre
        self.bind("<Configure>", self.redimensionner_image)

        # Appel à la méthode pour gérer le fond d'image changeant
        self.setup_background_animation()

    def setup_background_animation(self):
        self.image_paths = glob.glob("/Creation_dun_logiciel_de_Registre_delevage/images/*.png")  # Mettez le chemin correct vers vos images
        self.current_image_index = 0
        self.load_image()

    def load_image(self):
        # Charger l'image actuelle
        image_path = self.image_paths[self.current_image_index]
        image = Image.open(image_path)

        # Redimensionner l'image pour prendre toute la fenêtre
        image = image.resize((self.winfo_width(), self.winfo_height()))

        photo = ImageTk.PhotoImage(image)

        # Mettre à jour l'image dans le label
        self.label_image.configure(image=photo)
        self.label_image.image = photo  # Gardez une référence pour éviter la collecte des déchets

        # Mettre à jour l'index pour la prochaine image
        self.current_image_index = (self.current_image_index + 1) % len(self.image_paths)

        # Placer les boutons au-dessus du Label
        for child in self.label_image.winfo_children():
            child.lift()

        # Planifier l'appel de la fonction load_image après un certain délai (par exemple, 2000 millisecondes)
        self.after(2000, self.load_image)

    def redimensionner_image(self, event):
        # Redimensionner l'image pour prendre toute la fenêtre
        image_path = self.image_paths[self.current_image_index]
        image = Image.open(image_path)
        image = image.resize((self.winfo_width(), self.winfo_height()))

        photo = ImageTk.PhotoImage(image)

        # Mettre à jour l'image dans le label
        self.label_image.configure(image=photo)
        self.label_image.image = photo  # Gardez une référence pour éviter la collecte des déchets

    def ouvrir_nouvelle_fenetre(self):
        self.destroy()
        os.system("python Page_1_mouvements_temporaires_des_animaux.py")

    def ouvrir_fenetre_Lieu_detention(self):
        self.destroy()
        os.system("python Lieu_detention.py")

    def ouvrir_fenetre_Lieu_caratheristiques(self):
        self.destroy()
        os.system("python Page_caractéristique_du_lieu_de_detention.py")

    def renseigner_presence_caracteristiques(self):
        print("Bouton Renseigner Présence et Caractéristiques cliqué")


if __name__ == "__main__":
    fenetre_principale = FenetrePrincipale()
    fenetre_principale.mainloop()
