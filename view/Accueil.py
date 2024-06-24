 # L 
import io
import sys
sys.path.insert(1, '/Creation_dun_logiciel_de_Registre_delevage/')
import tkinter as tk
import glob
import os
import os.path           
import Methode1
import json      
import PyPDF2
import pypdf
import tableprint
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import numpy as np
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas 
from tkinter import ttk
from tkinter import Button   
from io import StringIO
from PIL import Image, ImageTk
from Page_caracteristique_du_lieu_de_detention import FenetrePrincipaleCaracth
from Soins_CourantGUI import Soins_cournat
from Presence_et_Caratheristiques_animauxGUI import Presence_CaratherisisGUI
from CaractheristiquesDetention import CaratheristiquesDetention
from EncadrementZootechnique import EncadrementZootechnique
from CaratheristiquesAnimaux import CaractheristiquesAnimaux 
from Interventions import Interventions
from ControleRegistreElevage import controle
from Movements import Movements 
from tkinter import scrolledtext
from tkinter import *
from tkinter import messagebox, Frame, Entry, Button, Label, BOTH, ttk, Canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from pypdf import PdfReader, PdfWriter, PageObject
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib import colors
from reportlab.platypus import Table
from reportlab.lib.styles import getSampleStyleSheet
import subprocess

class FenetrePrincipale(tk.Tk):

  def __init__(self,width,col_titles,height):
     
        super().__init__()

        self.root = tk.Tk
        self.numberColumns = width 
        self.numberLines = height
        self.col_title = col_titles
        self.data = []  
              
        self.title("Accueil")
        self.geometry("1920x1080")

        try:
         self.iconbitmap("/Creation_dun_logiciel_de_Registre_delevage/images/horse_sans_fond.ico")
        except Exception:
           print("erreur")    
        self.navbar_canvas = tk.Canvas(self, bd=2, relief=tk.GROOVE  , width=1200, height=400) #, width=1600, height=800)
        #self.navbar_canvas = tk.Canvas(self.root)
        self.navbar_canvas.grid(row=10, columnspan=len(self.col_title), sticky="ew")
     
        self.scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=self.navbar_canvas.yview)      
        self.scrollbar.grid(row=10, column=len(self.col_title) + 5, sticky="ns")        
 
        self.navbar_canvas.config(yscrollcommand=self.scrollbar.set)
        self.navbar_frame = tk.Frame(self.navbar_canvas, width=1600, height=600)
        self.navbar_canvas.create_window((0, 0), window=self.navbar_frame, anchor='nw')

        # Création d'un cadre intérieur pour les Entry widgets
        self.inner_frame = Frame(self.navbar_frame)

        self.btn_caractheristiques_animaux = tk.Button(self, text="Présence", command=lambda:self.ouvrir_caractheristiques_animaux())
        self.btn_caractheristiques_animaux.grid(row=0, column=2, sticky="ew")

        self.btn_mouvement_temporaire = tk.Button(self, text="Mouvements Temporaire des Animaux", command=lambda: self.ouvrir_mouvement_temporaires())
        self.btn_mouvement_temporaire.grid(row=0, column=3, sticky="ew")

        self.btn_intervention_soins = tk.Button(self, text="Interventions et Soins Courants", command=lambda:self.ouvrir_interventions())
        self.btn_intervention_soins.grid(row=0, column=4, sticky="ew")

        self.btn_controle_registre = tk.Button(self, text="Contrôle du Registre d'élevage", command=lambda:self.ouvrir_controle_registre_elevage())
        self.btn_controle_registre.grid(row=0, column=5, sticky="ew")

        self.btn_deconnexion = tk.Button(self, text="Déconnexion", command=self.deconnexion)
        self.btn_deconnexion.grid(row=0, column=6, sticky="ew")
    
        # Création du Label pour afficher les images
        self.label_image = tk.Label(self, bd=0, highlightthickness=0)
        self.label_image.grid(row=0, column=7, sticky="ew")

        # Texte additionnel 3
        self.texte_instruction3 = "Vous etes actuellement sur la page principale "
        self.etiquette_instruction3 = tk.Label(self, text=self.texte_instruction3, font=("Helvetica", 12))
        self.etiquette_instruction3.grid(row=50, column=0, columnspan=self.numberColumns, sticky="nsew")

        # Texte additionnel
        self.texte_instruction = "Pour générer le document PDF qui va regrouper toutes les informations que vous avez entré dans les différentes parties de l'application."
        #  etiquette_instruction.grid(row=2, column=0, columnspan=self.numberColumns, sticky="nsew")
        self.etiquette_instruction = tk.Label(self, text=self.texte_instruction, font=("Helvetica", 12))
        self.etiquette_instruction.grid(row=51, column=0, columnspan=self.numberColumns, sticky="nsew")

        # Texte additionnel2
        self.texte_instruction2 = "Veuillez cliquer sur le bouton suivant :"
        self.etiquette_instruction2 = tk.Label(self, text=self.texte_instruction2, font=("Helvetica", 12))    
        self.etiquette_instruction2.grid(row=52, column=0, columnspan=self.numberColumns, sticky="nsew")  

        # Bouton pour générer le document PDF      
        self.btn_generer_pdf = tk.Button(self, text="Générer le document PDF", command=lambda: self.ajouter_texte_pdf("/Creation_dun_logiciel_de_Registre_delevage/view/Fichier_de_base.pdf", 4))
        self.btn_generer_pdf.grid(row=53, column=0, columnspan=self.numberColumns, sticky="nsew")
  
        #self.setup_background_animation()
        self.create_navigation_panel()
        self.bind("<Configure>", self.redimensionner_canevas)

  def deconnexion(self):
        # Ajoutez ici la logique pour déconnecter l'utilisateur
        messagebox.showinfo("Déconnexion", "Vous vous êtes déconnecté avec succès de votre espace")
        self.destroy()  # Ferme la fenêtre actuelle
        # Exécute le script Python externe
        subprocess.run(["python", "/Creation_dun_logiciel_de_Registre_delevage/view/Compte.py"])
            # Redimensionner le canevas lorsque la taille de la fenêtre change
        self.bind("<Configure>", self.redimensionner_canevas)

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
        self.after(6000, self.load_image)

  def redimensionner_image(self):
      image_path = self.image_paths[self.current_image_index]
      image = Image.open(image_path)
      image = image.resize((self.winfo_width(), self.winfo_height()))
      photo = ImageTk.PhotoImage(image)
      self.label_image.configure(image=photo)
      self.label_image = photo
                 
  def redimensionner_image(self):
        image_path = self.image_paths[self.current_image_index]
        image = Image.open(image_path)
        image = image.resize((self.winfo_width(), self.winfo_height()))
        photo = ImageTk.PhotoImage(image)
        self.label_image.configure(image=photo)
        self.label_image = photo

  def setup_background_animation(self):
        self.image_paths = glob.glob("/Creation_dun_logiciel_de_Registre_delevage/images/*.png")
        self.current_image_index = 0
        self.load_image() 
  
  # print the  elements from the databases
  def afficher_elements_canevas(self):
        # Création du cadre à l'intérieur du canevas
        #self.navbar_frame = tk.Frame(self.navbar_canvas)
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


  #fonction pour voir les éléments du json
  def view_caratherisis_detention_place(self):
     
      with open('/Creation_dun_logiciel_de_Registre_delevage/view/caracteristiques_lieu_detention.json', 'r') as file:
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
     with open('/Creation_dun_logiciel_de_Registre_delevage/view/caracteristiques_animaux.json', 'r') as file:
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
                if i <= len(self.data):
                    # Insérer la valeur dans le champ d'entrée correspondant
                    entry = self.data[i - 1][col_index]
                    entry.delete(0, 'end')  # Supprimer le contenu précédent
                    entry.insert(0, value)  # Insérer la nouvelle valeur
                else:
                    print(f"Erreur: L'indice {i} dépasse la taille de self.data.")

    # Ajouter les boutons en dehors de la boucle pour éviter la duplication
     self.bouton_ajouter_ligne = Button(self, text="Ajouter une ligne", command=self.ajouter_ligne)
     self.bouton_ajouter_ligne.grid(row=self.numberLines + 4, columnspan=len(self.col_title), sticky='nsew')

     btn_valider = Button(self, text="Modifier les informations", command=self.valider_caratheristiques_animaux)         
     btn_valider.grid(row=self.numberLines + 5, columnspan=len(self.col_title), sticky='nsew')                                  
    # Redimensionner le canevas lorsque la taille de la fenêtre change                                                
     self.bind("<Configure>", self.redimensionner_canevas)

  #fonction de creation de PDF temporaires 
  def create_temp_mouvement_temporaires(self, chemin_fichier):
    existing_pdf = PdfReader(chemin_fichier)
    
    # Récupérer la taille de la page 5
    page_num = 5

    output = PdfWriter()
    for i in range(5):
        output.add_page(existing_pdf.pages[page_num])

    with open('/Creation_dun_logiciel_de_Registre_delevage/view/mouvements_temporaires_temp.pdf', 'wb') as outputStream:
        output.write(outputStream)           
 
   #fonction création de fichiers temporaires
  def create_temp_controle_registre(self, chemin_fichier):
    existing_pdf = PdfReader(chemin_fichier)
    
    # Récupérer la taille de la page 5
    page_num = 9

    output = PdfWriter()
    for i in range(5):
        output.add_page(existing_pdf.pages[page_num])

    with open('/Creation_dun_logiciel_de_Registre_delevage/view/controle_registre_temp.pdf', 'wb') as outputStream:
        output.write(outputStream)

  def create_temp_soins_courant(self, chemin_fichier):
    existing_pdf = PdfReader(chemin_fichier)
    
    # Récupérer la taille de la page 
    page_num = 7

    output = PdfWriter()
    for i in range(5):
        output.add_page(existing_pdf.pages[page_num])

    with open('/Creation_dun_logiciel_de_Registre_delevage/view/soins_courant_temp.pdf', 'wb') as outputStream:
        output.write(outputStream)

  def create_caractheristiques_animaux_tmp(self,chemin_fichier):
    existing_pdf = PdfReader(chemin_fichier)
    
    # Récupérer la taille de la page 
    page_num = 4

    output = PdfWriter()
    for i in range(5):
        output.add_page(existing_pdf.pages[page_num])

    with open('/Creation_dun_logiciel_de_Registre_delevage/view/caratheristiques_temp.pdf', 'wb') as outputStream:
        output.write(outputStream)  
  def create_temp_carathersistiques_lieu_detention(self,chemin_fichier):     

    output = PdfWriter()
    existing_pdf = PdfReader(chemin_fichier)
    output.add(existing_pdf.pages[2])
    with open('/Creation_dun_logiciel_de_Registre_delevage/view/caractersistiques_lieu_detention_temp.pdf', 'wb') as outputStream:
        output.write(outputStream) 
