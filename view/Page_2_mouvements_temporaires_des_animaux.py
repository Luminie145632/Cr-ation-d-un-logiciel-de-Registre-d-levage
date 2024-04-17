import tkinter as tk
from tkinter import Frame, Entry, Label, BOTH, Scrollbar, Canvas
from PIL import Image, ImageTk
import glob
from itertools import cycle

class FenetrePrincipale(Frame):
    def __init__(self, fenetre, height, width):
        super().__init__(fenetre)
        self.numberLines = height
        self.numberColumns = width
        self.pack(fill=BOTH, expand=True)

        # Ajout de la barre de défilement verticale
        scrollbar_y = Scrollbar(self, orient="vertical")
        scrollbar_y.pack(side="right", fill="y")

        # Création d'une toile (Canvas) pour contenir le cadre et la barre de défilement
        canvas = Canvas(self, yscrollcommand=scrollbar_y.set)
        canvas.pack(side="left", fill="both", expand=True)

        # Configurer la barre de défilement pour suivre les changements sur la toile
        scrollbar_y.config(command=canvas.yview)

        # Ajout du cadre à la toile
        self.cadre = Frame(canvas)
        canvas.create_window((0, 0), window=self.cadre, anchor="nw")

        # Configuration pour permettre l'adaptation dynamique des lignes et des colonnes
        for i in range(self.numberLines):
            self.cadre.grid_rowconfigure(i, weight=1)

        for j in range(self.numberColumns):
            self.cadre.grid_columnconfigure(j, weight=1)

        # Ajout du fond d'image en dessous du tableau
        self.setup_background_animation()

        # Ajout de la première ligne avec "Année" et "Mois"
        label_annee = Label(self.cadre, text="Année", width=10, relief="solid", bg="lightgray")
        label_annee.grid(row=0, column=0, sticky='nsew')

        label_mois = Label(self.cadre, text="Mois", width=5, relief="solid", bg="lightgray")
        label_mois.grid(row=0, column=1, columnspan=31, sticky='nsew')

        # Ajout de la deuxième ligne avec "Nom du cheval" et les nombres de 1 à 31
        label_nom_cheval = Label(self.cadre, text="Nom du cheval", width=10, relief="solid", bg="lightgray")
        label_nom_cheval.grid(row=1, column=0, sticky='nsew')

        for i in range(1, self.numberColumns):
            label_jour = Label(self.cadre, text=str(i), width=5, relief="solid", bg="lightgray")
            label_jour.grid(row=1, column=i, sticky='nsew')

        # Ajout des données du tableau pour le reste
        for i in range(2, self.numberLines - 2):
            entry_nom_cheval = Entry(self.cadre, width=10)
            entry_nom_cheval.grid(row=i, column=0, sticky='nsew')

            for j in range(1, self.numberColumns):
                cell = Entry(self.cadre, width=5)
                cell.grid(row=i, column=j, sticky='nsew')

        # Ajout de "1/" à "10/" dans la première colonne sous la case "Nom du cheval"
        for i in range(1, 11):
            label_num = Label(self.cadre, text=f"{i}/", width=5, relief="solid", bg="lightgray")
            label_num.grid(row=i + 1, column=0, sticky='nsew')

        # Espace vide entre le tableau et la légende
        label_espace_vide = Label(self.cadre, text="", width=5)
        label_espace_vide.grid(row=self.numberLines - 2, column=0, columnspan=self.numberColumns, sticky='nsew')

        # Ajout du titre à la légende
        label_legend_titre = Label(self.cadre, text="Légende (pour chaque sortie, noter l’adresse du lieu de destination)",
                                   width=10, relief="solid", bg="lightgray")
        label_legend_titre.grid(row=self.numberLines - 1, column=0, columnspan=self.numberColumns, sticky='nsew')

        # Ajout de la légende
        entries_legend = []
        for i in range(1, 13):
            label_num = Label(self.cadre, text=f"{i}.", width=5, relief="solid", bg="lightgray")
            label_num.grid(row=self.numberLines - 1 + (i - 1) // 4, column=((i - 1) % 4) * 8, sticky='nsew')

            entry_legend = Entry(self.cadre, width=10)
            entry_legend.grid(row=self.numberLines - 1 + (i - 1) // 4, column=((i - 1) % 4) * 8 + 1, columnspan=7, sticky='nsew')
            entries_legend.append(entry_legend)

        # Configurer la toile pour surveiller la taille du cadre et ajuster le défilement en conséquence
        self.cadre.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    def setup_background_animation(self):
        self.image_paths = cycle(glob.glob("images/*.png"))
        self.wait_visibility()  # Attendez que la fenêtre soit visible
        self.load_image()

    def load_image(self):
        image_path = next(self.image_paths)
        image = Image.open(image_path)

        # Calculer le rapport d'aspect pour redimensionner l'image tout en maintenant les proportions
        aspect_ratio = image.width / image.height
        new_width = self.winfo_width()
        new_height = int(new_width / aspect_ratio)

        # Redimensionner l'image en fonction de la taille de la fenêtre
        image = image.resize((new_width, new_height))

        photo = ImageTk.PhotoImage(image)

        # Afficher l'image en dessous de la légende
        label_image = Label(self.cadre, image=photo)
        label_image.image = photo
        label_image.grid(row=self.numberLines + 2, column=0, columnspan=self.numberColumns, sticky='nsew')

        # Mettre à jour la taille de la fenêtre pour le redimensionnement
        self.update_idletasks()

        # Continuer le chargement des images
        self.after(2000, self.load_image)

if __name__ == "__main__":
    self = tk.Tk()
    self.title("Tableau des Mouvements Temporaires des Chevaux")
    self.geometry("1920x1080")
    self.iconbitmap("/Creation_dun_logiciel_de_Registre_delevage/images/horse_sans_fond.ico")

    fenetre_principale = FenetrePrincipale(self, height=14, width=32)
    fenetre_principale.mainloop()
