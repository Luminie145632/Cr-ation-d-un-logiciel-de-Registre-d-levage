import tkinter as tk
from PIL import Image, ImageTk
import glob

class FenetrePrincipale(tk.Tk):
    def __init__(self, width, col_titles, height):
        super().__init__()

        self.width = width
        self.height = height
        self.numberColumns = width
        self.numberLines = height
        self.col_title = col_titles
        self.data = []

        self.title("Création de l'espace compte")
        self.geometry("1920x1080")  
        self.iconbitmap("/Creation_dun_logiciel_de_Registre_delevage/images/horse_sans_fond.ico")

        # Création du label pour afficher l'image
        self.label_image = tk.Label(self)
        self.label_image.pack(fill=tk.BOTH, expand=tk.YES)

        # Création du titre
        self.etiquette_bienvenue = tk.Label(self, text="Bienvenue sur la page de création de votre compte", font=("Helvetica", 16, "bold"))
        self.etiquette_bienvenue.place(relx=0.5, y=10, anchor="n")

        # Création du widget DemoWidget
        self.demo_widget = DemoWidget(self)
        self.demo_widget.place(relx=0.5, rely=0.5, anchor='center')

        # Cadre pour afficher les informations
        self.info_frame = tk.Frame(self)
        self.info_frame.pack(pady=20)  # Ajouter un espacement

        # Création de l'image en arrière-plan
        self.setup_background_animation()

        # Liaison de la méthode de mise à jour des informations à la variable de choix
        self.demo_widget.var_choix.trace_add("write", self.mettre_a_jour_informations)

        self.bind("<Configure>", self.redimensionner_image)

        # Dictionnaire pour stocker les pages
        self.pages = {}

        # Créer les pages pour les particuliers et les professionnels
        self.pages["Particulier"] = PageParticulier(self.info_frame)
        self.pages["Professionnel"] = PageProfessionnel(self.info_frame)

    def setup_background_animation(self):
        self.image_paths = glob.glob("/Creation_dun_logiciel_de_Registre_delevage/images/*.png")
        self.current_image_index = 0
        self.load_image()

    def load_image(self):
        image_path = self.image_paths[self.current_image_index]
        image = Image.open(image_path)
        image = image.resize((self.winfo_width(), self.winfo_height()))
        photo = ImageTk.PhotoImage(image)

        # Affichage de l'image en arrière-plan
        if hasattr(self, 'label_image'):
            self.label_image.configure(image=photo)
            self.label_image.image = photo
        else:
            self.label_image = tk.Label(self, bd=0, highlightthickness=0, image=photo)
            self.label_image.image = photo
            self.label_image.place(x=0, y=0, relwidth=1, relheight=1)

        self.current_image_index = (self.current_image_index + 1) % len(self.image_paths)
        self.after(6000, self.load_image)

    def redimensionner_image(self, event):
        image_path = self.image_paths[self.current_image_index]
        image = Image.open(image_path)
        image = image.resize((self.winfo_width(), self.winfo_height()))
        photo = ImageTk.PhotoImage(image)
        self.label_image.configure(image=photo)
        self.label_image.image = photo

    def mettre_a_jour_informations(self, *args):
        choix = self.demo_widget.var_choix.get()
        # Vérifier le choix et afficher la page correspondante
        if choix in self.pages:
            self.pages[choix].afficher()

class DemoWidget(tk.Frame):
    CHOIX = ["Particulier", "Professionnel"]

    def __init__(self, root):
        super().__init__(root)

        # Variable commune pour les boutons radio
        self.var_choix = tk.StringVar()

        for i, rb_label in enumerate(self.CHOIX):
            rb = tk.Radiobutton(self, text=rb_label, value=rb_label, variable=self.var_choix)
            rb.grid(column=i, row=0, padx=20)  # Ajout de l'espacement entre les boutons

        # Déselectionner tous les boutons radio par défaut
        self.var_choix.set(None)

class PageParticulier(tk.Frame):
    def __init__(self, root):
        super().__init__(root)

        # Création des widgets pour la page des particuliers
        self.label_particulier = tk.Label(self, text="Informations pour les particuliers...")
        self.label_particulier.pack()

    def afficher(self):
        # Afficher la page des particuliers
        self.pack(fill=tk.BOTH, expand=True)

class PageProfessionnel(tk.Frame):
    def __init__(self, root):
        super().__init__(root)

        # Création des widgets pour la page des professionnels
        self.label_professionnel = tk.Label(self, text="Informations pour les professionnels...")
        self.label_professionnel.pack()

    def afficher(self):
        # Afficher la page des professionnels
        self.pack(fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    # Définition des titres de colonnes
    col_titles = ["Colonne 1", "Colonne 2", "Colonne 3", "Colonne 4", "Colonne 5", "Colonne 6"]

    # Création de la fenêtre principale en fournissant les arguments requis
    fenetre_principale = FenetrePrincipale(width=6, col_titles=col_titles, height=3)
    fenetre_principale.mainloop()