# fonction de creation de PDF

  def PDF_Interventions_Soins_Courant(self, chemin_fichier):

    # Lire le PDF existant
    self.create_temp_soins_courant(chemin_fichier)                                                                                          
    existing_pdf = PdfReader("/Creation_dun_logiciel_de_Registre_delevage/view/soins_courant_temp.pdf")              

    # Récupérer la taille de la page 0         
    page_num = 0
    page_size = existing_pdf.pages[page_num].mediabox
    page_width = float(page_size[2]) - float(page_size[0])  # width
    page_height = float(page_size[3]) - float(page_size[1])  # height

    # Lire les données JSON
    with open("/Creation_dun_logiciel_de_Registre_delevage/view/Soins_Courant.json", 'r') as f:
        data = json.load(f)

    # Variables de gestion des pages
    ypos_index = 0
    result = 325 # Initialiser result au début de la première page
    output = PdfWriter()

    # Ajouter toutes les pages du PDF existant à la sortie
    for page in existing_pdf.pages:
        output.add_page(page)

    # Créer un nouvel objet PdfWriter sans les cinq premières pages
    filtered_output = PdfWriter()
    for i in range(5, len(output.pages)):
        filtered_output.add_page(output.pages[i])

    # Réassigner le writer original à celui filtré
    output = filtered_output

    # Variable pour suivre le numéro de page actuel dans le PDF final
    current_page = page_num

    while ypos_index < len(data["interventions"]):
        # Créer un nouveau PDF pour les dessins
        packet = BytesIO()
        can = canvas.Canvas(packet, pagesize=(page_width, page_height))
 
        # Dessiner le texte sur le canvas
        cpt = 0
        while cpt < 6 and ypos_index < len(data["interventions"]):
            intervention = data["interventions"][ypos_index]
            Date = intervention["Date"]
            Type_intervention = intervention["Type intervention"]
            Intervenant = intervention["Intervenant"]
            Nom_medicament = intervention["Traitement"]["Nom du medicament"]
            Voie_administration = intervention["Traitement"]["Voie administration"]
            Date_debut = intervention["Traitement"]["Date dedebut"]
            Date_fin = intervention["Traitement"]["Date dedefin"]
            N_ordonnance = intervention["N ordonnance"]
            Delai_attente_competition = intervention["Delai attente competition"]
            Delai_attente_abattage = intervention["Delai attente abattage"]

            # Dessiner du texte pour chaque élément
            can.drawString(50, result, Date)
            can.drawString(90, result, Type_intervention)
            can.drawString(150, result, Intervenant)
            can.drawString(250, result, Nom_medicament)
            can.drawString(330, result,  Voie_administration)
            can.drawString(470, result, Date_debut )

            can.drawString(510, result,  Date_fin)
            can.drawString(550, result,  N_ordonnance )
            can.drawString(620, result,  Delai_attente_competition)
            can.drawString(715, result, Delai_attente_abattage)    

            ypos_index += 1
            result -= 45  # Décalage vertical pour chaque nouvel élément
            cpt += 1

        # Sauvegarder la page actuelle
        can.save()
        packet.seek(0)

        new_pdf = PdfReader(packet)
        new_page = new_pdf.pages[0]

        # Ajouter la nouvelle page au PDF existant
        if current_page < len(existing_pdf.pages):

            existing_page = existing_pdf.pages[current_page]
            existing_page.merge_page(new_page)
            output.add_page(existing_page)
            
            print(" controle 1")
        else:
            print("surcharge")

        # Réinitialiser la position verticale et créer un nouveau canvas pour la prochaine page
        result = 325
        current_page += 1

    with open('/Creation_dun_logiciel_de_Registre_delevage/view/soins_courant.pdf', 'wb') as outputStream:
        output.write(outputStream)                                                                                         
  def PDF_controle_registre(self, chemin_fichier):  
    # Lire le PDF existant
    self.create_temp_controle_registre(chemin_fichier)                                                                                          
    existing_pdf = PdfReader("/Creation_dun_logiciel_de_Registre_delevage/view/controle_registre_temp.pdf")              

    # Récupérer la taille de la page 0         
    page_num = 0
    page_size = existing_pdf.pages[page_num].mediabox
    page_width = float(page_size[2]) - float(page_size[0])  # width
    page_height = float(page_size[3]) - float(page_size[1])  # height

    # Lire les données JSON
    with open("/Creation_dun_logiciel_de_Registre_delevage/view/controles.json", 'r') as f:
        data = json.load(f)

    # Variables de gestion des pages
    ypos_index = 0
    result = 365  # Initialiser result au début de la première page
    output = PdfWriter()

    # Ajouter toutes les pages du PDF existant à la sortie
    for page in existing_pdf.pages:
        output.add_page(page)

    # Créer un nouvel objet PdfWriter sans les cinq premières pages
    filtered_output = PdfWriter()
    for i in range(5, len(output.pages)):
        filtered_output.add_page(output.pages[i])

    # Réassigner le writer original à celui filtré
    output = filtered_output

    # Variable pour suivre le numéro de page actuel dans le PDF final
    current_page = page_num

    while ypos_index < len(data["controle"]):
        # Créer un nouveau PDF pour les dessins
        packet = BytesIO()
        can = canvas.Canvas(packet, pagesize=(page_width, page_height))
 
        # Dessiner le texte sur le canvas
        cpt = 0
        result=355
        while cpt < 6 and ypos_index < len(data["controle"]):
            controle = data["controle"][ypos_index]
            Date = controle["Date"]
            Organisme_controle = controle["Organisme de controle"]
            Motif_controle = controle["Motif de controle"]
            Nom_controleur = controle["Nom du controleur"]
            Cachet = controle["Cachet"]
            Signature = controle["Signature"]

            # Dessiner du texte pour chaque élément
            can.drawString(90, result, Date)
            can.drawString(180, result, Organisme_controle)
            can.drawString(300, result, Motif_controle)
            can.drawString(430, result, Nom_controleur)
            can.drawString(560, result, Cachet )
            can.drawString(675, result, Signature )

            ypos_index += 1
            result -= 45  # Décalage vertical pour chaque nouvel élément
            cpt += 1

        # Sauvegarder la page actuelle
        can.save()
        packet.seek(0)

        new_pdf = PdfReader(packet)
        new_page = new_pdf.pages[0]

        # Ajouter la nouvelle page au PDF existant
        if current_page < len(existing_pdf.pages):

            existing_page = existing_pdf.pages[current_page]
            existing_page.merge_page(new_page)
            output.add_page(existing_page)
            
            print(" controle 1")
        else:
            print("surcharge")

        # Réinitialiser la position verticale et créer un nouveau canvas pour la prochaine page
        result = 325
        current_page += 1

    with open('/Creation_dun_logiciel_de_Registre_delevage/view/controle_registre.pdf', 'wb') as outputStream:
        output.write(outputStream)
  def PDF_mouvement_temporaires(self, chemin_fichier):  
    # Lire le PDF existant
    self.create_temp_mouvement_temporaires(chemin_fichier)   #   Creation_dun_logiciel_de_Registre_delevage                                                                                       
    existing_pdf = PdfReader( "/Creation_dun_logiciel_de_Registre_delevage/view/mouvements_temporaires_temp.pdf" )          

    # Récupérer la taille de la page 0         
    page_num = 0
    page_size = existing_pdf.pages[page_num].mediabox
    page_width = float(page_size[2]) - float(page_size[0])  # width
    page_height = float(page_size[3]) - float(page_size[1])  # height
                    
    # Lire les données JSON
    with open("/Creation_dun_logiciel_de_Registre_delevage/view/mouvements_temporaires.json", 'r') as f:
        data = json.load(f)

    # Variables de gestion des pages
    ypos_index = 0
    result = 325  # Initialiser result au début de la première page
    output = PdfWriter()

    # Ajouter toutes les pages du PDF existant à la sortie
    for page in existing_pdf.pages:
        output.add_page(page)

    # Créer un nouvel objet PdfWriter sans les cinq premières pages
    filtered_output = PdfWriter()
    for i in range(5, len(output.pages)):
        filtered_output.add_page(output.pages[i])

    # Réassigner le writer original à celui filtré
    output = filtered_output

    # Variable pour suivre le numéro de page actuel dans le PDF final
    current_page = page_num

    while ypos_index < len(data["mouvements_temporaires"]):
        # Créer un nouveau PDF pour les dessins
        packet = BytesIO()
        can = canvas.Canvas(packet, pagesize=(page_width, page_height))

        # Dessiner le texte sur le canvas
        cpt = 0
        while cpt < 6 and ypos_index < len(data["mouvements_temporaires"]):
            mouvement = data["mouvements_temporaires"][ypos_index]
            Date_de_sortie = mouvement["Date de sortie"]
            Nom_equide = mouvement["Nom equide"]
            Motif = mouvement["Motif"]
            Etape_eventuelle = mouvement["Etape eventuelle"]
            Lieu_destination = mouvement["Lieu de destination (Adresse)"]
            Date_retour = mouvement["Date de retour"]

            # Dessiner du texte pour chaque élément
            can.drawString(90, result, Date_de_sortie)
            can.drawString(180, result, Nom_equide)
            can.drawString(300, result, Motif)
            can.drawString(430, result, Etape_eventuelle)
            can.drawString(560, result, Lieu_destination)
            can.drawString(675, result, Date_retour)

            ypos_index += 1
            result -= 45  # Décalage vertical pour chaque nouvel élément
            cpt += 1

        # Sauvegarder la page actuelle
        can.save()
        packet.seek(0)

        new_pdf = PdfReader(packet)
        new_page = new_pdf.pages[0]

        # Ajouter la nouvelle page au PDF existant
        if current_page < len(existing_pdf.pages):

            existing_page = existing_pdf.pages[current_page]
            existing_page.merge_page(new_page)
            output.add_page(existing_page)
            
        else:
            print("surcharge")

        # Réinitialiser la position verticale et créer un nouveau canvas pour la prochaine page
        result = 325
        current_page += 1

    with open('/Creation_dun_logiciel_de_Registre_delevage/view/mouvements_temporaires.pdf', 'wb') as outputStream:
        output.write(outputStream)

  def PDF_caratheristiques_animaux(self,chemin_fichier):        
     # Lire le PDF existant
    self.create_temp_soins_courant(chemin_fichier)                                                                                          
    existing_pdf = PdfReader("/Creation_dun_logiciel_de_Registre_delevage/view/soins_courant_temp.pdf")              

    # Récupérer la taille de la page 0         
    page_num = 0
    page_size = existing_pdf.pages[page_num].mediabox
    page_width = float(page_size[2]) - float(page_size[0])  # width
    page_height = float(page_size[3]) - float(page_size[1])  # height

    # Lire les données JSON
    with open("/Creation_dun_logiciel_de_Registre_delevage/view/caracteristiques_animaux.json", 'r') as f:
        data = json.load(f)

    # Variables de gestion des pages
    ypos_index = 0
    result = 325  # Initialiser result au début de la première page
    output = PdfWriter()

    # Ajouter toutes les pages du PDF existant à la sortie
    for page in existing_pdf.pages:
        output.add_page(page)

    # Créer un nouvel objet PdfWriter sans les cinq premières pages
    filtered_output = PdfWriter()
    for i in range(5, len(output.pages)):
        filtered_output.add_page(output.pages[i])

    # Réassigner le writer original à celui filtré
    output = filtered_output

    # Variable pour suivre le numéro de page actuel dans le PDF final
    current_page = page_num

    while ypos_index < len(data["caracteristiques"]):
        # Créer un nouveau PDF pour les dessins
        packet = BytesIO()
        can = canvas.Canvas(packet, pagesize=(page_width, page_height))

        # Dessiner le texte sur le canvas
        cpt = 0
        while cpt < 6 and ypos_index < len(data["caracteristiques"]):
            caracteristiques = data["caracteristiques"][ypos_index]
            nom =   caracteristiques["Nom"]
            NeSIRE =   caracteristiques["NeSIRE"]
            Netranspondeur =   caracteristiques["Netranspondeur"]
            Nom_proprietaire =   caracteristiques["Nom et coordonnees du proprietaire"]
            Date_de_premiere_entree =   caracteristiques["Date de premiere entree"]
            Adresse_de_provenance =   caracteristiques["Adresse de provenance"]
            Date_de_sortie_definitive =   caracteristiques["Date de sortie definitive"]
            Adresse_destination =   caracteristiques["Adresse de destination"]

            # Dessiner du texte pour chaque élément
            can.drawString(80, 320 + ypos_index, nom)
            can.drawString(160, 320 + ypos_index, NeSIRE)
            can.drawString(250, 320 + ypos_index, Netranspondeur)
            can.drawString(340, 320 + ypos_index, Nom_proprietaire)
            can.drawString(440, 320 + ypos_index, Date_de_premiere_entree)
            can.drawString(520, 320 + ypos_index, Adresse_de_provenance)
            can.drawString(620, 320 + ypos_index, Date_de_sortie_definitive)
            can.drawString(720, 320 + ypos_index, Adresse_destination)

            ypos_index += 1
            result -= 45  # Décalage vertical pour chaque nouvel élément
            cpt += 1

        # Sauvegarder la page actuelle
        can.save()
        packet.seek(0)

        new_pdf = PdfReader(packet)
        new_page = new_pdf.pages[0]

        # Ajouter la nouvelle page au PDF existant
        if current_page < len(existing_pdf.pages):

            existing_page = existing_pdf.pages[current_page]
            existing_page.merge_page(new_page)
            output.add_page(existing_page)
            
        else:
            print("surcharge")

        # Réinitialiser la position verticale et créer un nouveau canvas pour la prochaine page
        result = 325
        current_page += 1

    with open('/Creation_dun_logiciel_de_Registre_delevage/view/caratheristiques_animaux.pdf', 'wb') as outputStream:
        output.write(outputStream)
  def PDF_carathersistiques_lieu_detention_particulier(self,chemin_fichier,id):        
     # Lire le PDF existant
    self.create_temp_carathersistiques_lieu_detention_particulier(chemin_fichier)                                                                                          
    existing_pdf = PdfReader("/Creation_dun_logiciel_de_Registre_delevage/view/carathersistiques_lieu_detention_temp.pdf")              

    # Récupérer la taille de la page 0         
    page_num = 0
    page_size = existing_pdf.pages[page_num].mediabox
    page_width = float(page_size[2]) - float(page_size[0])  # width
    page_height = float(page_size[3]) - float(page_size[1])  # height

    # Lire les données JSON
    with open("/Creation_dun_logiciel_de_Registre_delevage/view/comptes_particuliers.json.json", 'r') as f:
        data = json.load(f)

    # Variables de gestion des pages

    result = 325  # Initialiser result au début de la première page
    output = PdfWriter()

    # Ajouter toutes les pages du PDF existant à la sortie
    #for page in existing_pdf.pages:
    page=existing_pdf.pages[page_num]
    output.add_page(page)

    # Variable pour suivre le numéro de page actuel dans le PDF final
    current_page = page_num

    if id ==data["comptes"]["Numero de detenteur (SIRE)"]:
        # Créer un nouveau PDF pour les dessins
        packet = BytesIO()
        can = canvas.Canvas(packet, pagesize=(page_width, page_height))

        # Dessiner le texte sur le canvas

        caracteristiques = data["caracteristiques"][id]
        NeSIRE =   caracteristiques["Numero de detenteur (SIRE)"]
        prenomn =   caracteristiques["Prenom"]
        Nom_usage =   caracteristiques["Nom d'usage"]
        NUMAGRIT =   caracteristiques["NUMAGRIT"]
        Adresse =   caracteristiques["Adresse"]
        Telephone =   caracteristiques["Telephone"]
        Portable =   caracteristiques["Portable"]
        Adresse_mail =   caracteristiques["Adresse e-mail"]
        Mail =   caracteristiques["Mail"]

        # Dessiner du texte pour chaque élément
        can.drawString(80, 320 ,  NeSIRE)
        can.drawString(160, 320 , prenomn)
        can.drawString(250, 320 , Nom_usage)
        can.drawString(340, 320 , NUMAGRIT)
        can.drawString(440, 320 , Adresse)
        can.drawString(520, 320 , Telephone)
        can.drawString(620, 320 , Portable)
        can.drawString(720, 320 , Adresse_mail)

            # ypos_index += 1
        result -= 45  # Décalage vertical pour chaque nouvel élément
            # cpt += 1

        # Sauvegarder la page actuelle
        can.save()
        packet.seek(0)

        new_pdf = PdfReader(packet)
        new_page = new_pdf.pages[0]

        # Ajouter la nouvelle page au PDF existant
        if current_page < len(existing_pdf.pages):

            existing_page = existing_pdf.pages[current_page]
            existing_page.merge_page(new_page)
            output.add_page(existing_page)
            
        else:
            print("surcharge")

        # Réinitialiser la position verticale et créer un nouveau canvas pour la prochaine page
        result = 325
        current_page += 1

    with open('/Creation_dun_logiciel_de_Registre_delevage/view/caratheristiques_animaux.pdf', 'wb') as outputStream:
        output.write(outputStream)

  def ajouter_texte_pdf(self, chemin_fichier, page_num):   
    # Exécuter les fonctions pour générer les PDF temporaires
    self.PDF_mouvement_temporaires(chemin_fichier)
    # self.PDF_Interventions_Soins_Courant(chemin_fichier)
    self.PDF_controle_registre(chemin_fichier)
    self.PDF_caratheristiques_animaux(chemin_fichier)

    # Créer un PdfWriter pour le fichier final combiné
    final_output = PdfWriter()

    # Sauvegarder les pages modifiées dans un fichier temporaire
    self.create_caractheristiques_animaux_tmp(chemin_fichier)                                                                                         
    existing_pdf = PdfReader("/Creation_dun_logiciel_de_Registre_delevage/view/caratheristiques_temp.pdf")              

    # Récupérer la taille de la page 0         
    page_num = 0
    page_size = existing_pdf.pages[page_num].mediabox
    page_width = float(page_size[2]) - float(page_size[0])  # width
    page_height = float(page_size[3]) - float(page_size[1])  # height

    # Lire les données JSON
    with open("/Creation_dun_logiciel_de_Registre_delevage/view/caracteristiques_animaux.json", 'r') as f:
        data = json.load(f)
    
    result = 325  # Initialiser result au début de la première page
    output_temp = PdfWriter()
    ypos_index = 0

    # Ajouter toutes les pages du PDF existant à la sortie
    for page in existing_pdf.pages:
       output_temp.add_page(page)

    # Créer un nouvel objet PdfWriter sans les cinq premières pages
    filtered_output = PdfWriter()
    for i in range(5, len(output_temp.pages)):
        filtered_output.add_page(output_temp.pages[i])

    # Réassigner le writer original à celui filtré
    output_temp = filtered_output

    # Variable pour suivre le numéro de page actuel dans le PDF final
    current_page = page_num

    while ypos_index < len(data["caracteristiques"]):
        # Créer un nouveau PDF pour les dessins
        packet = BytesIO()
        can = canvas.Canvas(packet, pagesize=(page_width, page_height))

        # Dessiner le texte sur le canvas
        cpt = 0
   
        ypos_index2 = 0
        while cpt < 6 and ypos_index < len(data["caracteristiques"]):

            caracteristiques = data["caracteristiques"][ypos_index]
            nom =   caracteristiques["Nom"]
            NeSIRE =   caracteristiques["NeSIRE"]
            Netranspondeur =   caracteristiques["Netranspondeur"]
            Nom_proprietaire =   caracteristiques["Nom et coordonnees du proprietaire"]
            Date_de_premiere_entree =   caracteristiques["Date de premiere entree"]
            Adresse_de_provenance =   caracteristiques["Adresse de provenance"]
            Date_de_sortie_definitive =   caracteristiques["Date de sortie definitive"]
            Adresse_destination =   caracteristiques["Adresse de destination"]

            # Dessiner du texte pour chaque élément
            can.drawString(80, 320 + ypos_index2, nom)
            can.drawString(160, 320 + ypos_index2, NeSIRE)
            can.drawString(250, 320 + ypos_index2, Netranspondeur)
            can.drawString(340, 320 + ypos_index2, Nom_proprietaire)
            can.drawString(440, 320 + ypos_index2, Date_de_premiere_entree)
            can.drawString(520, 320 + ypos_index2, Adresse_de_provenance)
            can.drawString(620, 320 + ypos_index2, Date_de_sortie_definitive)
            can.drawString(720, 320 + ypos_index2, Adresse_destination)
            
            ypos_index+=1
            ypos_index2 -= 45
            result -= 45  # Décalage vertical pour chaque nouvel élément
            cpt += 1

        # Sauvegarder la page actuelle
        can.save()
        packet.seek(0)

        new_pdf = PdfReader(packet)
        new_page = new_pdf.pages[0]

        # Ajouter la nouvelle page au PDF existant
        if current_page < len(existing_pdf.pages):
            existing_page = existing_pdf.pages[current_page]
            existing_page.merge_page(new_page)
            output_temp.add_page(existing_page)
            
        else:
            print("surcharge  texte ")

        # Réinitialiser la position verticale et créer un nouveau canvas pour la prochaine page
        result = 325
        current_page += 1

        temp_output_path = "/Creation_dun_logiciel_de_Registre_delevage/view/caracteristiques_animaux_temp.pdf"
        with open(temp_output_path, "wb") as outputStream:
         output_temp.write(outputStream)

    # Créer un PdfWriter pour le fichier final combiné
    final_output = PdfWriter()

    # Ajouter les pages de chaque fichier PDF temporaire au fichier final
    for file_path in ["/Creation_dun_logiciel_de_Registre_delevage/view/caracteristiques_animaux_temp.pdf",  "/Creation_dun_logiciel_de_Registre_delevage/view/mouvements_temporaires.pdf", "soins_courant.pdf", "controle_registre.pdf"]:
        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
            continue
        reader = PdfReader(file_path)
        for page in reader.pages:
            final_output.add_page(page)

    # Enregistrer les pages combinées dans le fichier final
    final_output_path = "/Creation_dun_logiciel_de_Registre_delevage/Registre_delevage_detenteurs_dequides/Registre_delevage_detenteurs_dequide.pdf"
    try:
        with open(final_output_path, "wb") as finalOutputStream:
            final_output.write(finalOutputStream)
        self.texte_instruction3 = "Votre fichier PDF est enregistré. Il a pour chemin /Creation_dun_logiciel_de_Registre_delevage/Registre_delevage_detenteurs_dequides/ et pour nom ceci Registre_delevage_detenteurs_dequide.pdf "
        self.etiquette_instruction3 = tk.Label(self, text=self.texte_instruction3, font=("Helvetica", 12))
        self.etiquette_instruction3.grid(row=50, column=0, columnspan=self.numberColumns, sticky="nsew")
    except Exception as e:
        self.texte_instruction3 = "Désolé nous n'avons pas pu sauvegarder votre pdf  "
        self.etiquette_instruction3 = tk.Label(self, text=self.texte_instruction3, font=("Helvetica", 12))
        self.etiquette_instruction3.grid(row=50, column=0, columnspan=self.numberColumns, sticky="nsew")

  #fonction de gestion de la fenetre    
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
    widgets_a_garder = [
      #  self.navbar_canvas, 
        self.scrollbar,# self.navbar_frame,
      #  self.btn_encadrement,
        self.btn_generer_pdf,self.texte_instruction3,self.texte_instruction2, self.texte_instruction, self.etiquette_instruction,  self.etiquette_instruction2 , self.etiquette_instruction3,
        self.btn_caractheristiques_animaux,
        self.btn_mouvement_temporaire, self.btn_intervention_soins,
        self.btn_controle_registre,
        self.btn_deconnexion
    ]

    for widget in self.winfo_children():
        if isinstance(widget, tk.Entry) and widget not in widgets_a_garder:
            widget.destroy()
     #       print("destruction de " + str(widget))
        elif isinstance(widget, tk.Label) and widget not in widgets_a_garder:
            if widget.cget("text") in self.col_title:
                widget.destroy()
      #          print("destruction de " + str(widget))
            else:
                widget.destroy()
       #         print("destruction de " + str(widget))
        elif isinstance(widget, tk.Button) and widget not in widgets_a_garder:
            widget.destroy()
        #    print("destruction de " + str(widget))
  def ajouter_ligne(self):
        # Function to add a new row
        row_data = []
        for j in range(len(self.col_title)):
            cell = tk.Entry(self.navbar_frame, width=22)
            cell.grid(row=self.numberLines+14, column=j, sticky='nsew')
            row_data.append(cell)
        self.data.append(row_data)
        self.numberLines += 1

  def redimensionner_canevas(self, event=None):
      self.navbar_canvas.configure(scrollregion=self.navbar_canvas.bbox("all"))

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
   
