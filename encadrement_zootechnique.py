from tkinter import *
from PIL import Image, ImageTk

class EncadrementZootechnique(Frame):
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

        # Configurer la gestion des colonnes pour qu'elles s'adaptent au contenu
        for j in range(self.numberColumns):
            self.grid_columnconfigure(j, weight=1)

        # Bouton pour ajouter une nouvelle ligne
        self.bouton_ajouter_ligne = Button(self, text="Ajouter une ligne", command=self.ajouter_ligne, width=20, height=1)
        self.bouton_ajouter_ligne.grid(row=self.numberLines + 1, columnspan=self.numberColumns, sticky='nsew')

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
        self.can1.create_image(0, 0, anchor=NW, image=self.image)

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
    fenetre.title("Encadrement Zootechnique")
    fenetre.geometry("1920x1080")# Définir la taille initiale de la fenêtre
    fenetre.iconbitmap("/Creation_dun_logiciel_de_Registre_delevage/images/horse_sans_fond.ico")
    fenetre.resizable(height=False, width=False)

    label_principal = Label(fenetre, text="")
    label_principal.pack()

    # Liste des titres des colonnes
    col_titles = ["Date", "Organisme de contrôle", "Motif de contrôle", "Nom du contrôleur", "Cachet", "Signature"]

    fenetre_principale = EncadrementZootechnique(fenetre, height=3, width=6, col_titles=col_titles)
    fenetre_principale.mainloop()
# import tkinter as tk
# import os
# from tkinter import*
# from PIL import Image, ImageTk
# from tkinter import messagebox, Frame, Entry, Button, Label, BOTH, END,Canvas

# tableau_entries = []  # Liste pour stocker les zones de texte
# class EncadrementZootechnique(Frame):
#     def __init__(self, fenetre, height, width, col_titles):
#         super().__init__(fenetre)
#         self.numberLines = height
#         self.numberColumns = width
#         self.col_titles = col_titles
#         self.pack(fill=BOTH)



        

#         tex1 = Label(self, text='Encadrement Zootechnique Sanitaire et Meidcal des Animaux', fg='cyan')
#         tex1.grid(row=0, column=0, columnspan=8)  # Ajout de columnspan pour couvrir toutes les colonnes

#         can1 = Canvas(self, bg='blue', width=450, height=450)
#         can1.grid(row=2, column=0, columnspan=8, pady=5)  # Ajout de columnspan pour couvrir toutes les colonnes


#         image = Image.open("cheval_blanc.png")
# # Augmenter la taille de l'image (dans cet exemple, je l'ai doublée)
#         image = image.resize((960,540), Image.BICUBIC)
# # Convertir l'image en format Tkinter PhotoImage
#         image = ImageTk.PhotoImage(image)

# # Afficher l'image sur le canvas
#         can1.create_image(0, 0, anchor=NW, image=image)

        

#         #Frame mainloop


#         # Ajout des titres de colonnes
#         for j in range(self.numberColumns):
#             col_title = Label(self, text=self.col_titles[j], width=20, relief="solid", bg="lightgray", anchor="w")
#             col_title.grid(row=0, column=j, sticky='nsew')  # Utilise sticky pour que la colonne s'adapte

#         # Ajout des données du tableau
#         self.data = []
#         for i in range(1, self.numberLines + 1):
#             line = []
#             for j in range(self.numberColumns):
#                 cell = Entry(self, width=20)  # Ajustez la largeur selon vos besoins
#                 cell.grid(row=i, column=j, sticky='nsew')  # Utilise sticky pour que la colonne s'adapte
#                 line.append(cell)
#             self.data.append(line)

#         # Configurer la gestion des colonnes pour qu'elles s'adaptent au contenu
#         for j in range(self.numberColumns):
#             self.grid_columnconfigure(j, weight=1)

#         # Bouton pour ajouter une nouvelle ligne
#         self.bouton_ajouter_ligne = Button(self, text="Ajouter une ligne", command=self.ajouter_ligne, width=20, height=1)
#         self.bouton_ajouter_ligne.grid(row=self.numberLines + 1, columnspan=self.numberColumns, sticky='nsew')

#     def ajouter_ligne(self):
#         # Cacher le bouton
#         self.bouton_ajouter_ligne.grid_remove()

#         # Ajouter une nouvelle ligne
#         nouvelle_ligne = []
#         for j in range(self.numberColumns):
#             cell = Entry(self, width=20)  # Ajustez la largeur selon vos besoins
#             cell.grid(row=self.numberLines + 2, column=j, sticky='nsew')  # Utilise sticky pour que la colonne s'adapte
#             nouvelle_ligne.append(cell)
#         self.data.append(nouvelle_ligne)
#         self.numberLines += 1

