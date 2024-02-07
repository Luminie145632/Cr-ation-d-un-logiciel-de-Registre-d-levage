import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import glob

class FenetrePrincipale(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Accueil")
        self.geometry("1920x1080")  # Taille de la fenêtre ajustée
        self.iconbitmap("/Creation_dun_logiciel_de_Registre_delevage/images/horse_sans_fond.ico")

        # Création du label avec le message en gras et plus grand
        message_label = tk.Label(self, text="Bienvenue, veuillez vous connecter à votre compte pour accéder à vos informations.\nSi vous n'avez pas de compte, nous vous invitons à créer un compte.", font=("Helvetica", 24, "bold"))
        message_label.pack(pady=20)

        # Création du canvas pour afficher les images
        self.canvas = tk.Canvas(self, width=1920, height=800)
        self.canvas.pack()

        # Création du label pour afficher l'image
        self.label_image = tk.Label(self.canvas)
        self.label_image.pack(fill=tk.BOTH, expand=tk.YES)

        # Appel à la méthode pour gérer le fond d'image changeant
        self.setup_background_animation()

        # Création du bouton Création d'un compte
        btn_creation = ttk.Button(self, text="Création d'un compte", command=self.on_creation_click, style="TButton")
        self.canvas.create_window(950, 200, window=btn_creation, anchor='center')

        # Création du bouton Connexion
        btn_connexion = ttk.Button(self, text="Connexion", command=self.on_connexion_click, style="TButton")
        self.canvas.create_window(950, 250, window=btn_connexion, anchor='center')

    def on_connexion_click(self):
        print("Bouton Connexion cliqué")

    def on_creation_click(self):
        print("Bouton Création d'un compte cliqué")

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

if __name__ == "__main__":
    fenetre_principale = FenetrePrincipale()
    fenetre_principale.mainloop()
