import json
from tkinter import *
from tkinter import ttk 
import os


def charger_donnees():
    with open('lieux.json', 'r') as file:
        data = json.load(file)
    return data['lieux']

def ouvrir_open_new_window():
    fen1.destroy()  # Ferme la fenêtre actuelle
    # Crée une nouvelle fenêtre (remplacez "test_q.py" par le chemin réel de votre fichier)
    os.system("python test_q.py")

def charger_donnees_equide():
    with open('equide.json', 'r') as file_equide:
             data = json.load(file_equide)
    return data['equides']

def afficher_info_lieu(ville):

    for lieu in lieux:
        if lieu['ville'] == ville:
            ville = lieu.get('ville', '')
            adresse=lieu.get('adresse','')
            region = lieu.get('region', '')
            departement = lieu.get('departement', 0)
            
            # Ajouter une condition pour afficher les informations seulement si la ville est l'une des trois actions spécifiques
            if ville in ['Paris', 'Bobigny', 'Marseilles']:
                city_frame.config(text=f'Ville: {ville}', fg='black')
                region_frame.config(text=f'Région: {region}', fg='black')
                Departement_frame.config(text=f'Département: {departement}', fg='black')
                #effacer le tableau existant
                for item in tree.get_children():
                    tree.delete(item)
                
                for equide in equides:

                     nom=equide.get('nom')
                     race=equide.get('race')
                     poids=equide.get('poids')
                     adresse_equide=equide.get('adresse')
                     if adresse_equide==adresse:
                        
                        tree.insert('','end',values=(nom,race,poids))
                        # liste_equides_affiches.append({
                        # 'nom': nom,
                        # 'race': race,
                        # 'poids': poids
                        # })
                        # rajouter le cheval à la liste de chevaux
                        # ensuite parcourir la liste et rajouter un panel à chaques éléments de la liste
                        # for equides2 in liste_equides_affiches:
                         

                        #  col_titles = ["nom", "Race", "no_sir", "adresse", "age", "poids"]
                        #  label_principal = Label(fenetre, text="Intervention et soins courant")
                        #  label_principal.pack()
                        #  fenetre_principale = Soins_cournat(fenetre, height=3, width=6, col_titles=col_titles)
                        #  label_frame6.config(text=f'nom: {equides2["nom"]}', fg='black')
                        #  label_frame7.config(text=f'race: {equides2["race"]}', fg='black')
                        #  label_frame8.config(text=f'poids: {equides2["poids"]}', fg='black')
            else:
                city_frame.config(text='', fg='black')
                region_frame.config(text='', fg='black')
                Departement_frame.config(text='', fg='black')

# Initialisation de l'interface graphique
fen1 = Tk()
image = PhotoImage(file="white_horse.png")
tex1 = Label(fen1, text='Quelle Ville voulez vous choisir ?', fg='black')
tex1.pack(side=TOP)

# Charger les données depuis le fichier JSON
lieux = charger_donnees()
equides=charger_donnees_equide()
liste_equides_affiches = []

# Créer une liste déroulante avec les villes disponibles
options_villes = [lieu.get('ville', lieu.get('Ville', '')) for lieu in lieux]
var_ville = StringVar(fen1)
var_ville.set(options_villes[0])  # Définit la première ville comme valeur par défaut
menu_deroulant_ville = OptionMenu(fen1, var_ville, *options_villes)
menu_deroulant_ville.pack(side=TOP)

frame2 = Frame(fen1, bg='deepskyblue', height=200, width=200)
frame2.pack(side=LEFT)

city_frame = Label(frame2, text='', fg='black')
region_frame = Label(frame2, text='', fg='black')
Departement_frame = Label(frame2, text='', fg='black')

label_frame6 = Label(frame2, text='', fg='black')
label_frame7 = Label(frame2, text='', fg='black')
label_frame8 = Label(frame2, text='', fg='black')

boutton =Button(frame2,text='',fg='black')


city_frame.pack(side=TOP)
region_frame.pack(side=TOP)
Departement_frame.pack(side=TOP)

label_frame6.pack(side=BOTTOM)
label_frame7.pack(side=BOTTOM)
label_frame8.pack(side=BOTTOM)

# Créer le tableau
tree = ttk.Treeview(frame2, columns=('Nom', 'Race', 'Poids'), show='headings')
tree.heading('Nom', text='Nom')
tree.heading('Race', text='Race')
tree.heading('Poids', text='Poids')
tree.pack(side=TOP)

# Définir l'action à effectuer lorsque la valeur du menu déroulant change
var_ville.trace("w", lambda *args: afficher_info_lieu(var_ville.get()))
can1 = Canvas(fen1, bg='cyan', height=500, width=500)
can1.create_image(0, 0, anchor=NW, image=image)
can1.pack(side=TOP)

fen1.mainloop()
