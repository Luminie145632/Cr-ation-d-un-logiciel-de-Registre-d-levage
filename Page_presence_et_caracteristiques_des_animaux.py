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


if __name__ == "__main__":
    fenetre_principale = FenetrePrincipale()
    fenetre_principale.mainloop()
