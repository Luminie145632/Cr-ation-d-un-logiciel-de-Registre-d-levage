    #  self.supprimer_widgets()
    #  self.numberLines = width
    #  self.numberColumns = width
     
    #   # Définition des titres des colonnes
    #  self.col_title = ["Nom","NeSIRE","Netranspondeur","Nom proprietaire","Adresse proprietaire","Date de premiere entree", "Adresse de provenance", "Date de sortie definitive", "Adresse de destination"]
    
    #  for j, col_tmp in enumerate(self.col_title):
    #   print("nombres " +str(self.numberColumns))
    #   col_tmp = self.col_title[j]
    #   col_title = tk.Label(self, text=col_tmp, width=28, relief="solid", bg="lightgray")#, anchor="w")
    #   col_title.grid(row=13,column=j,sticky='nsew')  # Utilise sticky pour que la colonne s'adapte

    #  # Ajout des données du tableau
    #  self.data = []
    #  for i in range( 15, 24):
    #     line = []
    #     for j in range(9):
    #         cell = Entry(self, width=28)
    #         cell.grid(row=i, column=j, sticky='nsew')
    #         line.append(cell)
    #     self.data.append(line) 
    #  # Boutons pour ajouter une ligne, valider et consulter les animaux
        
    #  # Configurer la gestion des colonnes pour qu'elles s'adaptent au contenu
    #  for j in range(self.numberColumns):
    #     self.grid_columnconfigure(j, weight=1)     
    #  self.bouton_ajouter_ligne = Button(self, text="Ajouter une ligne", command=self.ajouter_ligne)
    #  self.bouton_ajouter_ligne.grid(row=self.numberLines + 4, columnspan=len(self.col_title), sticky='nsew')
    
    #  btn_valider = Button(self, text="Valider", command= self.valider_caratheristiques_animaux)
    #  btn_valider.grid(row=self.numberLines + 5, columnspan=len(self.col_title), sticky='nsew')
    
    #  btn_consulter_animaux = Button(self, text="Consulter mes animaux", command=self.view_animals)
    #  btn_consulter_animaux.grid(row=self.numberLines + 6, columnspan=len(self.col_title), sticky='nsew')
    #  #open datas functions
    #  # Gestionnaire d'événements pour détecter les changements de taille de fenêtre
    #  self.bind("<Configure>", self.redimensionner_image) 
    
    # def view_animals(self):
    #     print("koko")
    #     with open('caratheristiques_animaux.json', 'r') as file:
    #         data = json.load(file)
        
    #     # Création d'un canevas avec une barre de défilement verticale
    #     self.canvas = tk.Canvas(self)
    #     scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
    #     scrollbar.grid(row=0, column=len(self.col_title), sticky='ns')
    #     self.canvas.config(yscrollcommand=scrollbar.set)
    #     self.canvas.grid(row=15, column=0, columnspan=len(self.col_title), sticky='nsew')
        
    #     # Conteneur pour les champs de texte
    #     # self.frame = tk.Frame(self.canvas)
    #     # self.canvas.create_window((0, 0), window=self.frame, anchor='nw')
         
    #     # Affichage des animaux dans les champs de texte
    #     for i, animal in enumerate(data['caractheristiques'], start=15):
    #         text_fields = []
    #         for j, key in enumerate(self.col_title):
    #             # Utilisation de ScrolledText à la place de Entry
    #             text_field = scrolledtext.ScrolledText(self, width=30, height=1)
    #             text_field.grid(row=i, column=j, sticky='nsew')  
                
    #             text_field = Entry(self.frame, width=3)
    #             text_field.grid(row=i, column=j, sticky='nsew')
    #             value = animal.get(key, '')
    #             text_field.insert(END, f"{key}: {value}\n")
    #             text_fields.append(text_field)
    #         self.data.append(text_fields)

    #     # Bouton pour ajouter une ligne
    #     self.bouton_ajouter_ligne = Button(self.frame, text="Ajouter une ligne", command=self.ajouter_ligne)
    #     self.bouton_ajouter_ligne.grid(row=self.numberLines + 4, columnspan=len(self.col_title), sticky='nsew')
         
    #     # # Bouton pour modifier les informations
    #     # btn_valider = Button(self.frame, text="Modifier les informations", command=self.valider_caratheristiques_animaux)
    #     # btn_valider.grid(row=self.numberLines + 5, columnspan=len(self.col_title), sticky='nsew')

    #     # Redimensionner le canevas lorsque la taille de la fenêtre change
    #     self.bind("<Configure>", self.redimensionner_canevas)  


  # def view_animals(self):
    
    #  with open('caratheristiques_animaux.json', 'r') as file:
    #     data = json.load(file)
    
    # # Affichage des animaux dans les zones de texte
    #  for i, animal in enumerate(data['caractheristiques'], start=15):
    #     text_fields = []

    #     for j, key in enumerate(self.col_title):
    #         text_field = Entry(self, width=3)
    #         text_field.grid(row=i, column=j, sticky='nsew')
    #         # Récupérer la valeur de la clé si elle existe, sinon utiliser une chaîne vide
    #         value = animal.get(key, '')
    #         text_field.insert(END, f"{key}: {value}\n")
    #         text_fields.append(text_field)
    #     self.data.append(text_fields)
        
    #  self.bouton_ajouter_ligne = Button(self, text="Ajouter une ligne", command=self.ajouter_ligne)
    #  self.bouton_ajouter_ligne.grid(row=self.numberLines + 4, columnspan=len(self.col_title), sticky='nsew')
    
    #  btn_valider = Button(self, text="Modifier les informations", command=self.valider_caratheristiques_animaux)
    #  btn_valider.grid(row=self.numberLines + 5, columnspan=len(self.col_title), sticky='nsew')  
    # def setup_background_animation(self):       
    #  try: 
    #   self.image_paths = glob.glob("/Creation_dun_logiciel_de_Registre_delevage/images/*.png")

    #   image_path = self.image_paths[self.current_image_index]
    #   image = Image.open(image_path)
    #   image = image.resize((self.winfo_width(), self.winfo_height()))
        
    #   photo = ImageTk.PhotoImage(image)
    #   self.label_image.configure(image=photo)
    #   self.label_image.image = photo
     
    #   for child in self.label_image.winfo_children():
    #     child.lift()
    #  except Exception:
    #    print("ça marche pas") 

    #valider les informations         




      # Configuration du Canvas pour le défilement
       # self.create_window((0, 0), window=self, anchor='nw')
        #ajouter dans le navbar
     

        # Barre de défilement verticale pour le Canvas
        # scrollbar = tk.Scrollbar(self, orient="vertical", command=self.navbar_canvas.yview)
        # scrollbar.grid(row=10, column=len(self.col_title)+1, sticky='ns')
        # self.navbar_canvas.config(yscrollcommand=scrollbar.set)
   
        # # Configuration du Canvas pour le défilement
        # self.navbar_canvas.create_window((0, 0), window=self.navbar_frame, anchor='nw')



        # Gestionnaire d'événements pour détecter les changements de taille de fenêtre
       # self.bind("<Configure>", self.redimensionner_image)

        # Appel à la méthode pour gérer le fond d'image changeant
    # def view_zootechnical_supervision(self):
    
    #  with open('encadrement_zootechnique.json', 'r') as file:
    
    #     data = json.load(file)

    #     # Parcourir les données
    #     for i, element in enumerate(data['encadrement'], start=1):
    #         text_fields = []

    #         # Parcourir les clés des sous-dictionnaires
    #         for key in element:
    #             # Récupérer la valeur correspondante à la clé
    #             value = element[key]

    #             # Trouver l'index de la colonne correspondant à la clé
    #             col_index = self.col_title.index(key)

    #             # Insérer la valeur dans le champ d'entrée correspondant
    #             entry = self.data[i-1][col_index]
    #             entry.delete(0, 'end')  # Supprimer le contenu précédent
    #             entry.insert(0, value)  # Insérer la nouvelle valeur

    # # Ajouter les boutons en dehors de la boucle pour éviter la duplication
    #  self.bouton_ajouter_ligne = Button(self, text="Ajouter une ligne", command=self.ajouter_ligne)
    #  self.bouton_ajouter_ligne.grid(row=self.numberLines + 4, columnspan=len(self.col_title), sticky='nsew')

    #  btn_valider = Button(self, text="Modifier les informations", command=self.valider_encadrement_Zootechnique_animaux)
    #  btn_valider.grid(row=self.numberLines + 5, columnspan=len(self.col_title), sticky='nsew')
    # def view_control(self):
    
    #  with open('controles.json', 'r') as file:
    #     data = json.load(file)

    #     # Parcourir les données
    #     for i, element in enumerate(data['controle'], start=1):
    #         text_fields = []

    #         # Parcourir les clés des sous-dictionnaires
    #         for key in element:
    #             # Récupérer la valeur correspondante à la clé
    #             value = element[key]

    #             # Trouver l'index de la colonne correspondant à la clé
    #             col_index = self.col_title.index(key)

    #             # Vérifier si l'indice i est valide pour self.data
    #             if i < len(self.data):
    #                 # Insérer la valeur dans le champ d'entrée correspondant
    #                 entry = self.data[i - 1][col_index]
    #                 entry.delete(0, 'end')  # Supprimer le contenu précédent
    #                 entry.insert(0, value)  # Insérer la nouvelle valeur
    #             else:
    #                 print(f"Erreur: L'indice {i} dépasse la taille de self.data.")

    # # Ajouter les boutons en dehors de la boucle pour éviter la duplication
    #  self.bouton_ajouter_ligne = Button(self, text="Ajouter une ligne", command=self.ajouter_ligne)
    #  self.bouton_ajouter_ligne.grid(row=self.numberLines + 4, columnspan=len(self.col_title), sticky='nsew')

    #  btn_valider = Button(self, text="Modifier les informations", command=lambda: self.valider_informations_controle())
    #  btn_valider.grid(row=self.numberLines + 5, columnspan=len(self.col_title), sticky='nsew')       
    # def view_temporary_movements(self):
    #  #  self.supprimer_widgets()
     
    #   # Définition des titres des colonnes
    #   # self.col_title = ["Date de sortie", "Nom equide", "Motif", "Etape eventuelle (adresse)", "Lieu de destination (Adresse)", "Date de retour"]
    #    with open('mouvements_temporaires.json', 'r') as file:
    #     data = json.load(file)

    #     # Parcourir les données
    #     for i, element in enumerate(data['mouvements_temporaires'], start=1):
    #         text_fields = []

    #         # Parcourir les clés des sous-dictionnaires
    #         for key in element:
    #             # Récupérer la valeur correspondante à la clé
    #             value = element[key]

    #             # Trouver l'index de la colonne correspondant à la clé
    #             col_index = self.col_title.index(key)

    #             # Vérifier si l'indice i est valide pour self.data
    #             if i < len(self.data):
    #                 # Insérer la valeur dans le champ d'entrée correspondant
    #                 entry = self.data[i - 1][col_index]
    #                 entry.delete(0, 'end')  # Supprimer le contenu précédent
    #                 entry.insert(0, value)  # Insérer la nouvelle valeur
    #             else:
    #                 print(f"Erreur: L'indice {i} dépasse la taille de self.data.")

    # # Ajouter les boutons en dehors de la boucle pour éviter la duplication
    #     self.bouton_ajouter_ligne = Button(self, text="Ajouter une ligne", command=self.ajouter_ligne)
    #     self.bouton_ajouter_ligne.grid(row=self.numberLines + 4, columnspan=len(self.col_title), sticky='nsew')

    #     btn_valider = Button(self, text="Modifier les informations", command=lambda: self.valider_informations_controle())
    #     btn_valider.grid(row=self.numberLines + 5, columnspan=len(self.col_title), sticky='nsew')   
    # def view_informations_intervention(self):
       
    #  with open('Soins_Courant.json', 'r') as file:
    #     data = json.load(file)

    #     # Parcourir les données
    #     for i, element in enumerate(data['interventions'], start=1):
    #         text_fields = []

    #         # Parcourir les clés des sous-dictionnaires
    #         for key in element:
    #             # Récupérer la valeur correspondante à la clé
    #             value = element[key]

    #             # Trouver l'index de la colonne correspondant à la clé
    #             col_index = self.col_title.index(key)

    #             # Vérifier si l'indice i est valide pour self.data
    #             if i < len(self.data):
    #                 # Insérer la valeur dans le champ d'entrée correspondant
    #                 entry = self.data[i - 1][col_index]
    #                 entry.delete(0, 'end')  # Supprimer le contenu précédent
    #                 entry.insert(0, value)  # Insérer la nouvelle valeur
    #             else:
    #                 print(f"Erreur: L'indice {i} dépasse la taille de self.data.")

    # # Ajouter les boutons en dehors de la boucle pour éviter la duplication
    #  self.bouton_ajouter_ligne = Button(self, text="Ajouter une ligne", command=self.ajouter_ligne)
    #  self.bouton_ajouter_ligne.grid(row=self.numberLines + 4, columnspan=len(self.col_title), sticky='nsew')

    #  btn_valider = Button(self, text="Modifier les informations", command=lambda: self.valider_informations_intervention())
    #  btn_valider.grid(row=self.numberLines + 5, columnspan=len(self.col_title), sticky='nsew')     
    # def view_animals(self):
    #  with open('caratheristiques_animaux.json', 'r') as file:
    #     data = json.load(file)
    
    # # Affichage des animaux dans les zones de texte
    #  for i, animal in enumerate(data['caratheristiques_animaux'], start=15):
    #     text_fields = []
    #     for j, key in enumerate(self.col_title):
    #         text_field = Text(self, wrap=WORD)
    #         text_field.grid(row=i, column=j, sticky='nsew')
    #         value = animal.get(key, '')
    #         text_field.insert(END, f"{key}: {value}\n")
    #         text_fields.append(text_field)
    #     self.data.append(text_fields)
    #     for i in range(15,23):
    #         line = []
    #         for j in range(8):
    #             cell = Entry(self, width=5)
    #             cell.grid(row=i, column=j, sticky='nsew')
    #             line.append(cell)
    #         self.data.append(line)

    #         self.date_sortie=line[1]    

    #  print(" marche pas ")

    # def view_animals(self):
    #     print("koko")
    #     with open('caratheristiques_animaux.json', 'r') as file:
    #         data = json.load(file)

    #     # Affichage des animaux dans les zones de texte
    #     for i, animal in enumerate(data['caractheristiques'], start=15):
    #         text_fields = []

    #         for j, key in enumerate(self.col_title):
    #             # Utilisation de ScrolledText à la place de Entry
    #             text_field = scrolledtext.ScrolledText(self, width=30, height=1)
    #             text_field.grid(row=i, column=j, sticky='nsew')
    #             # Récupérer la valeur de la clé si elle existe, sinon utiliser une chaîne vide
    #             value = animal.get(key, '')
    #             text_field.insert(END, f"{key}: {value}\n")
    #             text_fields.append(text_field)

    #         self.data.append(text_fields)

    #     self.bouton_ajouter_ligne = Button(self, text="Ajouter une ligne", command=self.ajouter_ligne)
    #     self.bouton_ajouter_ligne.grid(row=self.numberLines + 4, columnspan=len(self.col_title), sticky='nsew')

    #     btn_valider = Button(self, text="Modifier les informations", command=self.valider_caratheristiques_animaux)
    #     btn_valider.grid(row=self.numberLines + 5, columnspan=len(self.col_title), sticky='nsew')

    #     # Redimensionner le canevas lorsque la taille de la fenêtre change
    #     self.bind("<Configure>", self.redimensionner_canevas)