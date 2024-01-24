import tkinter as tk
from tkinter import messagebox, Frame, Entry, Button, Label, BOTH, END

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

    def ajouter_ligne(self):
        # Cacher le bouton
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
    fenetre.iconbitmap("horse_sans_fond.ico")

    col_titles = ["Date de sortie", "Nom de l'équidé", "Motif", "Etape éventuelle (adresse)", "Lieu de destination (Adresse)", "Date de retour"]
    
    fenetre_principale = FenetrePrincipale(fenetre, height=3, width=6, col_titles=col_titles)
    fenetre_principale.mainloop()
