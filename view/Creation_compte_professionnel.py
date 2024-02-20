import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


class FenetrePrincipale(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Formulaire de création d'un compte professionnel")
        self.geometry("1920x1080")  # Taille de la fenêtre ajustée
        self.iconbitmap("/Creation_dun_logiciel_de_Registre_delevage/images/horse_sans_fond.ico")

        # Ajout d'une barre de défilement verticale
        scrollbar = tk.Scrollbar(self, orient="vertical")
        scrollbar.pack(side="right", fill="y")

        # Ajout d'un canevas pour la zone défilable
        canvas = tk.Canvas(self, yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)

        # Configuration de la barre de défilement
        scrollbar.config(command=canvas.yview)

        # Frame pour contenir les parties du formulaire
        self.formulaire_frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=self.formulaire_frame, anchor="nw")

        # Création d'un titre pour la page
        titre_page = tk.Label(self.formulaire_frame, text="Caractéristiques du Lieu de Détention", font=("Helvetica", 20, "bold"))
        titre_page.grid(row=0, column=0, pady=20)

        # Création des parties du formulaire
        self.creer_partie_1(row=1)
        self.creer_partie_2(row=2)
        self.creer_partie_3(row=3)

        btn_soumettre = tk.Button(self.formulaire_frame, text="Valider", command=self.soumettre_formulaire)
        btn_soumettre.grid(row=4, column=0, pady=10)

        # Configurer la zone défilable pour ajuster la taille en fonction du contenu
        self.formulaire_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

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
        self.create_radio_buttons(partie_frame, row=2)  # Boutons radio sous le titre
        self.create_label_entry(partie_frame, "N° SIRET :", "entry_siret", "Saisissez votre N° SIRET", required=True, row=3)
        self.create_label_entry(partie_frame, "Code APE :", "entry_code_ape", "Saisissez votre Code APE", required=True, row=4)
        self.create_label_entry(partie_frame, "Statut juridique :", "entry_statut_juridique", "Saisissez votre statut juridique (facultatif)", required=False, row=5)
        self.create_label_entry(partie_frame, "Dénomination :", "entry_denomination", "Saisissez votre dénomination (facultatif)", required=False, row=6)

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

    def create_radio_buttons(self, frame, row):
        # Frame pour les boutons radio
        radio_frame = tk.Frame(frame)
        radio_frame.grid(row=row, column=0, pady=10, sticky="w")

        # Variable commune pour les boutons radio
        self.var_choix = tk.StringVar()
        self.var_choix.set(None)  # Ajuste la valeur par défaut à None

        # Création des boutons radio
        choix1 = tk.Radiobutton(radio_frame, text="Personne Physique", value="Choix 1", variable=self.var_choix, command=self.update_radio_buttons)
        choix1.grid(row=0, column=0, padx=20)

        choix2 = tk.Radiobutton(radio_frame, text="Personne Morale", value="Choix 2", variable=self.var_choix, command=self.update_radio_buttons)
        choix2.grid(row=0, column=1, padx=20)

        # Configurer le poids de la colonne pour permettre l'ajustement dynamique
        frame.grid_columnconfigure(0, weight=1)

    def update_radio_buttons(self):
        # Désactiver la validation si l'un des boutons radio est sélectionné
        self.validate_entries()

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

        entry.placeholder_text = placeholder_text  # Ajout de l'attribut placeholder_text à l'objet Entry

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

    def get_entry_value(self, entry):
        value = entry.get()
        placeholder_text = entry.placeholder_text if hasattr(entry, 'placeholder_text') else ""
        return value if value != placeholder_text else ""

    def validate_entries(self):
        # Vous pouvez ajouter ici la logique de validation
        pass

    def soumettre_formulaire(self):
        # Récupération des valeurs des champs pour chaque partie
        num_detenteur = self.get_entry_value(self.entry_num_detenteur)
        choix_type_detenteur = self.var_choix.get()
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
            f"Type de détenteur : {choix_type_detenteur}\n"
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
