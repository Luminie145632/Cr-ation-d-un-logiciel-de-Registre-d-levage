import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import glob
import json

class FenetrePrincipale(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Page de création des identifiants de compte")
        self.geometry("1920x1080")
        self.iconbitmap("/Creation_dun_logiciel_de_Registre_delevage/images/horse_sans_fond.ico")

        # Ajout de la phrase au centre
        etiquette_bienvenue = tk.Label(self, text="Veuillez compléter les différents champs pour pouvoir vous connecter à votre espace.", font=("Helvetica", 16, "bold"))
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
        self.label_nom = tk.Label(self.formulaire_frame, text="Nom :")
        self.entry_nom = tk.Entry(self.formulaire_frame)

        self.label_prenom = tk.Label(self.formulaire_frame, text="Prénom :")
        self.entry_prenom = tk.Entry(self.formulaire_frame)

        self.label_mot_de_passe = tk.Label(self.formulaire_frame, text="Mot de passe :")
        self.entry_mot_de_passe = tk.Entry(self.formulaire_frame, show="*")  # Mot de passe masqué par défaut

        self.label_confirmation_mot_de_passe = tk.Label(self.formulaire_frame, text="Confirmer le mot de passe :")
        self.entry_confirmation_mot_de_passe = tk.Entry(self.formulaire_frame, show="*")  # Mot de passe masqué par défaut

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

        self.label_confirmation_mot_de_passe.grid(row=3, column=0, padx=10, pady=5)
        self.entry_confirmation_mot_de_passe.grid(row=3, column=1, padx=10, pady=5)

        self.btn_soumettre.grid(row=4, column=0, columnspan=2, pady=10)

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

    def creacompte(self, identifiant):
        # Collecte des informations du formulaire
        nom = self.entry_nom.get()
        prenom = self.entry_prenom.get()
        mot_de_passe = self.entry_mot_de_passe.get()

        # Création d'un dictionnaire pour stocker les informations du compte
        compte = {
            "Nom": nom,
            "Prénom": prenom,
            "Mot de passe": mot_de_passe,
            "Identifiant": identifiant
        }

        # Lecture des données existantes du fichier JSON s'il en existe
        try:
            with open('comptes.json', 'r') as json_file:
                comptes_data = json.load(json_file)["comptes"]
        except FileNotFoundError:
            comptes_data = []

        # Ajout du nouveau compte à la liste
        comptes_data.append(compte)

        # Écriture des données dans un fichier JSON
        with open('comptes.json', 'w') as json_file:
            json.dump({"comptes": comptes_data}, json_file, indent=4)

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
            self.entry_confirmation_mot_de_passe.configure(show="")
        else:
            self.entry_mot_de_passe.configure(show="*")
            self.entry_confirmation_mot_de_passe.configure(show="*")

    def soumettre_formulaire(self):
        nom = self.entry_nom.get()
        prenom = self.entry_prenom.get()
        mot_de_passe = self.entry_mot_de_passe.get()
        confirmation_mot_de_passe = self.entry_confirmation_mot_de_passe.get()

        # Vérifier que le mot de passe contient uniquement des chiffres et des lettres et a une longueur maximale de 24 caractères
        if not (mot_de_passe.isalnum() and len(mot_de_passe) <= 24):
            messagebox.showwarning("Mot de passe invalide", "Le mot de passe doit contenir des chiffres et/ou des lettres et avoir une longueur maximale de 24 caractères.")
            return

        # Vérifier si le nom et le prénom sont saisis
        if not nom or not prenom:
            messagebox.showwarning("Champs requis", "Veuillez saisir votre nom et prénom.")
            return

        # Vérifier si le mot de passe et sa confirmation sont les mêmes
        if mot_de_passe != confirmation_mot_de_passe:
            messagebox.showwarning("Confirmation invalide", "Le mot de passe et sa confirmation ne correspondent pas.")
            return

        # Si tout est valide, générer l'identifiant et afficher les informations
        identifiant = self.generer_identifiant(nom, prenom)
        self.creacompte(identifiant)

        messagebox.showinfo("Informations du compte", f"Nom : {nom}\nPrénom : {prenom}\nIdentifiant : {identifiant}\nMot de passe : {mot_de_passe}")


if __name__ == "__main__":
    fenetre_principale = FenetrePrincipale()
    fenetre_principale.mainloop()
