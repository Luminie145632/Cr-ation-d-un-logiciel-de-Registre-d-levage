import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import glob
import random
import string

class FenetrePrincipale(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Formulaire d'inscription")
        self.geometry("800x600")

        etiquette_bienvenue = tk.Label(self, text="Veuillez remplir les champs du formulaire d'inscription.", font=("Helvetica", 16, "bold"))
        etiquette_bienvenue.pack(side="top", pady=20)

        self.label_image = tk.Label(self, bd=0, highlightthickness=0)
        self.label_image.pack(side="bottom", fill="both", expand=True)

        self.bind("<Configure>", self.redimensionner_image)
        self.setup_background_animation()

        self.formulaire_frame = tk.Frame(self)
        self.formulaire_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Initialisation des valeurs par défaut
        self.initial_values = {}

        # Création des champs de saisie et des labels
        self.create_label_entry("N° SIRET :", "entry_siret", "Saisissez votre N° SIRET", required=True)
        self.create_label_entry("Code APE :", "entry_code_ape", "Saisissez votre Code APE", required=True)
        self.create_label_entry("Saisisez votre statut juridique (facultatif) :", "entry_statut_juridique", "Facultatif", required=False)
        self.create_label_entry("Saisisez votre dénomination :", "entry_denomination", "Facultatif", required=False)
        self.create_label_entry("Saisisez votre adresse :", "entry_adresse", "Saisissez votre adresse", required=True)
        self.create_label_entry("Saisisez votre tél :", "entry_tel", "Saisissez le numéro de votre téléphone", required=True)
        self.create_label_entry("Saisisez votre portable :", "entry_portable", "Saisissez le numéro de votre portable", required=True)
        self.create_label_entry("Saisisez votre mail :", "entry_mail", "Saisissez votre adresse e-mail", required=True)

        btn_soumettre = tk.Button(self.formulaire_frame, text="Valider", command=self.soumettre_formulaire)
        btn_soumettre.grid(row=len(self.formulaire_frame.grid_slaves()), column=0, columnspan=2, pady=10)

    def create_label_entry(self, label_text, entry_name, placeholder_text, required=True):
        label_frame = tk.Frame(self.formulaire_frame)
        label_frame.grid(sticky="e", row=len(self.formulaire_frame.grid_slaves()) // 2, column=0, padx=10, pady=5)

        if required:
            ast_label = tk.Label(label_frame, text="*", fg="red")
            ast_label.grid(row=0, column=0, padx=(0, 5))

        label = tk.Label(label_frame, text=label_text)
        label.grid(row=0, column=1)

        # Utilisation d'une variable de contrôle pour gérer le placeholder
        entry_var = tk.StringVar()
        entry = tk.Entry(self.formulaire_frame, textvariable=entry_var, fg="grey")
        entry.grid(sticky="w", row=len(self.formulaire_frame.grid_slaves()) // 2, column=1, padx=10, pady=5)
        entry.insert(0, placeholder_text)  # Initialisation du placeholder
        entry.bind("<FocusIn>", lambda event, var=entry_var: self.on_entry_focus_in(var, placeholder_text))
        entry.bind("<FocusOut>", lambda event, var=entry_var: self.on_entry_focus_out(var, placeholder_text))
        setattr(self, entry_name, entry)
        self.initial_values[entry_name] = entry_var  # Ajout de la variable à initial_values

    def on_entry_focus_in(self, var, placeholder_text):
        if var.get() == placeholder_text:
            var.set('')
            entry.config(fg='black')  # Changez la couleur du texte lorsque vous entrez dans le champ

    def on_entry_focus_out(self, var, placeholder_text):
        if not var.get():
            var.set(placeholder_text)
            entry.config(fg='grey')  # Changez la couleur du texte lorsque vous quittez le champ

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

        for child in self.label_image.winfo_children():
            child.lift()

        self.after(2000, self.load_image)

    def redimensionner_image(self, event):
        image_path = self.image_paths[self.current_image_index]
        image = Image.open(image_path)
        image = image.resize((self.winfo_width(), self.winfo_height()))
        photo = ImageTk.PhotoImage(image)
        self.label_image.configure(image=photo)
        self.label_image.image = photo

    def generer_identifiant(self, nom, prenom):
        identifiant = (nom[:3] + prenom[:3]).lower()
        return identifiant

    def generer_code(self):
        code = ''.join(random.choices(string.digits, k=6))
        return code

    def soumettre_formulaire(self):
        # Récupération des valeurs des champs
        siret = self.entry_siret.get()
        code_ape = self.entry_code_ape.get()
        statut_juridique = self.entry_statut_juridique.get()
        denomination = self.entry_denomination.get()
        adresse = self.entry_adresse.get()
        tel = self.entry_tel.get()
        portable = self.entry_portable.get()
        mail = self.entry_mail.get()

        # Vérification des champs obligatoires
        if not siret or not code_ape or not adresse or not tel or not portable or not mail:
            messagebox.showerror("Erreur", "Veuillez remplir tous les champs obligatoires.")
            return

        # Vérification des champs modifiés
        for entry_name, entry_var in self.initial_values.items():
            entry = getattr(self, entry_name)
            if entry.get() == entry_var.get():
                messagebox.showerror("Erreur", f"{entry_name} doit être modifié.")
                return

        # Affichage des informations dans une boîte de dialogue
        message = f"N° SIRET: {siret}\nCode APE: {code_ape}\nStatut juridique: {statut_juridique}\nDénomination: {denomination}\nAdresse: {adresse}\nTél: {tel}\nPortable: {portable}\nMail: {mail}"
        messagebox.showinfo("Formulaire d'inscription", message)

if __name__ == "__main__":
    fenetre_principale = FenetrePrincipale()
    fenetre_principale.mainloop()