#         # Afficher le bouton à la nouvelle position
#         self.bouton_ajouter_ligne.grid(row=self.numberLines + 2, columnspan=self.numberColumns, sticky='nsew')

    
# if __name__ == "__main__":
#     fenetre = tk.Tk()
#     fenetre.title("")
#     fenetre.geometry("960x540")
#     fenetre.iconbitmap("horse_sans_fond.ico")
#     fenetre.resizable(height=False, width=False)

#     label_principal = Label(fenetre, text="")
#     label_principal.pack()

#     # Liste des titres des colonnes
#     col_titles = ["Date", "Organisme de contrôle", "Motif de contrôle", "Nom du contrôleur", "Cachet", "Signature"]

#     fenetre_principale = EncadrementZootechnique(fenetre, height=3, width=6, col_titles=col_titles)
#     fenetre_principale.mainloop()

# #     bou1 = Button(fenetre, text='Modifier', command=fenetre.destroy)
# # bou1.grid(row=len(fenetre) + 3, column=0, columnspan=8, pady=5, sticky="nsew")  

# #



# # # Créer des labels à gauche de chaque ligne
# # labels_lignes = ['Espèce et type de production', 'Lieu habituel et durée de détention', 'Nom/Coordonnées du vétérinaire traitant', '...']
# # for i, texte in enumerate(labels_lignes):
# #     label_ligne = Label(fen1, text=texte, borderwidth=1, relief="solid", width=20, height=2)
# #     label_ligne.grid(row=i+3, column=0, padx=2, pady=2, sticky="e")

# # # Créer des labels en haut de chaque colonne
# # labels_colonnes = ['...', '...', '...', '...', '...', '...', '...', '...']
# # for j, texte in enumerate(labels_colonnes):
# #     label_colonne = Label(fen1, text=texte, borderwidth=1, relief="solid", width=8, height=2)
# #     label_colonne.grid(row=2, column=j+1, padx=2, pady=2, sticky="n")





# # for i, ligne in enumerate(tableau):
# #     ligne_entries = []  # Liste pour stocker les zones de texte de chaque ligne
# #     for j, valeur in enumerate(ligne):
# #         entry = Entry(Frame, width=8, borderwidth=1, relief="solid")
# #         entry.grid(row=i+3, column=j, padx=2, pady=2)  # Ajustement de la ligne (i+3 au lieu de i)
# #         ligne_entries.append(entry)
# #     tableau_entries.append(ligne_entries)

# # Placer le bouton "Modifier" sous le tableau






# # from tkinter import *
# # from PIL import Image, ImageTk

# # class encadrement_zootechnique():
# #     def __init__(self, horse_data):
# #         pass       

# # fen1 = Tk()

# # tex1 = Label(fen1, text='Encadrement Zootechnique !', fg='cyan')
# # tex1.grid(row=0, column=0, columnspan=8)  # Ajout de columnspan pour couvrir toutes les colonnes

# # can1 = Canvas(fen1, bg='blue', width=450, height=450)
# # can1.grid(row=2, column=0, columnspan=8, pady=5)  # Ajout de columnspan pour couvrir toutes les colonnes

# # # Créer un tableau 4x8 avec des valeurs spécifiques
# # tableau = [
# #     ['...', '...', '...', '...', '...', '...', '...'],
# #     ['...', '...', '...', '...', '...', '...', '...'],
# #     ['...', '...',  '...', '...', '...','...', '...'],
# #     ['...', '...',  '...', '...', '...','...', '...']
# # ]

# # tab2 = [
# #     ['', '', '...', '...', '...', '...', '...', '...'],
    
# # ]


# # tableau_entries = []  # Liste pour stocker les zones de texte


# # for j, ligne in enumerate(tab2):
# #         label = Label(fen1, text=str(valeur), borderwidth=1, relief="solid", width=5, height=2)

# # for i, ligne in enumerate(tableau):
# #     ligne_entries = []  # Liste pour stocker les zones de texte de chaque ligne
# #     for j, valeur in enumerate(ligne):
# #        if i==3 ||


# #         entry = Entry(fen1, width=8, borderwidth=1, relief="solid")
# #         entry.grid(row=i+3, column=j, padx=2, pady=2)  # Ajustement de la ligne (i+3 au lieu de i)
# #         ligne_entries.append(entry)
# #     tableau_entries.append(ligne_entries)

# # # Placer le bouton "Modifier" sous le tableau
# # bou1 = Button(fen1, text='Modifier', command=fen1.destroy)
# # bou1.grid(row=len(tableau) + 3, column=0, columnspan=8, pady=5, sticky="nsew")  

# # # Charger l'image avec PIL
# # image = Image.open("cheval_blanc.png")
# # # Augmenter la taille de l'image (dans cet exemple, je l'ai doublée)
# # image = image.resize((900, 900),  Image.BICUBIC)
# # # Convertir l'image en format Tkinter PhotoImage
# # image = ImageTk.PhotoImage(image)

# # # Afficher l'image sur le canvas
# # can1.create_image(0, 0, anchor=NW, image=image)

# # fen1.resizable(height=False, width=False)

# # fen1.mainloop()

