from tkinter import *

class Menu_navigation:
    def __init__(self, horse_data):
        pass
   
fen1 = Tk()
image = PhotoImage(file="white_horse.png")

# Création des éléments graphiques
bou = Button(fen1, text='xxxxx', fg='black')

bou.place(x=10, y=10)

can1 = Canvas(fen1, bg='cyan', height=500, width=500)
# bou1 = Button(fen1, text='Annuler', fg='cyan')
tex1 = Label(fen1, text='Horse Managing', fg='black')

# Positionnement des éléments
can1.pack(side=TOP)
bou.pack(side=TOP)
# bou1.pack(side=TOP)
tex1.pack(side=BOTTOM)

frame2 = Frame(fen1, bg='deepskyblue', height=200, width=200)
frame2.pack(side=LEFT)  # Choisissez le côté où vous voulez placer le panneau 2

# Ajoutez des éléments au panneau 2
label_frame2 = Label(frame2, text='Information', fg='black')
label_frame2.pack(side=LEFT)
can1.pack()
can1.create_image(0, 0, anchor=NW, image=image)
fen1.resizable(height=False,width=False)
fen1.mainloop()




# while on==True:
# init_window()
# fen1 = Tk()
# bou1 = Button(fen1,text='Annuler',command=fen1.quit)
# bou1.pack(side=BOTTOM)
# bou2 = Button(fen1,text='Tracer une ligne',command=drawline)
# bou2.pack()
# bou3 = Button(fen1,text='Autre couleur',command=changecolor,padx=7,pdy=8)
# bou3.pack(padx=7,pady=8)

