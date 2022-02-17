# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 18:32:54 2022

@author: HP-2016
"""

"""
1.-Escribir una aplicación GUI , como la que se ve en la figura. Cada ves
que se haga clic en el botón "+", el valor del contador se incrementa en
1

"""
#importamos la libreria 

from tkinter import *

# creamos una ventana 
ventana=Tk() # generamos la ventana 
ventana.geometry("300x50") # dimecionamos la ventana
ventana.title("p1") # ponemos titulo a la ventana 

# creamos etiquetas 
eti_contador=Label(ventana,text="contador") # creamos el nombre de la etiqueta

# creamos el boton
bt_sumador=Button(ventana,text="+",command=lambda:incrementar_2())

# input text caja de texto
Ent_text=Entry(ventana)

# posicionar 
eti_contador.place(x=10,y=10)
Ent_text.place(x=80,y=10)
bt_sumador.place(x=220,y=10)


# hacemos funcionar el boton
contador=0 # creamos una variable 
Ent_text.insert(0,str(contador)) #insertamos la variable en la caja de texto


def incrementar():
    global contador # ponemos global pa modificar la variable 
    contador=contador+1
    Ent_text.delete(0,END) #remplazar de 0 a final
    Ent_text.insert(0,str(contador)) #insertar el contador 

#bt_sumador=Button(command=lambda: incrementar())


def incrementar_2():
    numero=int(Ent_text.get()) # copiamos lo que hay en caj de texto en entero
    numero = numero + 1 # incrementamos ese numero
    Ent_text.delete(0,END) #remplazar de 0 a final
    Ent_text.insert(0,str(numero)) #insertar el contador 




ventana.mainloop()









