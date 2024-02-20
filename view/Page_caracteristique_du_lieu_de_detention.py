import tkinter as tk
from tkinter import messagebox,Button
from PIL import Image, ImageTk
import glob
import os

class FenetrePrincipaleCaracth(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("CARACTÉRISTIQUES DU LIEU DE DÉTENTION")
        self.geometry("1920x1080")
        
        try:
         self.iconbitmap("/Creation_dun_logiciel_de_Registre_delevage/images/horse_sans_fond.ico")
        except Exception:
           print("Marche pas")
           
        label_principal = tk.Label(self, text="CARACTÉRISTIQUES DU LIEU DE DÉTENTION")
        label_principal.pack()

        label_adresse = tk.Label(self, text="Adresse du lieu de détention et type d’activité")
        label_adresse.pack()

        label_denomination = tk.Label(self, text="Dénomination :")
        label_denomination.pack()

        self.entry_denomination = tk.Text(self, width=50, height=1)
        self.entry_denomination.focus_set()
        self.entry_denomination.pack()

        label_adresse = tk.Label(self, text="Adresse :")
        label_adresse.pack()

        self.entry_adresse = tk.Text(self, width=50, height=2)
        self.entry_adresse.focus_set()
        self.entry_adresse.pack()

        label_activite = tk.Label(self, text="Type d'activité :")
        label_activite.pack()

        self.entry_activite = tk.Text(self, width=50, height=1)
        self.entry_activite.focus_set()
        self.entry_activite.pack()

        # Ajouter un label pour afficher les images
        self.label_image = tk.Label(self)
        self.label_image.pack()
        
        self.btn_mouvement_temporaire = Button(self, text="Retour au menu principal", command=  self.return_main_menu )#self.signaler_mouvement_temporaire)
        self.btn_mouvement_temporaire.pack()



        # Appeler la méthode setup_background_animation pour démarrer l'animation des images
        self.setup_background_animation()

    def setup_background_animation(self):
        try:
         self.image_paths = glob.glob("/Creation_dun_logiciel_de_Registre_delevage/images/*.png")
         self.current_image_index = 0
         self.load_image()
        except Exception:
         print("Lool")    
    def load_image(self):
        image_path = self.image_paths[self.current_image_index]
        
        try:
        
         image = Image.open(image_path)

        except Exception:
         print("Lool")   
        image = image.resize((self.winfo_width(), self.winfo_height()))
        photo = ImageTk.PhotoImage(image)

        self.label_image.configure(image=photo)
        self.label_image.image = photo

        self.current_image_index = (self.current_image_index + 1) % len(self.image_paths)

        self.after(2000, self.load_image)

    def return_main_menu(self):
     self.destroy()
     os.system("python Accueil.py")

     

    def redimensionner_image(self, event):
        image_path = self.image_paths[self.current_image_index]
        image = Image.open(image_path)
        image = image.resize((self.winfo_width(), self.winfo_height()))
        photo = ImageTk.PhotoImage(image)

        self.label_image.configure(image=photo)
        self.label_image.image = photo

if __name__ == "__main__":
    fenetre_principale = FenetrePrincipaleCaracth()
    fenetre_principale.mainloop()
