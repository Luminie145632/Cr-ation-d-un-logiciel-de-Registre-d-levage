import tkinter as tk
from tkinter import messagebox, Frame, Entry, Button, Label, BOTH, END
from PIL import Image, ImageTk
import glob

class FenetrePrincipale(Frame):
    def __init__(self, fenetre, height, width, col_titles):
        super().__init__(fenetre)
        self.numberLines = height
        self.numberColumns = width
        self.col_titles = col_titles
        self.pack(fill=BOTH)
        
        # Ajout de la phrase "Bienvenue sur notre application." au centre
        etiquette_bienvenue = tk.Label(self, text="Bienvenue sur la page Contrôle du Registre d'Élevage.", font=("Helvetica", 16, "bold"))
        etiquette_bienvenue.grid(row=0, columnspan=len(self.col_titles), sticky="ew")

        # Création de la barre de navigation
        navbar = tk.Frame(self, bd=2, relief=tk.GROOVE)
        navbar.grid(row=1 ,  columnspan=len(self.col_titles), sticky="ew")

        # Création des boutons de la barre de navigation
        btn_caracteristiques_lieu = tk.Button(navbar, text="Caractéristiques du Lieu de Détention") 
        btn_caracteristiques_lieu.grid(row=0, column=0 , sticky="ew")

        btn_mouvement_temporaire = tk.Button(navbar, text="Encadrement Zootechnique, Sanitaire et Medical des Animaux") 
        btn_mouvement_temporaire.grid(row=0, column=1, sticky="ew")

        btn_mouvement_temporaire = tk.Button(navbar, text="Présence et Caractéristiques des Animaux") 
        btn_mouvement_temporaire.grid(row=0, column=2, sticky="ew")

        btn_mouvement_temporaire_mvt = tk.Button(navbar, text="Mouvements Temporaire des Animaux") 
        btn_mouvement_temporaire_mvt.grid(row=0, column=3, sticky="ew")

        btn_mouvement_temporaire = tk.Button(navbar, text="Interventions et Soins Courants") 
        btn_mouvement_temporaire.grid(row=0, column=4, sticky="ew")

        btn_mouvement_temporaire = tk.Button(navbar, text="Contrôle du Registre d'élevage") 
        btn_mouvement_temporaire.grid(row=0, column=5, sticky="ew")   

        # Ajout des titres de colonnes
        for j in range(self.numberColumns):
            col_title = Label(self, text=self.col_titles[j], width=20, relief="solid", bg="lightgray", anchor="w")
            col_title.grid(row=2, column=j, sticky='nsew')  

        # Ajout des données du tableau
        self.data = []
        for i in range(3, self.numberLines + 3):
            line = []
            for j in range(self.numberColumns):
                cell = Entry(self, width=20)  
                cell.grid(row=i, column=j, sticky='nsew')  
                line.append(cell)
            self.data.append(line)

        # Configurer la gestion des colonnes pour qu'elles s'adaptent au contenu
        for j in range(self.numberColumns):
            self.grid_columnconfigure(j, weight=1)

        # Bouton pour ajouter une nouvelle ligne
        self.bouton_ajouter_ligne = Button(self, text="Ajouter une ligne", command=self.ajouter_ligne, width=20, height=1)
        self.bouton_ajouter_ligne.grid(row=self.numberLines + 3, columnspan=self.numberColumns, sticky='nsew')

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


    def ajouter_ligne(self):
        # Cacher le bouton
        self.bouton_ajouter_ligne.grid_remove()

        # Ajouter une nouvelle ligne
        nouvelle_ligne = []
        for j in range(self.numberColumns):
            cell = Entry(self, width=20)  
            cell.grid(row=self.numberLines + 4, column=j, sticky='nsew')  
            nouvelle_ligne.append(cell)
        self.data.append(nouvelle_ligne)
        self.numberLines += 1

        # Afficher le bouton à la nouvelle position
        self.bouton_ajouter_ligne.grid(row=self.numberLines + 4, columnspan=self.numberColumns, sticky='nsew')
        

if __name__ == "__main__":
    fenetre = tk.Tk()
    fenetre.title("Page du Contrôle du Registre d'Élevage")
    fenetre.geometry("1920x1080")
    fenetre.iconbitmap("/Creation_dun_logiciel_de_Registre_delevage/images/horse_sans_fond.ico")
    # Liste des titres des colonnes
    col_titles = ["Date", "Organisme de contrôle", "Motif de contrôle", "Nom du contrôleur", "Cachet", "Signature"]

    fenetre_principale = FenetrePrincipale(fenetre, height=3, width=6, col_titles=col_titles)
    fenetre_principale.mainloop()
