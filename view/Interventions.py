# Accueil.py  
import sys
sys.path.insert(1, '/Creation_dun_logiciel_de_Registre_delevage/')
import tkinter as tk
import glob
import os
import Methode1
import json
from tkinter import ttk
from tkinter import Button  
from PIL import Image, ImageTk

class Interventions:
   
   def view_informations_intervention(self):
     print("appel view_zootechnical_supervision") 
   #  animal_frame = tk.Frame(self.navbar_canvas)
      #  self.navbar_canvas.create_window((0, 0), window=animal_frame, anchor='nw')

     with open('Soins_Courant.json', 'r') as file:
            data = json.load(file)

     for i, animal in enumerate( data['interventions']  ):#, start=15):
            text_fields = []
            for j, key in enumerate(self.col_title):
                text_field = tk.Entry(self.inner_frame, width=3)
                text_field.grid(row=i, column=j, sticky='nsew')
                value = animal.get(key, '')
                text_field.insert(tk.END,  value)#  f"{key}: {value}\n")
                text_fields.append(text_field)
            self.data.append(text_fields)

     for j in range(len(self.col_title)):
            self.inner_frame.grid_columnconfigure(j, weight=1)
     self.inner_frame.update_idletasks()
     self.navbar_canvas.configure(scrollregion=self.navbar_canvas.bbox("all"))      
 




