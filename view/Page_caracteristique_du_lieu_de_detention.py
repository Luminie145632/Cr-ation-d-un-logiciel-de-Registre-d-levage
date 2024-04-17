import tkinter as tk
from tkinter import messagebox, Button
from PIL import Image, ImageTk
import glob
import os

class FenetrePrincipaleCaracth(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("CARACTÉRISTIQUES DU LIEU DE DÉTENTION")
        self.geometry("1920x1080")
        self.iconbitmap("/Creation_dun_logiciel_de_Registre_delevage/images/horse_sans_fond.ico")
                   
        # Créer un canvas pour afficher l'image
        self.canvas = tk.Canvas(self, width=1920, height=1080)
        self.canvas.pack()

        # Appeler la méthode setup_background_animation pour démarrer l'animation des images
        self.setup_background_animation()

    def setup_background_animation(self):
        self.image_paths = glob.glob("/Creation_dun_logiciel_de_Registre_delevage/images/*.png")
        self.current_image_index = 0
        self.load_image()
   
    def load_image(self):
        image_path = self.image_paths[self.current_image_index]
        image = Image.open(image_path) 
        image = image.resize((1920, 1080))  # Redimensionner l'image pour qu'elle remplisse toute la fenêtre
        self.photo = ImageTk.PhotoImage(image)

        # Effacer tout contenu précédent du canvas
        self.canvas.delete("all")

        # Afficher l'image sur le canvas
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

        # Ajouter un fond derrière les notes pour les rendre plus visibles
        self.canvas.create_rectangle(50, 50, 1870, 350, fill='#f0f0f0', outline='')

        # Ajouter les autres éléments (labels, boutons, etc.) sur le canvas
        label_principal = self.canvas.create_text(960, 100, text="CARACTÉRISTIQUES DU LIEU DE DÉTENTION", font=("Helvetica", 24), fill="black")
        label_adresse = self.canvas.create_text(960, 150, text="Adresse du lieu de détention et type d’activité", font=("Helvetica", 16), fill="black")
        label_denomination = self.canvas.create_text(300, 200, text="Dénomination :", font=("Helvetica", 16), fill="black")
        self.entry_denomination = tk.Entry(self, width=50)
        self.entry_denomination.place(x=400, y=190)
        label_adresse = self.canvas.create_text(300, 250, text="Adresse :", font=("Helvetica", 16), fill="black")
        self.entry_adresse = tk.Entry(self, width=50)
        self.entry_adresse.place(x=400, y=240)
        label_activite = self.canvas.create_text(300, 300, text="Type d'activité :", font=("Helvetica", 16), fill="black")
        self.entry_activite = tk.Entry(self, width=50)
        self.entry_activite.place(x=440, y=290)
        
        # Ajoutez d'autres éléments sur le canvas en utilisant les coordonnées appropriées

        self.current_image_index = (self.current_image_index + 1) % len(self.image_paths)

        self.after(2000, self.load_image)

    def return_main_menu(self):
        self.destroy()
        os.system("python Accueil.py")

if __name__ == "__main__":
    fenetre_principale = FenetrePrincipaleCaracth()
    fenetre_principale.mainloop()
