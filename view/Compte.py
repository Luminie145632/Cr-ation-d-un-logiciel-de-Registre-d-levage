import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import glob  # Importez le module glob

class FenetrePrincipale(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Accueil")
        self.geometry("1920x1080")
        self.iconbitmap("/Creation_dun_logiciel_de_Registre_delevage/images/horse_sans_fond.ico")

        message_label = tk.Label(self, text="Bienvenue, veuillez vous connecter à votre compte pour accéder à vos informations.\nSi vous n'avez pas de compte, nous vous invitons à créer un compte.", font=("Helvetica", 24, "bold"))
        message_label.pack(pady=20)

        self.canvas = tk.Canvas(self, width=1920, height=800)
        self.canvas.pack()

        self.label_image = tk.Label(self.canvas)
        self.label_image.pack(fill=tk.BOTH, expand=tk.YES)

        self.setup_background_animation()

        btn_creation = ttk.Button(self, text="Création d'un compte", command=self.executer_script_creation_compte, style="TButton")
        self.canvas.create_window(950, 200, window=btn_creation, anchor='center')

        btn_connexion = ttk.Button(self, text="Connexion", command=self.on_connexion_click, style="TButton")
        self.canvas.create_window(950, 250, window=btn_connexion, anchor='center')

    def on_connexion_click(self):
        print("Bouton Connexion cliqué")

    def executer_script_creation_compte(self):
        try:
            # Exécutez le script Python depuis un fichier externe
            with open("/Creation_dun_logiciel_de_Registre_delevage/view/Creation_identifiant_code_PIN.py", "r") as script_file:
                script_code = script_file.read()
                exec(script_code)
        except Exception as e:
            print(f"Une erreur s'est produite : {e}")

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

    def redimensionner_image(self, event):
        image_path = self.image_paths[self.current_image_index]
        image = Image.open(image_path)
        image = image.resize((self.winfo_width(), self.winfo_height()))
        photo = ImageTk.PhotoImage(image)
        self.label_image.configure(image=photo)
        self.label_image.image = photo

if __name__ == "__main__":
    fenetre_principale = FenetrePrincipale()
    fenetre_principale.mainloop()
