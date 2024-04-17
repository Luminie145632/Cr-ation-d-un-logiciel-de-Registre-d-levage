import tkinter as tk
from tkinter import messagebox, Frame, Entry, Button, Label, BOTH, ttk, Canvas
import os
from PIL import Image, ImageTk
import json

# Définition de la classe lieu_de_detention
class InterventionsGUI(Frame):
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
        Date = self.data[0][0].get()
        type = self.data[0][1].get()
        Intervenant = self.data[0][2].get()
        Traitement = self.data[0][3].get()
        nom_medoc = self.data[0][4].get()
        voie_administration = self.data[0][5].get()
        date_debut=  self.data[0][6].get()
        date_fin= self.data[0][7].get()
        no_ordoonnance= self.data[0][8].get()
        delai_attente_compet= self.data[0][9].get()
        delai_attente_kill= self.data[0][10].get()

        # Afficher les valeurs dans la console (vous pouvez remplacer cela par vos propres actions)
    
        nouveau_caract = {
       "Date": Date,
        "Type intervention": type, 
        "Traitement": Traitement,
        "Nom médicament": nom_medoc,
        "Voie administration": voie_administration,
       # "Dose (facultatif si ordonnance)": "1 tablet",
        "Date de debut": date_debut,
        "Date de fin": date_fin,
        "N°d’ordonnance": no_ordoonnance,
        "Délai d’attente competition (facultatif)": delai_attente_compet,
        "Délai d’attente abattage ou exclusion abattage": delai_attente_kill
     
    }            


    # profesionnel =Profesionnel(code_ape, statut_juridique, denomination)
        with open('Interventions.json', 'r') as json_file:
         data = json.load(json_file)

    # Ajouter le nouveau professionnel à la liste des professionnels
         data["Interventions"].append(nouveau_caract)

    # Réécrire le fichier JSON avec la nouvelle structure
        with open('Interventions.json', 'w') as json_file:
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
    col_titles = ["Date", "Type intervention", "n° Transpondeur", "Traitement","nom médicament" ,"Voie administration,dose (facultatif siordonnance) à conserver 5 ans"," Date de début", "Date de fin ","N°d’ordonnance","Délai d’attentecompétition(facultatif)","Délai d’attente abatage ouexclusion abattage"]  
    fenetre_principale = InterventionsGUI(fenetre, height=3, width=11, col_titles=col_titles)
    fenetre_principale.mainloop()