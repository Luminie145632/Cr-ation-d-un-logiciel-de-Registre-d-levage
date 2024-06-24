from tkinter import *
from PIL import Image, ImageTk
import os
import json
import glob

class Soins_cournat(Frame):
    def __init__(self, fenetre, height, width, col_titles):
        super().__init__(fenetre)
        self.numberLines = height
        self.numberColumns = width
        self.col_titles = col_titles
        self.pack(fill=BOTH)

        fenetre.title("Encadrement Zootechnique Sanitaire et Médical des Animaux")
        fenetre.geometry("1920x1080")  
        fenetre.iconbitmap("/Creation_dun_logiciel_de_Registre_delevage/images/horse_sans_fond.ico")

        # Canvas pour l'animation d'arrière-plan
        self.canvas = Canvas(fenetre, bg='blue', width=1920, height=1080)
        self.canvas.pack(fill=BOTH, expand=True)

        # Animation d'arrière-plan
        self.setup_background_animation()

        # Cadre pour le contenu
        self.content_frame = Frame(self.canvas, bg="white")
        self.canvas.create_window(0, 0, window=self.content_frame, anchor='nw')

        # Titre
        self.title_label = Label(self.content_frame, text='Encadrement Zootechnique Sanitaire et Médical des Animaux', font=("Helvetica", 14, "bold"), bg="white")
        self.title_label.grid(row=0, column=0, columnspan=self.numberColumns, sticky='ew')

        # Ajout des titres de colonnes
        self.create_table_headers()

        # Ajout des données du tableau
        self.create_table_data()

        # Centrer le cadre principal dans la fenêtre
        fenetre.update_idletasks()  # Mettre à jour la fenêtre
        width = fenetre.winfo_width()
        height = fenetre.winfo_height()
        x = (fenetre.winfo_screenwidth() // 2) - (width // 2)
        y = (fenetre.winfo_screenheight() // 2) - (height // 2)
        fenetre.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def setup_background_animation(self):
        self.image_paths = glob.glob("/Creation_dun_logiciel_de_Registre_delevage/images/*.png")
        self.current_image_index = 0
        self.load_image()

    def load_image(self):
        image_path = self.image_paths[self.current_image_index]
        original_image = Image.open(image_path)
        original_image = original_image.resize((1920, 1080))
        self.photo = ImageTk.PhotoImage(original_image)

        self.canvas.create_image(0, 0, anchor=NW, image=self.photo)

        self.current_image_index = (self.current_image_index + 1) % len(self.image_paths)
        self.after(6000, self.load_image)

    def create_table_headers(self):
        # Ajout des titres de colonnes
        for j in range(self.numberColumns):
            col_title = Label(self.content_frame, text=self.col_titles[j], width=20, relief="solid", bg="lightgray", anchor="center")
            col_title.grid(row=1, column=j, sticky='ew')

    def create_table_data(self):
        # Ajout des données du tableau
        self.data = []
        for i in range(2, self.numberLines + 2):
            line = []
            for j in range(self.numberColumns):
                cell = Entry(self.content_frame, width=20, justify='center')
                cell.grid(row=i, column=j, sticky='nsew')  # Utilisation de 'nsew' pour centrer le contenu
                line.append(cell)
            self.data.append(line)

        # Bouton pour ajouter une nouvelle ligne
        self.bouton_ajouter_ligne = Button(self.content_frame, text="Ajouter une ligne", command=self.ajouter_ligne, width=20, height=1)
        self.bouton_ajouter_ligne.grid(row=self.numberLines + 2, columnspan=self.numberColumns, sticky='ew')

        btn_mouvement_temporaire = Button(self.content_frame, text="Retour au menu principal", command=self.return_main_menu, width=20, height=1)
        btn_mouvement_temporaire.grid(row=self.numberLines + 3, columnspan=self.numberColumns, sticky='ew')

        btn_mouvement_temporaire = Button(self.content_frame, text="Valider", command=self.valider_informations, width=20, height=1)
        btn_mouvement_temporaire.grid(row=self.numberLines + 4, columnspan=self.numberColumns, sticky='ew')

        btn_valider = Button(self.content_frame, text="Consulter l'historique de mes Soins", command=self.view_animals)
        btn_valider.grid(row=self.numberLines + 5, column=0, columnspan=self.numberColumns, sticky='ew')

    def view_animals(self):
        with open('Soins_Courant.json', 'r') as file:
            data = json.load(file)
            
        text_field = Text(self.content_frame, wrap=WORD)
        text_field.grid(row=self.numberLines + 6, column=0, columnspan=self.numberColumns, sticky='ew')
        text_field2 = Text(self.content_frame, wrap=WORD)
        text_field2.grid(row=self.numberLines + 7, column=0, columnspan=self.numberColumns, sticky='ew')
        for animal in data:
            text_field.insert(END, f"Date: {animal.get('Date','')}\n")
            text_field.insert(END, f"Numéro SIRE: {animal.get('type_intervention', '')}\n")
            text_field.insert(END, f"Nom du medicament: {animal.get('Nom du medicament', '')}\n")
            text_field.insert(END, f"Voie administration: {animal.get('Voie administration', '')}\n")
            text_field2.insert(END, f"Date dedebut: {animal.get('Date dedebut', '')}\n")
            text_field2.insert(END, f"Date dedefin: {animal.get('Date dedefin', '')}\n")
            text_field2.insert(END, f"N_ordonnance: {animal.get('N_ordonnance', '')}\n\n")
            text_field2.insert(END, f": {animal.get('Delai_attente_competition', '')}\n\n")
            text_field2.insert(END, f"Delai_attente_abattage: {animal.get('Delai_attente_abattage', '')}\n\n")
            
        self.adjust_columns_width()

    def adjust_columns_width(self):
        for j in range(self.numberColumns):
            max_width = max(cell.winfo_reqwidth() for row in self.data for cell in row)
            self.content_frame.grid_columnconfigure(j, weight=1)  # Ajuster la largeur des colonnes

    def return_main_menu(self):
        self.destroy()
        os.system("python Accueil.py")
        
    def valider_informations(self):
        mouvements_temporaires = []
        for row in self.data:
            mouvement = {
                "Date": row[0].get(),
                "Type_intervention": row[1].get(),
                "Intervenant": row[2].get(),
                "Traitement": {
                    "Nom du medicament": row[3].get(),
                    "Voie administration": row[4].get(),
                    "Date dedebut": row[5].get(),
                    "Date dedefin": row[6].get(),
                },
                "N_ordonnance": row[7].get(),
                "Delai_attente_competition": row[8].get(),
                "Delai_attente_abattage": row[9].get()
            }   
            mouvements_temporaires.append(mouvement)

        with open('/Creation_dun_logiciel_de_Registre_delevage/view/Soins_Courant.json', 'w') as f:
            json.dump(mouvements_temporaires, f, indent=4)

    def ajouter_ligne(self):
        self.bouton_ajouter_ligne.grid_forget()

        nouvelle_ligne = []
        for j in range(self.numberColumns):
            cell = Entry(self.content_frame, width=20, justify='center')  
            cell.grid(row=self.numberLines + 3, column=j, sticky='ew')
            nouvelle_ligne.append(cell)
        self.data.append(nouvelle_ligne)
        self.numberLines += 1

        self.bouton_ajouter_ligne.grid(row=self.numberLines + 3, columnspan=self.numberColumns, sticky='ew')

if __name__ == "__main__":
    root = Tk()
    root.title("Encadrement Zootechnique Sanitaire et Médical des Animaux")
    root.geometry("1920x1080")  
    root.iconbitmap("/Creation_dun_logiciel_de_Registre_delevage/images/horse_sans_fond.ico")

    col_titles = ["Date", "Type d'intervention", "Intervenant (si vétérianire)", "Traitement", "N ordonnance","Date de début", "Date de fin","N°d’ordonnance","Délai d’attentecompétition(facultatif)","Délai d’attente abatage ou exclusion abattage"]

    fenetre_principale = Soins_cournat(root, height=6, width=10, col_titles=col_titles)
    fenetre_principale.mainloop()
