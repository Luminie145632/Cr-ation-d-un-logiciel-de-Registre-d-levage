from tkinter import *
from PIL import Image, ImageTk
import glob

class EncadrementZootechnique(Frame):
    def __init__(self, master=None, height=0, width=0, col_titles=[]):
        super().__init__(master)

        self.master = master
        self.master.title("Encadrement Zootechnique")
        self.master.geometry("1920x1080")  # Définir la taille initiale de la fenêtre
        self.master.iconbitmap("/Creation_dun_logiciel_de_Registre_delevage/images/horse_sans_fond.ico")
        self.master.resizable(height=True, width=True)

        # Créer un conteneur pour le titre, l'image, le tableau et l'espace séparateur
        self.container = Frame(self.master)
        self.container.pack(fill=BOTH, expand=True)

        # Récupérer le chemin des images dans le dossier
        image_folder = "/Creation_dun_logiciel_de_Registre_delevage/images/*.png"
        self.image_paths = glob.glob(image_folder)  # Ajouter cette ligne pour définir l'attribut image_paths

        self.current_image_index = 0
        self.load_image()

        # Ajouter un espace entre le titre et le tableau
        self.separator_frame = Frame(self.container, height=20)
        self.separator_frame.grid(row=1, column=0, columnspan=width, sticky='nsew')

        self.numberLines = height
        self.numberColumns = width
        self.col_titles = col_titles

        # Ajout des titres de colonnes
        for j in range(self.numberColumns):
            col_title = Label(self.container, text=self.col_titles[j], width=20, relief="solid", bg="lightgray", anchor="w")
            col_title.grid(row=2, column=j, sticky='nsew')

        # Ajout des données du tableau
        self.data = []
        for i in range(3, self.numberLines + 3):
            line = []
            for j in range(self.numberColumns):
                cell = Entry(self.container, width=20)
                cell.grid(row=i, column=j, sticky='nsew')
                line.append(cell)
            self.data.append(line)

        # Configurer la gestion des colonnes pour qu'elles s'adaptent au contenu
        for j in range(self.numberColumns):
            self.container.grid_columnconfigure(j, weight=1)

        # Bouton pour ajouter une nouvelle ligne
        self.bouton_ajouter_ligne = Button(self.container, text="Ajouter une ligne", command=self.ajouter_ligne, width=20, height=1)
        self.bouton_ajouter_ligne.grid(row=self.numberLines + 3, column=0, columnspan=width, sticky='nsew')

    def load_and_display_image(self, image_paths):
        if self.current_image_index < len(image_paths):
            # Charger l'image
            background_image = Image.open(image_paths[self.current_image_index])
            background_image = background_image.resize((1920, 1080))
            background_image = ImageTk.PhotoImage(background_image)

            # Afficher l'image en arrière-plan du conteneur
            self.label_image = Label(self.container, image=background_image)
            self.label_image.image = background_image
            self.label_image.place(x=0, y=0, relwidth=1, relheight=1)

            # Mettre à jour l'index de l'image pour afficher la prochaine image la prochaine fois
            self.current_image_index += 1

            # Appeler cette méthode après un délai pour passer à l'image suivante
            self.after(6000, lambda: self.load_and_display_image(image_paths))

    def ajouter_ligne(self):
        # Cacher le bouton
        self.bouton_ajouter_ligne.grid_remove()

        # Ajouter une nouvelle ligne
        nouvelle_ligne = []
        for j in range(self.numberColumns):
            cell = Entry(self.container, width=20)
            cell.grid(row=self.numberLines + 3, column=j, sticky='nsew')
            nouvelle_ligne.append(cell)
        self.data.append(nouvelle_ligne)
        self.numberLines += 1

        # Afficher le bouton à la nouvelle position
        self.bouton_ajouter_ligne.grid(row=self.numberLines + 3, column=0, columnspan=self.numberColumns, sticky='nsew')
    
    def load_image(self):
        image_path = self.image_paths[self.current_image_index]
        original_image = Image.open(image_path)
        original_image = original_image.resize((1920, 1080))
        self.photo = ImageTk.PhotoImage(original_image)

        if hasattr(self, 'label_image'):
            self.label_image.configure(image=self.photo)
            self.label_image.image = self.photo
        else:
            self.label_image = Label(self.container, image=self.photo)
            self.label_image.image = self.photo
            self.label_image.place(x=0, y=0, relwidth=1, relheight=1)

        self.current_image_index = (self.current_image_index + 1) % len(self.image_paths)
        self.after(6000, self.load_image)

if __name__ == "__main__":
    root = Tk()

    # Ajouter le titre sur la fenêtre principale
    title_label = Label(root, text="Encadrement Zootechnique", font=("Helvetica", 14, "bold"))
    title_label.pack()

    # Liste des titres des colonnes
    col_titles = ["Date", "Organisme de contrôle", "Motif de contrôle", "Nom du contrôleur", "Cachet", "Signature"]

    fenetre_principale = EncadrementZootechnique(master=root, height=3, width=6, col_titles=col_titles)
    fenetre_principale.mainloop()
