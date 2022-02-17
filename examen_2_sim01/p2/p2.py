# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 19:35:05 2022

@author: HP-2016
"""
"""
2.-Escribir una aplicación GUI. que permita añadir, agregará en el
listBox el contenido de una pelicula

"""

from tkinter import *

ventana=Tk()
ventana.title("peliculas")
ventana.geometry("350x230")

# creamos las etiquetas y la posicionamos
eti_escrib_peli=Label(ventana,text="excribe el titulo de la pelicula")
eti_escrib_peli.place(x=20,y=20)

eti_list_peli=Label(ventana,text="PELICULAS")
eti_list_peli.place(x=200,y=20)


# creamos el campo de texto y la posicionamos
ent_text=Entry(ventana)
ent_text.place(x=20,y=50)


#creamos el boton y la posicionamos 
bt_añadir=Button(ventana,text="añadir",command=lambda:listar_peli())
bt_añadir.place(x=50,y=80)

# creamos la hoja de registro
lista_pelis=Listbox(ventana)
lista_pelis.place(x=200,y=40)

#hacemos funcionar el boton añadir

def listar_peli():
    nom_peli=ent_text.get() #obtenemos el nombre en una variable
    lista_pelis.insert(0, nom_peli) #insertamos el nombre en la hoja de registro
    ent_text.delete(0,END) # borramos lo que hay en la entrada de texto








ventana.mainloop()













