import tkinter as tk
from tkinter import Button

class MyApp(tk.Tk):
    def __init__(self, width, col_titles, height):
        super().__init__()

        self.numberColumns = width 
        self.numberLines = height
        self.col_title = col_titles
        self.data = []  

        self.title("Accueil")
        self.geometry("1920x1080")  # Ajustez la taille de la fenêtre principale si nécessaire

        try:
            self.iconbitmap("/Creation_dun_logiciel_de_Registre_delevage/images/horse_sans_fond.ico")
        except Exception:
            print("photo de cheval")

        self.navbar_canvas = tk.Canvas(self, bd=2, relief=tk.GROOVE, width=1800, height=800)  # Ajustez la taille du canevas ici
        self.navbar_canvas.grid(row=10, columnspan=len(self.col_title), sticky="ew")

        self.scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=self.navbar_canvas.yview)
        self.scrollbar.grid(row=10, column=len(self.col_title) + 5, sticky="ns")
        self.navbar_canvas.config(yscrollcommand=self.scrollbar.set)

        self.navbar_frame = tk.Frame(self.navbar_canvas, width=1800, height=800)  # Ajustez la taille du cadre ici
        self.navbar_canvas.create_window((0, 0), window=self.navbar_frame, anchor='nw')

        self.create_navigation_panel()
        self.bind("<Configure>", self.redimensionner_canevas)

        # Création des boutons de la barre de navigation
        btn_caracteristiques_lieu = tk.Button(self, text="Caractéristiques", command=lambda: self.ouvrir_caracteristiques_lieu_detention())
        btn_caracteristiques_lieu.grid(row=0, column=1, sticky="ew")

        btn_encadrement = tk.Button(self, text="Encadrement", command=lambda: self.open_encadrement_zootechnique())
        btn_encadrement.grid(row=0, column=2, sticky="ew")

        btn_mouvement_temporaire = tk.Button(self, text="Présence", command=lambda: self.ouvrir_caractheristiques_animaux())
        btn_mouvement_temporaire.grid(row=0, column=3, sticky="ew")

        btn_mouvement_temporaire_mvt = tk.Button(self, text="Mouvements Temporaire des Animaux", command=lambda: self.ouvrir_mouvement_temporaires(width, height))
        btn_mouvement_temporaire_mvt.grid(row=0, column=4, sticky="ew")

        btn_mouvement_temporaire = tk.Button(self, text="Interventions et Soins Courants", command=lambda: self.ouvrir_interventions())
        btn_mouvement_temporaire.grid(row=0, column=5, sticky="ew")

        btn_mouvement_temporaire = tk.Button(self, text="Contrôle du Registre d'élevage", command=lambda: self.ouvrir_controle_registre_elevage())
        btn_mouvement_temporaire.grid(row=0, column=6, sticky="ew")

        # Création du Label pour afficher les images
        self.label_image = tk.Label(self, bd=0, highlightthickness=0)
        self.label_image.grid(row=0, column=7, sticky="ew")

        # Texte additionnel
        texte_instruction = "Pour générer le document PDF qui va regrouper toutes les informations que vous avez entré dans les différentes parties de l'application."
        etiquette_instruction = tk.Label(self, text=texte_instruction, font=("Helvetica", 12))
        etiquette_instruction.grid(row=19, column=0, columnspan=self.numberColumns, sticky="nsew")

        # Texte additionnel 2
        texte_instruction2 = "Veuillez cliquer sur le bouton suivant :"
        etiquette_instruction2 = tk.Label(self, text=texte_instruction2, font=("Helvetica", 12))
        etiquette_instruction2.grid(row=20, column=0, columnspan=self.numberColumns, sticky="nsew")

        # Bouton pour générer le document PDF
        btn_generer_pdf = tk.Button(self, text="Générer le document PDF", command=lambda: self.ajouter_texte_pdf('C:\\Cr-ation-d-un-logiciel-de-Registre-d-levage\\view\\nouilles.pdf', 4))
        btn_generer_pdf.place(relx=0.375, rely=0.55, anchor="center")

        try:
            self.setup_background_animation()
        except Exception:
            print("Marche pas photo de fond")

        self.create_navigation_panel()
        self.bind("<Configure>", self.redimensionner_canevas)

    def create_navigation_panel(self):
        # Méthode pour créer le panneau de navigation
        pass

    def redimensionner_canevas(self, event):
        # Redimensionner le canevas lorsque la taille de la fenêtre change
        self.navbar_canvas.config(scrollregion=self.navbar_canvas.bbox("all"))

    def ouvrir_caracteristiques_lieu_detention(self):
        # Méthode pour ouvrir les caractéristiques du lieu de détention
        pass

    def open_encadrement_zootechnique(self):
        self.data = []
        print("flag netoyage data")
        self.navbar_frame = tk.Frame(self.navbar_canvas, width=1800, height=800)  # Ajustez la taille du cadre ici
        self.col_title = ["Lieu Habituel et coordonee de detention", "Nom et coordonees veterianire traitant", "Nom et coordonnees du veterinaire sanitaire", "Nom et coordonnees du referent bien-etre animal", "Nom adresse tel des Organismes sanitaires reconnus", "Nom, adresse tel marechal ferrand", "Nom, adresse et N de telephone du dentiste"]
        self.navbar_canvas.create_window((0, 0), window=self.navbar_frame, height=800, width=1800, anchor='nw')

        for j in range(len(self.col_title)):
            col_tmp = self.col_title[j]
            col_title = tk.Label(self.navbar_frame, text=col_tmp, width=250, relief="solid", bg="lightgray", anchor="w")
            col_title.grid(row=10, column=j, sticky='nsew')

        for i in range(15):
            row_data = []
            for j in range(len(self.col_title)):
                cell = tk.Entry(self.navbar_frame, width=15)
                cell.grid(row=i + 14, column=j, sticky='nsew')
                row_data.append(cell)
            self.data.append(row_data)

        for j in range(len(self.col_title)):
            self.navbar_frame.grid_columnconfigure(j, weight=1)

        self.navbar_frame.bouton_ajouter_ligne = Button(self, text="Ajouter une ligne", command=self.ajouter_ligne)
        self.navbar_frame.bouton_ajouter_ligne.grid(row=self.numberLines + 4, column=0, columnspan=len(self.col_title), sticky='nsew')

        btn_valider = tk.Button(self, text="Valider", command=self.valider_encadrement_Zootechnique_animaux)
        btn_valider.grid(row=self.numberLines + 5, column=0, columnspan=len(self.col_title), sticky='nsew')

        btn_valider = tk.Button(self, text="encadrement zootechnique", command=lambda: EncadrementZootechnique.view_zootechnical_supervision(self))
        btn_valider.grid(row=self.numberLines + 6, column=0, columnspan=len(self.col_title), sticky='nsew')

        self.bind("<Configure>", self.redimensionner_canevas)

    def ajouter_texte_pdf(self, path, page_num):
        # Méthode pour ajouter du texte à un PDF
        pass

    def ouvrir_mouvement_temporaires(self, width, height):
        # Méthode pour ouvrir les mouvements temporaires
        pass

    def ouvrir_interventions(self):
        # Méthode pour ouvrir les interventions
        pass

    def ouvrir_controle_registre_elevage(self):
        # Méthode pour ouvrir le contrôle du registre d'élevage
        pass

    def valider_encadrement_Zootechnique_animaux(self):
        # Méthode pour valider l'encadrement zootechnique des animaux
        pass

    def setup_background_animation(self):
        # Méthode pour configurer l'animation de fond
        pass


if __name__ == "__main__":
    app = MyApp(width=10, col_titles=["Titre1", "Titre2", "Titre3"], height=10)
    app.mainloop()