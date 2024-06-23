import subprocess
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import glob
import json

class FenetrePrincipale(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Formulaire de création d'un compte particulier")
        self.geometry("1920x1080")  # Ajustez la taille selon vos besoins
        self.iconbitmap("images/horse_sans_fond.ico")

        # Création du canvas pour afficher les images
        self.canvas = tk.Canvas(self, width=1920, height=1080)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Création du label pour afficher l'image
        self.label_image = tk.Label(self.canvas)
        self.label_image.pack(fill=tk.BOTH, expand=tk.YES)

        # Frame pour contenir les parties du formulaire
        self.formulaire_frame = tk.Frame(self.canvas, bg="white")  # Changer la couleur d'arrière-plan au besoin
        self.formulaire_frame.place(x=450, y=8)  # Ajustez selon vos besoins

        # Création d'un titre pour la page
        titre_page = tk.Label(self.formulaire_frame, text="Bienvenue sur la page Caractéristiques du Lieu de Détention", font=("Helvetica", 20, "bold"))
        titre_page.grid(row=0, column=0, pady=20)

        # Création des parties du formulaire
        self.creer_partie_1(row=1)
        self.creer_partie_2(row=2)
        self.creer_partie_3(row=3)
        self.creer_partie_4(row=4)

        btn_soumettre = tk.Button(self.formulaire_frame, text="Valider", command=self.soumettre_formulaire)
        btn_soumettre.grid(row=5, column=0, pady=10)

        # Appel à la méthode pour gérer le fond d'image changeant
        self.setup_background_animation()

    def setup_background_animation(self):
        self.image_paths = glob.glob("images/*.png")
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

    def creer_partie_1(self, row):
        partie_frame = tk.Frame(self.formulaire_frame)
        partie_frame.grid(row=row, column=0, pady=5, padx=5, sticky="w")

        etiquette_bienvenue_1 = tk.Label(partie_frame, text="Adresse du lieu de détention et type d'activité", font=("Helvetica", 16, "bold"))
        etiquette_bienvenue_1.grid(row=0, column=0, pady=(0, 5), sticky="w")

        self.create_label_entry(partie_frame, "Denomination :", "entry_denomination", "Saisissez votre denomination", row=1)
        self.create_label_entry(partie_frame, "Adresse :", "entry_adresse_partie_1", "Saisissez votre adresse", row=2)
        self.create_label_entry(partie_frame, "Type d'activite :", "entry_type_activite", "Saisissez votre type d'activite", row=3)

    def creer_partie_2(self, row):
        partie_frame = tk.Frame(self.formulaire_frame)
        partie_frame.grid(row=row, column=0, pady=5, padx=5, sticky="w")

        etiquette_bienvenue_2 = tk.Label(partie_frame, text="Informations concernant le détenteur des équidés", font=("Helvetica", 16, "bold"))
        etiquette_bienvenue_2.grid(row=0, column=0, pady=(0, 5), sticky="w")

        self.create_label_entry(partie_frame, "Numéro de détenteur (SIRE) :", "entry_num_detenteur", "Saisissez votre numero de détenteur", row=1)
        self.create_label_entry(partie_frame, "Titre :", "entry_titre", "Saisissez votre titre", row=2)
        self.create_label_entry(partie_frame, "Prénom :", "entry_prenom", "Saisissez votre prénom", row=3)
        self.create_label_entry(partie_frame, "Nom d'usage :", "entry_nom_usage", "Saisissez votre nom d'usage", row=4)
        self.create_label_entry(partie_frame, "NUMAGRIT (Facultatif) :", "entry_numagrit", "Saisissez votre NUMAGRIT", row=5)

    def creer_partie_3(self, row):
        partie_frame = tk.Frame(self.formulaire_frame)
        partie_frame.grid(row=row, column=0, pady=5, padx=5, sticky="w")

        etiquette_bienvenue_3 = tk.Label(partie_frame, text="Coordonnées du détenteur (si différente du lieu de stationnement des équidés) :", font=("Helvetica", 16, "bold"))
        etiquette_bienvenue_3.grid(row=0, column=0, pady=(0, 5), sticky="w")

        self.create_label_entry(partie_frame, "Adresse :", "entry_adresse_partie_3", "Saisissez votre adresse", row=1)
        self.create_label_entry(partie_frame, "Tél :", "entry_tel", "Saisissez le numero de votre telephone", row=2)
        self.create_label_entry(partie_frame, "Portable :", "entry_portable", "Saisissez le numero de votre portable", row=3)
        self.create_label_entry(partie_frame, "Mail :", "entry_mail", "Saisissez votre adresse e-mail", row=4)

    def creer_partie_4(self, row):
        partie_frame = tk.Frame(self.formulaire_frame)
        partie_frame.grid(row=row, column=0, pady=5, padx=5, sticky="w")

        etiquette_bienvenue_4 = tk.Label(partie_frame, text="Personne responsable de la tenue du registre d'élevage", font=("Helvetica", 16, "bold"))
        etiquette_bienvenue_4.grid(row=0, column=0, pady=(0, 5), sticky="w")

        self.create_label_entry(partie_frame, "Prénom :", "entry_prenom_4", "Saisissez votre prenom", row=1)
        self.create_label_entry(partie_frame, "Nom d'usage :", "entry_nom_usage_partie_4", "Saisissez votre nom d'usage", row=2)
        self.create_label_entry(partie_frame, "Adresse :", "entry_adresse_partie_4", "Saisissez votre adresse", row=3)
        self.create_label_entry(partie_frame, "Tél :", "entry_tel_partie_4", "Saisissez le numero de votre telephone", row=4)
        self.create_label_entry(partie_frame, "Portable :", "entry_portable_partie_4", "Saisissez le numero de votre portable", row=5)
        self.create_label_entry(partie_frame, "Mail :", "entry_mail_partie_4", "Saisissez votre adresse e-mail", row=6)

    def create_label_entry(self, frame, label_text, entry_name, placeholder_text, row):
        label_frame = tk.Frame(frame)
        label_frame.grid(row=row, column=0, pady=5, padx=5, sticky="w")

        label = tk.Label(label_frame, text=label_text)
        label.grid(row=0, column=0, sticky="w", pady=5)

        entry_var = tk.StringVar()
        entry = tk.Entry(label_frame, textvariable=entry_var, fg="grey")
        entry.grid(row=0, column=1, pady=5, padx=5, sticky="w")

        entry.insert(0, placeholder_text)
        entry.placeholder_text = placeholder_text
        entry.bind("<FocusIn>", lambda event: self.on_entry_focus_in(entry_var, placeholder_text, entry))
        entry.bind("<FocusOut>", lambda event: self.on_entry_focus_out(entry_var, placeholder_text, entry))

        setattr(self, entry_name, entry)

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
        denomination = self.get_entry_value(self.entry_denomination)
        adresse_partie_1 = self.get_entry_value(self.entry_adresse_partie_1)
        type_activite = self.get_entry_value(self.entry_type_activite)
        num_detenteur = self.get_entry_value(self.entry_num_detenteur)
        titre = self.get_entry_value(self.entry_titre)
        prenom = self.get_entry_value(self.entry_prenom)
        nom_usage = self.get_entry_value(self.entry_nom_usage)
        numagrit = self.get_entry_value(self.entry_numagrit)
        adresse_partie_3 = self.get_entry_value(self.entry_adresse_partie_3)
        tel = self.get_entry_value(self.entry_tel)
        portable = self.get_entry_value(self.entry_portable)
        mail = self.get_entry_value(self.entry_mail)
        prenom_4 = self.get_entry_value(self.entry_prenom_4)
        nom_usage_partie_4 = self.get_entry_value(self.entry_nom_usage_partie_4)
        adresse_partie_4 = self.get_entry_value(self.entry_adresse_partie_4)
        tel_partie_4 = self.get_entry_value(self.entry_tel_partie_4)
        portable_partie_4 = self.get_entry_value(self.entry_portable_partie_4)
        mail_partie_4 = self.get_entry_value(self.entry_mail_partie_4)

        message = (
            f"Denomination : {denomination}\n"
            f"Adresse : {adresse_partie_1}\n"
            f"Type d_activite : {type_activite}\n"
            f"Numero de detenteur (SIRE) : {num_detenteur}\n"
            f"Titre : {titre}\n"
            f"Prenom : {prenom}\n"
            f"Nom d'usage : {nom_usage}\n"
            f"NUMAGRIT : {numagrit}\n"
            f"Adresse : {adresse_partie_3}\n"
            f"Telephone : {tel}\n"
            f"Portable : {portable}\n"
            f"Adresse e-mail : {mail}\n"
            f"Prenom : {prenom_4}\n"
            f"Nom d'usage : {nom_usage_partie_4}\n"
            f"Adresse : {adresse_partie_4}\n"
            f"Telephone : {tel_partie_4}\n"
            f"Portable : {portable_partie_4}\n"
            f"Adresse e-mail : {mail_partie_4}"
        )

        messagebox.showinfo("Récapitulatif des informations", message)
        self.destroy()  # Ferme la fenêtre actuelle
        # Exécute le script Python externe
        subprocess.run(["python", "/Creation_dun_logiciel_de_Registre_delevage/view/Accueil.py"])
            # Redimensionner le canevas lorsque la taille de la fenêtre change
        #self.bind("<Configure>", self.redimensionner_canevas)
    
    def creacompte(self):
        comptes = {
            "Denomination": self.entry_denomination.get(),
            "Adresse": self.entry_adresse_partie_1.get(),
            "Type d_activite": self.entry_type_activite.get(),
            "Numero de detenteur (SIRE)" : self.entry_num_detenteur.get(),
            "Titre": self.entry_titre.get(),
            "Prenom": self.entry_prenom.get(),
            "Nom d'usage": self.entry_nom_usage.get(),
            "NUMAGRIT": self.entry_numagrit.get(),
            "Adresse": self.entry_adresse_partie_3.get(),
            "Telephone": self.entry_tel.get(),
            "Portable": self.entry_portable.get(),
            "Adresse e-mail": self.entry_mail.get(),
            "Prenom": self.entry_prenom_4.get(),
            "Nom d'usage": self.entry_nom_usage_partie_4.get(),
            "Adresse": self.entry_adresse_partie_4.get(),
            "Telephone": self.entry_tel_partie_4.get(),
            "Portable": self.entry_portable_partie_4.get(),
            "Mail": self.entry_mail_partie_4.get()
        }

        try:
            with open('view/comptes_particuliers.json', 'r') as json_file:
                comptes_data = json.load(json_file)["comptes"]
        except (FileNotFoundError, json.JSONDecodeError):
            comptes_data = []

        comptes_data.append(comptes)

        with open('view/comptes_particuliers.json', 'w') as json_file:
            json.dump({"comptes": comptes_data}, json_file, indent=4)

if __name__ == "__main__":
    fenetre_principale = FenetrePrincipale()
    fenetre_principale.mainloop()
