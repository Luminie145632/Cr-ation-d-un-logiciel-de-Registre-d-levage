import tkinter as tk

class FenetrePrincipale(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Accueil")
        self.geometry("1920x1080")
        self.iconbitmap("horse_sans_fond.ico")

        label_principal = tk.Label(self, text="Accueil")
        label_principal.pack()

    
def on_creation_click():
    print("Bouton Création cliqué")

def create_window():
    window = tk.Tk()
    window.title("Fenêtre avec Boutons")

    # Création du bouton Connexion
    btn_connexion = tk.Button(window, text="Connexion", command=on_connexion_click)
    btn_connexion.pack(pady=10)

    # Création du bouton Création
    btn_creation = tk.Button(window, text="Création", command=on_creation_click)
    btn_creation.pack(pady=10)

if __name__ == "__main__":
    fenetre_principale = FenetrePrincipale()
    fenetre_principale.mainloop()