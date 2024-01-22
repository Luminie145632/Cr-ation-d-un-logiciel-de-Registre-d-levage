import tkinter as tk

class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Barre de Navigation")

        # Création de la barre de navigation
        self.navbar = tk.Menu(self)

        # Ajout des éléments de la barre de navigation
        self.navbar.add_command(label="Accueil", command=self.accueil)
        self.navbar.add_command(label="Page 1", command=self.page1)
        self.navbar.add_command(label="Page 2", command=self.page2)
        self.navbar.add_command(label="Quitter", command=self.quit)

        # Configurer la barre de navigation comme barre de menu principale
        self.config(menu=self.navbar)

        # Configurer la fenêtre principale
        self.geometry("400x300")

    def accueil(self):
        print("Affichage de la page d'accueil")

    def page1(self):
        print("Affichage de la page 1")

    def page2(self):
        print("Affichage de la page 2")

if __name__ == "__main__":
    app = Application()
    app.mainloop()
