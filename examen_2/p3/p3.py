# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 08:18:40 2022

@author: HP-2016
"""

"""
3.- Crear un programa con GUI, que permita hacer operaciones de suma, resta y multiplicacion.
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

bt_sumar=Button(ventana,text="sumar",command=lambda:sumar())
bt_sumar.place(x=150,y=100)

bt_restar=Button(ventana,text="restar",command=lambda:restar())
bt_restar.place(x=100,y=100)

bt_multiplicar=Button(ventana,text="multiplicar",command=lambda:multiplicar())
bt_multiplicar.place(x=250,y=100)
# hacemos funcionar el boton

def sumar():
    M=int(ent_M.get())
    N=int(ent_N.get())
    suma=M + N
    eti_res.config(text=f"la suma es : {M} +{N}= {suma}")
    
def restar():
    M=int(ent_M.get())
    N=int(ent_N.get())
    resta=M - N
    eti_res.config(text=f"la resta es : {M} - {N}= {resta}")

def multiplicar():
    M=int(ent_M.get())
    N=int(ent_N.get())
    multiplicacion= M * N
    eti_res.config(text=f"la multiplicacion es : {M} *{N}= {multiplicacion}")    
ventana.mainloop()
