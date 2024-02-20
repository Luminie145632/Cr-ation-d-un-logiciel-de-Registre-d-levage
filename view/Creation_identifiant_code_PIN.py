import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import glob
import string
import json

class FenetrePrincipale(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Page de création des identifiants de compte")
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

        self.label_mot_de_passe = tk.Label(self.formulaire_frame, text="Mot de passe:")
        self.entry_mot_de_passe = tk.Entry(self.formulaire_frame, show="*")  # Mot de passe masqué par défaut

        self.btn_oeil = ttk.Button(self.formulaire_frame, text="👁", command=self.toggle_mot_de_passe, style="Toggle.TButton")

        self.btn_soumettre = tk.Button(self.formulaire_frame, text="Valider", command=self.soumettre_formulaire)

        # Placement des éléments du formulaire
        self.label_nom.grid(row=0, column=0, padx=10, pady=5)
        self.entry_nom.grid(row=0, column=1, padx=10, pady=5)

        self.label_prenom.grid(row=1, column=0, padx=10, pady=5)
        self.entry_prenom.grid(row=1, column=1, padx=10, pady=5)

        self.label_mot_de_passe.grid(row=2, column=0, padx=10, pady=5)
        self.entry_mot_de_passe.grid(row=2, column=1, padx=10, pady=5)
        self.btn_oeil.grid(row=2, column=2, padx=5, pady=5)

        self.btn_soumettre.grid(row=3, column=0, columnspan=2, pady=10)

        # Variables pour stocker les informations générées
        self.identifiant = tk.StringVar()

        # Style pour le bouton Toggle
        style = ttk.Style()
        style.configure("Toggle.TButton", padding=(5, 5))

        # Variable pour le suivi de l'état du mot de passe (affiché ou masqué)
        self.mot_de_passe_visible = False

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
        # Génération de l'identifiant en combinant la première lettre du prénom et les 5 premières lettres du nom
        identifiant = (prenom[0] + nom[:5]).lower()
        return identifiant

    def toggle_mot_de_passe(self):
        # Fonction pour basculer entre l'affichage et le masquage du mot de passe
        self.mot_de_passe_visible = not self.mot_de_passe_visible
        if self.mot_de_passe_visible:
            self.entry_mot_de_passe.configure(show="")
        else:
            self.entry_mot_de_passe.configure(show="*")

    def soumettre_formulaire(self):
        nom = self.entry_nom.get()
        prenom = self.entry_prenom.get()
        mot_de_passe = self.entry_mot_de_passe.get()

        # Vérifier que le mot de passe contient uniquement des chiffres et des lettres et a une longueur maximale de 7 caractères
        if not (mot_de_passe.isalnum() and len(mot_de_passe) <= 24):
            messagebox.showwarning("Mot de passe invalide", "Le mot de passe doit contenir uniquement des chiffres et des lettres et avoir une longueur maximale de 24 caractères.")
            return

        self.identifiant.set(self.generer_identifiant(nom, prenom))

        # Afficher les informations dans une boîte de message
        message = f"Nom: {nom}\nPrénom: {prenom}\nIdentifiant: {self.identifiant.get()}\nMot de passe: {mot_de_passe}"
        messagebox.showinfo("Informations de connexion à votre espace", message)

if __name__ == "__main__":
    fenetre_principale = FenetrePrincipale()
    fenetre_principale.mainloop()
