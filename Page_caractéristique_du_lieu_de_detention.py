import tkinter as tk
from tkinter import messagebox

class FenetrePrincipale(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("CARACTÉRISTIQUES DU LIEU DE DÉTENTION")
        self.geometry("1920x1080")
        self.iconbitmap("horse_sans_fond.ico")

        label_principal = tk.Label(self, text="CARACTÉRISTIQUES DU LIEU DE DÉTENTION")
        label_principal.pack()

        label_adresse = tk.Label(self, text="Adresse du lieu de détention et type d’activité")
        label_adresse.pack()

        label_denomination = tk.Label(self, text="Dénomination :")
        label_denomination.pack()

        self.entry_denomination = tk.Text(self, width=50, height=1)  # Ajustez la largeur et la hauteur selon vos besoins
        self.entry_denomination.focus_set()
        self.entry_denomination.pack()

        label_adresse = tk.Label(self, text="Adresse :")
        label_adresse.pack()

        self.entry_adresse = tk.Text(self, width=50, height=2)  # Ajustez la largeur et la hauteur selon vos besoins
        self.entry_adresse.focus_set()
        self.entry_adresse.pack()

        label_activite = tk.Label(self, text="Type d'activité :")
        label_activite.pack()

        self.entry_activite = tk.Text(self, width=50, height=1)  # Ajustez la largeur et la hauteur selon vos besoins
        self.entry_activite.focus_set()
        self.entry_activite.pack()

if __name__ == "__main__":
    fenetre_principale = FenetrePrincipale()
    fenetre_principale.mainloop()
