import tkinter as tk

def on_connexion_click():
    print("Bouton Connexion cliqué")

def on_creation_click():
    print("Bouton Création cliqué")

def create_window():
    window = tk.Tk()
    window.title("Fenêtre avec Boutons")

    # Configuration de la taille de la fenêtre
    window.geometry("300x200")

    # Chemin vers le fichier ICO (remplacez-le par le chemin de votre propre fichier ICO)
    chemin_logo = "chemin/vers/votre/fichier.ico"

    # Modification du logo de la fenêtre
    window.iconbitmap(chemin_logo)

    # Création du bouton Connexion
    btn_connexion = tk.Button(window, text="Connexion", command=on_connexion_click)
    btn_connexion.pack(pady=10)

    # Création du bouton Création
    btn_creation = tk.Button(window, text="Création", command=on_creation_click)
    btn_creation.pack(pady=10)

    # Exécution de la boucle principale
    window.mainloop()

# Appel de la fonction pour créer la fenêtre avec les boutons et le logo
create_window()
