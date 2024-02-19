import tkinter as tk
from tkinter import messagebox, Frame, Entry, Button, Label, BOTH
from PIL import Image, ImageTk
import glob
import os


class FenetrePrincipale(Frame):
    def __init__(self, fenetre, height, width, col_titles):
        super().__init__(fenetre)
        self.numberLines = height
        self.numberColumns = width
        self.col_titles = col_titles
        self.pack(fill=BOTH)
        
        # Titre du tableau
        label_titre_tableau = Label(self, text="MOUVEMENTS TEMPORAIRES DES ANIMAUX")
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

        # Création du Label pour afficher les images
        self.label_image = tk.Label(self, bd=0, highlightthickness=0)
        self.label_image.grid(row=self.numberLines + 5, column=0, columnspan=self.numberColumns, sticky='nsew')
        

        btn_mouvement_temporaire = Button(self, text="Retour au menu principal", command=  self.return_main_menu )#self.signaler_mouvement_temporaire)
        btn_mouvement_temporaire.grid(row=self.numberLines + 5, column=self.numberColumns, columnspan=self.numberColumns, sticky='nsew')
        # Appel à la méthode pour gérer le fond d'image changeant
        self.setup_background_animation()

        # Gestionnaire d'événements pour détecter les changements de taille de fenêtre
        self.bind("<Configure>", self.redimensionner_image)

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
        self.label_image.grid(row=self.numberLines + 7, column=0, columnspan=self.numberColumns, sticky='nsew')

    def setup_background_animation(self):
       
       try:
        self.image_paths = glob.glob("/Creation_dun_logiciel_de_Registre_delevage/images/*.png")  # Mettez le chemin correct vers vos images
        self.current_image_index = 0
        self.load_image()
       except:
           print(" ça marche pas ")

    def return_main_menu(self):
     self.destroy()
     os.system("python Accueil.py")


    def load_image(self):
        # Charger l'image actuelle
        image_path = self.image_paths[self.current_image_index]
        image = Image.open(image_path)

        # Redimensionner l'image pour prendre toute la fenêtre
        image = image.resize((self.winfo_width(), self.winfo_height()))

        photo = ImageTk.PhotoImage(image)

        # Mettre à jour l'image dans le label
        self.label_image.configure(image=photo)
        self.label_image.image = photo  # Gardez une référence pour éviter la collecte des déchets

        # Mettre à jour l'index pour la prochaine image
        self.current_image_index = (self.current_image_index + 1) % len(self.image_paths)

        # Planifier l'appel de la fonction load_image après un certain délai (par exemple, 2000 millisecondes)
        self.after(2000, self.load_image)

    def redimensionner_image(self, event):
        # Redimensionner l'image pour prendre toute la fenêtre
        image_path = self.image_paths[self.current_image_index]
        image = Image.open(image_path)
        image = image.resize((self.winfo_width(), self.winfo_height()))

        photo = ImageTk.PhotoImage(image)

        # Mettre à jour l'image dans le label
        self.label_image.configure(image=photo)
        self.label_image.image = photo  # Gardez une référence pour éviter la collecte des déchets


if __name__ == "__main__":
    fenetre = tk.Tk()
    fenetre.title("MOUVEMENTS TEMPORAIRES DES ANIMAUX")
    fenetre.geometry("1920x1080")
    fenetre.iconbitmap("horse_sans_fond.ico")

    col_titles = ["Date de sortie", "Nom de l'équidé", "Motif", "Etape éventuelle (adresse)", "Lieu de destination (Adresse)", "Date de retour"]
    
    fenetre_principale = FenetrePrincipale(fenetre, height=3, width=6, col_titles=col_titles)
    fenetre_principale.mainloop()
