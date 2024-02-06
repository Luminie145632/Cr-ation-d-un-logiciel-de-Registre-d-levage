import tkinter as tk
from tkinter import ttk

class FenetrePrincipale(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Accueil")
        self.geometry("1920x1080")  # Taille de la fenêtre ajustée
        self.iconbitmap("horse_sans_fond.ico")

        # Création du label avec le message en gras et plus grand
        message_label = tk.Label(self, text="Bienvenue, veuillez vous connecter à votre compte pour accéder à vos informations.\nSi vous n'avez pas de compte, nous vous invitons à créer un compte.", font=("Helvetica", 24, "bold"))
        message_label.pack(pady=20)

        # Création du canvas pour afficher les images
        self.canvas = tk.Canvas(self, width=1920, height=800)
        self.canvas.pack()

        # Création du bouton Création d'un compte
        btn_creation = ttk.Button(self, text="Création d'un compte", command=self.on_creation_click, style="TButton")
        btn_creation.pack(pady=10, side=tk.TOP, anchor=tk.CENTER)
        
        # Création du bouton Connexion
        btn_connexion = ttk.Button(self, text="Connexion", command=self.on_connexion_click, style="TButton")
        btn_connexion.pack(pady=10, side=tk.TOP, anchor=tk.CENTER)

        
    def on_connexion_click(self):
        print("Bouton Connexion cliqué")

    def on_creation_click(self):
        print("Bouton Création d'un compte cliqué")

if __name__ == "__main__":
    fenetre_principale = FenetrePrincipale()
    fenetre_principale.mainloop()
