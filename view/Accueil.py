# Accueil.py  
# flag tag github pull
import sys
sys.path.insert(1, '/Creation_dun_logiciel_de_Registre_delevage/')
import tkinter as tk
import glob
import os
import os.path
import Methode1
import json
from tkinter import ttk
from tkinter import Button  
from PIL import Image, ImageTk
from Page_caracteristique_du_lieu_de_detention import FenetrePrincipaleCaracth
from Soins_CourantGUI import Soins_cournat
from Presence_et_Caratheristiques_animauxGUI import Presence_CaratherisisGUI
#from Page_controle_du_registre_delevage import FenetrePrincipaleControle
from CaractheristiquesDetention import CaratheristiquesDetention
from EncadrementZootechnique import EncadrementZootechnique
from CaratheristiquesAnimaux import CaractheristiquesAnimaux 
from Interventions import Interventions
from ControleRegistreElevage import controle
from Movements import Movements 
from tkinter import scrolledtext
from tkinter import *
from tkinter import messagebox, Frame, Entry, Button, Label, BOTH, ttk, Canvas

class FenetrePrincipale(tk.Tk):
##tag



    #  intervention_data = []

    #   for row_data in self.data:
         
    #    encadrement = {
    #     "Lieu Habituel et coordonee de detention": row_data[0].get(),
    #     "Nom et coordonees veterianire traitant": row_data[1].get(),
    #     "Nom et coordonnees du veterinaire sanitaire": row_data[2].get(),
    #     "Nom et coordonnees du referent bien-etre animal": row_data[3].get(),
    #     "Nom adresse tel des Organismes sanitaires reconnus": row_data[4].get(),
    #     "Nom, adresse tel marcechal ferrand": row_data[5].get(),  # ← Utilisez l'indice 5 ici
    #     "Nom, adresse et N de telephone du dentiste": row_data[6].get()  # ← Cet indice est en dehors des limites de la liste
    #    }
       
       
    #    intervention_data.append(encadrement)

    # # Écriture des données dans un fichier JSON
    #   with open('encadrement_zootechnique.json', 'w') as json_file:
    #    json.dump({"encadrement":intervention_data}, json_file, indent=4)     

