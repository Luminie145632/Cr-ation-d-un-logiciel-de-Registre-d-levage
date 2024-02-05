import tkinter as tk
from tkinter import messagebox, Frame, Entry, Button, Label, BOTH, ttk, Canvas
import os
from PIL import Image, ImageTk
import json

# Définition de la classe lieu_de_detention
class Presence_CaratherisisGUI(Frame):
    # Constructeur de la classe lieu_de_detention
    def __init__(self, fenetre, height, width, col_titles):
        # Attributs de la classe
        super().__init__(fenetre)
        self.fenetre=fenetre
        self.height=height
        self.width=width
        self.col_titles=col_titles
        self.numberLines = 1
        self.numberColumns=width
        self.pack(fill=BOTH)
        #ouou
        tex1 = Label(self, text='Encadrement Zootechnique Sanitaire et Médical des Animaux', fg='cyan')
        tex1.grid(row=0, column=0, columnspan=8)

        # Ajout des titres de colonnes
        for j in range(self.numberColumns):
            col_title = Label(self, text=self.col_titles[j], width=20, relief="solid", bg="lightgray", anchor="w")
            col_title.grid(row=0, column=j, sticky='nsew')

        # Ajout des données du tableau
        self.data = []
        for i in range(1, self.numberLines + 1):
            line = []
            for j in range(self.numberColumns):
                cell = Entry(self, width=20)
                cell.grid(row=i, column=j, sticky='nsew')
                line.append(cell)
            self.data.append(line)
        
            self.date_sortie=line[1]    
        # Configurer la gestion des colonnes pour qu'elles s'adaptent au contenu
        for j in range(self.numberColumns):
            self.grid_columnconfigure(j, weight=1)
        
        self.can1 = Canvas(self, bg='blue', width=450, height=450)
        self.can1.grid(row=self.numberLines + 2, column=0, columnspan=self.numberColumns, pady=5)

        # Ajout du Canvas
        self.can1 = Canvas(self, bg='blue', width=450, height=450)
        self.can1.grid(row=self.numberLines + 2, column=0, columnspan=self.numberColumns, pady=5)

        # Charger l'image avec PIL
        image = Image.open("cheval_blanc.png")
        # Augmenter la taille de l'image (dans cet exemple, je l'ai doublée)
        image = image.resize((960, 540), Image.BICUBIC)
        # Convertir l'image en format Tkinter PhotoImage
        self.image = ImageTk.PhotoImage(image)

        # Afficher l'image sur le canvas
        self.can1.create_image(0, 0, anchor=tk.NW, image=self.image)
        
        btn_valider = Button(self, text="Valider", command=self.valider_informations)
        btn_valider.grid(row=10, column=0, columnspan=self.numberColumns, sticky='nsew')

        # Création des boutons de la barre de navigation
        btn_mouvement_temporaire = Button(self, text="Retour au menu principal", command=self.return_main_menu)
        btn_mouvement_temporaire.grid(row=11, column=0, columnspan=self.numberColumns, sticky='nsew')

    def valider_informations(self):
        # Récupérer les informations depuis les champs d'entrée (à adapter en fonction de votre logique)
        nom = self.data[0][0].get()
        sire = self.data[0][1].get()
        no_transpondeur = self.data[0][2].get()
        nom_proprio = self.data[0][3].get()
        date_entree = self.data[0][4].get()
        adresse_provenance = self.data[0][5].get()
        date_sortie_def=  self.data[0][6].get()
        adresse_destination= self.data[0][7].get()

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
        "Date_sortie_definitive":   date_sortie_def,
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
    def return_main_menu(self):
        self.destroy()
        os.system("python Accueil.py")

if __name__ == "__main__":
    fenetre = tk.Tk()
    fenetre.title("Présence et caractéristiques des animaux")
    fenetre.geometry("960x540")
    fenetre.iconbitmap("horse_sans_fond.ico")
   # fenetre.resizable(height=False, width=False)
    col_titles = ["Nom", "n° SIRE", "n° Transpondeur", "Nom et coordonnées du propriétaires", "Date de première entrée", "Adresse de provenance","Date de sortie définitive","Adresse de destination"]  
    fenetre_principale = Presence_CaratherisisGUI(fenetre, height=3, width=8, col_titles=col_titles)
    fenetre_principale.mainloop()