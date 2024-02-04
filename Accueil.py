import tkinter as tk
from tkinter import ttk
from liaison_pages import LiaisonPages
import os

class FenetrePrincipale(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Accueil")
        self.geometry("1920x1080")  # Taille de la fenêtre ajustée
        self.iconbitmap("horse_sans_fond.ico")

        # Ajout de la phrase "Bienvenue sur notre application." au centre
        etiquette_bienvenue = ttk.Label(self, text="Bienvenue sur notre application.", font=("Helvetica", 16, "bold"))
        etiquette_bienvenue.pack(side="top", pady=20)

        # Création de la barre de navigation
        navbar = tk.Frame(self, bd=2, relief=tk.GROOVE)
        navbar.pack(side="top", fill="x")

        # Création des boutons de la barre de navigation
        btn_mouvement_temporaire = ttk.Button(navbar, text="Mouvement Temporaire", command=  self.ouvrir_nouvelle_fenetre )#self.signaler_mouvement_temporaire)
        btn_mouvement_temporaire.pack(side="left", expand=True, fill='both')

        btn_lieux_detention = ttk.Button(navbar, text="Lieux de Détention", command=self.ouvrir_fenetre_Lieu_detention)
        btn_lieux_detention.pack(side="left", expand=True, fill='both')

        btn_presence_caracteristiques = ttk.Button(navbar, text="Présence et Caractéristiques", command=self.renseigner_presence_caracteristiques)
        btn_presence_caracteristiques.pack(side="left", expand=True, fill='both')

        btn_interventions = ttk.Button(navbar, text="Interventions", command=self.ouvrir_fenetre_Lieu_caratheristiques)
        btn_interventions.pack(side="left", expand=True, fill='both')

        # Ajout d'un séparateur pour plus de clarté
        ttk.Separator(navbar, orient="vertical").pack(side="left", padx=5)

        # Ajoutez d'autres boutons de la barre de navigation si nécessaire

    def signaler_mouvement_temporaire(self):
        print("Bouton Signal Mouvement Temporaire cliqué")
    def ouvrir_nouvelle_fenetre(self):
     self.destroy()  # Ferme la fenêtre actuelle
     # Crée une nouvelle fenêtre (remplacez "test_q.py" par le chemin réel de votre fichier)
     os.system("python Page_1_mouvements_temporaires_des_animaux.py")
     
    def ouvrir_fenetre_Lieu_detention(self):
      self.destroy()  # Ferme la fenêtre actuelle
     # Crée une nouvelle fenêtre (remplacez "test_q.py" par le chemin réel de votre fichier)
      os.system("python Lieu_detention.py")

    def ouvrir_fenetre_Lieu_caratheristiques(self):
      self.destroy()  # Ferme la fenêtre actuelle
     # Crée une nouvelle fenêtre (remplacez "test_q.py" par le chemin réel de votre fichier)
      os.system("Page_caractéristique_du_lieu_de_detention.py")
     


    def acceder_lieux_detention(self):
        print("Bouton Accéder aux Lieux de Détention cliqué")

    def renseigner_presence_caracteristiques(self):
        print("Bouton Renseigner Présence et Caractéristiques cliqué")

    def renseigner_intervention(self):
        print("Bouton Renseigner Intervention cliqué")


if __name__ == "__main__":
    fenetre_principale = FenetrePrincipale()
    fenetre_principale.mainloop()
