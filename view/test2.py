import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import glob

class FenetrePrincipale(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Formulaire de création d'un compte particulier")
        self.geometry("1920x1080")  # Taille de la fenêtre ajustée
        # Chemin vers l'icône
        self.iconbitmap("/Creation_dun_logiciel_de_Registre_delevage/images/horse_sans_fond.ico")

        # Création du canvas pour afficher les images
        self.canvas = tk.Canvas(self, width=1920, height=1080)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=False)

        # Création du label pour afficher l'image
        self.label_image = tk.Label(self.canvas)
        self.label_image.pack(fill=tk.BOTH, expand=tk.YES)

        # Frame pour contenir les parties du formulaire
        self.formulaire_frame = tk.Frame(self.canvas)
        self.formulaire_frame.pack(side=tk.LEFT, padx=100, pady=200)  # Ajustez selon vos besoins

        # Création d'un titre pour la page
        titre_page = tk.Label(self.formulaire_frame, text="Caractéristiques du Lieu de Détention", font=("Helvetica", 20, "bold"))
        titre_page.grid(row=0, column=0, pady=20)

        # Création des parties du formulaire
        self.creer_partie_1(row=1)
        self.creer_partie_2(row=2)
        self.creer_partie_3(row=3)

        btn_soumettre = tk.Button(self.formulaire_frame, text="Valider", command=self.soumettre_formulaire)
        btn_soumettre.grid(row=4, column=0, pady=10)

         # Appel à la méthode pour gérer le fond d'image changeant
        self.setup_background_animation()

        # Appel à la méthode pour gérer le fond d'image changeant
        self.setup_background_animation()

    def setup_background_animation(self):
        self.image_paths = glob.glob("/Creation_dun_logiciel_de_Registre_delevage/images/*.png")
        self.current_image_index = 0
        self.load_image()

    def load_image(self):
        image_path = self.image_paths[self.current_image_index]
        image = Image.open(image_path)
        image = image.resize((self.winfo_width(), self.winfo_height()))
        photo = ImageTk.PhotoImage(image)
        self.label_image.configure(image=photo)
        self.label_image.image = photo
        self.current_image_index = (self.current_image_index + 1) % len(self.image_paths)

        self.after(2000, self.load_image)
        #self.afficher_contenu_sur_image()

        # Configurer la zone défilable pour ajuster la taille en fonction du contenu
        self.formulaire_frame.update_idletasks()
        #canvas.config(scrollregion=canvas.bbox("all"))

        # Centrer la fenêtre après la création
        self.center_window()

    def center_window(self):
        # Centrer la fenêtre sur l'écran
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        window_width = self.winfo_reqwidth()
        window_height = self.winfo_reqheight()

        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2

        self.geometry("+{}+{}".format(x_position, y_position))

    def creer_partie_1(self, row):
        partie_frame = tk.Frame(self.formulaire_frame)
        partie_frame.grid(row=row, column=0, pady=20)

        etiquette_bienvenue_1 = tk.Label(partie_frame, text="Informations concernant le détenteur des équidés", font=("Helvetica", 16, "bold"))
        etiquette_bienvenue_1.grid(row=0, column=0, pady=(0, 10), sticky="w")

        self.create_label_entry(partie_frame, "Numéro de détenteur (SIRE) :", "entry_num_detenteur", "Saisissez votre numéro de détenteur", required=True, row=1)
        self.create_label_entry(partie_frame, "Titre :", "entry_siret", "Saisissez votre titre", required=True, row=2)
        self.create_label_entry(partie_frame, "Prénom :", "entry_code_ape", "Saisissez votre prénom", required=True, row=3)
        self.create_label_entry(partie_frame, "Nom d'usage :", "entry_statut_juridique", "Saisissez votre nom d'usage", required=True, row=4)
        self.create_label_entry(partie_frame, "NUMAGRIT :", "entry_denomination", "Saisissez votre NUMAGRIT (facultatif)", required=False, row=5)

    def creer_partie_2(self, row):
        partie_frame = tk.Frame(self.formulaire_frame)
        partie_frame.grid(row=row, column=0, pady=20)

        etiquette_bienvenue_2 = tk.Label(partie_frame, text="Coordonnées du détenteur (si différente du lieu de stationnement des équidés) :", font=("Helvetica", 16, "bold"))
        etiquette_bienvenue_2.grid(row=0, column=0, pady=(0, 10), sticky="w")

        self.create_label_entry(partie_frame, "Adresse :", "entry_adresse", "Saisissez votre adresse", required=False, row=1)
        self.create_label_entry(partie_frame, "Tél :", "entry_tel", "Saisissez le numéro de votre téléphone", required=False, row=2)
        self.create_label_entry(partie_frame, "Portable :", "entry_portable", "Saisissez le numéro de votre portable", required=False, row=3)
        self.create_label_entry(partie_frame, "Mail :", "entry_mail", "Saisissez votre adresse e-mail", required=False, row=4)

    def creer_partie_3(self, row):
        partie_frame = tk.Frame(self.formulaire_frame)
        partie_frame.grid(row=row, column=0, pady=20)

        etiquette_bienvenue_3 = tk.Label(partie_frame, text="Personne responsable de la tenue du registre d'élevage", font=("Helvetica", 16, "bold"))
        etiquette_bienvenue_3.grid(row=0, column=0, pady=(0, 10), sticky="w")

        self.create_label_entry(partie_frame, "Prénom :", "entry_prenom", "Saisissez votre prénom", required=True, row=1)
        self.create_label_entry(partie_frame, "Nom d'usage :", "entry_nom_usage", "Saisissez votre nom d'usage", required=True, row=2)
        self.create_label_entry(partie_frame, "Adresse :", "entry_adresse_partie_4", "Saisissez votre adresse", required=True, row=3)
        self.create_label_entry(partie_frame, "Tél :", "entry_tel_partie_4", "Saisissez le numéro de votre téléphone", required=True, row=4)
        self.create_label_entry(partie_frame, "Portable :", "entry_portable_partie_4", "Saisissez le numéro de votre portable", required=True, row=5)
        self.create_label_entry(partie_frame, "Mail :", "entry_mail_partie_4", "Saisissez votre adresse e-mail", required=True, row=6)

    def create_label_entry(self, frame, label_text, entry_name, placeholder_text, required=True, row=0):
        label_frame = tk.Frame(frame)
        label_frame.grid(row=row, column=0, pady=5, padx=(10, 5), sticky="w")

        if required:
            ast_label = tk.Label(label_frame, text="*", fg="red")
            ast_label.grid(row=0, column=0, padx=(0, 5), pady=5)

        label = tk.Label(label_frame, text=label_text)
        label.grid(row=0, column=1, sticky="w", pady=5)

        entry_var = tk.StringVar()
        entry = tk.Entry(frame, textvariable=entry_var, fg="black")
        entry.grid(row=row, column=1, pady=5, sticky="w")

        entry.insert(0, placeholder_text)
        entry.bind("<FocusIn>", lambda event, var=entry_var: self.on_entry_focus_in(var, placeholder_text, entry))
        entry.bind("<FocusOut>", lambda event, var=entry_var: self.on_entry_focus_out(var, placeholder_text, entry))

        # Configurer le poids de la colonne pour permettre l'ajustement dynamique
        frame.grid_columnconfigure(1, weight=1)

        setattr(self, entry_name, entry)

    def on_entry_focus_in(self, var, placeholder_text, entry):
        if var.get() == placeholder_text:
            var.set('')
            entry.config(fg='black')

    def on_entry_focus_out(self, var, placeholder_text, entry):
        if not var.get():
            var.set(placeholder_text)
            entry.config(fg='grey')

    def soumettre_formulaire(self):
        # Récupération des valeurs des champs pour chaque partie
        num_detenteur = self.get_entry_value(self.entry_num_detenteur)
        siret = self.get_entry_value(self.entry_siret)
        code_ape = self.get_entry_value(self.entry_code_ape)
        statut_juridique = self.get_entry_value(self.entry_statut_juridique)
        denomination = self.get_entry_value(self.entry_denomination)
        adresse = self.get_entry_value(self.entry_adresse)
        tel = self.get_entry_value(self.entry_tel)
        portable = self.get_entry_value(self.entry_portable)
        mail = self.get_entry_value(self.entry_mail)
        prenom = self.get_entry_value(self.entry_prenom)
        nom_usage = self.get_entry_value(self.entry_nom_usage)
        adresse_partie_4 = self.get_entry_value(self.entry_adresse_partie_4)
        tel_partie_4 = self.get_entry_value(self.entry_tel_partie_4)
        portable_partie_4 = self.get_entry_value(self.entry_portable_partie_4)
        mail_partie_4 = self.get_entry_value(self.entry_mail_partie_4)

        # Affichage des informations dans une boîte de dialogue
        message = (
            f"Numéro de détenteur (SIRE) : {num_detenteur}\n"
            f"N° SIRET : {siret}\n"
            f"Code APE : {code_ape}\n"
            f"Statut juridique : {statut_juridique}\n"
            f"Dénomination : {denomination}\n"
            f"Adresse : {adresse}\n"
            f"Téléphone : {tel}\n"
            f"Portable : {portable}\n"
            f"Adresse e-mail : {mail}\n"
            f"Prénom : {prenom}\n"
            f"Nom d'usage : {nom_usage}\n"
            f"Adresse : {adresse_partie_4}\n"
            f"Téléphone : {tel_partie_4}\n"
            f"Portable : {portable_partie_4}\n"
            f"Adresse e-mail : {mail_partie_4}"
        )

        messagebox.showinfo("Récapitulatif des informations", message)

if __name__ == "__main__":
    fenetre_principale = FenetrePrincipale()
    fenetre_principale.mainloop()
