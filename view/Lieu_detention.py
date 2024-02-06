import Lieu
import tkinter as tk
from tkinter import messagebox, Frame, Entry, Button, Label, BOTH, END,ttk
import os
import Profesionnel
import Particulier
import Practicien
import json
from PIL import Image, ImageTk
import glob

class FenetrePrincipale(Frame):
    def __init__(self, fenetre, height, width, col_titles):
        super().__init__(fenetre)
        self.numberLines = height
        self.numberColumns = width
        self.col_titles = col_titles
        self.pack(fill=BOTH)
           
        # Titre du tableau
        label_titre_tableau = Label(self, text="Informations concernant le détenteur des équidés")
        label_titre_tableau.grid(row=0, column=0, columnspan=self.numberColumns, sticky='nsew')
        
        # Phrase à deux trous
        label_intro = Label(self, text="Numéro de détenteur (SIRE) :")
        label_intro.grid(row=1, column=0, sticky='nsew')

        self.entry_Sire = Entry(self, width=5)
        self.entry_Sire.grid(row=1, column=1, sticky='nsew')

        label_et_le = Label(self, text="Particulier")
        label_et_le.grid(row=1, column=2, sticky='nsew')

        self.entry_particulier = Entry(self, width=5)
        self.entry_particulier.grid(row=1, column=3, sticky='nsew')

        # Phrase additionnelle
        label_option = Label(self, text="Statut juridique (facultatif) : ")
        label_option.grid(row=2, column=0, columnspan=self.numberColumns, sticky='nsew')
        
        self.entry_statut_juridique = Entry(self, width=5)
        self.entry_statut_juridique.grid(row=2, column=3, sticky='nsew')


        label_option = Label(self, text="Dénomination (facultatif) : ")
        label_option.grid(row=3, column=0, columnspan=self.numberColumns, sticky='nsew')
        
        self.entry_denomination = Entry(self, width=5)
        self.entry_denomination.grid(row=3, column=3, sticky='nsew')

        label_option = Label(self, text="Coordonnées du détenteur (si différente du lieu de stationnement des équidés) :")
        label_option.grid(row=4, column=0, columnspan=self.numberColumns, sticky='nsew')
        
        self.entry_coordonnees = Entry(self, width=8)
        self.entry_coordonnees.grid(row=4, column=6, sticky='nsew')

        label_option = Label(self, text="Adresse :")
        label_option.grid(row=5, column=0, columnspan=self.numberColumns, sticky='nsew')
        
        self.entry_adresse = Entry(self, width=4)
        self.entry_adresse.grid(row=5, column=3, sticky='nsew')

        label_option = Label(self, text="Tél :")
        label_option.grid(row=6, column=0, columnspan=self.numberColumns, sticky='nsew')
        
        self.entry_tel = Entry(self, width=4)
        self.entry_tel.grid(row=6, column=3 , sticky='nsew')

        label_option = Label(self, text=" Portable : ")
        label_option.grid(row=7, column=0, columnspan=self.numberColumns, sticky='nsew')
        
        self.entry_portable = Entry(self, width=4)
        self.entry_portable.grid(row=7, column=  3 , sticky='nsew')
        
        label_option = Label(self, text=" Mail : ")
        label_option.grid(row=7, column=0, columnspan=self.numberColumns, sticky='nsew')
        
        self.entry_mail = Entry(self, width=4)
        self.entry_mail.grid(row=7, column=3, sticky='nsew')


        label_option = Label(self, text=" nom : ")
        label_option.grid(row=8, column=0, columnspan=self.numberColumns, sticky='nsew')
        
        self.entry_nom = Entry(self, width=4)
        self.entry_nom.grid(row=8, column=3, sticky='nsew')

        label_option = Label(self, text=" ape : ")
        label_option.grid(row=9, column=0, columnspan=self.numberColumns, sticky='nsew')
        
        self.entry_code_ape = Entry(self, width=4)
        self.entry_code_ape.grid(row=9, column=3, sticky='nsew')

        btn_valider = Button(self, text="Valider", command=self.valider_informations)
        btn_valider.grid(row=10, column=0, columnspan=self.numberColumns, sticky='nsew')

        # Création des boutons de la barre de navigation
        btn_mouvement_temporaire = Button(self, text="Retour au menu principal", command=  self.return_main_menu )#self.signaler_mouvement_temporaire)
        btn_mouvement_temporaire.grid(row=11, column=0, columnspan=self.numberColumns, sticky='nsew')
        #btn_mouvement_temporaire.pack(side="left", expand=True, fill='both')
        # Ajout des titres de colonnes
        # for j in range(self.numberColumns):
        #     col_title = Label(self, text=self.col_titles[j], width=15, relief="solid", bg="lightgray", anchor="w")
        #     col_title.grid(row=3, column=j, sticky='nsew')  # Utilise sticky pour que la colonne s'adapte

        # # Ajout des données du tableau
        # self.data = []
        # for i in range(4, self.numberLines + 4):
        #     line = []
        #     for j in range(self.numberColumns):
        #         cell = Entry(self, width=15)  # Ajustez la largeur selon vos besoins
        #         cell.grid(row=i, column=j, sticky='nsew')  # Utilise sticky pour que la colonne s'adapte
        #         line.append(cell)
        #     self.data.append(line)

        # # Configurer la gestion des colonnes pour qu'elles s'adaptent au contenu
        # for j in range(self.numberColumns):
        #     self.grid_columnconfigure(j, weight=1)

        # # Bouton pour ajouter une nouvelle ligne
        # self.bouton_ajouter_ligne = Button(self, text="Ajouter une ligne", command=self.ajouter_ligne, width=15, height=1)
        # self.bouton_ajouter_ligne.grid(row=self.numberLines + 4, columnspan=self.numberColumns, sticky='nsew')
  
    def valider_informations(self):
    # Récupérer les informations depuis les champs d'entrée (à adapter en fonction de votre logique)
     numero_detenteur = self.entry_Sire.get()
     statut_juridique = self.entry_statut_juridique.get()
     denomination = self.entry_denomination.get()
     adresse_coordonnees = self.entry_coordonnees.get()
     adresse = self.entry_adresse.get()
     tel = self.entry_tel.get()
     portable = self.entry_portable.get()
     mail = self.entry_mail.get()
     nom=self.entry_nom.get()
    # prenom=self.entry_prenom.get()
   #  num_siret=self.entry_num_siret.get()
     code_ape=self.entry_code_ape.get()
     
     nouveau_professionnel = {
     #   "num_siret": "321546",
        "code_ape": code_ape,
        "statut_juridique": statut_juridique,
        "denomination": denomination
    }


    # profesionnel =Profesionnel(code_ape, statut_juridique, denomination)
     with open('Profesionnel.json', 'r') as json_file:
      data = json.load(json_file)

    # Ajouter le nouveau professionnel à la liste des professionnels
      data["Professionnel"].append(nouveau_professionnel)

    # Réécrire le fichier JSON avec la nouvelle structure
     with open('Profesionnel.json', 'w') as json_file:
        json.dump(data, json_file, indent=2)

    # Retourner le JSON du nouveau professionnel (à des fins de débogage ou autre)
     return json.dumps(nouveau_professionnel)
    
    
    
    
    
    
    
    #  return json.dumps({
         
        
    #       "code_ape":code_ape, 
    #       "statut_juridique":statut_juridique, 
    #       "denomination":denomination,
         
    #       })


     
    def return_main_menu(self):
        self.destroy()
        os.system("python Accueil.py")
     
    def animal_to_json(profesionnel):
        if isinstance(profesionnel, Profesionnel):
         return json.dumps({"nom": profesionnel.nom, "prenom": profesionnel.prenom, "adresse": profesionnel.adresse , "tel": profesionnel.tel,"Siret":profesionnel.siret,"code_Ape":profesionnel.code_ape,"statut_juridique":profesionnel.statut_juridique,"denomination":profesionnel.denomination})
        #profesionnel =Profesionnel(nom,prenom,adresse,tel ,self, num_siret, code_ape, statut_juridique, denomination)
                                               

    def ajouter_ligne(self):
        # Cacher le bouton"
        self.bouton_ajouter_ligne.grid_remove()

        # Ajouter une nouvelle ligne
        nouvelle_ligne = []
        for j in range(self.numberColumns):
            cell = Entry(self, width=15)  # Ajustez la largeur selon vos besoins
            cell.grid(row=self.numberLines + 5, column=j, sticky='nsew')  # Utilise sticky pour que la colonne s'adapte
            nouvelle_ligne.append(cell)
        self.data.append(nouvelle_ligne)
        self.numberLines += 1

        # Afficher le bouton à la nouvelle position
        self.bouton_ajouter_ligne.grid(row=self.numberLines + 5, columnspan=self.numberColumns, sticky='nsew')

