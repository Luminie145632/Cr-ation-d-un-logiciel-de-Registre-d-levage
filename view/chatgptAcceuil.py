# Accueil.py
import sys
sys.path.insert(1, '/Creation_dun_logiciel_de_Registre_delevage/')
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import glob
import os
import Methode1
from Page_caracteristique_du_lieu_de_detention import FenetrePrincipaleCaracth
from Soins_CourantGUI import Soins_cournat
from Presence_et_Caratheristiques_animauxGUI import Presence_CaratherisisGUI
from Page_controle_du_registre_delevage import FenetrePrincipaleControle
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
        etiquette_bienvenue.grid(row=10, column=0, sticky="ew")

        # Création de la barre de navigation
        navbar = tk.Frame(self, bd=2, relief=tk.GROOVE)
        navbar.grid(row=0, column=0, sticky="ew")

        # Création des boutons de la barre de navigation
        btn_caracteristiques_lieu = tk.Button(navbar, text="Caractéristiques du Lieu de Détention", command=self.ouvrir_caracteristiques_lieu)
        btn_caracteristiques_lieu.grid(row=1, column=0, sticky="ew")

        btn_mouvement_temporaire = tk.Button(navbar, text="Encadrement Zootechnique, Sanitaire et Medical des Animaux", command=self.open_new_window)
        btn_mouvement_temporaire.grid(row=2, column=0, sticky="ew")

        btn_mouvement_temporaire = tk.Button(navbar, text="Présence et Caractéristiques des Animaux", command=self.ouvrir_caractheristiques)
        btn_mouvement_temporaire.grid(row=3, column=0, sticky="ew")

        btn_mouvement_temporaire = tk.Button(navbar, text="Mouvement Temporaire des Animaux", command=self.ouvrir_nouvelle_fenetre)
        btn_mouvement_temporaire.grid(row=4, column=0, sticky="ew")

        btn_mouvement_temporaire = tk.Button(navbar, text="Intervents et Soins Courants", command=self.ouvrir_interventions)
        btn_mouvement_temporaire.grid(row=5, column=0, sticky="ew")

        btn_mouvement_temporaire = tk.Button(navbar, text="Contrôle du Registre d'élevage", command=self.ouvrir_registre_elevage)
        btn_mouvement_temporaire.grid(row=6, column=0, sticky="ew")

        # Création du Label pour afficher les images
        self.label_image = tk.Label(self, bd=0, highlightthickness=0)
        self.label_image.grid(row=7, column=0, sticky="ew")

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
    def Caratherisis_Window(self, fenetre, height, width, col_titles):
     self.numberColumns=width
     self.col_titles=col_titles
    # Attributs de la classe
     tex1 = tk.Label(self, text='Encadrement Zootechnique Sanitaire et Médical des Animaux', fg='cyan')
     tex1.grid(row=0, column=0, columnspan=8)
    
    # Ajout des titres de colonnes
     for j in range(self.numberColumns):
        col_title = tk.Label(self, text=self.col_titles[j], width=20, relief="solid", bg="lightgray", anchor="w")
        col_title.grid(row=1, column=j, sticky='nsew')
    
    # Ajout des données du tableau
     self.data = []
     for i in range(2, self.numberLines + 2):
        line = []
        for j in range(self.numberColumns):
            cell = tk.Entry(self, width=20)
            cell.grid(row=i, column=j, sticky='nsew')
            line.append(cell)
        self.data.append(line)

        self.date_sortie = line[1]  # ???

     btn_valider = tk.Button(self, text="Valider", command=self.valider_informations)
     btn_valider.grid(row=12, column=0, columnspan=self.numberColumns, sticky='nsew')

     btn_valider = tk.Button(self, text="Consulter mes animaux", command=self.view_animals)
     btn_valider.grid(row=13, column=0, columnspan=self.numberColumns, sticky='nsew')

     btn_mouvement_temporaire = tk.Button(self, text="Retour au menu principal", command=self.return_main_menu)
     btn_mouvement_temporaire.grid(row=14, column=0, columnspan=self.numberColumns, sticky='nsew')
    def Caratherisis_Window(self, fenetre, height, width, col_titles):
        # Attributs de la classe
        # super().__init__(fenetre)
        # self.fenetre=fenetre
        # self.height=height
        # self.width=width
        # self.col_titles=col_titles
        # self.numberLines = 1
        # self.numberColumns=width
        # self.pack(fill="both")
        #ouou
        tex1 = tk.Label(self, text='Encadrement Zootechnique Sanitaire et Médical des Animaux', fg='cyan')
        tex1.grid(row=0, column=0, columnspan=8)
        # Ajout des titres de colonnes

        for j in range(self.numberColumns):
         col_title = tk.Label(self, text=self.col_titles[j], width=20, relief="solid", bg="lightgray", anchor="w")
         col_title.grid(row=0, column=j, sticky='nsew')

        # Ajout des données du tableau
        self.data = []
        for i in range(1, self.numberLines + 1):
            line = []
            for j in range(self.numberColumns):
                cell = tk.Entry(self, width=20)
                cell.grid(row=i, column=j, sticky='nsew')
                line.append(cell)
            self.data.append(line)

            self.date_sortie=line[1]    
        # Configurer la gestion des colonnes pour qu'elles s'adaptent au contenu
        for j in range(self.numberColumns):
            self.grid_columnconfigure(j, weight=1)
        try:
        # Charger l'image avec PIL
         image = Image.open("cheval_blanc.png")
        # Augmenter la taille de l'image (dans cet exemple, je l'ai doublée)
         image = image.resize((960, 540), Image.BICUBIC)
        # Convertir l'image en format Tkinter PhotoImage
         self.image = ImageTk.PhotoImage(image)

        # Afficher l'image sur le canvas
         self.can1.create_image(0, 0, anchor=tk.NW, image=self.image)
        
        except Exception:
          print("oyvxies")
        
        btn_valider = tk.Button(self, text="Valider", command=self.valider_informations)
        btn_valider.grid(row=10, column=0, columnspan=self.numberColumns, sticky='nsew')

        btn_valider = tk.Button(self, text="Consulter mes animaux", command=self.view_animals)
        btn_valider.grid(row=11, column=0, columnspan=self.numberColumns, sticky='nsew')
        
        city_frame = tk.Label(self, text='', fg='black')
        region_frame = tk.Label(self, text='', fg='black')
        Departement_frame = tk.Label(self, text='', fg='black')

        # Création des boutons de la barre de navigation
        btn_mouvement_temporaire = tk.Button(self, text="Retour au menu principal", command=self.return_main_menu)
        btn_mouvement_temporaire.grid(row=12, column=0, columnspan=self.numberColumns, sticky='nsew')


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
      
     col_titles = ["Nom", "n° SIRE", "n° Transpondeur", "Nom et coordonnées du propriétaires", "Date de première entrée", "Adresse de provenance","Date de sortie définitive","Adresse de destination"]  
     self.Caratherisis_Window( tk.Tk(), 3, 8 , col_titles);
    
  
  
    # self.destroy()
    # os.system("python Page_caracteristique_du_lieu_de_detention.py")

    def ouvrir_interventions(self):
     
     col_titles = ["Date", "Type d'intervention", "Intervenant (si vétérianire)", "Traitement", "N ordonnance","Date de début", "Date de fin","N°d’ordonnance","Délai d’attentecompétition(facultatif)","Délai d’attente abatage ou exclusion abattage"]

     fenetre_principale = Soins_cournat(tk.Tk(), height=6, width=10, col_titles=col_titles)
     fenetre_principale.mainloop() 

    #  self.destroy()
    #  os.system("python Soins_CourantGUI.py") 

    def ouvrir_registre_elevage(self):
     self.destroy()
     os.system("python Page_controle_du_registre_delevage.py") 

     col_titles = ["Date oo", "Organisme de contrôle", "Motif de contrôle", "Nom du contrôleur", "Cachet", "Signature"]
     fenetre_principale = FenetrePrincipaleControle(tk.Tk(), height=3, width=6, col_titles=col_titles)
     fenetre_principale.mainloop()
    
    #  chemin_fichier = "/Creation_dun_logiciel_de_Registre_delevage/view/Page_caracteristique_du_lieu_de_detention.py"
    #  fichier = Methode1.ouvrir_fichier(chemin_fichier)
    #   #  fichier = controller.Methode_1.ouvrir_fichier(chemin_fichier)
    #     #fermer_fichier(fichier)
    #     # Ajoutez ici le code pour traiter le contenu du fichier si nécessaire
    
    #checked
    def open_healthcare(self):
        
        col_titles = ["Nom", "n° SIRE", "n° Transpondeur", "Nom et coordonnées du propriétaires", "Date de première entrée", "Adresse de provenance","Date de sortie définitive","Adresse de destination"]  
        fenetre_principale = Soins_cournat(tk.Tk(), height=6, width=10, col_titles=col_titles)
        fenetre_principale.mainloop()


        # self.destroy()
        # os.system("python Soins_CourantGUI.py")

        # chemin_fichier = "/Creation_dun_logiciel_de_Registre_delevage/view/Soins_CourantGUI.py"
        # fichier = Methode1.ouvrir_fichier(chemin_fichier)
        # #fermer_fichier(fichier)
        # # Ajoutez ici le code pour traiter le contenu du fichier si nécessaire
    def ouvrir_caractheristiques(self):
    #  self.destroy()
    #  os.system("python Presence_et_Caratheristiques_animauxGUI.py")
     col_titles = ["Nom", "n° SIRE", "n° Transpondeur", "Nom et coordonnées du propriétaires", "Date de première entrée", "Adresse de provenance","Date de sortie définitive","Adresse de destination"]  
     fenetre_principale = Presence_CaratherisisGUI(tk.Tk(), height=3, width=8, col_titles=col_titles)
     fenetre_principale.mainloop()

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