# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 08:35:40 2022

@author: HP-2016
"""

"""
2.- Crear un programa en GUI, que permita contar de forma acendente, decendente y resetear el contador a 0, dependiendo al boton que precionen
"""
from tkinter import *


ventana=Tk() 
ventana.geometry("700x50") 
ventana.title("contador") 

# creamos etiquetas 
eti_contador=Label(ventana,text="contador") 
eti_contador.place(x=10,y=10)

# creamos el boton
bt_sumador=Button(ventana,text="incrementar",command=lambda:incrementar())
bt_sumador.place(x=220,y=10)


bt_restar=Button(ventana,text="disminuir",command=lambda:disminuir())
bt_restar.place(x=300,y=10)

bt_reset=Button(ventana,text="reset",command=lambda:resetear())
bt_reset.place(x=380,y=10)


Ent_text=Entry(ventana) 
Ent_text.place(x=80,y=10)



contador=0 
Ent_text.insert(0,str(contador)) 


def disminuir():
    dism=int(Ent_text.get())
    dismi=dism-1
    Ent_text.delete(0,END)
    Ent_text.insert(0,str(dismi))
   




def incrementar():
    numero=int(Ent_text.get())
    numero = numero + 1 
    Ent_text.delete(0,END) 
    Ent_text.insert(0,str(numero)) 

def resetear():
    Ent_text.delete(0,END)
    Ent_text.insert(0,str(contador))

ventana.mainloop()

