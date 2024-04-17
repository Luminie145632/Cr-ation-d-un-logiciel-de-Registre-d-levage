import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import glob

class FenetrePrincipale(tk.Tk):
    def __init__(self, width, col_titles, height):
        super().__init__()

        self.title("Page de connexion ou de création de compte")
        self.geometry("1920x1080")
        self.iconbitmap("images/horse_sans_fond.ico")  # Modifiez le chemin de l'icône si nécessaire

        # Titre distinct
        self.titre_frame = tk.Frame(self)
        self.titre_frame.pack(pady=5)  # Ajoute un espacement en y pour séparer du reste

        titre_label = tk.Label(self.titre_frame, text="Bienvenue, veuillez vous connecter à votre compte pour accéder à vos informations.\nSi vous n'avez pas de compte, nous vous invitons à créer votre compte.", font=("Helvetica", 24, "bold"))
        titre_label.pack()

        # Cadre pour les boutons
        self.boutons_frame = tk.Frame(self)
        self.boutons_frame.pack(pady=5)  # Ajoute un espacement en y pour séparer du reste

        btn_creation = ttk.Button(self.boutons_frame, text="Création d'un compte", command=self.executer_script_creation_compte, style="TButton")
        btn_creation.pack(side=tk.LEFT, padx=10)  # Aligne à gauche avec un espace horizontal

        btn_connexion = ttk.Button(self.boutons_frame, text="Connexion", command=self.on_connexion_click, style="TButton")
        btn_connexion.pack(side=tk.LEFT, padx=10)  # Aligne à gauche avec un espace horizontal

        # Canevas pour l'animation de fond
        self.canvas = tk.Canvas(self, width=1920, height=1080)
        self.canvas.pack()

        self.setup_background_animation()

    def on_connexion_click(self):
        print("Bouton Connexion cliqué")

    def executer_script_creation_compte(self):
        # Exécutez le script Python depuis un fichier externe
        with open("view/Creation_identifiant_code_PIN.py", "r") as script_file:  # Modifiez le chemin du script si nécessaire
            script_code = script_file.read()
            exec(script_code)

    def setup_background_animation(self):
        self.image_paths = glob.glob("images/*.png")
        self.current_image_index = 0
        self.load_image()

    def load_image(self):
        image_path = self.image_paths[self.current_image_index]
        image = Image.open(image_path)
        image = image.resize((self.winfo_width(), self.winfo_height()))
        photo = ImageTk.PhotoImage(image)

        # Affichage de l'image en arrière-plan
        if hasattr(self, 'label_image'):
            self.label_image.configure(image=photo)
            self.label_image.image = photo
        else:
            self.label_image = tk.Label(self.canvas, bd=0, highlightthickness=0, image=photo)
            self.label_image.image = photo
            self.label_image.place(x=0, y=0, relwidth=1, relheight=1)

        self.current_image_index = (self.current_image_index + 1) % len(self.image_paths)
        self.after(6000, self.load_image)

    def redimensionner_image(self, event):
        image_path = self.image_paths[self.current_image_index]
        image = Image.open(image_path)
        image = image.resize((self.winfo_width(), self.winfo_height()))
        photo = ImageTk.PhotoImage(image)
        self.label_image.configure(image=photo)
        self.label_image.image = photo


if __name__ == "__main__":
    # Définition des titres de colonnes
    col_titles = ["Colonne 1", "Colonne 2", "Colonne 3", "Colonne 4", "Colonne 5", "Colonne 6"]

    # Création de la fenêtre principale en fournissant les arguments requis
    fenetre_principale = FenetrePrincipale(width=6, col_titles=col_titles, height=3)
    fenetre_principale.mainloop()
