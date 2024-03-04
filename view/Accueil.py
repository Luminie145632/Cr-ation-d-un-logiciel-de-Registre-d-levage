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
    def __init__(self,width,col_titles,height):
        super().__init__()

        self.numberColumns = width 
        self.numberLines = height
        self.col_title=col_titles
        self.data=[]  
         
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
        navbar.grid(row=10 ,  columnspan= len(self.col_title), sticky="ew")

        # Création des boutons de la barre de navigation # checked
        btn_caracteristiques_lieu = tk.Button(navbar, text="Caractéristiques du Lieu de Détention", command=self.ouvrir_caracteristiques_lieu_detention) # del title
        btn_caracteristiques_lieu.grid(row=0, column=1 , sticky="ew")

        btn_mouvement_temporaire = tk.Button(navbar, text="Encadrement Zootechnique, Sanitaire et Medical des Animaux", command=self.open_encadrement_zootechnique) #det title
        btn_mouvement_temporaire.grid(row=0, column=2, sticky="ew")

        #checked 
        btn_mouvement_temporaire = tk.Button(navbar, text="Présence et Caractéristiques des Animaux", command=self.ouvrir_caractheristiques_animaux) #det title
        btn_mouvement_temporaire.grid(row=0, column=3, sticky="ew")

        btn_mouvement_temporaire_mvt = tk.Button(navbar, text="Mouvements Temporaire des Animaux", command=lambda: self.ouvrir_mouvement_temporaires(width)) #det title
        btn_mouvement_temporaire_mvt.grid(row=0, column=4, sticky="ew")

        btn_mouvement_temporaire = tk.Button(navbar, text="Intervents et Soins Courants", command=lambda:self.ouvrir_interventions(width)) # det title
        btn_mouvement_temporaire.grid(row=0, column=5, sticky="ew")

        btn_mouvement_temporaire = tk.Button(navbar, text="Contrôle du Registre d'élevage", command=lambda:self.ouvrir_controle_registre_elevage(width)) # det title
        btn_mouvement_temporaire.grid(row=0, column=6, sticky="ew")   

        # Création du Label pour afficher les images
        self.label_image = tk.Label(self, bd=0, highlightthickness=0)
        self.label_image.grid(row=0, column=7, sticky="ew")

        # Gestionnaire d'événements pour détecter les changements de taille de fenêtre
        self.bind("<Configure>", self.redimensionner_image)

        # Appel à la méthode pour gérer le fond d'image changeant
        try:
         self.setup_background_animation()
        except Exception:     
          print(" Marche pas photo de fond ") 
    # pages
    def setup_background_animation(self):
      
        self.image_paths = glob.glob("/Creation_dun_logiciel_de_Registre_delevage/images/*.png")
        self.current_image_index = 0
        self.load_image()
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
        
         btn_mouvement_temporaire = Button(self, text="Voir l'histoire de mes mouvements", command= lambda: self.view_animals, width=15, height=1)#self.signaler_mouvement_temporaire)
         btn_mouvement_temporaire.grid(row=self.numberLines + 6, columnspan=self.numberColumns, sticky='nsew')
        
        # Création du Label pour afficher les images
         self.label_image = tk.Label(self, bd=0, highlightthickness=0)
         self.label_image.grid(row=self.numberLines + 9, column=0, columnspan=self.numberColumns, sticky='nsew')
          
        # Appel à la méthode pour gérer le fond d'image changeant
         self.setup_background_animation()

        # Gestionnaire d'événements pour détecter les changements de taille de fenêtre
         self.bind("<Configure>", self.redimensionner_image)  
    
    def load_image(self):
        
        try:
     
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
        except Exception:
          print(" ça marche pas ")
    
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
    

    # view informations
    def view_caratherisis_detention_place(self):
     with open('caracteristiques_lieu_detention.json', 'r') as file:
        data = json.load(file)
    
    # Affichage des animaux dans les zones de texte
     for i, animal in enumerate(data['caracteristiques_lieu_detention'], start=15):
        text_fields = []

        for j, key in enumerate(self.col_title):
            text_field = Entry(self, width=3) 
            text_field.grid(row=i, column=j, sticky='nsew')
            # Récupérer la valeur de la clé si elle existe, sinon utiliser une chaîne vide
            value = animal.get(key, '')
            text_field.insert(END, f"{key}: {value}\n")
            text_fields.append(text_field)
        self.data.append(text_fields)
        
     self.bouton_ajouter_ligne = Button(self, text="Ajouter une ligne", command=self.ajouter_ligne)
     self.bouton_ajouter_ligne.grid(row=self.numberLines + 4, columnspan=len(self.col_title), sticky='nsew')
    
     btn_valider = Button(self, text="Modifier les informations", command=self.valider_carathersitiques_lieu)
     btn_valider.grid(row=self.numberLines + 5, columnspan=len(self.col_title), sticky='nsew')
    
    def view_animals(self):
     with open('caratheristiques_animaux.json', 'r') as file:
        data = json.load(file)
    
    # Affichage des animaux dans les zones de texte
     for i, animal in enumerate(data['caratheristiques_animaux'], start=15):
        text_fields = []
        for j, key in enumerate(self.col_title):
            text_field = Text(self, wrap=WORD)
            text_field.grid(row=i, column=j, sticky='nsew')
            value = animal.get(key, '')
            text_field.insert(END, f"{key}: {value}\n")
            text_fields.append(text_field)
        self.data.append(text_fields)
        for i in range(15,23):
            line = []
            for j in range(8):
                cell = Entry(self, width=5)
                cell.grid(row=i, column=j, sticky='nsew')
                line.append(cell)
            self.data.append(line)

            self.date_sortie=line[1]    

     print(" marche pas ")
    # def view_informations_(slef):  
    
    
    
    def controle_registre(self,width):    

        self.numberLines = width
        self.numberColumns = width

        for j in range(self.numberColumns):   # sui ça affiche pas c'est qu'il y a zero 
            col_title = Label(self, text=self.col_titles[j], width=20, relief="solid", bg="lightgray", anchor="w")
            col_title.grid(row=0, column=j, sticky='nsew')  # Utilise sticky pour que la colonne s'adapte

        # Ajout des données du tableau
        self.data = []
        for i in range(1, self.numberLines + 1):
            line = []
            for j in range(self.numberColumns):
                cell = Entry(self, width=20)  # Ajustez la largeur selon vos besoins
                cell.grid(row=i, column=j, sticky='nsew')  # Utilise sticky pour que la colonne s'adapte
                line.append(cell)
            self.data.append(line)

        # Configurer la gestion des colonnes pour qu'elles s'adaptent au contenu
        for j in range(self.numberColumns):
            self.grid_columnconfigure(j, weight=1)

        # Bouton pour ajouter une nouvelle ligne
        self.bouton_ajouter_ligne = Button(self, text="Ajouter une ligne", command=self.ajouter_ligne, width=20, height=1)
        self.bouton_ajouter_ligne.grid(row=self.numberLines + 1, columnspan=self.numberColumns, sticky='nsew')
             
        self.bouton_ajouter_ligne = Button(self, text="Valider les informations", command=self.valider_informations, width=20, height=1)
        self.bouton_ajouter_ligne.grid(row=self.numberLines + 3, columnspan=self.numberColumns, sticky='nsew')
        
        self.bouton_menu_principal = Button(self, text="Retour au menu principal", command=self.return_main_menu, width=20, height=1)
        self.bouton_menu_principal.grid(row=self.numberLines + 4, columnspan=self.numberColumns, sticky='nsew')
    #checked           
    def create_text(self):
       for i in range(10, 15):
           line = []
           for j in range(self.numberColumns):
             cell = Entry(self, width=20)
             cell.grid(row=i, column=j, sticky='nsew')
             line.append(cell)
             self.data.append(line) #je veux que lorsque l'on appuie sur le bouton valider les informations entrées dans les champ de texte soient mises dans le fichier json suivant
       return self.data   
    def supprimer_widgets(self):
     # Parcours de tous les widgets de la fenêtre
     for widget in self.winfo_children():
            # Vérifie si le widget a été créé dans __init__
         if isinstance(widget, tk.Entry) and widget not in [self.__init__]:   #, self.bouton_init]:
                # Destruction du widget s'il n'a pas été créé dans __init__
                widget.destroy()
         
         if isinstance(widget,tk.Label):
                widget.destroy()
         if isinstance(widget,tk.Button):
                widget.destroy()       
         for title in self.col_title:
            self.col_title.remove(title) 
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
    #open the windows of the navigation map     
    def ouvrir_caracteristiques_lieu_detention(self):
    # Assurez-vous que les données précédentes sont effacées si nécessaire
     self.supprimer_widgets()  # Assurez-vous que cette méthode est correctement implémentée

    # Calcul de la longueur de la phrase "Caractéristiques lieu de détention"
    # Définition des titres des colonnes
     self.col_title = ["Sire","statut juridique","denomination","Adresse", " numéro de Téléphone", "Portable", "Mail","prenom","nom_usage","Adresse","portable","mail"
                      ,"x","x","x"]
                     
    # Ajout de l'espace entre le menu de navigation et "Sire"
     
     for j, col_tmp in enumerate(self.col_title):
  
       col_tmp = self.col_title[j]
       col_title_label = tk.Label(self,text=col_tmp,width=22,relief="solid",bg="lightgray",font=("Helvetica", 8)) # , anchor="w")
       col_title_label.grid(row=11,column=j,sticky='nsew')
    # Ajustement de la largeur de la première colonne
    # Initialisation des données
     self.data = []

    # Création des champs d'entrée
     for i in range(5):
        row_data = []
        for j in range(len(self.col_title)):
            cell = tk.Entry(self, width=22)
            cell.grid(row=i+12, column=j, sticky='nsew')  # Commencer à la ligne 12
            row_data.append(cell)
        self.data.append(row_data)


        # Configurer la gestion des colonnes pour qu'elles s'adaptent au contenu
     for j in range(self.numberColumns):
        self.grid_columnconfigure(j, weight=1) 

    # Bouton de validationxx
     self.bouton_ajouter_ligne = Button(self, text="Ajouter une ligne", command=self.ajouter_ligne)
     self.bouton_ajouter_ligne.grid(row=self.numberLines + 4, column=0, columnspan=len(self.col_title), sticky='nsew')
     
     btn_valider = tk.Button(self, text="Valider", command=self.valider_carathersitiques_lieu)
     btn_valider.grid(row=self.numberLines + 5, column=0, columnspan=len(self.col_title), sticky='nsew')

     btn_valider = tk.Button(self, text="Afficher mes lieux de détention", command=self.valider_carathersitiques_lieu)
     btn_valider.grid(row=self.numberLines + 6, column=0, columnspan=len(self.col_title), sticky='nsew')
    def open_encadrement_zootechnique(self):
       self.supprimer_widgets()  # Assurez-vous que cette méthode est correctement implémentée
    
    # Définition des titres des colonnes
       self.col_title =   ["Lieu habituel et durée détention moyenne", "Nom et coordonnées vétérinaire traitant", "Nom et coordonnées vétérinaire sanitaire" ,"Nom et coordonnées du référent bien-être animal(pour les structures équines professionnelles)", "Nom, adresse et N° de téléphone desOrganisme(s) à vocation sanitaire reconnu(s) et dessociétés mères (facultatif)", "Nom, adresse et N° de téléphone du maréchalferrant (facultatif)","Nom, adresse et N° de téléphone du dentiste(facultatif)"] #Nom, adresse et N° de téléphone du dentiste(facultatif)
    
    # Affichage des titres des colonnes
       for j, col_tmp in enumerate(self.col_title):

        col_title_label = tk.Label(self, text=col_tmp, width=90, relief="solid", bg="lightgray", anchor="w",font=("Helvetica", 8))
        col_title_label.grid(row=11,column=j,sticky='nsew')

    # Initialisation des données
       self.data = []

    # Création des champs d'entrée
       for i in range(7):
        row_data = []
        for j in range(7):
            cell = tk.Entry(self, width=90)
            cell.grid(row=i+12, column=j, sticky='nsew')  # Commencer à la ligne 12
            row_data.append(cell)
        self.data.append(row_data)


       for j in range(len(self.col_title)):
        self.grid_columnconfigure(j, weight=1) 


       # Configurer la gestion des colonnes pour qu'elles s'adaptent au contenu
       for j in range(self.numberColumns):
        self.grid_columnconfigure(j, weight=1)  
       
    # Bouton de validation
       self.bouton_ajouter_ligne = Button(self, text="Ajouter une ligne", command=self.ajouter_ligne)
       self.bouton_ajouter_ligne.grid(row=self.numberLines + 4, columnspan=len(self.col_title), sticky='nsew')

       btn_valider = tk.Button(self, text="Valider", command=self.valider_encadrement_Zootechnique_animaux)
       btn_valider.grid(row=self.numberLines + 5, columnspan=len(self.col_title), sticky='nsew') 

       btn_valider = tk.Button(self, text="Afficher les informations concernant l'encadrement zoottechnique des animaux", command=self.view_zootechnical_supervision)
       btn_valider.grid(row=self.numberLines + 6, column=0, columnspan=len(self.col_title), sticky='nsew')
  
    def ouvrir_controle_registre_elevage(self,width):
         # Ajout des titres de colonnes
         self.numberLines = width
         self.supprimer_widgets()  
         self.col_title = ["Date", "Organisme de controle ", "Motif de controle", "Nom du controleur ", "Cachet","Signature"]
         tex1 = Label(self, text='Encadrement Zootechnique Sanitaire et Médical des Animaux', fg='cyan')
         tex1.grid(row=14, column=0, columnspan=8)
         
         for j in range(6):
            col_title_tmp=self.col_title[j]  
            col_title_label = Label(self, text=col_title_tmp, width=5, relief="solid", bg="lightgray", anchor="w")
            col_title_label.grid(row=16, column=j, sticky='nsew')  # Utilise sticky pour que la colonne s'adapte

         # Ajout des données du tableau
         self.data = []
         for i in range(17, self.numberLines + 1):
            line = []
            for j in range(6):
                cell = Entry(self, width=5)  # Ajustez la largeur selon vos besoins
                cell.grid(row=i, column=j, sticky='nsew')  # Utilise sticky pour que la colonne s'adapte
                line.append(cell)
            self.data.append(line)

         # Configurer la gestion des colonnes pour qu'elles s'adaptent au contenu
         for j in range(self.numberColumns):
            self.grid_columnconfigure(j, weight=1)

         # Bouton pour ajouter une nouvelle ligne
         self.bouton_ajouter_ligne = Button(self, text="Ajouter une ligne", command=self.ajouter_ligne)
         self.bouton_ajouter_ligne.grid(row=self.numberLines + 4, columnspan=len(self.col_title), sticky='nsew')

         btn_valider = tk.Button(self, text="Afficher les informations concernant le controle de mon registre d'élévage", command=self.valider_carathersitiques_lieu)
         btn_valider.grid(row=self.numberLines + 5, column=0, columnspan=len(self.col_title), sticky='nsew')

         self.bouton_ajouter_ligne = Button(self, text="Valider les informations", command=lambda : self.valider_informations_controle())
         self.bouton_ajouter_ligne.grid(row=self.numberLines + 3, columnspan=len(self.col_title), sticky='nsew')
        
    def ouvrir_interventions(self,width):
         self.supprimer_widgets()  
         self.numberLines = width
         self.col_title = ["Date", "Type d'intervention", "Intervenant (si vétérianire)", "Traitement", "N ordonnance","Date de début", "Date de fin","N°d’ordonnance","Délai attente compétition(facultatif)","Délai attente abatage ou exclusion abattage"]
         tex1 = Label(self, text='Encadrement Zootechnique Sanitaire et Médical des Animaux', fg='cyan')
         tex1.grid(row=15, column=0, columnspan=8)

        # Ajout des titres de colonnes
         for j in range(10):
            col_title_item=self.col_title[j]
            col_title_label = Label(self, text=str(col_title_item), width=34, relief="solid", bg="lightgray", anchor="w",font=("Helvetica", 8))
            col_title_label.grid(row=16, column=j, sticky='nsew')

        # Ajout des données du tableau
            
         self.data = []
         for i in range(17, self.numberLines + 1):
           line = []
           for j in range(10):
             cell = Entry(self, width=34)
             cell.grid(row=i, column=j, sticky='nsew')
             line.append(cell)
             self.data.append(line)
                                                                                               
        # Configurer la gestion des colonnes pour qu'elles s'adaptent au contenu
         for j in range(self.numberColumns):
            self.grid_columnconfigure(j, weight=1)

        # Bouton pour ajouter une nouvelle ligne
         self.bouton_ajouter_ligne = Button(self, text="Ajouter une ligne", command=self.ajouter_ligne, width=20, height=1)
         self.bouton_ajouter_ligne.grid(row=self.numberLines + 1, columnspan=self.numberColumns, sticky='nsew')

         btn_mouvement_temporaire = Button(self, text="Valider", command=  self.valider_informations_intervention, width=20, height=1 )#self.signaler_mouvement_temporaire)
         btn_mouvement_temporaire.grid(row=self.numberLines + 3,  columnspan=self.numberColumns, sticky='nsew')

         btn_valider = Button(self, text="Consulter l'historitque de mes Soins", command=self.view_animals)
         btn_valider.grid(row=self.numberLines + 4,  columnspan=self.numberColumns, sticky='nsew')
         
       # Ajout du Canvas
       # self.can1 = Canvas(self, bg='blue', width=450, height=450)
       # self.can1.grid(row=self.numberLines + 5, column=0, columnspan=self.numberColumns, pady=5)

         try:
        # Charger l'image avec PIL
          image = Image.open("/Creation_dun_logiciel_de_Registre_delevage/images/cheval_blanc.png")
        # Augmenter la taille de l'image (dans cet exemple, je l'ai doublée)
          image = image.resize((960, 540), Image.BICUBIC)
        # Convertir l'image en format Tkinter PhotoImage
          self.image = ImageTk.PhotoImage(image)
        
        # Afficher l'image sur le canvas
          self.can1.create_image(0, 0, anchor=NW, image=self.image)
         except Exception:
            print("l'image ne marche pas ")      
    # def open_healthcare(self):
        
    #     col_titles = ["Nom", "n° SIRE", "n° Transpondeur", "Nom et coordonnées du propriétaires", "Date de première entrée", "Adresse de provenance","Date de sortie définitive","Adresse de destination"]  
    #     fenetre_principale = Soins_cournat(tk.Tk(), height=20, width=10, col_titles=col_titles)
    #     fenetre_principale.mainloop()
    def ouvrir_caractheristiques_animaux(self):
    
     self.supprimer_widgets()
     
      # Définition des titres des colonnes
     self.col_title = ["Nom","NeSIRE","Netranspondeur","Nom proprietaire","Date de premiere entree", "Adresse de provenance", "Date de sortie definitive", "Adresse de destination"]
    
     for j, col_tmp in enumerate(self.col_title):
      print("nombres " +str(self.numberColumns))
      col_tmp = self.col_title[j]
      col_title = tk.Label(self, text=col_tmp, width=28, relief="solid", bg="lightgray")#, anchor="w")
      col_title.grid(row=13,column=j,sticky='nsew')  # Utilise sticky pour que la colonne s'adapte

     # Ajout des données du tableau
     self.data = []
     for i in range( 15, 24):
        line = []
        for j in range(8):
            cell = Entry(self, width=28)
            cell.grid(row=i, column=j, sticky='nsew')
            line.append(cell)
        self.data.append(line) 
     # Boutons pour ajouter une ligne, valider et consulter les animaux
        
    # Configurer la gestion des colonnes pour qu'elles s'adaptent au contenu
     for j in range(self.numberColumns):
        self.grid_columnconfigure(j, weight=1)     
     self.bouton_ajouter_ligne = Button(self, text="Ajouter une ligne", command=self.ajouter_ligne)
     self.bouton_ajouter_ligne.grid(row=self.numberLines + 4, columnspan=len(self.col_title), sticky='nsew')
    
     btn_valider = Button(self, text="Valider", command= self.valider_caratheristiques_animaux)
     btn_valider.grid(row=self.numberLines + 5, columnspan=len(self.col_title), sticky='nsew')
    
     btn_consulter_animaux = Button(self, text="Consulter mes animaux", command=self.view_animals)
     btn_consulter_animaux.grid(row=self.numberLines + 6, columnspan=len(self.col_title), sticky='nsew')

     # Ajout des données du tableau
     self.data = []  
    def view_animals(self):
     with open('caratheristiques_animaux.json', 'r') as file:
        data = json.load(file)
    
    # Affichage des animaux dans les zones de texte
     for i, animal in enumerate(data['caratheristiques_animaux'], start=15):
        text_fields = []

        for j, key in enumerate(self.col_title):
            text_field = Entry(self, width=3) #,state='readonly')# , wrap=WORD)
            text_field.grid(row=i, column=j, sticky='nsew')
            # Récupérer la valeur de la clé si elle existe, sinon utiliser une chaîne vide
            value = animal.get(key, '')
            text_field.insert(END, f"{key}: {value}\n")
            text_fields.append(text_field)
        self.data.append(text_fields)
        
     self.bouton_ajouter_ligne = Button(self, text="Ajouter une ligne", command=self.ajouter_ligne)
     self.bouton_ajouter_ligne.grid(row=self.numberLines + 4, columnspan=len(self.col_title), sticky='nsew')
    
     btn_valider = Button(self, text="Modifier les informations", command=self.valider_caratheristiques_animaux)
     btn_valider.grid(row=self.numberLines + 5, columnspan=len(self.col_title), sticky='nsew')
    def view_zootechnical_supervision(self):
    
      with open('encadrement_zootechnique.json', 'r') as file:
        data = json.load(file)
    
        # Affichage des animaux dans les zones de texte
        for i, animal in enumerate(data['caratheristiques_animaux'], start=15):
         text_fields = []

         for j, key in enumerate(self.col_title):
            text_field = Entry(self, width=3) #,state='readonly')# , wrap=WORD)
            text_field.grid(row=i, column=j, sticky='nsew')
            # Récupérer la valeur de la clé si elle existe, sinon utiliser une chaîne vide
            value = animal.get(key, '')
            text_field.insert(END, f"{key}: {value}\n")
            text_fields.append(text_field)
        self.data.append(text_fields)
        
        self.bouton_ajouter_ligne = Button(self, text="Ajouter une ligne", command=self.ajouter_ligne)
        self.bouton_ajouter_ligne.grid(row=self.numberLines + 4, columnspan=len(self.col_title), sticky='nsew')
    
        btn_valider = Button(self, text="Modifier les informations", command=self.valider_encadrement_Zootechnique_animaux)
        btn_valider.grid(row=self.numberLines + 5, columnspan=len(self.col_title), sticky='nsew')
    def view_temporary_movements(self):
       self.supprimer_widgets()
     
      # Définition des titres des colonnes
       self.col_title = ["Nom","NeSIRE","Netranspondeur","Nom proprietaire","Date de premiere entree", "Adresse de provenance", "Date de sortie definitive", "Adresse de destination"]
    
       for j, col_tmp in enumerate(self.col_title):
        print("nombres " +str(self.numberColumns))
        col_tmp = self.col_title[j]
        col_title = tk.Label(self, text=col_tmp, width=28, relief="solid", bg="lightgray")#, anchor="w")
        col_title.grid(row=13,column=j,sticky='nsew')  # Utilise sticky pour que la colonne s'adapte

     # Ajout des données du tableau
        self.data = []
       for i in range( 15, 24):
        line = []
        for j in range(8):
            cell = Entry(self, width=28)
            cell.grid(row=i, column=j, sticky='nsew')
            line.append(cell)
        self.data.append(line) 
     # Boutons pour ajouter une ligne, valider et consulter les animaux
        
    # Configurer la gestion des colonnes pour qu'elles s'adaptent au contenu
       for j in range(self.numberColumns):
        self.grid_columnconfigure(j, weight=1)     
        self.bouton_ajouter_ligne = Button(self, text="Ajouter une ligne", command=self.ajouter_ligne)
        self.bouton_ajouter_ligne.grid(row=self.numberLines + 4, columnspan=len(self.col_title), sticky='nsew')
    
        btn_valider = Button(self, text="Valider", command= self.valider_caratheristiques_animaux)
        btn_valider.grid(row=self.numberLines + 5, columnspan=len(self.col_title), sticky='nsew')
    
        btn_consulter_animaux = Button(self, text="Consulter mes animaux", command=self.view_animals)
        btn_consulter_animaux.grid(row=self.numberLines + 6, columnspan=len(self.col_title), sticky='nsew')

        # Ajout des données du tableau
        self.data = []  
       


    # Ajuster la ligne en conséquence
    def ouvrir_mouvement_temporaires(self, width):
      
        self.supprimer_widgets()
        self.col_title = ["Date de sortie", "Nom de l'équidé", "Motif", "Etape éventuelle (adresse)", "Lieu de destination (Adresse)", "Date de retour"]
        self.numberLines = width
        self.numberColumns = width
        
        # Titre du tableau
        label_titre_tableau = tk.Label(self, text="MOUVEMENTS TEMPORAIRES DES ANIMAUX")
        label_titre_tableau.grid(row=9, column=0, columnspan=20, sticky='nsew')

        # Phrase à deux trous
        label_intro = tk.Label(self, text="Liste des mouvements temporaires entre le")
        label_intro.grid(row=11, column=11, sticky='nsew')

        self.entry_debut = tk.Entry(self, width=5)
        self.entry_debut.grid(row=11, column=1, sticky='nsew')

        label_et_le = tk.Label(self, text="et le")
        label_et_le.grid(row=11, column=2, sticky='nsew')

        self.entry_fin = tk.Entry(self, width=5)
        self.entry_fin.grid(row=11, column=3, sticky='nsew')

        # Phrase additionnelle
        label_option = tk.Label(self, text="(Option 1 : mouvements peu fréquents)")
        label_option.grid(row=12, column=0, columnspan=20, sticky='nsew')

        # Ajout des titres de colonnes
        for j in range(6):
            print("nombres " +str(self.numberColumns))
            col_tmp = self.col_title[j]
            col_title = tk.Label(self, text=col_tmp, width=15, relief="solid", bg="lightgray", anchor="w")
            col_title.grid(row=13, column=j, sticky='nsew')  # Utilise sticky pour que la colonne s'adapte

        # Ajout des données du tableau
        self.data = []
        for i in range(14, self.numberLines + 4):
            line = []
            for j in range(6):
                cell = tk.Entry(self, width=15)  # Ajustez la largeur selon vos besoins
                cell.grid(row=i, column=j, sticky='nsew')  # Utilise sticky pour que la colonne s'adapte
                line.append(cell)
            self.data.append(line)

        # Configurer la gestion des colonnes pour qu'elles s'adaptent au contenu
        for j in range(self.numberColumns):
            self.grid_columnconfigure(j, weight=1)

        # Bouton pour ajouter une nouvelle ligne
        self.bouton_ajouter_ligne = tk.Button(self, text="Ajouter une ligne", command=self.ajouter_ligne, width=15, height=1)
        self.bouton_ajouter_ligne.grid(row=self.numberLines + 4, columnspan=len(self.col_title), sticky='nsew')
        
        btn_mouvement_temporaire = tk.Button(self, text="Valider", command= self.valider_mouvements_temporaires, width=15, height=1)#self.signaler_mouvement_temporaire)
        btn_mouvement_temporaire.grid(row=self.numberLines + 5, columnspan=len(self.col_title), sticky='nsew')
        
        btn_mouvement_temporaire = tk.Button(self, text="Voir l'historique de mes mouvements", command= self.view_temporary_movements, width=15, height=1)#self.signaler_mouvement_temporaire)
        btn_mouvement_temporaire.grid(row=self.numberLines + 6, columnspan=len(self.col_title), sticky='nsew')
         
        # Création du Label pour afficher les images
        self.label_image = tk.Label(self, bd=0, highlightthickness=0)
        self.label_image.grid(row=self.numberLines + 9, column=0, columnspan=self.numberColumns, sticky='nsew')

        # Appel à la méthode pour gérer le fond d'image changeant
        self.setup_background_animation()

        # Gestionnaire d'événements pour détecter les changements de taille de fenêtre
        self.bind("<Configure>", self.redimensionner_image)
    def setup_background_animation(self):
      
     self.image_paths = glob.glob("/Creation_dun_logiciel_de_Registre_delevage/images/*.png")



     image_path = self.image_paths[self.current_image_index]
     image = Image.open(image_path)
     image = image.resize((self.winfo_width(), self.winfo_height()))
        
     

     photo = ImageTk.PhotoImage(image)
     self.label_image.configure(image=photo)
     self.label_image.image = photo


    #except Exception:
     # print(" ça marche pas ")  


     for child in self.label_image.winfo_children():
        child.lift()

    #valider
    def valider_mouvements_temporaires(self):
     caracteristiques_lieu_detention = []

    # Parcourir toutes les lignes de données
     for row_data in self.data:
        mouvements_temporaires = {
       
            "Date_sortie": self.data[0][0].get(),
            "Nom_equide": self.data[0][1].get(),
            "Motif": self.data[0][2].get(),
            "Etape_eventuelle": self.data[0][3].get(),
            "Lieu_destination": self.data[0][4].get(),
            "Date_retour": self.data[0][5].get(),



        }

    # Écriture des données dans un fichier JSON
     with open('mouvements_temporaires.json', 'w') as json_file:
        json.dump({"mouvements_temporaires": mouvements_temporaires}, json_file, indent=4)      
    def valider_carathersitiques_lieu(self):
     caracteristiques_lieu_detention = []

    # Parcourir toutes les lignes de données
     for row_data in self.data:
        detenteur_equides = {
            "Sire": row_data[0].get(),
            "Statut Juridique": row_data[1].get(),
            "Denomination": row_data[2].get()
        }

        coordonee_detenteur = {
            "Adresse": row_data[3].get(),
            "Tel": row_data[4].get(),
            "Portable": row_data[5].get(),
            "mail": row_data[6].get()
        }

        responsable_registre_elevage = {
            "prenom": row_data[7].get(),
            "nom_usage": row_data[8].get(),
            "Adresse": row_data[9].get(),
            "tel": row_data[10].get(),
            "Portable": row_data[11].get(),
            "mail": row_data[12].get()
        }

        caracteristiques_lieu_detention.append({
            "detenteur_equides": detenteur_equides,
            "coordonee_detenteur": coordonee_detenteur,
            "responsable_registre_elevage": responsable_registre_elevage
        })

    # Écriture des données dans un fichier JSON
     with open('caracteristiques_lieu_detention.json', 'w') as json_file:
        json.dump({"caracteristiques_lieu_detention": caracteristiques_lieu_detention}, json_file, indent=4)
    def valider_informations_controle(self):
        controle_data = []

        # Parcourir toutes les lignes de données
        for row_data in self.data:
            controle = {
                "Date": row_data[0].get(),
                "Organisme de controle": row_data[1].get(),
                "Motif de controle": row_data[2].get(),
                "Nom du controleur": row_data[3].get(),
                "Cachet": row_data[4].get(),
                "Signature": row_data[5].get()
            }
            controle_data.append(controle)

        # Écriture des données dans un fichier JSON
        with open('controles.json', 'w') as json_file:
            json.dump({"controle": controle_data}, json_file, indent=4)
    def valider_encadrement_Zootechnique_animaux(self):
        # Collecte des données depuis les champs d'entrée
     intervention_data = []

     for row_data in self.data:
         
       encadrement = {
        "Lieu Habituel et coordonee de detention": row_data[0].get(),
        "Nom et coordonées du veterianire traitant": row_data[1].get(),
        "Nom et coordonnées du veterinaire sanitaire": row_data[2].get(),
        "Nom et coordonnées du referent bien-etre animal(pour les structures équines professionnelles)": row_data[3].get(),
        "Nom, adresse et N° de telephone desOrganisme(s) à vocation sanitaire reconnu(s) et dessociétés mères (facultatif": row_data[4].get(),
        "Nom, adresse et N° de telephone du maréchalferrant (facultatif)": row_data[5].get(),  # ← Utilisez l'indice 5 ici
        "Nom, adresse et N° de telephone du dentiste(facultatif)": row_data[6].get()  # ← Cet indice est en dehors des limites de la liste
       }


       intervention_data.append(encadrement)

    # Écriture des données dans un fichier JSON
     with open('encadrement_zootechnique.json', 'w') as json_file:
      json.dump(intervention_data, json_file, indent=4)  
    def valider_informations_lieu(self):
    # Collecte des données depuis les champs d'entrée
     intervention_data = []

     for row_data in self.data:
        intervention = {
            "Date": row_data[0].get(),
            "Type_intervention": row_data[1].get(),
            "Intervenant": row_data[2].get(),
            "Traitement": {
                "Nom du medicament": row_data[3].get(),
                "Voie administration": "",  # Vous devez remplir cette information
                "Date de debut": row_data[5].get(),
                "Date de fin": row_data[6].get()
            },
            "N_ordonnance": row_data[4].get(),
            "Delai_attente_competition": row_data[8].get(),
            "Delai_attente_abattage": row_data[9].get()
        }
        intervention_data.append(intervention)

    # Écriture des données dans un fichier JSON
     with open('interventions.json', 'w') as json_file:
      json.dump(intervention_data, json_file, indent=4)
    def valider_informations_intervention(self):
        mouvements_temporaires = []
        for row in self.data:
            mouvement = {
        "Date": row[0].get(),
        "Type_intervention": row[1].get(),
        "Intervenant": row[2].get(),
        "Traitement": {
            "Nom du medicament": row[3].get(),
            "Voie administration": row[4].get(),
            "Date dedebut": row[5].get(),
            "Date dedefin": row[6].get(),
          },
        
      
        "N_ordonnance": row[7].get(),
        "Delai_attente_competition": row[8].get(),
        "Delai_attente_abattage": row[9].get()
               
            }   
            mouvements_temporaires.append(mouvement)

        with open('Soins_Courant.json', 'w') as f:
            json.dump(mouvements_temporaires, f, indent=4)           
    def valider_caratheristiques_animaux(self):
    # Initialiser une liste pour stocker les nouveaux caractéristiques
     nouveaux_caract = []

    # Récupérer les informations depuis les champs d'entrée
     for row in self.data:
        # Créer un dictionnaire avec les nouvelles caractéristiques
        nouveau_caract = {
            "Nom": row[0].get(),
            "NeSIRE": row[1].get(),
            "Netranspondeur": row[2].get(),
            "Nom et coordonnees du proprietaire": {
                "Nom proprietaire": row[3].get(),
                "Coordonnees": {
                    "Adresse": row[4].get(),
                    "Ville": "Ville_1",
                    "Code postal": "12345"
                }
            },
            "Date de premiere entree": row[5].get(),
            "Adresse de provenance": row[6].get(),
            "Date de sortie definitive": row[7].get(),  # Changer l'indice à 6
            "Adresse de destination": "zz",##row[8].get()
        }

        # Ajouter le nouveau caractère à la liste
        nouveaux_caract.append(nouveau_caract)

    # Charger les données existantes depuis le fichier JSON
     with open('caratheristiques_animaux.json', 'r') as json_file:
        data = json.load(json_file)
       
    # Ajouter les nouveaux caractéristiques à la liste existante
        data["caratheristiques_animaux"].extend(nouveaux_caract)

    # Réécrire le fichier JSON avec la nouvelle structure
     with open('caratheristiques_animaux.json', 'w') as json_file:
        json.dump(data, json_file, indent=2)


if __name__ == "__main__":
    col_titles = ["Date", "Organisme de contrôle", "Motif de contrôle", "Nom du contrôleur", "Cachet", "Signature"]

    fenetre_principale = FenetrePrincipale(width=20,col_titles=col_titles,height=19)
    fenetre_principale.mainloop()