if __name__ == "__main__":
    fenetre = tk.Tk()
    fenetre.title("MOUVEMENTS TEMPORAIRES DES ANIMAUX")
    fenetre.geometry("1920x1080")
    fenetre.iconbitmap("/Creation_dun_logiciel_de_Registre_delevage/images/horse_sans_fond.ico")

    col_titles = ["Date de sortie", "Nom de l'équidé", "Motif", "Etape éventuelle (adresse)", "Lieu de destination (Adresse)", "Date de retour"]
    
    fenetre_principale = FenetrePrincipale(fenetre, height=3, width=6, col_titles=col_titles)
    fenetre_principale.mainloop()


class LieuDetention(Lieu):
    def __init__(self, adresse, nom_rue_ville, code_postal, domaine_activite, types_activites):
        super().__init__(adresse, nom_rue_ville, code_postal, domaine_activite)
        self.types_activites = types_activites

    def gtypes_activites(self):
        return self.types_activites

    def stypes_activites(self, ntypes_activites):
        self.types_activites = ntypes_activites


# Exemple d'utilisation
ld = LieuDetention('5 rue de la prison', 'rue de la prison', '12345', 'Correctionnel', 'Prison')
print(ld.gcode_postal())  # Affiche le code postal initial
ld.scode_postal('54321')   # Change le code postal
print(ld.gcode_postal())  # Affiche le nouveau code postal
print(ld.gtypes_activites())  # Affiche le type d'activités initial
ld.stypes_activites('Centre de détention')  # Change le type d'activités
print(ld.gtypes_activites())  # Affiche le nouveau type d'activités