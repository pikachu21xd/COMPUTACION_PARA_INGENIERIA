# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 12:39:06 2022

@author: HP-2016
"""
#impotarmos la libreria 
import tkinter
"""
----------------- ventana ramdom -------------------------------
"""
ventana = tkinter.Tk() # ventana ramdom
ventana.mainloop()  #registro lo que se hace en la ventana 
"""
----------------- etiquetas y remarcados -------------------------------
"""

# creamos ventana con dimenciones 
ventana_2 = tkinter.Tk()
ventana_2.geometry("400x300")


# creamos etiquetas Y resaltamos con color 
#
etiqueta=tkinter.Label(ventana_2, text= "etiqueta centrada arriba", bg = "red")
etiqueta.pack() #centramos la etiqueta arriba
etiqueta_2=tkinter.Label(ventana_2,text= "etiqueta centrada abajo ", bg = "blue")
etiqueta_2.pack(side= tkinter.BOTTOM)
etiqueta_3=tkinter.Label(ventana_2,text= "etiqueta centrada a la DERECHA ")
etiqueta_3.pack(side= tkinter.RIGHT)
etiqueta_4=tkinter.Label(ventana_2,text= "etiqueta centrada a la IZQUIERDA ")
etiqueta_4.pack(side= tkinter.LEFT)
ventana_2.mainloop()
"""
------------- creamos botones -----------------------------------
"""

#creamos botones 
ventana_3= tkinter.Tk()
ventana_3.geometry("500x500")
def saludo():
    print("hola bobo")
#                                                 tamaño=x  tamaño=y  ejec.funcion           
boton1=tkinter.Button(ventana_3,text= "saludar",padx=30 ,pady=30,command=saludo)
boton1.pack()

ventana_3.mainloop()
"""
--------------- caja de texto ---------------------------------
"""
ventana_4=tkinter.Tk()
ventana_4.geometry("500x500")
#                                   fuente
caja_texto=tkinter.Entry(ventana_4, font="arial 10")
caja_texto.pack()

def texto_caja():
    texto=caja_texto.get()
    print(texto)
boton_2 = tkinter.Button(ventana_4, text= "click",command= texto_caja)
boton_2.pack()
ventana_4.mainloop()

"""
--------------- posicionar  ---------------------------------
"""
ventana_5 = tkinter.Tk()
ventana_5.geometry("500x500")

boton_3=tkinter.Button(ventana_5, text= "boton 1", width=10,height=5)
boton_4=tkinter.Button(ventana_5, text= "boton 2",width=10,height=5)
boton_5=tkinter.Button(ventana_5, text= "boton 3",width=10,height=5)
#            fila  columna 
boton_3.grid(row=0,column=0)
boton_4.grid(row=1,column=1)
boton_5.grid(row=2,column=2)


ventana_5.mainloop()




