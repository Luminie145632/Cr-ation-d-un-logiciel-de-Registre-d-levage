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



class EncadrementZootechnique:
    def view_zootechnical_supervision(self):
     print("appel view_zootechnical_supervision") 

     with open('encadrement_zootechnique.json', 'r') as file:
            data = json.load(file)

     for i, animal in enumerate( data['encadrement'] ):#, start=15):
            text_fields = []
            for j, key in enumerate(self.col_title):
                text_field = tk.Entry(self.inner_frame, width=3)
                text_field.grid(row=i, column=j, sticky='nsew')
                value = animal.get(key, '')
                text_field.insert(tk.END,  value)
                text_fields.append(text_field)
            self.data.append(text_fields)

     for j in range(len(self.col_title)):
            self.inner_frame.grid_columnconfigure(j, weight=1)
     self.inner_frame.update_idletasks()
     self.navbar_canvas.configure(scrollregion=self.navbar_canvas.bbox("all"))      

