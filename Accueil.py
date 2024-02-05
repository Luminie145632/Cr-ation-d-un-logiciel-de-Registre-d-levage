import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import glob
import os

class FenetrePrincipale(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Accueil")
        self.geometry("1920x1080")
        self.iconbitmap("horse_sans_fond.ico")

        # Ajout de la phrase "Bienvenue sur notre application." au centre
        etiquette_bienvenue = ttk.Label(self, text="Bienvenue sur notre application.", font=("Helvetica", 16, "bold"))
        etiquette_bienvenue.pack(side="top", pady=20)

        # Création de la barre de navigation
        navbar = tk.Frame(self, bd=2, relief=tk.GROOVE)
        navbar.pack(side="top", fill="x")

        # Création des boutons de la barre de navigation
        self.btn_mouvement_temporaire = ttk.Button(navbar, text="Mouvement Temporaire", command=self.ouvrir_nouvelle_fenetre)
        self.btn_lieux_detention = ttk.Button(navbar, text="Lieux de Détention", command=self.ouvrir_fenetre_Lieu_detention)
        self.btn_presence_caracteristiques = ttk.Button(navbar, text="Présence et Caractéristiques", command=self.renseigner_presence_caracteristiques)
        self.btn_interventions = ttk.Button(navbar, text="Interventions", command=self.ouvrir_fenetre_Lieu_caratheristiques)

        self.boutons = [self.btn_mouvement_temporaire, self.btn_lieux_detention, self.btn_presence_caracteristiques, self.btn_interventions]

        for bouton in self.boutons:
            bouton.pack(side="left", expand=True, fill='both')

        # Ajout d'un séparateur pour plus de clarté
        ttk.Separator(navbar, orient="vertical").pack(side="left", padx=5)

        # Ajoutez d'autres boutons de la barre de navigation si nécessaire

        # Création du Canvas pour afficher les images
        self.canvas = tk.Canvas(self, bd=0, highlightthickness=0)
        self.canvas.pack(side="bottom", fill="both", expand=True)

        # Ajout d'une étiquette pour afficher l'image
        self.label_image = tk.Label(self.canvas)
        self.label_image.pack(side="bottom", fill="both", expand=True)

        # Appel à la méthode pour gérer le fond d'image changeant
        self.setup_animation_arriere_plan()

    def setup_animation_arriere_plan(self):
        self.chemins_images = glob.glob("/Creation_dun_logiciel_de_Registre_delevage/images/*.png")  # Mettez le chemin correct vers vos images
        self.index_image_actuelle = 0
        self.charger_image()

    def charger_image(self):
        # Charger l'image actuelle
        chemin_image = self.chemins_images[self.index_image_actuelle]
        image = Image.open(chemin_image)

        # Adapter l'image à la taille de la fenêtre
        largeur_fenetre, hauteur_fenetre = self.winfo_width(), self.winfo_height()
        image = image.resize((largeur_fenetre, hauteur_fenetre), Image.ANTIALIAS if hasattr(Image, 'ANTIALIAS') else Image.NEAREST)

        photo = ImageTk.PhotoImage(image)

        # Mettre l'image dans le Label
        self.label_image.configure(image=photo)
        self.label_image.image = photo  # Gardez une référence pour éviter la collecte des déchets

        # Mettre à jour l'index pour la prochaine image
        self.index_image_actuelle = (self.index_image_actuelle + 1) % len(self.chemins_images)

        # Placer les boutons au-dessus du Label
        for bouton in self.boutons:
            bouton.lift()

        # Planifier l'appel de la fonction charger_image après un certain délai (par exemple, 2000 millisecondes)
        self.after(2000, self.charger_image)

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
