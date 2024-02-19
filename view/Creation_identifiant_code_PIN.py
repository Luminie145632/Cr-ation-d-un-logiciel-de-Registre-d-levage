import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import glob
import random
import string
import json

class FenetrePrincipale(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Accueil")
        self.geometry("1920x1080")
        self.iconbitmap("/Creation_dun_logiciel_de_Registre_delevage/images/horse_sans_fond.ico")

        # Ajout de la phrase au centre
        etiquette_bienvenue = tk.Label(self, text="Pour créer votre compte, veuillez compléter les différents champs qui vont vous permettre de vous connecter à votre espace.", font=("Helvetica", 16, "bold"))
        etiquette_bienvenue.pack(side="top", pady=20)

        # Création du Label pour afficher les images
        self.label_image = tk.Label(self, bd=0, highlightthickness=0)
        self.label_image.pack(side="bottom", fill="both", expand=True)

        # Gestionnaire d'événements pour détecter les changements de taille de fenêtre
        self.bind("<Configure>", self.redimensionner_image)

        # Appel à la méthode pour gérer le fond d'image changeant
        self.setup_background_animation()

        # Création du conteneur pour les champs de saisie
        self.formulaire_frame = tk.Frame(self)
        self.formulaire_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Création des étiquettes, champs de saisie et bouton
        self.label_nom = tk.Label(self.formulaire_frame, text="Nom:")
        self.entry_nom = tk.Entry(self.formulaire_frame)

        self.label_prenom = tk.Label(self.formulaire_frame, text="Prénom:")
        self.entry_prenom = tk.Entry(self.formulaire_frame)

        self.btn_soumettre = tk.Button(self.formulaire_frame, text="Valider", command=self.soumettre_formulaire)

        # Placement des éléments du formulaire
        self.label_nom.grid(row=0, column=0, padx=10, pady=5)
        self.entry_nom.grid(row=0, column=1, padx=10, pady=5)

        self.label_prenom.grid(row=1, column=0, padx=10, pady=5)
        self.entry_prenom.grid(row=1, column=1, padx=10, pady=5)

        self.btn_soumettre.grid(row=3, column=0, columnspan=2, pady=10)

        # Variables pour stocker les informations générées
        self.identifiant = tk.StringVar()
        self.code = tk.StringVar()

    def setup_background_animation(self):
        self.image_paths = glob.glob("images/*.png")
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

    def generer_identifiant(self, nom, prenom):
        # Génération de l'identifiant en combinant les trois premières lettres du nom et du prénom
        identifiant = (nom[:3] + prenom[:3]).lower()
        return identifiant

    def generer_code(self):
        # Génération d'un code aléatoire de 6 chiffres
        code = ''.join(random.choices(string.digits, k=6))
        return code

    def soumettre_formulaire(self):
        nom = self.entry_nom.get()
        prenom = self.entry_prenom.get()

        self.identifiant.set(self.generer_identifiant(nom, prenom))
        self.code.set(self.generer_code())

        # Afficher les informations dans une boîte de message
        message = f"Nom: {nom}\nPrénom: {prenom}\nIdentifiant: {self.identifiant.get()}\nCode: {self.code.get()}"
        messagebox.showinfo("Informations de connexion à votre espace", message)

        # Appel de la fonction pour afficher les informations depuis un autre fichier
        self.afficher_informations()

    def afficher_informations(self):
        # Charger les informations depuis un fichier (par exemple, un fichier JSON)
        try:
            with open("informations_utilisateur.json", "r") as fichier:
                donnees_utilisateur = json.load(fichier)
                # Afficher les informations à partir du fichier
                messagebox.showinfo("Informations utilisateur", f"Informations provenant du fichier:\n{json.dumps(donnees_utilisateur, indent=2)}")
        except FileNotFoundError:
            messagebox.showwarning("Fichier introuvable", "Le fichier d'informations utilisateur n'a pas été trouvé.")

if __name__ == "__main__":
    fenetre_principale = FenetrePrincipale()
    fenetre_principale.mainloop()
