import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import glob
import string
import json

class FenetrePrincipale(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Page de connexion")
        self.geometry("1920x1080")
        self.iconbitmap("/Creation_dun_logiciel_de_Registre_delevage/images/horse_sans_fond.ico")

        # Ajout de la phrase au centre
        etiquette_bienvenue = tk.Label(self, text="Veuillez saisir vos informations de connexion.", font=("Helvetica", 16, "bold"))
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
        self.label_identifiant = tk.Label(self.formulaire_frame, text="Identifiant :")
        self.entry_identifiant = tk.Entry(self.formulaire_frame)

        self.label_mot_de_passe = tk.Label(self.formulaire_frame, text="Mot de passe :")
        self.entry_mot_de_passe = tk.Entry(self.formulaire_frame, show="*")  # Mot de passe masqué par défaut

        self.btn_oeil = ttk.Button(self.formulaire_frame, text="👁", command=self.toggle_mot_de_passe, style="Toggle.TButton")

        self.btn_connexion = tk.Button(self.formulaire_frame, text="Connexion", command=self.connexion)

        # Placement des éléments du formulaire
        self.label_identifiant.grid(row=0, column=0, padx=10, pady=5)
        self.entry_identifiant.grid(row=0, column=1, padx=10, pady=5)

        self.label_mot_de_passe.grid(row=1, column=0, padx=10, pady=5)
        self.entry_mot_de_passe.grid(row=1, column=1, padx=10, pady=5)
        self.btn_oeil.grid(row=1, column=2, padx=5, pady=5)

        self.btn_connexion.grid(row=2, column=0, columnspan=2, pady=10)

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

    def toggle_mot_de_passe(self):
        # Fonction pour basculer entre l'affichage et le masquage du mot de passe
        self.mot_de_passe_visible = not self.mot_de_passe_visible
        if self.mot_de_passe_visible:
            self.entry_mot_de_passe.configure(show="")
        else:
            self.entry_mot_de_passe.configure(show="*")

    def connexion(self):
        identifiant = self.entry_identifiant.get()
        mot_de_passe = self.entry_mot_de_passe.get()

        # Vérifier que l'identifiant et le mot de passe ne sont pas vides
        if not identifiant or not mot_de_passe:
            messagebox.showwarning("Champs vides", "Veuillez remplir tous les champs.")
            return

        # Effectuer ici la vérification de l'identifiant et du mot de passe (par exemple, vérifier dans une base de données)

        # Afficher un message de réussite de connexion avec une boîte de message personnalisée
        self.message_connexion_reussie(f"Bienvenue, {identifiant} dans votre espace !")

    def message_connexion_reussie(self, message):
        # Créer une boîte de message personnalisée pour s'adapter à la longueur du texte
        messagebox.showinfo("Connexion réussie", message)

if __name__ == "__main__":
    fenetre_principale = FenetrePrincipale()
    fenetre_principale.mainloop()
