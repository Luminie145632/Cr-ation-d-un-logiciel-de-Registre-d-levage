# Accueil.py
import sys
sys.path.insert(1, '/Creation_dun_logiciel_de_Registre_delevage/')
import tkinter as tk
from tkinter import ttk
from tkinter import Button  
from PIL import Image, ImageTk
import glob
import os
import Methode1
from Page_caracteristique_du_lieu_de_detention import FenetrePrincipaleCaracth
from Soins_CourantGUI import Soins_cournat
from Presence_et_Caratheristiques_animauxGUI import Presence_CaratherisisGUI
from Page_controle_du_registre_delevage import FenetrePrincipaleControle
import json
from tkinter import *
from tkinter import messagebox, Frame, Entry, Button, Label, BOTH, ttk, Canvas
#from controller.Methode_1 import ouvrir_fichier, fermer_fichier

class FenetrePrincipale(tk.Tk):
    def __init__(self,width):
        super().__init__()

        self.numberColumns = width   
         
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


        btn_mouvement_temporaire_mvt = tk.Button(navbar, text="Mouvement Temporaire des Animaux", command=lambda: self.ouvrir_mouvement_temporaires(width))
        btn_mouvement_temporaire_mvt.grid(row=3, column=0, sticky="ew")

        btn_mouvement_temporaire = tk.Button(navbar, text="Intervents et Soins Courants", command=self.ouvrir_interventions)
        btn_mouvement_temporaire.grid(row=4, column=0, sticky="ew")

        btn_mouvement_temporaire = tk.Button(navbar, text="Contrôle du Registre d'élevage", command=self.ouvrir_registre_elevage)
        btn_mouvement_temporaire.grid(row=5, column=0, sticky="ew")   

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

    def ouvrir_mouvement_temporaires(self, width):

        col_titles = ["Date de sortie", "Nom de l'équidé", "Motif", "Etape éventuelle (adresse)", "Lieu de destination (Adresse)", "Date de retour"]
        self.numberLines = width
        self.numberColumns = width
        self.col_titles = col_titles
        
        # Titre du tableau
        label_titre_tableau = tk.Label(self, text="MOUVEMENTS TEMPORAIRES DES ANIMAUX")
        label_titre_tableau.grid(row=0, column=0, columnspan=20, sticky='nsew')

        # Phrase à deux trous
        label_intro = tk.Label(self, text="Liste des mouvements temporaires entre le")
        label_intro.grid(row=1, column=0, sticky='nsew')

        self.entry_debut = tk.Entry(self, width=5)
        self.entry_debut.grid(row=1, column=1, sticky='nsew')

        label_et_le = tk.Label(self, text="et le")
        label_et_le.grid(row=1, column=2, sticky='nsew')

        self.entry_fin = tk.Entry(self, width=5)
        self.entry_fin.grid(row=1, column=3, sticky='nsew')

        # Phrase additionnelle
        label_option = tk.Label(self, text="(Option 1 : mouvements peu fréquents)")
        label_option.grid(row=2, column=0, columnspan=20, sticky='nsew')

        # Ajout des titres de colonnes
        for j in range(6):
            print("nombres " +str(self.numberColumns))
            col_title = tk.Label(self, text=col_titles[j], width=15, relief="solid", bg="lightgray", anchor="w")
            col_title.grid(row=3, column=j, sticky='nsew')  # Utilise sticky pour que la colonne s'adapte

        # Ajout des données du tableau
        self.data = []
        for i in range(4, self.numberLines + 4):
            line = []
            for j in range(20):
                cell = tk.Entry(self, width=15)  # Ajustez la largeur selon vos besoins
                cell.grid(row=i, column=j, sticky='nsew')  # Utilise sticky pour que la colonne s'adapte
                line.append(cell)
            self.data.append(line)

        # Configurer la gestion des colonnes pour qu'elles s'adaptent au contenu
        for j in range(self.numberColumns):
            self.grid_columnconfigure(j, weight=1)

        # Bouton pour ajouter une nouvelle ligne
        self.bouton_ajouter_ligne = tk.Button(self, text="Ajouter une ligne", command=self.ajouter_ligne, width=15, height=1)
        self.bouton_ajouter_ligne.grid(row=self.numberLines + 4, columnspan=self.numberColumns, sticky='nsew')
        
        btn_mouvement_temporaire = tk.Button(self, text="Valider", command=  self.valider_informations, width=15, height=1)#self.signaler_mouvement_temporaire)
        btn_mouvement_temporaire.grid(row=self.numberLines + 5, columnspan=self.numberColumns, sticky='nsew')
        
        btn_mouvement_temporaire = tk.Button(self, text="Voir l'histoire de mes mouvements", command=  self.view_animals, width=15, height=1)#self.signaler_mouvement_temporaire)
        btn_mouvement_temporaire.grid(row=self.numberLines + 6, columnspan=self.numberColumns, sticky='nsew')
         
     

        # Création du Label pour afficher les images
        self.label_image = tk.Label(self, bd=0, highlightthickness=0)
        self.label_image.grid(row=self.numberLines + 9, column=0, columnspan=self.numberColumns, sticky='nsew')

        # Appel à la méthode pour gérer le fond d'image changeant
        self.setup_background_animation()

        # Gestionnaire d'événements pour détecter les changements de taille de fenêtre
        self.bind("<Configure>", self.redimensionner_image)


    def redimensionner_image(self, event):
        image_path = self.image_paths[self.current_image_index]
        image = Image.open(image_path)
        image = image.resize((self.winfo_width(), self.winfo_height()))
        photo = ImageTk.PhotoImage(image)
        self.label_image.configure(image=photo)
        self.label_image = photo
    
    def Mouvements_temporaires(self,numberColumns):
       label_titre_tableau = Label(self, text="MOUVEMENTS OEMPORAIRES DES ANIMAUX")
       label_titre_tableau.grid(row=0, column=0, columnspan=self.numberColumns, sticky='nsew')

        # Phrase à deux trous
       label_intro = Label(self, text="Liste des mouvements temporaires entre le")
       label_intro.grid(row=1, column=0, sticky='nsew')

       self.entry_debut = Entry(self, width=5)
       self.entry_debut.grid(row=1, column=1, sticky='nsew')

       label_et_le = Label(self, text="et le")
       label_et_le.grid(row=1, column=2, sticky='nsew')

       self.entry_fin = Entry(self, width=5)
       self.entry_fin.grid(row=1, column=3, sticky='nsew')

        # Phrase additionnelle
       label_option = Label(self, text="(Option 1 : mouvements peu fréquents)")
       label_option.grid(row=2, column=0, columnspan=self.numberColumns, sticky='nsew')

        # Ajout des titres de colonnes
       for j in range(self.numberColumns):
         col_title = Label(self, text=self.col_titles[j], width=15, relief="solid", bg="lightgray", anchor="w")
         col_title.grid(row=3, column=j, sticky='nsew')  # Utilise sticky pour que la colonne s'adapte

        # Ajout des données du tableau
         self.data = []
         for i in range(4, self.numberLines + 4):
            line = []
            for j in range(self.numberColumns):
                cell = Entry(self, width=15)  # Ajustez la largeur selon vos besoins
                cell.grid(row=i, column=j, sticky='nsew')  # Utilise sticky pour que la colonne s'adapte
                line.append(cell)
            self.data.append(line)

        # Configurer la gestion des colonnes pour qu'elles s'adaptent au contenu
         for j in range(self.numberColumns):
            self.grid_columnconfigure(j, weight=1)

        # Bouton pour ajouter une nouvelle ligne
         self.bouton_ajouter_ligne = Button(self, text="Ajouter une ligne", command=self.ajouter_ligne, width=15, height=1)
         self.bouton_ajouter_ligne.grid(row=self.numberLines + 4, columnspan=self.numberColumns, sticky='nsew')
        
         btn_mouvement_temporaire = Button(self, text="Valider", command=  self.valider_informations, width=15, height=1)#self.signaler_mouvement_temporaire)
         btn_mouvement_temporaire.grid(row=self.numberLines + 5, columnspan=self.numberColumns, sticky='nsew')
        
         btn_mouvement_temporaire = Button(self, text="Voir l'histoire de mes mouvements", command=  self.view_animals, width=15, height=1)#self.signaler_mouvement_temporaire)
         btn_mouvement_temporaire.grid(row=self.numberLines + 6, columnspan=self.numberColumns, sticky='nsew')
        
         btn_mouvement_retour = Button(self, text="Retour au menu principal", command=  self.return_main_menu, width=15, height=1 )#self.signaler_mouvement_temporaire)
         btn_mouvement_retour.grid(row=self.numberLines + 7, columnspan=self.numberColumns, sticky='nsew')



        # Création du Label pour afficher les images
         self.label_image = tk.Label(self, bd=0, highlightthickness=0)
         self.label_image.grid(row=self.numberLines + 9, column=0, columnspan=self.numberColumns, sticky='nsew')
        
      
        # Appel à la méthode pour gérer le fond d'image changeant
         self.setup_background_animation()

        # Gestionnaire d'événements pour détecter les changements de taille de fenêtre
         self.bind("<Configure>", self.redimensionner_image)


    def Caratherisis_Window(self, height, width, col_titles):
     
     tex1 = tk.Label(self, text='Encadrement Zootechnique Sanitaire et Médical des Animaux', fg='cyan')
     tex1.grid(row=11, column=0, columnspan=8)
     self.numberColumns = width
     self.col_titles=col_titles
    

    # Ajout des titres de colonnes
     for j in range(self.numberColumns):
        col_title = tk.Label(self, text=self.col_titles[j], width=20, relief="solid", bg="lightgray", anchor="w")
        col_title.grid(row=12, column=j, sticky='nsew')

    # Ajout des données du tableau
     self.data = []
     for i in range(13, height + 13):  # Démarrez à la ligne 13
        line = []
        for j in range(self.numberColumns):
            cell = tk.Entry(self, width=20)
            cell.grid(row=i, column=j, sticky='nsew')
            line.append(cell)
        self.data.append(line)

    # Boutons et autres widgets
     btn_valider = tk.Button(self, text="Valider", command=self.valider_informations)
     btn_valider.grid(row=height + 13, column=0, columnspan=self.numberColumns, sticky='nsew')

     btn_view_animals = tk.Button(self, text="Consulter mes animaux", command=self.view_animals)
     btn_view_animals.grid(row=height + 14, column=0, columnspan=self.numberColumns, sticky='nsew')

    #  btn_return_main_menu = tk.Button(self, text="Retour au menu principal", command=self.return_main_menu)
    #  btn_return_main_menu.grid(row=height + 15, column=0, columnspan=self.numberColumns, sticky='nsew')    

    def load_image(self):
        

        try:
         image_path = self.image_paths[self.current_image_index]
         image = Image.open(image_path)
         image = image.resize((self.winfo_width(), self.winfo_height()))
         photo = ImageTk.PhotoImage(image)
         self.label_image.configure(image=photo)
         self.label_image.image = photo
         self.current_image_index = (self.current_image_index + 1) % len(self.image_paths)
        
        except Exception:
          print(" ça marche pas ")   

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
    
    def view_animals(self):
    
     with open('caratheristiques_animaux.json', 'r') as file:
        data = json.load(file)
        
    # Création d'un champ de texte pour afficher les informations
     text_field = Text(self, wrap=WORD)
     text_field.grid(row=13, column=0, columnspan=self.numberColumns, sticky='nsew')
     text_field2 = Text(self, wrap=WORD)
     text_field2.grid(row=14, column=0, columnspan=self.numberColumns, sticky='nsew')
    # Récupération des informations et ajout dans le champ de texte
     for animal in data['caratheristiques_animaux']:
        text_field.insert(END, f"Nom: {animal['Nom']}\n")
        text_field.insert(END, f"Numéro SIRE: {animal.get('NeSIRE', '')}\n")
        text_field.insert(END, f"Numéro transpondeur: {animal.get('Netranspondeur', '')}\n")
       # text_field.insert(END, f"Nom et coordonnées du propriétaire: {animal.get('Nom et coordonnees du proprietaire')}\n")
        text_field.insert(END, f"Date de première entrée: {animal.get('Date de premiere entree', '')}\n")
        text_field2.insert(END, f"Adresse de provenance: {animal.get('Adresse de provenance', '')}\n")
        text_field2.insert(END, f"Date de sortie définitive: {animal.get('Date de sortie definitive', '')}\n")
        text_field2.insert(END, f"Adresse de destination: {animal.get('Adresse de destination', '')}\n\n")

    #checked
    def ouvrir_caracteristiques_lieu(self):
     col_titles = ["Nom", "n° SIRE", "n° Transpondeur", "Nom et coordonnées du propriétaires", "Date de première entrée", "Adresse de provenance","Date de sortie définitive","Adresse de destination"]  
     
     self.Caratherisis_Window(  3, 8 ,col_titles=col_titles)

    # self.destroy()
    # os.system("python Page_caracteristique_du_lieu_de_detention.py")

    def ouvrir_interventions(self):
     
     col_titles = ["Date", "Type d'intervention", "Intervenant (si vétérianire)", "Traitement", "N ordonnance","Date de début", "Date de fin","N°d’ordonnance","Délai d’attentecompétition(facultatif)","Délai d’attente abatage ou exclusion abattage"]
     fenetre_principale = Soins_cournat(tk.Tk(), height=6, width=10, col_titles=col_titles)
     fenetre_principale.mainloop() 

    def ajouter_ligne(self):
        # Ajouter une nouvelle ligne
     nouvelle_ligne = []
     for j in range(self.numberColumns):
            cell = Entry(self, width=15)  # Ajustez la largeur selon vos besoins
            cell.grid(row=self.numberLines + 6, column=j, sticky='nsew')  # Utilise sticky pour que la colonne s'adapte
            nouvelle_ligne.append(cell)
     self.data.append(nouvelle_ligne)
     self.numberLines += 1

        # Déplacer le bouton et l'image vers le bas
     self.bouton_ajouter_ligne.grid(row=self.numberLines + 6, columnspan=self.numberColumns, sticky='nsew')
     self.label_image.grid(row=self.numberLines + 8, column=0, columnspan=self.numberColumns, sticky='nsew')



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
        fenetre_principale = Soins_cournat(tk.Tk(), height=20, width=10, col_titles=col_titles)
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

    def open_new_window(self):
     self.destroy()
     os.system("python Page_1_mouvements_temporaires_des_animaux.py")

    def valider_informations(self):
     
        # Récupérer les informations depuis les champs d'entrée (à adapter en fonction de votre logique)
        nom = self.data[1][0].get()
        sire = self.data[2][0].get()
        no_transpondeur = self.data[3][0].get()
        nom_proprio = self.data[4][0].get()
        date_entree = self.data[5][0].get()
        adresse_provenance = self.data[6][0].get()
        date_sortie_def=  self.data[7][0].get()
        adresse_destination= self.data[8][0].get()

        # Afficher les valeurs dans la console (vous pouvez remplacer cela par vos propres actions)
    
        nouveau_caract = {
           
       "num_siret": "321546",
        "Nom": nom,
        "NO_SIRE": sire,
        "NO_transpondeur": no_transpondeur,
        "Nom_coordonnees_proprietaire": {
          "Nom": nom_proprio,
          "Coordonnees": {
            "Adresse": adresse_provenance,
            "Ville": "Ville_1",
            "Code postal": "12345"
          }
        },
        "Date_premiere_entree": date_entree,
        "Adresse_provenance": adresse_provenance,
        "Date_sortie_definitive": date_sortie_def,
        "Adresse_destination": "Destination_1"
     
    }

    # profesionnel =Profesionnel(code_ape, statut_juridique, denomination)
        with open('caratheristiques_animaux.json', 'r') as json_file:
         data = json.load(json_file)

    # Ajouter le nouveau professionnel à la liste des professionnels
         data["caratheristiques_animaux"].append(nouveau_caract)

    # Réécrire le fichier JSON avec la nouvelle structure
        with open('caratheristiques_animaux.json', 'w') as json_file:
         json.dump(data, json_file, indent=2)

    # Retourner le JSON du nouveau professionnel (à des fins de débogage ou autre)
         return json.dumps(nouveau_caract)

if __name__ == "__main__":
    fenetre_principale = FenetrePrincipale(width=20)
    fenetre_principale.mainloop()
