import tkinter as tk
import glob
import os
import Methode1
import json
from tkinter import *
from tkinter import messagebox, Frame, Entry, Button, Label, BOTH, ttk, Canvas



class Movements:
    
    def view_temporary_movements(self):
      
        print("appel view animal")
      #  self.navbar_canvas.create_window((0, 0), window=animal_frame, anchor='nw')
        with open('mouvements_temporaires.json', 'r') as file:
            data = json.load(file)

        for i, animal in enumerate( data['mouvements']  ):#, start=15):
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
