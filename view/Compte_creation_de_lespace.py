# Compte_creation_de_lespace.py
import tkinter as tk
import sys
sys.path.insert(1, '/Creation_dun_logiciel_de_Registre_delevage/')
from PIL import Image, ImageTk
import glob
import os
from tkinter import ttk
from PIL import Image, ImageTk


class FenetrePrincipale(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Création de l'espace de votre compte")
        self.geometry("1920x1080")  # Taille de la fenêtre ajustée
        self.iconbitmap("/Creation_dun_logiciel_de_Registre_delevage/images/horse_sans_fond.ico")

        # Création du canvas pour afficher les images
        self.canvas = tk.Canvas(self, width=1920, height=800)
        self.canvas.pack()

        # Création du label pour afficher l'image
        self.label_image = tk.Label(self.canvas)
        self.label_image.pack(fill=tk.BOTH, expand=tk.YES)

        # Appel à la méthode pour gérer le fond d'image changeant
        self.setup_background_animation()

        # Création de la fenêtre DemoWidget
        demo_widget = DemoWidget(self)
        # Placer DemoWidget directement sur l'image du canvas
        self.canvas.create_window(950, 320, window=demo_widget, anchor='center')

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


class DemoWidget(tk.Frame):
    CHOIX = ["Particulier", "Professionnel"]

    def __init__(self, root):
        super().__init__(root)
        self.pack()

        # Variable commune pour les boutons radio
        self.var_choix = tk.StringVar()

        # Création du style personnalisé
        style = ttk.Style()
        style.configure("TRadiobutton", background=root.cget("bg"), foreground="black", borderwidth=0)

        for i, rb_label in enumerate(self.CHOIX):
            rb = ttk.Radiobutton(self, text=rb_label, value=rb_label, variable=self.var_choix,
                                 compound='center', style='TRadiobutton')
            rb.grid(column=i, row=2, padx=20)  # Ajout de l'espacement entre les boutons


if __name__ == "__main__":
    fenetre_principale = FenetrePrincipale()
    fenetre_principale.mainloop()
