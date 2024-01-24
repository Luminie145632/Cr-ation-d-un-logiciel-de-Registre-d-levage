import tkinter as tk
from tkinter import messagebox, Frame, Entry, Button, Label, BOTH, END

class FenetrePrincipale(Frame):
    def __init__(self, fenetre, height, width):
        super().__init__(fenetre)
        self.numberLines = height
        self.numberColumns = width
        self.pack(fill=BOTH)

        # Ajout de la première ligne avec "Année" et "Mois"
        label_annee = Label(self, text="Année", width=10, relief="solid", bg="lightgray")
        label_annee.grid(row=0, column=0, sticky='nsew')

        label_mois = Label(self, text="Mois", width=5, relief="solid", bg="lightgray")
        label_mois.grid(row=0, column=1, columnspan=31, sticky='nsew')

        # Ajout de la deuxième ligne avec "Nom du cheval" et les nombres de 1 à 31
        label_nom_cheval = Label(self, text="Nom du cheval", width=10, relief="solid", bg="lightgray")
        label_nom_cheval.grid(row=1, column=0, sticky='nsew')

        for i in range(1, self.numberColumns):
            label_jour = Label(self, text=str(i), width=5, relief="solid", bg="lightgray")
            label_jour.grid(row=1, column=i, sticky='nsew')

        # Ajout des données du tableau pour le reste
        for i in range(2, self.numberLines - 2):  # Modification ici pour exclure les deux dernières lignes
            entry_nom_cheval = Entry(self, width=10)
            entry_nom_cheval.grid(row=i, column=0, sticky='nsew')

            for j in range(1, self.numberColumns):
                cell = Entry(self, width=5)
                cell.grid(row=i, column=j, sticky='nsew')

        # Ajout de "1/" à "10/" dans la première colonne sous la case "Nom du cheval"
        for i in range(1, 11):
            label_num = Label(self, text=f"{i}/", width=5, relief="solid", bg="lightgray")
            label_num.grid(row=i + 1, column=0, sticky='nsew')

        # Espace vide entre le tableau et la légende
        label_espace_vide = Label(self, text="", width=5)
        label_espace_vide.grid(row=self.numberLines - 2, column=0, columnspan=self.numberColumns, sticky='nsew')

        # Ajout du titre à la légende
        label_legend_titre = Label(self, text="Légende (pour chaque sortie, noter l’adresse du lieu de destination)",
                                   width=10, relief="solid", bg="lightgray")
        label_legend_titre.grid(row=self.numberLines - 1, column=0, columnspan=self.numberColumns, sticky='nsew')

        # Ajout de la légende
        entries_legend = []
        for i in range(1, 13):  # Ajustez selon le nombre d'éléments dans la légende
            label_num = Label(self, text=f"{i}.", width=5, relief="solid", bg="lightgray")
            label_num.grid(row=self.numberLines - 1 + (i - 1) // 4, column=((i - 1) % 4) * 8, sticky='nsew')

            entry_legend = Entry(self, width=10)  # Ajustez la largeur selon vos besoins
            entry_legend.grid(row=self.numberLines - 1 + (i - 1) // 4, column=((i - 1) % 4) * 8 + 1, columnspan=7, sticky='nsew')
            entries_legend.append(entry_legend)

        # Configuration pour permettre l'adaptation dynamique des lignes et des colonnes
        for i in range(self.numberLines):
            self.grid_rowconfigure(i, weight=1)

        for j in range(self.numberColumns):
            self.grid_columnconfigure(j, weight=1)

if __name__ == "__main__":
    fenetre = tk.Tk()
    fenetre.title("Tableau des Mouvements Temporaires des Chevaux")

    fenetre_principale = FenetrePrincipale(fenetre, height=14, width=32)  # Ajustez la hauteur selon le nombre de lignes nécessaires
    fenetre_principale.mainloop()
