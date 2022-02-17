# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 13:02:02 2022

@author: HP-2016
"""

"""
3.-Implement el siguiente GUI, dado un comboBox que lista lenguages
de programacion, mostrar el lenguage seleccionado:

"""
from tkinter import *
from tkinter import ttk # importamos el combobox
ventana= Tk()
ventana.geometry("400x400")
ventana.title("combobox")

eti_res=Label(ventana,text="<<resultado>>")
eti_res.place(x=10,y=60)

comb_1=ttk.Combobox(ventana,values=["java","python","c#"])
comb_1.place(x=10,y=20)

#hacemos funcionar el combobox
def selecione_opcion(event):
    seleccionado=comb_1.get()
    eti_res.config(text=f"lenguaje: {seleccionado}")
comb_1.bind("<<ComboboxSelected>>",selecione_opcion)
ventana.mainloop()
