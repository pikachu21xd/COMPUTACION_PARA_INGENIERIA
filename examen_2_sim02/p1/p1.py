# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 12:07:35 2022

@author: HP-2016
"""

"""
1.-Crear un programa GUI que permita sumar dos valos ingresados por el
usuario
"""
from tkinter import *

ventana=Tk()
ventana.geometry("350x150")


eti_M=Label(ventana,text="ingrese el valor M")
eti_M.place(x=20,y=20)

eti_N=Label(ventana,text="ingrese el valor N")
eti_N.place(x=20,y=40)


eti_res=Label(ventana,text="<<resultado>>")
eti_res.place(x=150,y=60)


ent_M=Entry(ventana)
ent_M.place(x=150,y=20)

ent_N=Entry(ventana)
ent_N.place(x=150,y=40)

bt_validar=Button(ventana,text="VALIDAR",command=lambda:sumar())
bt_validar.place(x=150,y=100)

# hacemos funcionar el boton

def sumar():
    M=int(ent_M.get())
    N=int(ent_N.get())
    suma=M + N
    eti_res.config(text=f"la suma es : {M} +{N}= {suma}")
    

ventana.mainloop()