# open the window on the dashboard
  def ouvrir_mouvement_temporaires(self):
      self.data=[]
      self.supprimer_widgets()
        
    # Création du cadre à l'intérieur du canevas
      self.navbar_frame = tk.Frame(self.navbar_canvas)
      self.navbar_canvas.create_window((0, 0), window=self.navbar_frame, anchor='nw')
      self.col_title = ["Date de sortie", "Nom equide", "Motif", "Etape eventuelle", "Lieu de destination (Adresse)", "Date de retour"] 


      for j in range(len(self.col_title)):      
        col_tmp = self.col_title[j]
        col_title = tk.Label(self.navbar_frame, text=col_tmp, width=30, relief="solid", bg="lightgray", anchor="w")
        col_title.grid(row=10, column=j, sticky='nsew')  # Utilise sticky pour que la colonne s'adapte
    
    # Création des champs d'entrée
      for i in range(30):
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
      self.navbar_frame.bouton_ajouter_ligne.grid(row=self.numberLines + 4, column=0, columnspan=len(self.col_title)+4, sticky='nsew')
     
      btn_valider = tk.Button(self, text="Valider", command=self.valider_mouvements_temporaires)
      btn_valider.grid(row=self.numberLines + 5, column=0, columnspan=len(self.col_title)+4, sticky='nsew')

      btn_valider = tk.Button(self, text="Afficher mouvements temporaires ", command=lambda: Movements.view_temporary_movements(self))
      btn_valider.grid(row=self.numberLines + 6, column=0, columnspan=len(self.col_title)+4, sticky='nsew')   

    # Texte additionnel 3
      self.texte_instruction3 = "Vous etes actuellement sur la page mouvmements temporaires "
      self.etiquette_instruction3 = tk.Label(self, text=self.texte_instruction3, font=("Helvetica", 12))
      self.etiquette_instruction3.grid(row=50, column=0, columnspan=self.numberColumns, sticky="nsew") 
  def open_encadrement_zootechnique(self):
      self.data=[]
      self.supprimer_widgets()
  
   # Création du cadre à l'intérieur du canevas
      self.navbar_frame = tk.Frame(self.navbar_canvas)
      self.navbar_canvas.create_window((0, 0), window=self.navbar_frame, anchor='nw')
      self.col_title =  ["Lieu Habituel et coordonee de detention", "Nom et coordonees veterianire traitant", "Nom et coordonnees du veterinaire sanitaire" ,"Nom et coordonnees du referent bien-etre animal", "Nom adresse tel des Organismes sanitaires reconnus", "Nom, adresse tel marechal ferrand","Nom, adresse et N de telephone du dentiste"] #Nom, adresse et N° de téléphone du dentiste(facultatif)
                                                                       
    # Ajout de l'espace entre le menu de navigation et "Sire"         
      for j in range(len(self.col_title)):
        col_tmp = self.col_title[j]
        col_title = tk.Label(self.navbar_frame, text=col_tmp, width=15, relief="solid", bg="lightgray", anchor="w")
        col_title.grid(row=0, column=j, sticky='nsew')  # Utilise sticky pour que la colonne s'adapte   
    
    # Création des champs d'entrée
      for i in range(30):
        row_data = []
        for j in range(len(self.col_title)):
            cell = tk.Entry(self.navbar_frame, width=22)
            cell.grid(row=i+1, column=j, sticky='nsew')  # Commencer à la ligne 12
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
      
          # Texte additionnel 3
      self.texte_instruction3 = "Vous etes actuellement sur la page encadrement zootechnoique "
      self.etiquette_instruction3 = tk.Label(self, text=self.texte_instruction3, font=("Helvetica", 12))
      self.etiquette_instruction3.grid(row=50, column=0, columnspan=self.numberColumns, sticky="nsew") 

   # Redimensionner le canevas lorsque la taille de la fenêtre change
      self.bind("<Configure>", self.redimensionner_canevas)

  def ouvrir_interventions(self):
      self.supprimer_widgets()
      self.data = []  # Assurez-vous que self.data est initialisé
    # Création du cadre à l'intérieur du canevas
      self.navbar_frame = tk.Frame(self.navbar_canvas)
      self.navbar_canvas.create_window((0, 0), window=self.navbar_frame, anchor='nw')
      self.col_title = ["Date", "Type intervention", "Intervenant", "Traitement", "N ordonnance","Date de debut","Date de fin","Delai attente competition","Delai attente abattage"]


  # Ajout de l'espace entre le menu de navigation et "Sire"

      for j in range(len(self.col_title)):
        col_tmp = self.col_title[j]
        col_title = tk.Label(self.navbar_frame, text=col_tmp, width=15, relief="solid", bg="lightgray", anchor="w")
        col_title.grid(row=10, column=j, sticky='nsew')  # Utilise sticky pour que la colonne s'adapte
    
    # Création des champs d'entrée
      for i in range(30):
        row_data = []
        for j in range(len(self.col_title)):
            cell = tk.Entry(self.navbar_frame, width=22)
            cell.grid(row=i+14, column=j, sticky='nsew') 
            row_data.append(cell)
        self.data.append(row_data)

    # Configurer la gestion des colonnes pour qu'elles s'adaptent au contenu
      for j in range(len(self.col_title)):
        self.navbar_frame.grid_columnconfigure(j, weight=1) 

    # Bouton de validation
      self.navbar_frame.bouton_ajouter_ligne = Button(self, text="Ajouter une ligne", command=self.ajouter_ligne)
      self.navbar_frame.bouton_ajouter_ligne.grid(row=self.numberLines + 4, column=0, columnspan=len(self.col_title), sticky='nsew')
    
      btn_valider = tk.Button(self, text="Valider", command=self.valider_informations_intervention)
      btn_valider.grid(row=self.numberLines + 5, column=0, columnspan=len(self.col_title), sticky='nsew')

      btn_valider = tk.Button(self, text="Afficher interventions", command=lambda: Interventions.view_informations_intervention(self))
      btn_valider.grid(row=self.numberLines + 6, column=0, columnspan=len(self.col_title), sticky='nsew') 
         
      self.texte_instruction3 = "Vous etes actuellement sur la page intervention et soins courant"
      self.etiquette_instruction3 = tk.Label(self, text=self.texte_instruction3, font=("Helvetica", 12))
      self.etiquette_instruction3.grid(row=50, column=0, columnspan=self.numberColumns, sticky="nsew") 

      # Redimensionner le canevas lorsque la taille de la fenêtre change
      self.bind("<Configure>", self.redimensionner_canevas)

  def ouvrir_controle_registre_elevage(self):
      # Création du cadre à l'intérieur du canevas
      self.supprimer_widgets()
      self.data = []  # Assurez-vous que self.data est initialisé
    # Création du cadre à l'intérieur du canevas
      self.navbar_frame = tk.Frame(self.navbar_canvas)
      self.navbar_canvas.create_window((0, 0), window=self.navbar_frame, anchor='nw')
      self.col_title = ["Date", "Organisme de controle", "Motif de controle", "Nom du controleur", "Cachet","Signature"]    
 
    # Ajout de l'espace entre le menu de navigation et "Sire"
    
      for j in range(len(self.col_title)):#len(self.col_title)):
        col_tmp = self.col_title[j]
        col_title = tk.Label(self.navbar_frame, text=col_tmp, width=30, relief="solid", bg="lightgray", anchor="w")
        col_title.grid(row=10, column=j, sticky='nsew')  # Utilise sticky pour que la colonne s'adapte
    
    # Création des champs d'entrée
      for i in range(30):
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

              # # Bouton pour ajouter une nouvelle ligne
      self.bouton_ajouter_ligne = Button(self, text="Ajouter une ligne", command=self.ajouter_ligne)
      self.bouton_ajouter_ligne.grid(row=self.numberLines + 4, column=0, columnspan=len(self.col_title)+4, sticky='nsew')

      btn_valider = tk.Button(self, text="Afficher les informations concernant le controle de mon registre d'élévage", command=lambda:controle.view_control(self))
      btn_valider.grid(row=self.numberLines + 5, column=0, columnspan=len(self.col_title)+4, sticky='nsew')

      self.bouton_ajouter_ligne = Button(self, text="Valider les informations", command= lambda : self.valider_informations_controle)
      self.bouton_ajouter_ligne.grid(row=self.numberLines + 6, column=0, columnspan=len(self.col_title)+4, sticky='nsew')  

      self.texte_instruction3 = "Vous etes actuellement sur la page controle du registre d'élévage "
      self.etiquette_instruction3 = tk.Label(self, text=self.texte_instruction3, font=("Helvetica", 12))
      self.etiquette_instruction3.grid(row=50, column=0, columnspan=self.numberColumns, sticky="nsew")   

    # Redimensionner le canevas lorsque la taille de la fenêtre change
      self.bind("<Configure>", self.redimensionner_canevas)

  def ouvrir_caractheristiques_animaux(self):
      self.supprimer_widgets()
      self.data=[] 
    # Création du cadre à l'intérieur du canevas
      self.navbar_frame = tk.Frame(self.navbar_canvas)
      self.navbar_canvas.create_window((0, 0), window=self.navbar_frame, anchor='nw')
      self.col_title =  ["Nom","NeSIRE","Netranspondeur","Nom et coordonnees du proprietaire","Adresse proprietaire","Date de premiere entree", "Adresse de provenance", "Date de sortie definitive", "Adresse de destination"] 
          
    # Ajout de l'espace entre le menu de navigation et "Sire"
      for j in range(9):
        col_tmp = self.col_title[j]
        col_title = tk.Label(self.navbar_frame, text=col_tmp, width=15, relief="solid", bg="lightgray", anchor="w")
        col_title.grid(row=10, column=j, sticky='nsew')  # Utilise sticky pour que la colonne s'adapte
    
    # Création des champs d'entrée
      for i in range(30):
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
     
      btn_valider = tk.Button(self, text="Valider", command=self.valider_caratheristiques_animaux)
      btn_valider.grid(row=self.numberLines + 5, column=0, columnspan=len(self.col_title), sticky='nsew')

      btn_valider = tk.Button(self, text="Afficher mes caractheristiques d'animaux", command=self.view_animals)  
      btn_valider.grid(row=self.numberLines + 6, column=0, columnspan=len(self.col_title), sticky='nsew')

      self.texte_instruction3 = "Vous etes actuellement sur la page caratheristiques de animaux"
      self.etiquette_instruction3 = tk.Label(self, text=self.texte_instruction3, font=("Helvetica", 12))
      self.etiquette_instruction3.grid(row=50, column=0, columnspan=self.numberColumns, sticky="nsew") 

 # Redimensionner le canevas lorsque la taille de la fenêtre change
      self.bind("<Configure>", self.redimensionner_canevas)
  def ouvrir_caracteristiques_lieu_detention(self):

      self.navbar_frame = tk.Frame(self.navbar_canvas)
      self.navbar_canvas.create_window((0, 0), window=self.navbar_frame, anchor='nw')
      self.col_title = ["Statut juridique (faculatitif)", "Organisme de controle", "Motif de controle", "Nom du controleur", "Cachet", "Signature"]

    # Ajouter tous les titres de colonne
      for j in range(len(self.col_title)):
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

    # Bouton de validation
      self.navbar_frame.bouton_ajouter_ligne = Button(self, text="Ajouter une ligne", command=self.ajouter_ligne)
      self.navbar_frame.bouton_ajouter_ligne.grid(row=self.numberLines + 4, column=0, columnspan=len(self.col_title), sticky='nsew')
     
      btn_valider = tk.Button(self, text="Valider", command=self.valider_carathersitiques_lieu)
      btn_valider.grid(row=self.numberLines + 5, column=0, columnspan=len(self.col_title), sticky='nsew')

      btn_valider = tk.Button(self, text="Afficher mes caractheristiques de lieu  de détention", command=CaratheristiquesDetention.regarder_carachersitiques_lieu_detention(self)) 
      btn_valider.grid(row=self.numberLines + 6, column=0, columnspan=len(self.col_title), sticky='nsew')   
          # Redimensionner le canevas lorsque la taille de la fenêtre change
      self.texte_instruction3 = "Vous etes actuellement sur la page caratheristiques du lieu de détention"
      self.etiquette_instruction3 = tk.Label(self, text=self.texte_instruction3, font=("Helvetica", 12))
      self.etiquette_instruction3.grid(row=50, column=0, columnspan=self.numberColumns, sticky="nsew")   

      self.bind("<Configure>", self.redimensionner_canevas) 

  #validations informations functions and put them in json  
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
      with open('/Creation_dun_logiciel_de_Registre_delevage/view/mouvements_temporaires.json', 'w') as json_file:
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
      with open('/Creation_dun_logiciel_de_Registre_delevage/view/caracteristiques_lieu_detention.json', 'w') as json_file:
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
        with open('/Creation_dun_logiciel_de_Registre_delevage/view/controles.json', 'w') as json_file:
            json.dump({"controle": controle_data}, json_file, indent=4)

  
  def valider_informations_soins_courant(self):      
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
        with open('/Creation_dun_logiciel_de_Registre_delevage/view/controles.json', 'w') as json_file:
            json.dump({"controle": controle_data}, json_file, indent=4)          

  def valider_encadrement_Zootechnique_animaux(self): # elargir le panel pour que l'on voit tout
    # Collecte des données depuis les champs d'entrée
    #flag code test
    intervention_data = []

    for row_data in self.data:

        encadrement = {
            "Lieu Habituel et coordonee de detention": row_data[0].get() ,
            "Nom et coordonees veterianire traitant": row_data[1].get() ,
            "Nom et coordonnees du veterinaire sanitaire": row_data[2].get() ,
            "Nom et coordonnees du referent bien-etre animal": row_data[3].get() ,
            "Nom adresse tel des Organismes sanitaires reconnus": row_data[4].get() ,
            "Nom, adresse tel marechal ferrand": row_data[5].get() ,
            "Nom, adresse et N de telephone du dentiste": row_data[6].get() ,
        }
       
        intervention_data.append(encadrement)
 
    try:
        with open('/Creation_dun_logiciel_de_Registre_delevage/view/encadrement_zootechnique.json', 'w') as json_file:
            json.dump({"encadrement": intervention_data}, json_file, indent=4)
            # Impression de débogage
            print("Les données ont été écrites dans encadrement_zootechnique.json")
    except Exception as e:
        print(f"Erreur lors de l'écriture du fichier JSON: {e}")

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
       with open('/Creation_dun_logiciel_de_Registre_delevage/view/interventions.json', 'w') as json_file:
        json.dump(intervention_data, json_file, indent=4)  
    
  def valider_informations_intervention(self):
      interventions = []  # Initialiser la liste des interventions
    
      for row in self.data:
        # Créer un dictionnaire pour chaque intervention
        intervention = {
            "Date": row[0].get(),
            "Type intervention": row[1].get(),
            "Intervenant": row[2].get(),
            
            "Nom du medicament": row[3].get(),
            "Voie administration": row[4].get(),
            "Date dedebut": row[5].get(),
            "Date dedefin": row[6].get(),
        
            "N ordonnance": row[7].get(),
            "Delai attente competition": row[8].get(),
            "Delai attente abattage": row[9].get()
        }

        interventions.append(intervention)  # Ajouter l'intervention à la liste
    
    # Écrire le fichier JSON avec la liste des interventions
      with open('/Creation_dun_logiciel_de_Registre_delevage/view/Soins_Courant.json', 'w') as f:
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
            "Nom et coordonnees du proprietaire": row[3].get(),  
            "Adresse proprietaire": row[4].get(),
            "Date de premiere entree": row[5].get(),
            "Adresse de provenance": row[6].get(),
            "Date de sortie definitive": row[7].get(),  # Changer l'indice à 6
            "Adresse de destination":  row[8].get()
        }

        # Ajouter le nouveau caractère à la liste
        nouveaux_caract.append(caratheristiques_animaux)
            
    # Réécrire le fichier JSON avec la nouvelle structure
      with open('/Creation_dun_logiciel_de_Registre_delevage/view/caracteristiques_animaux.json', 'w') as json_file:
         json.dump({"caracteristiques":nouveaux_caract}, json_file, indent=4) 

if __name__ == "__main__":
    app = FenetrePrincipale(width=1920, col_titles=["Colonne 1", "Colonne 2","c","c","c","colonne","c","c"], height=1080)
    app.mainloop() 
