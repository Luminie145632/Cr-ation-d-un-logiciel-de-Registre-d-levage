import tkinter as tk
from tkinter import ttk


class FenetrePrincipale(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Particuliers ou Professionnels")
        self.geometry("800x600")  # Taille de la fenêtre ajustée
        self.iconbitmap("horse_sans_fond.ico")

        # Création des cadres
        cadre_particuliers = ttk.Frame(self, padding="20")
        cadre_particuliers.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        cadre_professionnels = ttk.Frame(self, padding="20")
        cadre_professionnels.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        # Configuration de la gestion de la taille de la grille
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Ajout de la phrase "Qui êtes-vous ?" au milieu en haut
        etiquette_question = ttk.Label(self, text="Qui êtes-vous ?", font=("Helvetica", 14))
        etiquette_question.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        # Ajout du bouton "Particuliers" dans le cadre Particuliers
        bouton_particuliers = ttk.Button(cadre_particuliers, text="Particuliers")
        bouton_particuliers.pack(expand=True)

        # Ajout du bouton "Professionnels" dans le cadre Professionnels
        bouton_professionnels = ttk.Button(cadre_professionnels, text="Professionnels")
        bouton_professionnels.pack(expand=True)

if __name__ == "__main__":
    fenetre_principale = FenetrePrincipale()
    fenetre_principale.mainloop()
