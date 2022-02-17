# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 12:36:31 2022

@author: HP-2016
"""

"""
2.- Crear un programa GUI que permita invertir una cadena ingresada
por el usario
"""
from tkinter import *

ventana=Tk()
ventana.geometry("300x200")

eti_entr_text=Label(ventana,text="ingrese texto")
eti_entr_text.place(x=20,y=20)
eti_tex_rev=Label(ventana,text="")
eti_tex_rev.place(x=100,y=40)

ent_text=Entry(ventana)
ent_text.place(x=100,y=20)

bt_rev=Button(ventana,text="revertir",command=lambda:text_rev())
bt_rev.place(x=100,y=60)


# hacemos funcionar el boton
def text_rev():
    texto=ent_text.get()
    text_inv=texto[::-1] # invertir texto
    eti_tex_rev.config(text=f"{text_inv}")
    
ventana.mainloop()
