# Accueil.py
import sys
sys.path.insert(1, '/Creation_dun_logiciel_de_Registre_delevage/')
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import glob
import os
import Methode1

#from controller.Methode_1 import ouvrir_fichier, fermer_fichier

class FenetrePrincipale(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Accueil")
        self.geometry("1920x1080")
        try:
         self.iconbitmap("/Creation_dun_logiciel_de_Registre_delevage/images/horse_sans_fond.ico")
        except Exception:
           print(" photo de cheval ") 
        # Ajout de la phrase "Bienvenue sur notre application." au centre
        etiquette_bienvenue = tk.Label(self, text="Bienvenue sur la page d'accueil de notre application.", font=("Helvetica", 16, "bold"))
        etiquette_bienvenue.pack(side="top", pady=20)

        # Création de la barre de navigation
        navbar = tk.Frame(self, bd=2, relief=tk.GROOVE)
        navbar.pack(side="top", fill="x")

        # Création des boutons de la barre de navigation
        btn_caracteristiques_lieu = tk.Button(navbar, text="Caractéristiques du Lieu de Détention", command=self.ouvrir_caracteristiques_lieu)
        btn_caracteristiques_lieu.pack(side="left", expand=True, fill='both')

        btn_mouvement_temporaire = tk.Button(navbar, text="Encadrement Zootechnique, Sanitaire et Medical des Animaux", command=self.open_new_window)
        btn_mouvement_temporaire.pack(side="left", expand=True, fill='both')

        btn_mouvement_temporaire = tk.Button(navbar, text="Présence et Caractéristiques des Animaux", command=self.ouvrir_caractheristiques)
        btn_mouvement_temporaire.pack(side="left", expand=True, fill='both')

        btn_mouvement_temporaire = tk.Button(navbar, text="Mouvement Temporaire des Animaux", command=self.ouvrir_nouvelle_fenetre)
        btn_mouvement_temporaire.pack(side="left", expand=True, fill='both')

        btn_mouvement_temporaire = tk.Button(navbar, text="Intervents et Soins Courants", command=self.ouvrir_interventions)
        btn_mouvement_temporaire.pack(side="left", expand=True, fill='both')

        btn_mouvement_temporaire = tk.Button(navbar, text="Contrôle du Registre d'élevage", command=self.ouvrir_registre_elevage)
        btn_mouvement_temporaire.pack(side="left", expand=True, fill='both')

        # Création du Label pour afficher les images
        self.label_image = tk.Label(self, bd=0, highlightthickness=0)
        self.label_image.pack(side="bottom", fill="both", expand=True)

        # Gestionnaire d'événements pour détecter les changements de taille de fenêtre
        self.bind("<Configure>", self.redimensionner_image)

        # Appel à la méthode pour gérer le fond d'image changeant
        try:
         self.setup_background_animation()
        except Exception:
          print(" Marche pas photo de fond ") 
    def setup_background_animation(self):
      
        self.image_paths = glob.glob("/Creation_dun_logiciel_de_Registre_delevage/images/*.png")
        self.current_image_index = 0
        self.load_image()

    # def load_image(self):
    #     image_path = self.image_paths[self.current_image_index]
    #     image = Image.open(image_path)
    #     image = image.resize((self.winfo_width(), self.winfo_height()))
    #     photo = ImageTk.PhotoImage(image)
    #     self.label_image.configure(image=photo)
    #     self.label_image.image = photo
    #     self.current_image_index = (self.current_image_index + 1) % len(self.image_paths)

    #     for child in self.label_image.winfo_children():
    #         child.lift()

    #     self.after(2000, self.load_image)

    def redimensionner_image(self, event):
        image_path = self.image_paths[self.current_image_index]
        image = Image.open(image_path)
        image = image.resize((self.winfo_width(), self.winfo_height()))
        photo = ImageTk.PhotoImage(image)
        self.label_image.configure(image=photo)
        self.label_image = photo


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
       try:
        image_path = self.image_paths[self.current_image_index]
        image = Image.open(image_path)
        image = image.resize((self.winfo_width(), self.winfo_height()))
        photo = ImageTk.PhotoImage(image)
        self.label_image.configure(image=photo)
        self.label_image = photo
       except Exception:
        print("photo march pas ")
    def open_control(self):
     chemin_fichier = "/Creation_dun_logiciel_de_Registre_delevage/view/Page_controle_du_registre_delevage.py"
     fichier = Methode1.ouvrir_fichier(chemin_fichier)

    #checked
    def ouvrir_caracteristiques_lieu(self):
     self.destroy()
     os.system("python Page_caracteristique_du_lieu_de_detention.py")

    def ouvrir_interventions(self):
     self.destroy()
     os.system("python Soins_CourantGUI.py") 

    def ouvrir_registre_elevage(self):
     self.destroy()
     os.system("python Page_controle_du_registre_delevage.py") 
    
    #  chemin_fichier = "/Creation_dun_logiciel_de_Registre_delevage/view/Page_caracteristique_du_lieu_de_detention.py"
    #  fichier = Methode1.ouvrir_fichier(chemin_fichier)
    #   #  fichier = controller.Methode_1.ouvrir_fichier(chemin_fichier)
    #     #fermer_fichier(fichier)
    #     # Ajoutez ici le code pour traiter le contenu du fichier si nécessaire
    
    #checked
    def open_healthcare(self):
        self.destroy()
        os.system("python Soins_CourantGUI.py")

        # chemin_fichier = "/Creation_dun_logiciel_de_Registre_delevage/view/Soins_CourantGUI.py"
        # fichier = Methode1.ouvrir_fichier(chemin_fichier)
        # #fermer_fichier(fichier)
        # # Ajoutez ici le code pour traiter le contenu du fichier si nécessaire
    def ouvrir_caractheristiques(self):
     self.destroy()
     os.system("python Presence_et_Caratheristiques_animauxGUI.py")

    def ouvrir_nouvelle_fenetre(self):
     self.destroy()
     os.system("python Page_1_mouvements_temporaires_des_animaux.py")
    
    def open_new_window(self):
     self.destroy()
     os.system("python Page_1_mouvements_temporaires_des_animaux.py")
    

# ... (autres méthodes)
        





    # def ouvrir_caracteristiques_lieu(self):
    #     chemin_fichier = "/Creation_dun_logiciel_de_Registre_delevage/view/Page_caractéristique_du_lieu_de_detention.py"
    #     fichier = ouvrir_fichier(chemin_fichier)
    #     #fermer_fichier(fichier)
    #     # Ajoutez ici le code pour traiter le contenu du fichier si nécessaire

    # def ouvrir_nouvelle_fenetre(self):
    #     self.destroy()
    #     os.system("python Page_1_mouvements_temporaires_des_animaux.py")

# ... (autres méthodes)

if __name__ == "__main__":
    fenetre_principale = FenetrePrincipale()
    fenetre_principale.mainloop()
