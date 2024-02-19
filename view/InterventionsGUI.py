import tkinter as tk
from tkinter import Frame, Entry, Button, Label, BOTH, Canvas
from PIL import Image, ImageTk
import os
import json

class InterventionsGUI(Frame):
    def __init__(self, fenetre, height, width, col_titles):
        super().__init__(fenetre)
        self.fenetre = fenetre
        self.height = height
        self.width = width
        self.col_titles = col_titles
        self.numberColumns = width
        self.pack(fill=BOTH)

        tex1 = Label(self, text='Présence et Caractéristiques des Animaux')
        tex1.grid(row=0, column=0, columnspan=self.numberColumns, sticky='nsew')

        # Phrase à deux trous
        label_intro = Label(self, text="Liste présence entre le")
        label_intro.grid(row=1, column=0, sticky='w')  # Utilisez 'w' pour aligner à gauche

        self.entry_debut = Entry(self, width=25)
        self.entry_debut.grid(row=1, column=1, sticky='w')  # Utilisez 'w' pour aligner à gauche

        label_et_le = Label(self, text="et le")
        label_et_le.grid(row=1, column=2, sticky='w')  # Utilisez 'w' pour aligner à gauche

        self.entry_fin = Entry(self, width=25)
        self.entry_fin.grid(row=1, column=3, sticky='w')  # Utilisez 'w' pour aligner à gauche

        # Phrase additionnelle
        label_option = Label(self, text="(Option 1 : mouvements peu fréquents)")
        label_option.grid(row=3, column=0, columnspan=self.numberColumns, sticky='nsew')

        # Ajout des titres de colonnes
        for j in range(self.numberColumns):
            col_title = Label(self, text=self.col_titles[j], relief="solid", bg="lightgray", anchor="w")
            col_title.grid(row=4, column=j, sticky='nsew')

        # Ajout des données du tableau
        self.data = []
        for i in range(5, 5 + self.height):
            line = []
            for j in range(self.numberColumns):
                cell = Entry(self)
                cell.grid(row=i, column=j, sticky='nsew')
                line.append(cell)
            self.data.append(line)

        # Configurer la gestion des colonnes pour qu'elles s'adaptent au contenu
        for j in range(self.numberColumns):
            self.grid_columnconfigure(j, weight=1)

        btn_valider = Button(self, text="Valider", command=self.valider_informations)
        btn_valider.grid(row=5 + self.height, column=0, columnspan=self.numberColumns, sticky='nsew')

        btn_mouvement_temporaire = Button(self, text="Retour au menu principal", command=self.return_main_menu)
        btn_mouvement_temporaire.grid(row=6 + self.height, column=0, columnspan=self.numberColumns, sticky='nsew')

        self.can1 = Canvas(self, bg='blue', width=450, height=450)
        self.can1.grid(row=7 + self.height, column=0, columnspan=self.numberColumns, pady=5)



        try:
        # Charger l'image avec PIL
         image = Image.open("/Creation_dun_logiciel_de_Registre_delevage/images/cheval_blanc.png")
        # Augmenter la taille de l'image (dans cet exemple, je l'ai doublée)
         image = image.resize((960, 540), Image.BICUBIC)
        # Convertir l'image en format Tkinter PhotoImage
         self.image = ImageTk.PhotoImage(image)
         self.can1.create_image(0, 0, anchor=tk.NW, image=self.image)

        except Exception:
            print("Ne marche pas")

        # Afficher l'image sur le canvas
       
    def valider_informations(self):
        # Votre logique pour valider les informations
        pass

    def return_main_menu(self):
        self.destroy()
        os.system("python Accueil.py")

if __name__ == "__main__":
    fenetre = tk.Tk()
    fenetre.title("Présence et caractéristiques des animaux")
    fenetre.geometry("1920x1080")
    try:
     fenetre.iconbitmap("/Creation_dun_logiciel_de_Registre_delevage/images/horse_sans_fond.ico")
    except Exception:
     print("enjkezbzkj")
    
    col_titles = ["Date", "Type intervention", "N° Transpondeur", "(Traitement) Nom de Médicament", "(Traitement) Voie d'Administration, dose (facultatif si ordonnance) à conserver 5 ans",
                  "(Traitement) Date de début", "(Traitement) Date de fin ", "N°d’ordonnance", "Délai d’Attente Compétition(facultatif)", "Délai d’attente Abatage ou Exclusion Abattage"]
    fenetre_principale = InterventionsGUI(fenetre, height=3, width=10, col_titles=col_titles)
    fenetre_principale.mainloop()
