from tkinter import *


class encadrement_zootechnique():
    def __init__(self,horse_data):
     pass       

fen1=Tk()
tex1 = Label(fen1, text='Encadrement Zootechnique !', fg='red')
can1 = Canvas(fen1,bg='blue',height=200,width=200)
can1.pack(side=LEFT)
tex1.pack()
bou1 = Button(fen1, text='Modifier', command = fen1.destroy)
bou1.pack()
fen1.mainloop()
on=True
# while on==True:
# init_window()
# fen1 = Tk()
bou1 = Button(fen1,text='Annuler',command=fen1.quit)
bou1.pack(side=BOTTOM)
bou2 = Button(fen1,text='Tracer une ligne',command=drawline)
bou2.pack()
bou3 = Button(fen1,text='Autre couleur',command=changecolor)
bou3.pack()





    




        