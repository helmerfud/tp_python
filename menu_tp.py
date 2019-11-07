#! /usr/bin/env python 
# -*- coding: UTF-8 -*-
#(c) Xavier 2019

# pour débugger… en ligne de commande !-) 
#import pdb; pdb.set_trace()
from tkinter import Tk, StringVar, Label, Radiobutton
from functools import partial

def update_label(label, var):
    """
    Met à jour le texte de label en fonction de var.
    """
    text = var.get()
    label.config(text='Choix :' + text)


root = Tk()
root.title('Game')
choice = ['10', '100', '1000']
color = StringVar(root, '10')
label_color = Label(root, text='Choix :' + color.get())

for i, value in enumerate(choice, 1):
    label = Label(root, text=value)
    radiobutton = Radiobutton(root, variable=color, value=value,
                              command=partial(update_label, 
                                              label_color, 
                                              color))

    label.grid(row=i, column=0)
    radiobutton.grid(row=i, column=1)


label_color.grid(row=0, column=0)
root.mainloop()

