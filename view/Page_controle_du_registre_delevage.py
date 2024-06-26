import tkinter as tk
from tkinter import messagebox, Frame, Entry, Button, Label, BOTH, END
import os
import json

class FenetrePrincipale(Frame):
    def __init__(self, fenetre, height, width, col_titles):
        super().__init__(fenetre)
        self.numberLines = height
        self.numberColumns = width
        self.col_titles = col_titles
        self.pack(fill=BOTH)
        
        # Ajout des titres de colonnes
        for j in range(self.numberColumns):
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
        
        self.bouton_ajouter_ligne = Button(self, text="Retour au menu principal", command=self.return_main_menu, width=20, height=1)
        self.bouton_ajouter_ligne.grid(row=self.numberLines + 2, columnspan=self.numberColumns, sticky='nsew')

        self.bouton_ajouter_ligne = Button(self, text="Valider les informations", command=self.valider_informations, width=20, height=1)
        self.bouton_ajouter_ligne.grid(row=self.numberLines + 3, columnspan=self.numberColumns, sticky='nsew')
        
        
        





    def ajouter_ligne(self):
        # Cacher le bouton
        self.bouton_ajouter_ligne.grid_remove()

        # Ajouter une nouvelle ligne
        nouvelle_ligne = []
        for j in range(self.numberColumns):
            cell = Entry(self, width=20)  # Ajustez la largeur selon vos besoins
            cell.grid(row=self.numberLines + 2, column=j, sticky='nsew')  # Utilise sticky pour que la colonne s'adapte
            nouvelle_ligne.append(cell)
        self.data.append(nouvelle_ligne)
        self.numberLines += 1

        # Afficher le bouton à la nouvelle position
        self.bouton_ajouter_ligne.grid(row=self.numberLines + 2, columnspan=self.numberColumns, sticky='nsew')

    def return_main_menu(self):
      self.destroy()
      os.system("python Accueil.py") 
    def valider_informations(self):
     caratheristiques_animaux = []

     for row in self.data:
        caratheristique = {
            "Date": row[0].get(),
            "Organisme": row[1].get(),
            "Motif": row[2].get(),  
            "Nom_controleur": row[3].get(),  
            "Cachet": row[4].get()  
        }
        caratheristiques_animaux.append(caratheristique)

        with open('Controle.json', 'w') as f:
         json.dump(caratheristiques_animaux, f, indent=4)
    # def valider_informations(self):
    #     mouvements_temporaires = []
    #     for row in self.data:
    #         mouvement = {
               
    #         "Date": row[0].get(),
    #         "Organisme": row[1].get(),
    #         "Motif": row[3].get(),
    #         "Nom_controleur":row[4].get(),
    #         "Cachet": row[5].get()

    #         }   
    #         mouvements_temporaires.append(mouvement)

    #     with open('Controle.json', 'w') as f:
    #         _json.dump(mouvements_temporaires, f, indent=4)
                                 
 







if __name__ == "__main__":
    fenetre = tk.Tk()
    fenetre.title("CONTRÔLE DU REGISTRE D’ÉLEVAGE")
    fenetre.geometry("1920x1080")

    try:

     fenetre.iconbitmap("/Creation_dun_logiciel_de_Registre_delevage/images/horse_sans_fond.ico")

    except Exception :
     print("ça ne marche pas ")


    label_principal = Label(fenetre, text="CONTRÔLE DU REGISTRE D’ÉLEVAGE")
    label_principal.pack()

    # Liste des titres des colonnes
    col_titles = ["Date", "Organisme de contrôle", "Motif de contrôle", "Nom du contrôleur", "Cachet", "Signature"]

    fenetre_principale = FenetrePrincipale(fenetre, height=3, width=6, col_titles=col_titles)
    fenetre_principale.mainloop()
