import tkinter as tk

def create_window():
    window = tk.Tk()
    window.title("CARACTÉRISTIQUES DU LIEU DE DÉTENTION")


    # Configuration de la taille de la fenêtre
    window.geometry("1920x1080")

    # Image du logo de la fenêtre
    window.iconbitmap("/Creation_dun_logiciel_de_Registre_delevage/horse_sans_fond.ico")

    

    # Exécution de la boucle principale
    window.mainloop()

# Appel de la fonction pour créer la fenêtre avec les boutons et le logo
create_window()
