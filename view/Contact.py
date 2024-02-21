import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import glob

class FenetrePrincipale(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Page de contact")
        self.geometry("1920x1080")
        self.iconbitmap("/Creation_dun_logiciel_de_Registre_delevage/images/horse_sans_fond.ico")

        # Ajout de la phrase au centre
        etiquette_bienvenue = tk.Label(self, text="Voici la page qui vous permet de nous contacter.", font=("Helvetica", 16, "bold"))
        etiquette_bienvenue.pack(side="top", pady=20)

        # Création du Label pour afficher les images
        self.label_image = tk.Label(self, bd=0, highlightthickness=0)
        self.label_image.pack(side="bottom", fill="both", expand=True)

        # Gestionnaire d'événements pour détecter les changements de taille de fenêtre
        self.bind("<Configure>", self.redimensionner_image)

        # Appel à la méthode pour gérer le fond d'image changeant
        self.setup_background_animation()

        # Création du conteneur pour les champs de saisie
        self.formulaire_frame = tk.Frame(self)
        self.formulaire_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Création des étiquettes, champs de saisie et bouton
        label_nom = tk.Label(self.formulaire_frame, text="Nom:")
        label_nom.grid(row=0, column=0, padx=10, pady=5)
        champ_nom = tk.Entry(self.formulaire_frame)
        champ_nom.grid(row=0, column=1, padx=10, pady=5)

        label_email = tk.Label(self.formulaire_frame, text="E-mail:")
        label_email.grid(row=1, column=0, padx=10, pady=5)
        champ_email = tk.Entry(self.formulaire_frame)
        champ_email.grid(row=1, column=1, padx=10, pady=5)

        label_message = tk.Label(self.formulaire_frame, text="Message:")
        label_message.grid(row=2, column=0, padx=10, pady=5)
        champ_message = tk.Text(self.formulaire_frame, height=10, width=30)
        champ_message.grid(row=2, column=1, padx=10, pady=5)

        bouton_envoyer = tk.Button(self.formulaire_frame, text="Envoyer", command=lambda: self.envoyer_message(champ_nom, champ_email, champ_message))
        bouton_envoyer.grid(row=3, column=0, columnspan=2, pady=10)

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

    def envoyer_message(self, champ_nom, champ_email, champ_message):
        # Vérification s'il y a quelque chose dans les champs d'e-mail et de message
        if champ_email.get() and champ_message.get("1.0", 'end-1c'):
            # Logique d'envoi du message ici
            print("Message envoyé !")

            # Boîte de message indiquant que le message est envoyé
            messagebox.showinfo("Message envoyé", "Votre message a été envoyé avec succès!")

            # Effacer les champs du formulaire après l'envoi
            champ_nom.delete(0, 'end')
            champ_email.delete(0, 'end')
            champ_message.delete("1.0", 'end')
        else:
            # Afficher un avertissement si l'e-mail ou le message est manquant
            messagebox.showwarning("Champs manquants", "Veuillez remplir les champs E-mail et Message.")

if __name__ == "__main__":
    fenetre_principale = FenetrePrincipale()
    fenetre_principale.mainloop()
