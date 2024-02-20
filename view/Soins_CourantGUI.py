from tkinter import *
from PIL import Image, ImageTk
import os
import  json

class Soins_cournat(Frame):
    def __init__(self, fenetre, height, width, col_titles):
        super().__init__(fenetre)
        self.numberLines = height
        self.numberColumns = width
        self.col_titles = col_titles
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
        



        # self.data = []
        # for i in range(1, self.numberLines + 1):
        #     line = []
        #     for j in range(self.numberColumns):
        #         cell = Entry(self, width=20)
        #         cell.grid(row=i, column=j, sticky='nsew')
        #         line.append(cell)
        #     self.data.append(line)
                                                                                             
        # Configurer la gestion des colonnes pour qu'elles s'adaptent au contenu
        for j in range(self.numberColumns):
            self.grid_columnconfigure(j, weight=1)

        # Bouton pour ajouter une nouvelle ligne
        self.bouton_ajouter_ligne = Button(self, text="Ajouter une ligne", command=self.ajouter_ligne, width=20, height=1)
        self.bouton_ajouter_ligne.grid(row=self.numberLines + 1, columnspan=self.numberColumns, sticky='nsew')

        btn_mouvement_temporaire = Button(self, text="Retour au menu principal", command=  self.return_main_menu, width=20, height=1 )#self.signaler_mouvement_temporaire)
        btn_mouvement_temporaire.grid(row=self.numberLines + 2,  columnspan=self.numberColumns, sticky='nsew')

        btn_mouvement_temporaire = Button(self, text="Valider", command=  self.valider_informations, width=20, height=1 )#self.signaler_mouvement_temporaire)
        btn_mouvement_temporaire.grid(row=self.numberLines + 3,  columnspan=self.numberColumns, sticky='nsew')


        btn_valider = Button(self, text="Consulter l'historitque de mes Soins", command=self.view_animals)
        btn_valider.grid(row=4, column=0, columnspan=self.numberColumns, sticky='nsew')
        
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
            print("l'imaghe ne marche pas ") 
    
    def view_animals(self):
    
     with open('Soins_Courant.json', 'r') as file:
        data = json.load(file)
        
    # Création d'un champ de texte pour afficher les informations
     text_field = Text(self, wrap=WORD)
     text_field.grid(row=13, column=0, columnspan=self.numberColumns, sticky='nsew')
     text_field2 = Text(self, wrap=WORD)
     text_field2.grid(row=14, column=0, columnspan=self.numberColumns, sticky='nsew')
    # Récupération des informations et ajout dans le champ de texte
     for animal in data:
        text_field.insert(END, f"Date: {animal.get('Date','')}\n")
        text_field.insert(END, f"Numéro SIRE: {animal.get('type_intervention', '')}\n")
        text_field.insert(END, f"Nom du medicament: {animal.get('Nom du medicament', '')}\n")
       # text_field.insert(END, f"Nom et coordonnées du propriétaire: {animal.get('Nom et coordonnees du proprietaire')}\n")
        text_field.insert(END, f"Voie administration: {animal.get('Voie administration', '')}\n")
        text_field2.insert(END, f"Date dedebut: {animal.get('Date dedebut', '')}\n")
        text_field2.insert(END, f"Date dedefin: {animal.get('Date dedefin', '')}\n")
        text_field2.insert(END, f"N_ordonnance: {animal.get('N_ordonnance', '')}\n\n")
        text_field2.insert(END, f": {animal.get('Delai_attente_competition', '')}\n\n")
        text_field2.insert(END, f"Delai_attente_abattage: {animal.get('Delai_attente_abattage', '')}\n\n")
        
       


    def return_main_menu(self):
    
     self.destroy()
     os.system("python Accueil.py")
    


    def valider_informations(self):
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

    def ajouter_ligne(self):
        # Cacher le bouton
        self.bouton_ajouter_ligne.grid_remove()

        # Ajouter une nouvelle ligne
        nouvelle_ligne = []
        for j in range(self.numberColumns):
            cell = Entry(self, width=20)
            cell.grid(row=self.numberLines + 2, column=j, sticky='nsew')
            nouvelle_ligne.append(cell)
        self.data.append(nouvelle_ligne)
        self.numberLines += 1

        # Afficher le bouton à la nouvelle position
        self.bouton_ajouter_ligne.grid(row=self.numberLines + 2, columnspan=self.numberColumns, sticky='nsew')
    
if __name__ == "__main__":
    
    fenetre = Tk()
    fenetre.title("")
    fenetre.geometry("1920x1080")
    
    try:
    
     fenetre.iconbitmap("/Creation_dun_logiciel_de_Registre_delevage/images/horse_sans_fond.ico")
     fenetre.resizable(height=True, width=True)
    
    except Exception:
     
     label_principal = Label(fenetre, text="Intervention et soins courant")
    
    label_principal.pack()

    # Liste des titres des colonnes
    col_titles = ["Date", "Type d'intervention", "Intervenant (si vétérianire)", "Traitement", "N ordonnance","Date de début", "Date de fin","N°d’ordonnance","Délai d’attentecompétition(facultatif)","Délai d’attente abatage ou exclusion abattage"]

    fenetre_principale = Soins_cournat(fenetre, height=6, width=10, col_titles=col_titles)
    fenetre_principale.mainloop()