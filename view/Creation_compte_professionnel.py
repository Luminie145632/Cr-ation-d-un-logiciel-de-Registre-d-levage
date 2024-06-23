import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import glob
import subprocess
import json

class FenetrePrincipale(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Page de création de l'espace d'un compte professionnel")
        self.geometry("1920x1080")  # Ajustez la taille de la fenêtre
        self.iconbitmap("/Creation_dun_logiciel_de_Registre_delevage/images/horse_sans_fond.ico")

        # Création du canvas pour afficher les images
        self.canvas = tk.Canvas(self, width=1920, height=1080)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Création du label pour afficher l'image
        self.label_image = tk.Label(self.canvas)
        self.label_image.pack(fill=tk.BOTH, expand=tk.YES)

        # Frame pour contenir les parties du formulaire
        self.formulaire_frame = tk.Frame(self.canvas)
        self.formulaire_frame.pack(side=tk.LEFT, padx=100, pady=200)  # Ajustez selon vos besoins

        # Création d'un titre pour la page
        titre_page = tk.Label(self.formulaire_frame, text="Bienvenue sur la page Caractéristiques du Lieu de Détention", font=("Helvetica", 15, "bold"))
        titre_page.grid(row=0, column=0, pady=20)

        # Création des parties du formulaire
        self.creer_partie_1(row=1, relx=None, rely=None)
        self.creer_partie_2(row=2, relx=None, rely=None)
        self.creer_partie_3(row=3, relx=None, rely=None)
        self.creer_partie_4(row=4, relx=None, rely=None)


        btn_soumettre = tk.Button(self.formulaire_frame, text="Valider", command=self.soumettre_formulaire)
        btn_soumettre.grid(row=5, column=0, pady=10)

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

        self.after(6000, self.load_image)
        self.afficher_contenu_sur_image()

    def afficher_contenu_sur_image(self):
        # Obtenez la position actuelle de défilement verticale
        y_scroll_position = self.canvas.yview()[0]

        # Ajustez la position du formulaire en fonction du défilement
        x_position = 500
        y_position = 25 + y_scroll_position * self.winfo_height()

        self.formulaire_frame.place(x=x_position, y=y_position)

    def creer_partie_1(self, row, relx=None, rely=None):
        partie_frame = tk.Frame(self.formulaire_frame)
        partie_frame.grid(row=row, column=0, pady=5, padx=((self.winfo_width() * relx) if relx is not None else 2), sticky="w")

        etiquette_bienvenue_1 = tk.Label(partie_frame, text="Adresse du lieu de détention et type d'activité", font=("Helvetica", 12, "bold"))
        etiquette_bienvenue_1.grid(row=0, column=0, pady=(0, 5), sticky="w")

        self.create_label_entry(partie_frame, "Denomination :", "entry_denomination", "Saisissez votre denomination", required=False, row=1, relx=relx, rely=rely)
        self.create_label_entry(partie_frame, "Adresse :", "entry_adresse", "Saisissez votre adresse", required=False, row=3, relx=relx, rely=rely)
        self.create_label_entry(partie_frame, "Type d'activite :", "entry_type_activite", "Saisissez votre type d'activite", required=False, row=4, relx=relx, rely=rely)

    def creer_partie_2(self, row, relx=None, rely=None):
        partie_frame = tk.Frame(self.formulaire_frame)
        partie_frame.grid(row=row, column=0, pady=5, padx=((self.winfo_width() * relx) if relx is not None else 2), sticky="w")

        etiquette_bienvenue_2 = tk.Label(partie_frame, text="Informations concernant le détenteur des équidés", font=("Helvetica", 12, "bold"))
        etiquette_bienvenue_2.grid(row=0, column=0, pady=(0, 5), sticky="w")

        self.create_label_entry(partie_frame, "Numéro de détenteur (SIRE) :", "entry_num_detenteur", "Saisissez votre numéro de détenteur", required=False, row=1, relx=relx, rely=rely)
        self.create_radio_buttons(partie_frame, row=2, relx=relx, rely=rely)  # Boutons radio sous le titre
        self.create_label_entry(partie_frame, "N° SIRET :", "entry_siret", "Saisissez votre N° SIRET", required=False, row=3, relx=relx, rely=rely)
        self.create_label_entry(partie_frame, "Code APE :", "entry_code_ape", "Saisissez votre Code APE", required=False, row=4, relx=relx, rely=rely)
        self.create_label_entry(partie_frame, "Statut juridique (Facultatif) :", "entry_statut_juridique", "Saisissez votre statut juridique (facultatif)", required=False, row=5, relx=relx, rely=rely)
        self.create_label_entry(partie_frame, "Dénomination (Facultatif) :", "entry_denomination_partie_2", "Saisissez votre dénomination (facultatif)", required=False, row=6, relx=relx, rely=rely)

    def creer_partie_3(self, row, relx=None, rely=None):
        partie_frame = tk.Frame(self.formulaire_frame)
        partie_frame.grid(row=row, column=0, pady=5, padx=((self.winfo_width() * relx) if relx is not None else 5), sticky="w")

        etiquette_bienvenue_3 = tk.Label(partie_frame, text="Coordonnées du détenteur (si différente du lieu de stationnement des équidés) :", font=("Helvetica", 12, "bold"))
        etiquette_bienvenue_3.grid(row=0, column=0, pady=(0, 5), sticky="w")

        self.create_label_entry(partie_frame, "Adresse :", "entry_adresse_partie_3", "Saisissez votre adresse", required=False, row=1, relx=relx, rely=rely)
        self.create_label_entry(partie_frame, "Téléphone :", "entry_tel", "Saisissez le numéro de votre téléphone", required=False, row=2, relx=relx, rely=rely)
        self.create_label_entry(partie_frame, "Portable :", "entry_portable", "Saisissez le numéro de votre portable", required=False, row=3, relx=relx, rely=rely)
        self.create_label_entry(partie_frame, "Adresse e-mail :", "entry_mail", "Saisissez votre adresse e-mail", required=False, row=4, relx=relx, rely=rely)

    def creer_partie_4(self, row, relx=None, rely=None):
        partie_frame = tk.Frame(self.formulaire_frame)
        partie_frame.grid(row=row, column=0, pady=5, padx=((self.winfo_width() * relx) if relx is not None else 5), sticky="w")

        etiquette_bienvenue_4 = tk.Label(partie_frame, text="Personne responsable de la tenue du registre d'élevage", font=("Helvetica", 12, "bold"))
        etiquette_bienvenue_4.grid(row=0, column=0, pady=(0, 5), sticky="w")

        self.create_label_entry(partie_frame, "Prénom :", "entry_prenom", "Saisissez votre prénom", required=False, row=1, relx=relx, rely=rely)
        self.create_label_entry(partie_frame, "Nom d'usage :", "entry_nom_usage", "Saisissez votre nom d'usage", required=False, row=2, relx=relx, rely=rely)
        self.create_label_entry(partie_frame, "Adresse :", "entry_adresse_partie_4", "Saisissez votre adresse", required=False, row=3, relx=relx, rely=rely)
        self.create_label_entry(partie_frame, "Tél :", "entry_tel_partie_4", "Saisissez le numéro de votre téléphone", required=False, row=4, relx=relx, rely=rely)
        self.create_label_entry(partie_frame, "Portable :", "entry_portable_partie_4", "Saisissez le numéro de votre portable", required=False, row=5, relx=relx, rely=rely)
        self.create_label_entry(partie_frame, "Adresse e-mail :", "entry_mail_partie_4", "Saisissez votre adresse e-mail", required=False, row=6, relx=relx, rely=rely)


    def create_radio_buttons(self, frame, row, relx=5, rely=5):
        # Frame pour les boutons radio
        radio_frame = tk.Frame(frame)
        radio_frame.grid(row=row, column=0, pady=5, padx=((self.winfo_width() * relx) if relx is not None else 5), sticky="w")

        # Variable commune pour les boutons radio
        self.var_choix = tk.StringVar()
        self.var_choix.set(None)  # Ajuste la valeur par défaut à None

        # Création des boutons radio
        choix1 = tk.Radiobutton(radio_frame, text="Personne Physique", value="Personne physique", variable=self.var_choix, command=self.update_radio_buttons)
        choix1.grid(row=0, column=0, padx=20)

        choix2 = tk.Radiobutton(radio_frame, text="Personne Morale", value="Personne morale", variable=self.var_choix, command=self.update_radio_buttons)
        choix2.grid(row=0, column=1, padx=20)

    def update_radio_buttons(self):
        choix_selectionne = self.var_choix.get()

        if choix_selectionne == "Personne physique":
            self.entry_siret.config(state="disabled")  # Désactiver le champ SIRET
            self.entry_code_ape.config(state="disabled")  # Désactiver le champ Code APE
        else:
            self.entry_siret.config(state="normal")  # Activer le champ SIRET
            self.entry_code_ape.config(state="normal")  # Activer le champ Code APE

    def create_label_entry(self, frame, label_text, entry_var_name, entry_placeholder, required=False, row=1, relx=5, rely=5):
        # Création d'un frame pour l'étiquette et le champ de saisie
        label_entry_frame = tk.Frame(frame)
        label_entry_frame.grid(row=row, column=0, pady=5, padx=((self.winfo_width() * relx) if relx is not None else 5), sticky="w")

        # Création de l'étiquette
        label = tk.Label(label_entry_frame, text=label_text, font=("Helvetica", 12))
        label.grid(row=0, column=0, pady=(0, 5), sticky="w")

        # Création du champ de saisie
        entry_var = tk.StringVar(value=entry_placeholder)
        entry = tk.Entry(label_entry_frame, textvariable=entry_var, font=("Helvetica", 12), foreground="gray")
        entry.grid(row=0, column=0, padx=(225, 0), sticky="w") # Ajustement du padding pour aligner correctement

        # Effacement du texte par défaut lors du clic sur le champ de saisie
        entry.bind("<FocusIn>", lambda event, e=entry: self.on_entry_click(e))
        entry.bind("<FocusOut>", lambda event, e=entry, p=entry_placeholder: self.on_focus_out(e, p))

        # Stockage du champ de saisie dans une variable d'instance
        setattr(self, entry_var_name, entry)

    def on_entry_focus_in(self, var, placeholder_text, entry):
        if var.get() == placeholder_text:
            entry.config(fg='black')
            var.set('')

    def on_entry_focus_out(self, var, placeholder_text, entry):
        if not var.get():
            var.set(placeholder_text)
            entry.config(fg='grey')

    def get_entry_value(self, entry):
        value = entry.get()
        placeholder_text = entry.placeholder_text if hasattr(entry, 'placeholder_text') else ""
        return value if value != placeholder_text else ""

    def soumettre_formulaire(self):
        # Récupération des valeurs des champs pour chaque partie
        denomination = self.get_entry_value(self.entry_denomination)
        adresse = self.get_entry_value(self.entry_adresse)
        type_activite = self.get_entry_value(self.entry_type_activite)
        num_detenteur = self.get_entry_value(self.entry_num_detenteur)
        choix_type_detenteur = self.var_choix.get()
        siret = self.get_entry_value(self.entry_siret)
        code_ape = self.get_entry_value(self.entry_code_ape)
        statut_juridique = self.get_entry_value(self.entry_statut_juridique)
        denomination_partie_2 = self.get_entry_value(self.entry_denomination_partie_2)
        adresse_partie_3 = self.get_entry_value(self.entry_adresse_partie_3)
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
            f"Denomination : {denomination}\n"
            f"Adresse : {adresse}\n"
            f"Type d'activité : {type_activite}\n"
            f"Numero de detenteur (SIRE) : {num_detenteur}\n"
            f"Type de detenteur : {choix_type_detenteur}\n"
            f"N° SIRET : {siret}\n"
            f"Code APE : {code_ape}\n"
            f"Statut juridique : {statut_juridique}\n"
            f"Denomination : {denomination_partie_2}\n"
            f"Adresse : {adresse_partie_3}\n"
            f"Telephone : {tel}\n"
            f"Portable : {portable}\n"
            f"Adresse e-mail : {mail}\n"
            f"Prenom : {prenom}\n"
            f"Nom d'usage : {nom_usage}\n"
            f"Adresse : {adresse_partie_4}\n"
            f"Telephone : {tel_partie_4}\n"
            f"Portable : {portable_partie_4}\n"
            f"Adresse e-mail : {mail_partie_4}"
        )

        messagebox.showinfo("Récapitulatif des informations", message)

        # Appel à la méthode creacompte pour enregistrer les données dans le fichier JSON
        self.creacompte()
        # Ouvrir la nouvelle fenêtre et fermer l'ancienne
        subprocess.Popen(["python", "/Creation_dun_logiciel_de_Registre_delevage/view/Accueil.py"])
        self.destroy()

    def creacompte(self):
        # Collecte des informations du formulaire
        comptes = {
            "Denomination": self.get_entry_value(self.denomination),
            "Adresse": self.get_entry_value(self.adresse),
            "Type d'activité": self.get_entry_value(self.entry_type_activite),
            "Numero de detenteur (SIRE)": self.get_entry_value(self.entry_num_detenteur),
            "Type de detenteur": self.var_choix.get(),
            "N° SIRET": self.get_entry_value(self.entry_siret),
            "Code APE": self.get_entry_value(self.entry_code_ape),
            "Statut juridique": self.get_entry_value(self.entry_statut_juridique),
            "Denomination": self.get_entry_value(self.entry_denomination_partie_2),
            "Adresse": self.get_entry_value(self.entry_adresse),
            "Telephone": self.get_entry_value(self.entry_tel),
            "Portable": self.get_entry_value(self.entry_portable),
            "Adresse e-mail": self.get_entry_value(self.entry_mail),
            "Prenom": self.get_entry_value(self.entry_prenom),
            "Nom d'usage": self.get_entry_value(self.entry_nom_usage),
            "Adresse (responsable)": self.get_entry_value(self.entry_adresse_partie_4),
            "Telephone (responsable)": self.get_entry_value(self.entry_tel_partie_4),
            "Portable (responsable)": self.get_entry_value(self.entry_portable_partie_4),
            "Adresse e-mail (responsable)": self.get_entry_value(self.entry_mail_partie_4)
        }

        # Lecture des données existantes du fichier JSON s'il en existe
        try:
            with open('/Creation_dun_logiciel_de_Registre_delevage/view/comptes_professionnels.json', 'r') as json_file:
                comptes_data = json.load(json_file)["comptes"]
        except FileNotFoundError:
            comptes_data = []

        # Ajout du nouveau compte à la liste
        comptes_data.append(comptes)

        # Écriture des données dans un fichier JSON
        with open('/Creation_dun_logiciel_de_Registre_delevage/view/comptes_professionnels.json', 'w') as json_file:
            json.dump({"comptes": comptes_data}, json_file, indent=4)

if __name__ == "__main__":
    app = FenetrePrincipale()
    app.mainloop()