## tag

  def __init__(self,width,col_titles,height):
     
        super().__init__()
        
        self.numberColumns = width 
        self.numberLines = height
        self.col_title = col_titles
        self.data = []  

        self.title("Accueil")
        self.geometry("1920x1080")

        try:
            self.iconbitmap("/Creation_dun_logiciel_de_Registre_delevage/images/horse_sans_fond.ico")
        except Exception:
            print("photo de cheval")

        self.navbar_canvas = tk.Canvas(self, bd=2, relief=tk.GROOVE)
        self.navbar_canvas.grid(row=10, columnspan=len(self.col_title), sticky="ew")
     
        self.scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=self.navbar_canvas.yview)
        self.scrollbar.grid(row=10, column=len(self.col_title) + 5, sticky="ns")        
        self.navbar_canvas.configure(yscrollcommand=self.scrollbar.set)
    
        self.navbar_frame = tk.Frame(self.navbar_canvas)
        self.navbar_canvas.create_window((0, 0), window=self.navbar_frame, anchor='nw')

        # Création d'un cadre intérieur pour les Entry widgets
        self.inner_frame = tk.Frame(self.navbar_frame)
        self.inner_frame.grid(row=0, column=0, sticky='nsew')

        self.create_navigation_panel()
        self.bind("<Configure>", self.redimensionner_canevas)

        # Création d'un cadre intérieur pour les Entry widgets
        self.inner_frame = tk.Frame(self.navbar_frame, width=250, height=250)
        self.inner_frame.grid(row=0, column=0, sticky='nsew')

        # Création des boutons de la barre de navigation # Caractéristiques Lieu de Détention
        btn_caracteristiques_lieu = tk.Button(self, text="Caractéristiques", command=lambda:self.ouvrir_caracteristiques_lieu_detention())
        btn_caracteristiques_lieu.grid(row=0, column=1 , sticky="ew")

        # Encadrement Zootechnique, Sanitaire et Medical des Animaux
        btn_mouvement_temporaire = tk.Button(self, text="Encadrement", command=lambda:self.open_encadrement_zootechnique(width))
        btn_mouvement_temporaire.grid(row=0, column=2, sticky="ew")

        # Présence et Caractéristiques des Animaux
        btn_mouvement_temporaire = tk.Button(self, text="Présence", command=lambda:self.ouvrir_caractheristiques_animaux(width,height))
        btn_mouvement_temporaire.grid(row=0, column=3, sticky="ew")
        
        btn_mouvement_temporaire_mvt = tk.Button(self, text="Mouvements Temporaire des Animaux", command=lambda: self.ouvrir_mouvement_temporaires(width,height))
        btn_mouvement_temporaire_mvt.grid(row=0, column=4, sticky="ew")
         
        btn_mouvement_temporaire = tk.Button(self, text="Intervents et Soins Courants", command=lambda:self.ouvrir_interventions(width,height))
        btn_mouvement_temporaire.grid(row=0, column=5, sticky="ew")

        btn_mouvement_temporaire = tk.Button(self, text="Contrôle du Registre d'élevage", command=lambda:self.ouvrir_controle_registre_elevage(width,height))
        btn_mouvement_temporaire.grid(row=0, column=6, sticky="ew")

        # Création du Label pour afficher les images
        self.label_image = tk.Label(self, bd=0, highlightthickness=0)
        self.label_image.grid(row=0, column=7, sticky="ew")

        # Texte additionnel
        texte_instruction = "Pour générer le document PDF qui va regrouper toutes les informations que vous avez entré dans les différentes parties de l'application."
        #  etiquette_instruction.grid(row=2, column=0, columnspan=self.numberColumns, sticky="nsew")
        etiquette_instruction = tk.Label(self, text=texte_instruction, font=("Helvetica", 12))
        etiquette_instruction.grid(row=19, column=0, columnspan=self.numberColumns, sticky="nsew")


        # Texte additionnel2
        texte_instruction2 = "Veuillez cliquer sur le bouton suivant :"
        etiquette_instruction2 = tk.Label(self, text=texte_instruction2, font=("Helvetica", 12))
        etiquette_instruction2.grid(row=20, column=0, columnspan=self.numberColumns, sticky="nsew")

        # Bouton pour générer le document PDF
      #  btn_generer_pdf = tk.Button(self, text="Générer le document PDF", command=self.generer_document_pdf, font=("Helvetica", 14, "bold"))
        btn_generer_pdf = tk.Button(self, text="Générer le document PDF", command=self.generer_document_pdf, font=("Helvetica", 16, "bold"))
        btn_generer_pdf.place(relx=0.375, rely=0.55, anchor="center")
     
        try:
         self.setup_background_animation()
        except Exception:     
          print(" Marche pas photo de fond ")

        self.create_navigation_panel()
        self.bind("<Configure>", self.redimensionner_canevas)

  def create_navigation_panel(self):
       
       self.col_title = ["Nom", "NeSIRE", "Netranspondeur", "Nom proprietaire", "Adresse proprietaire", "Date de premiere entree", "Adresse de provenance", "Date de sortie definitive", "Adresse de destination"]

       # Ajouter tous les titres de colonne à self.inner_frame
       for j in range(6):#len(self.col_title)):
        col_tmp = self.col_title[j]
        col_title = tk.Label(self.inner_frame, text=col_tmp, width=20, relief="solid", bg="lightgray", anchor="w")
        col_title.grid(row=0, column=j, sticky='nsew')

       # Ajouter des lignes de données vides (20 dans votre cas)
       for i in range(20):
        for j in range(len(self.col_title)):
            cell = tk.Entry(self.inner_frame, width=22)
            cell.grid(row=i+1, column=j, sticky='nsew')

       # Configurer la croissance des colonnes
       for j in range(len(self.col_title)):
        self.inner_frame.grid_columnconfigure(j, weight=1)

       # Mettre à jour la taille du cadre intérieur pour que la scrollbar fonctionne correctement
       self.inner_frame.update_idletasks()
       self.navbar_canvas.configure(scrollregion=self.navbar_canvas.bbox("all"))  

  def ouvrir_caracteristiques_lieu_detention(self):
  
      self.navbar_frame = tk.Frame(self.navbar_canvas)
      self.navbar_canvas.create_window((0, 0), window=self.navbar_frame, anchor='nw')
      self.col_title = ["Date", "Organisme de controle", "Motif de controle", "Nom du controleur", "Cachet", "Signature"]

    # Ajouter tous les titres de colonne
      for j in range( len(self.col_title)):
        col_tmp = self.col_title[j]
        col_title = tk.Label(self.inner_frame, text=col_tmp, width=10, relief="solid", bg="lightgray", anchor="w")
        col_title.grid(row=0, column=j, sticky='nsew')

    # Ajouter les lignes de données (20 dans votre cas)
      for i in range(20):
       for j in range(len(self.col_title)):
            cell = tk.Entry(self.inner_frame, width=20)
            cell.grid(row=i+1, column=j, sticky='nsew')

    # Configurer la croissance des colonnes
      for j in range(len(self.col_title)):
        self.inner_frame.grid_columnconfigure(j, weight=1)

    # Mettre à jour la taille du cadre intérieur pour que la scrollbar fonctionne correctement
      self.inner_frame.update_idletasks()
      self.navbar_canvas.configure(scrollregion=self.navbar_canvas.bbox("all"))
          # Redimensionner le canevas lorsque la taille de la fenêtre change
      self.bind("<Configure>", self.redimensionner_canevas) 
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
        
         btn_mouvement_temporaire = Button(self, text="Voir l'histoire de mes mouvements", command= lambda: Movements.view_temporary_movements , width=15, height=1)#self.signaler_mouvement_temporaire)
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

  def afficher_elements_canevas(self):
        # Création du cadre à l'intérieur du canevas
        self.navbar_frame = tk.Frame(self.navbar_canvas)
        self.navbar_canvas.create_window((0, 0), window=self.navbar_frame, anchor='nw')
                
        # Ajout de l'espace entre le menu de navigation et "Sire"
        for j in range(len(self.col_title)):
            col_tmp = self.col_title[j]
            col_title = tk.Label(self.navbar_frame, text=col_tmp, width=15, relief="solid", bg="lightgray", anchor="w")
            col_title.grid(row=13, column=j, sticky='nsew')  # Utilise sticky pour que la colonne s'adapte
        
        # Création des champs d'entrée
        for i in range(20):
            row_data = []
            for j in range(len(self.col_title)):
                cell = tk.Entry(self.navbar_frame, width=22)
                cell.grid(row=i+14, column=j, sticky='nsew')  # Commencer à la ligne 12
                row_data.append(cell)
            self.data.append(row_data)

        # Configurer la gestion des colonnes pour qu'elles s'adaptent au contenu
        for j in range(len(self.col_title)):
            self.navbar_frame.grid_columnconfigure(j, weight=1) 
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
     
  #       with open('lieu_detention.json', 'r') as file:
  #           data = json.load(file)

  #       for i, animal in enumerate( data['encadrement']  ):#, start=15):
  #      

     with open('caracteristiques_animaux.json', 'r') as file:
        data = json.load(file)

        # Parcourir les données
        for i, element in enumerate(data['caracteristiques'], start=1):
            text_fields = []

            # Parcourir les clés des sous-dictionnaires
            for key in element:
                # Récupérer la valeur correspondante à la clé
                value = element[key]

                # Trouver l'index de la colonne correspondant à la clé
                col_index = self.col_title.index(key)

                # Vérifier si l'indice i est valide pour self.data
                if i < len(self.data):
                    # Insérer la valeur dans le champ d'entrée correspondant
                    entry = self.data[i - 1][col_index]
                    entry.delete(0, 'end')  # Supprimer le contenu précédent
                    entry.insert(0, value)  # Insérer la nouvelle valeur
                else:
                    print(f"Erreur: L'indice {i} dépasse la taille de self.data.")

     # Ajouter les boutons en dehors de la boucle pour éviter la duplication
     self.bouton_ajouter_ligne = Button(self, text="Ajouter une ligne", command=self.ajouter_ligne)
     self.bouton_ajouter_ligne.grid(row=self.numberLines + 4, columnspan=len(self.col_title), sticky='nsew')

     btn_valider = Button(self, text="Modifier les informations", command=lambda: self.valider_informations_controle())
     btn_valider.grid(row=self.numberLines + 5, columnspan=len(self.col_title), sticky='nsew')       
     
     # Redimensionner le canevas lorsque la taille de la fenêtre change
     self.bind("<Configure>", self.redimensionner_canevas)
  def generer_document_pdf(self):
        # Ajoutez ici la logique pour générer le document PDF avec les informations de l'application
        pass
    
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
  def create_text(self):
       for i in range(10, 15):
           line = []
           for j in range(self.numberColumns):
             cell = Entry(self, width=20)
             cell.grid(row=i, column=j, sticky='nsew')
             line.append(cell)
             self.data.append(line) #je veux que lorsque l'on appuie sur le bouton valider les informations entrées dans les champ de texte soient mises dans le fichier json suivant
       return self.data   
     
  def supprimer_widgets( self): #  self,width,col_titles,height):
    # Liste des widgets à ne pas supprimer
      widgets_a_garder = [self.navbar_canvas, self.scrollbar, self.navbar_frame]

      for widget in self.winfo_children():
        # Vérifie si le widget a été créé dans __init__ et n'appartient pas au menu de navigation
        if isinstance(widget, tk.Entry) and widget  not in widgets_a_garder : # and widget not in self.__init__( ): ##width, col_titles, height  ):
            # Destruction du widget s'il n'a pas été créé dans __init__  
            widget.destroy()
            print(" destruction de "+str(widget))
        
        if isinstance(widget, tk.Label) and widget not in widgets_a_garder : # and widget not in self.__init__( ): #width, col_titles, height  ): 
            # Destruction du widget s'il n'a pas été créé dans __init__
            widget.destroy()
            print(" destruction de "+str(widget))
        
        if isinstance(widget, tk.Button) and widget not in widgets_a_garder  : #  and widget not in self.__init__( ): # width, col_titles, height ):
            # Destruction du widget s'il n'a pas été créé dans __init__
            widget.destroy()
            print(" destruction de "+str(widget)) 
  def ajouter_ligne(self):
         # Ajouter une nouvelle ligne
      # Création du cadre à l'intérieur du canevas
      self.navbar_frame = tk.Frame(self.navbar_canvas)
      self.navbar_canvas.create_window((0, 0), window=self.navbar_frame, anchor='nw')
      self.col_title =  ["Nom","NeSIRE","Netranspondeur","Nom proprietaire","Adresse proprietaire","Date de premiere entree", "Adresse de provenance", "Date de sortie definitive", "Adresse de destination"] 
          
    # Ajout de l'espace entre le menu de navigation et "Sire"
      for j in range(9):#len(self.col_title)):
        col_tmp = self.col_title[j]
        col_title = tk.Label(self.navbar_frame, text=col_tmp, width=15, relief="solid", bg="lightgray", anchor="w")
        col_title.grid(row=10, column=j, sticky='nsew')  # Utilise sticky pour que la colonne s'adapte
    
    # Création des champs d'entrée
      for i in range(20):
        row_data = []
        for j in range(len(self.col_title)):
            cell = tk.Entry(self.navbar_frame, width=22)
            cell.grid(row=i+14, column=j, sticky='nsew')  # Commencer à la ligne 12
            row_data.append(cell)
        self.data.append(row_data)

    # Configurer la gestion des colonnes pour qu'elles s'adaptent au contenu
      for j in range(len(self.col_title)):
        self.navbar_frame.grid_columnconfigure(j, weight=1) 

    # Redimensionner le canevas lorsque la taille de la fenêtre change
      self.bind("<Configure>", self.redimensionner_canevas)

    # Bouton de validation
      self.navbar_frame.bouton_ajouter_ligne = Button(self, text="Ajouter une ligne", command=self.ajouter_ligne)
      self.navbar_frame.bouton_ajouter_ligne.grid(row=self.numberLines + 4, column=0, columnspan=len(self.col_title), sticky='nsew')
     
      btn_valider = tk.Button(self, text="Valider", command=self.valider_encadrement_Zootechnique_animaux)
      btn_valider.grid(row=self.numberLines + 5, column=0, columnspan=len(self.col_title), sticky='nsew')

      btn_valider = tk.Button(self, text="Afficher mes lieux de détention", command=lambda:self.view_animals())
      btn_valider.grid(row=self.numberLines + 6, column=0, columnspan=len(self.col_title), sticky='nsew')       
   #ok
  def ouvrir_mouvement_temporaires(self, width,height):
    
    # Création du cadre à l'intérieur du canevas
      self.navbar_frame = tk.Frame(self.navbar_canvas)
      self.navbar_canvas.create_window((0, 0), window=self.navbar_frame, anchor='nw')
      self.col_title = ["Date_de_sortie", "Nom_equide", "Motif", "Etape_eventuelle", "Lieu_destination", "Date_retour"]  #["Date de sortie", "Nom equide", "Motif", "Etape eventuelle", "Lieu de destination (Adresse)", "Date de retour"]
    # Ajout de l'espace entre le menu de navigation et "Sire"
      for j in range(len(self.col_title)):#len(self.col_title)):
        col_tmp = self.col_title[j]
        col_title = tk.Label(self.navbar_frame, text=col_tmp, width=15, relief="solid", bg="lightgray", anchor="w")
        col_title.grid(row=10, column=j, sticky='nsew')  # Utilise sticky pour que la colonne s'adapte
    
    # Création des champs d'entrée
      for i in range(20):
        row_data = []
        for j in range(len(self.col_title)):
            cell = tk.Entry(self.navbar_frame, width=22)
            cell.grid(row=i+14, column=j, sticky='nsew')  # Commencer à la ligne 12
            row_data.append(cell)
        self.data.append(row_data)

    # Configurer la gestion des colonnes pour qu'elles s'adaptent au contenu
      for j in range(len(self.col_title)):
        self.navbar_frame.grid_columnconfigure(j, weight=1) 

    # Redimensionner le canevas lorsque la taille de la fenêtre change
      self.bind("<Configure>", self.redimensionner_canevas)

    # Bouton de validation
      self.navbar_frame.bouton_ajouter_ligne = Button(self, text="Ajouter une ligne", command=self.ajouter_ligne)
      self.navbar_frame.bouton_ajouter_ligne.grid(row=self.numberLines + 4, column=0, columnspan=len(self.col_title), sticky='nsew')
     
      btn_valider = tk.Button(self, text="Valider", command=self.valider_encadrement_Zootechnique_animaux)
      btn_valider.grid(row=self.numberLines + 5, column=0, columnspan=len(self.col_title), sticky='nsew')

      btn_valider = tk.Button(self, text="Afficher mouvements temporaires ", command=lambda: Movements.view_temporary_movements(self))
      btn_valider.grid(row=self.numberLines + 6, column=0, columnspan=len(self.col_title), sticky='nsew')    
  def open_encadrement_zootechnique(self,width):
   
   # Création du cadre à l'intérieur du canevas
      self.navbar_frame = tk.Frame(self.navbar_canvas)
      self.navbar_canvas.create_window((0, 0), window=self.navbar_frame, anchor='nw')
      self.col_title =  ["Lieu Habituel et coordonee de detention", "Nom et coordonees veterianire traitant", "Nom et coordonnees du veterinaire sanitaire" ,"Nom et coordonnees du referent bien-etre animal", "Nom adresse tel des Organismes sanitaires reconnus", "Nom, adresse tel marcechal ferrand","Nom, adresse et N de telephone du dentiste"] #Nom, adresse et N° de téléphone du dentiste(facultatif)
         
    # Ajout de l'espace entre le menu de navigation et "Sire"
      for j in range(len(self.col_title)):
        col_tmp = self.col_title[j]
        col_title = tk.Label(self.navbar_frame, text=col_tmp, width=15, relief="solid", bg="lightgray", anchor="w")
        col_title.grid(row=10, column=j, sticky='nsew')  # Utilise sticky pour que la colonne s'adapte
    
    # Création des champs d'entrée
      for i in range(20):
        row_data = []
        for j in range(len(self.col_title)):
            cell = tk.Entry(self.navbar_frame, width=22)
            cell.grid(row=i+14, column=j, sticky='nsew')  # Commencer à la ligne 12
            row_data.append(cell)
        self.data.append(row_data)

    # Configurer la gestion des colonnes pour qu'elles s'adaptent au contenu
      for j in range(len(self.col_title)):
        self.navbar_frame.grid_columnconfigure(j, weight=1) 

    # Bouton de validation
      self.navbar_frame.bouton_ajouter_ligne = Button(self, text="Ajouter une ligne", command=self.ajouter_ligne)
      self.navbar_frame.bouton_ajouter_ligne.grid(row=self.numberLines + 4, column=0, columnspan=len(self.col_title), sticky='nsew')
     
      btn_valider = tk.Button(self, text="Valider", command=self.valider_encadrement_Zootechnique_animaux)
      btn_valider.grid(row=self.numberLines + 5, column=0, columnspan=len(self.col_title), sticky='nsew')

      btn_valider = tk.Button(self, text="encadrement zootechnique", command=lambda:EncadrementZootechnique.view_zootechnical_supervision(self))
      btn_valider.grid(row=self.numberLines + 6, column=0, columnspan=len(self.col_title), sticky='nsew')  
   # Redimensionner le canevas lorsque la taille de la fenêtre change
      self.bind("<Configure>", self.redimensionner_canevas)
  def redimensionner_canevas(self, event):
      self.navbar_canvas.configure(scrollregion=self.navbar_canvas.bbox("all")) 
  def ouvrir_controle_registre_elevage(self, width,height):
      # Création du cadre à l'intérieur du canevas
      #  self.supprimer_widgets( ) #  width,self.col_title,height)
      self.navbar_frame = tk.Frame(self.navbar_canvas)
      self.navbar_canvas.create_window((0, 0), window=self.navbar_frame, anchor='nw')
      self.col_title = ["Date", "Organisme de controle", "Motif de controle", "Nom du controleur", "Cachet","Signature"]

      # Ajout de l'espace entre le menu de navigation et "Sire"
      for j in range(len(self.col_title)):
        col_tmp = self.col_title[j]
        col_title = tk.Label(self.navbar_frame, text=col_tmp, width=15, relief="solid", bg="lightgray", anchor="w")
        col_title.grid(row=13, column=j, sticky='nsew')  # Utilise sticky pour que la colonne s'adapte
    
      # Création des champs d'entrée
      for i in range(20):
        row_data = []
        for j in range(len(self.col_title)):
            cell = tk.Entry(self.navbar_frame, width=22)
            cell.grid(row=i+14, column=j, sticky='nsew')  # Commencer à la ligne 12
            row_data.append(cell)
        self.data.append(row_data)

    # Configurer la gestion des colonnes pour qu'elles s'adaptent au contenu
      for j in range(len(self.col_title)):
        self.navbar_frame.grid_columnconfigure(j, weight=1) 

    # Bouton pour ajouter une nouvelle ligne
      self.bouton_ajouter_ligne = Button(self, text="Ajouter une ligne", command=self.ajouter_ligne)
      self.bouton_ajouter_ligne.grid(row=self.numberLines + 4, columnspan=len(self.col_title), sticky='nsew')

      btn_valider = tk.Button(self, text="Afficher les informations concernant le controle de mon registre d'élévage", command=lambda:controle.view_control(self))
      btn_valider.grid(row=self.numberLines + 5, column=0, columnspan=len(self.col_title), sticky='nsew')

      self.bouton_ajouter_ligne = Button(self, text="Valider les informations", command=lambda : self.valider_informations_controle)
      self.bouton_ajouter_ligne.grid(row=self.numberLines + 3, columnspan=len(self.col_title), sticky='nsew')                                                                 
    # Redimensionner le canevas lorsque la taille de la fenêtre change
      self.bind("<Configure>", self.redimensionner_canevas)
  #checked
  def ouvrir_interventions(self,width,height):
    # Création du cadre à l'intérieur du canevas
      self.navbar_frame = tk.Frame(self.navbar_canvas)
      self.navbar_canvas.create_window((0, 0), window=self.navbar_frame, anchor='nw')
      self.col_title = ["Date", "Type intervention", "Intervenant", "Traitement", "N ordonnance","Date de debut","Date de fin","Delai attente competition","Delai attente abattage"]  # ["Lieu Habituel et coordonee de detention", "Nom et coordonees veterianire traitant", "Nom et coordonnees du veterinaire sanitaire" ,"Nom et coordonnees du referent bien-etre animal", "Nom adresse tel des Organismes sanitaires reconnus", "Nom, adresse tel marcechal ferrand","Nom, adresse et N de telephone du dentiste"] #Nom, adresse et N° de téléphone du dentiste(facultatif)   # ["Date_de_sortie", "Nom_equide", "Motif", "Etape_eventuelle", "Lieu_destination", "Date_retour"]  #["Date de sortie", "Nom equide", "Motif", "Etape eventuelle", "Lieu de destination (Adresse)", "Date de retour"]
    # Ajout de l'espace entre le menu de navigation et "Sire"
      for j in range(len(self.col_title)):#len(self.col_title)):
        col_tmp = self.col_title[j]
        col_title = tk.Label(self.navbar_frame, text=col_tmp, width=15, relief="solid", bg="lightgray", anchor="w")
        col_title.grid(row=10, column=j, sticky='nsew')  # Utilise sticky pour que la colonne s'adapte
    
    # Création des champs d'entrée
      for i in range(20):
        row_data = []
        for j in range(len(self.col_title)):
            cell = tk.Entry(self.navbar_frame, width=22)
            cell.grid(row=i+14, column=j, sticky='nsew')  # Commencer à la ligne 12
            row_data.append(cell)
        self.data.append(row_data)

    # Configurer la gestion des colonnes pour qu'elles s'adaptent au contenu
      for j in range(len(self.col_title)):
        self.navbar_frame.grid_columnconfigure(j, weight=1) 

    # Bouton de validation
      self.navbar_frame.bouton_ajouter_ligne = Button(self, text="Ajouter une ligne", command=self.ajouter_ligne)
      self.navbar_frame.bouton_ajouter_ligne.grid(row=self.numberLines + 4, column=0, columnspan=len(self.col_title), sticky='nsew')
     
      btn_valider = tk.Button(self, text="Valider", command=self.valider_encadrement_Zootechnique_animaux)
      btn_valider.grid(row=self.numberLines + 5, column=0, columnspan=len(self.col_title), sticky='nsew')

      btn_valider = tk.Button(self, text="Afficher interventions", command=lambda: Interventions.view_informations_intervention(self))
      btn_valider.grid(row=self.numberLines + 6, column=0, columnspan=len(self.col_title), sticky='nsew')   

          # Redimensionner le canevas lorsque la taille de la fenêtre change
      self.bind("<Configure>", self.redimensionner_canevas)
  #ok 
  def ouvrir_caractheristiques_animaux(self,width,height):
    
    # Création du cadre à l'intérieur du canevas
      self.navbar_frame = tk.Frame(self.navbar_canvas)
      self.navbar_canvas.create_window((0, 0), window=self.navbar_frame, anchor='nw')
      self.col_title =  ["Nom","NeSIRE","Netranspondeur","Nom proprietaire","Adresse proprietaire","Date de premiere entree", "Adresse de provenance", "Date de sortie definitive", "Adresse de destination"] 
          
    # Ajout de l'espace entre le menu de navigation et "Sire"
      for j in range(9):#len(self.col_title)):
        col_tmp = self.col_title[j]
        col_title = tk.Label(self.navbar_frame, text=col_tmp, width=15, relief="solid", bg="lightgray", anchor="w")
        col_title.grid(row=10, column=j, sticky='nsew')  # Utilise sticky pour que la colonne s'adapte
    
    # Création des champs d'entrée
      for i in range(20):
        row_data = []
        for j in range(len(self.col_title)):
            cell = tk.Entry(self.navbar_frame, width=22)
            cell.grid(row=i+14, column=j, sticky='nsew')  # Commencer à la ligne 12
            row_data.append(cell)
        self.data.append(row_data)

    # Configurer la gestion des colonnes pour qu'elles s'adaptent au contenu
      for j in range(len(self.col_title)):
        self.navbar_frame.grid_columnconfigure(j, weight=1) 

    # Redimensionner le canevas lorsque la taille de la fenêtre change
      self.bind("<Configure>", self.redimensionner_canevas)

    # Bouton de validation
      self.navbar_frame.bouton_ajouter_ligne = Button(self, text="Ajouter une ligne", command=self.ajouter_ligne)
      self.navbar_frame.bouton_ajouter_ligne.grid(row=self.numberLines + 4, column=0, columnspan=len(self.col_title), sticky='nsew')
     
      btn_valider = tk.Button(self, text="Valider", command=self.valider_encadrement_Zootechnique_animaux)
      btn_valider.grid(row=self.numberLines + 5, column=0, columnspan=len(self.col_title), sticky='nsew')

      btn_valider = tk.Button(self, text="Afficher mes lieux de détention", command=lambda:self.view_animals())
      btn_valider.grid(row=self.numberLines + 6, column=0, columnspan=len(self.col_title), sticky='nsew')   

 # Redimensionner le canevas lorsque la taille de la fenêtre change
      self.bind("<Configure>", self.redimensionner_canevas)
  # fontions de validations
  def valider_mouvements_temporaires(self):
      
      mouvements = []
     # Parcourir toutes les lignes de données
      for row_data in self.data:
        mouvements_temporaires = {
            "Date de sortie": row_data[0].get(),
            "Nom equide": row_data[1].get(),
            "Motif": row_data[2].get(),
            "Etape eventuelle": row_data[3].get(),
            "Lieu de destination (Adresse)": row_data[4].get(),
            "Date de retour": row_data[5].get(),
        }

        mouvements.append(mouvements_temporaires)  # Ajouter chaque mouvement à la liste

    # Écriture des données dans un fichier JSON
      with open('mouvements_temporaires.json', 'w') as json_file:
         json.dump({"mouvements_temporaires": mouvements}, json_file, indent=4)           
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
        "Nom et coordonees veterianire traitant": row_data[1].get(),
        "Nom et coordonnees du veterinaire sanitaire": row_data[2].get(),
        "Nom et coordonnees du referent bien-etre animal": row_data[3].get(),
        "Nom adresse tel des Organismes sanitaires reconnus": row_data[4].get(),
        "Nom, adresse tel marcechal ferrand": row_data[5].get(),  # ← Utilisez l'indice 5 ici
        "Nom, adresse et N de telephone du dentiste": row_data[6].get()  # ← Cet indice est en dehors des limites de la liste
       }
       
       
       intervention_data.append(encadrement)

    # Écriture des données dans un fichier JSON
      with open('encadrement_zootechnique.json', 'w') as json_file:
       json.dump({"encadrement":intervention_data}, json_file, indent=4)     
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
      interventions = []  # Initialiser la liste des interventions
    
      for row in self.data:
        # Créer un dictionnaire pour chaque intervention
        intervention = {
            "Date": row[0].get(),
            "Type intervention": row[1].get(),
            "Intervenant": row[2].get(),
            "Traitement": {
                "Nom du medicament": row[3].get(),
                "Voie administration": row[4].get(),
                "Date dedebut": row[5].get(),
                "Date dedefin": row[6].get(),
            },
            "N ordonnance": row[7].get(),
            "Delai attente competition": row[8].get(),
            "Delai attente abattage": row[9].get()
        }

        interventions.append(intervention)  # Ajouter l'intervention à la liste
    
    # Écrire le fichier JSON avec la liste des interventions
      with open('Soins_Courant.json', 'w') as f:
         json.dump({"interventions": interventions}, f, indent=4)            
  def valider_caratheristiques_animaux(self):
    # Initialiser une liste pour stocker les nouveaux caractéristiques
      nouveaux_caract = []

    # Récupérer les informations depuis les champs d'entrée
      for row in self.data:
        # Créer un dictionnaire avec les nouvelles caractéristiques
        caratheristiques_animaux = {
            "Nom": row[0].get(),
            "NeSIRE": row[1].get(),
            "Netranspondeur": row[2].get(),
            "Nom et coordonnees du proprietaire": {
                "Nom proprietaire": row[3].get(),
                "Coordonnees": {
                    "Adresse proprietaire": row[4].get(),
                    "Ville": "Ville_1",
                    "Code postal": "12345"
                }
            },
            "Date de premiere entree": row[5].get(),
            "Adresse de provenance": row[6].get(),
            "Date de sortie definitive": row[7].get(),  # Changer l'indice à 6
            "Adresse de destination":  row[8].get()
        }

        # Ajouter le nouveau caractère à la liste
        nouveaux_caract.append(caratheristiques_animaux)
            
    # Réécrire le fichier JSON avec la nouvelle structure
      with open('caratheristiques_animaux.json', 'w') as json_file:
         json.dump({"caractheristiques":nouveaux_caract}, json_file, indent=4) 



if __name__ == "__main__":
    app = FenetrePrincipale(width=1920, col_titles=["Colonne 1", "Colonne 2","c","c","c","colonne","c","c"], height=1080)
    app.mainloop() 

