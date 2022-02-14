# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 19:40:10 2022

@author: HP-2016
"""

from tkinter import * # importamos toda la libreria
import parser  # identificar una expresion
ventana=Tk() #creamos la ventana 

ventana.title(" CALCULADORA ") # le ponemos titulo 
ventana.geometry("120x180") # tamaño de la ventana 

# creamos la cja de texto (input)
caja_texto = Entry(ventana)
caja_texto.grid(row=1,columnspan=4,sticky=W+E) # sticky(para que abarque todo el ancho posible) 

# hacer funcionar los botones numeros 
i=0  #indice de insercion para que no se remplasen entre si

def obtner_numero(n):
    global i   # ya que i no pertenece a la funcion
    caja_texto.insert(i,n) # insertamos el indice y el numero en la caja de texto
    i +=1

#hacer funcionar los operadores 
def obtener_operador(operador):
    global i
    tamaño_operador=len(operador) # saber la longitud del operador 
    caja_texto.insert(i,operador) #insertamos en la caja de texto el operador 
    i += tamaño_operador
    
# limpiamos caja de texto
def limpiar():
    caja_texto.delete(0,END) # inicio hasta el final


# calculamos lo que se muestra en la caja de texto
def calcular():
    estado_caja_texto =caja_texto.get()  #
    try:
        expresion_matematica= parser.expr(estado_caja_texto).compile()
        resultado=eval(expresion_matematica)
        limpiar() #limpiamos la caja de texto
        caja_texto.insert(0, resultado) # insertamos el resultado 
    except Exception:
       limpiar() # limpiamos la caja
       caja_texto.insert(0, 'error') # colocamos error
    


# creamos los botones 

Button(ventana, text="1",command= lambda :obtner_numero(1)).grid(row=2,column=0,padx=5,pady=5,sticky=W+E)
Button(ventana, text="2",command= lambda :obtner_numero(2)).grid(row=2,column=1,padx=5,pady=5,sticky=W+E)
Button(ventana, text="3",command= lambda :obtner_numero(3)).grid(row=2,column=2,padx=5,pady=5,sticky=W+E)

Button(ventana, text="4",command= lambda :obtner_numero(4)).grid(row=3,column=0,padx=5,pady=5,sticky=W+E)
Button(ventana, text="5",command= lambda :obtner_numero(5)).grid(row=3,column=1,padx=5,pady=5,sticky=W+E)
Button(ventana, text="6",command= lambda :obtner_numero(6)).grid(row=3,column=2,padx=5,pady=5,sticky=W+E)

Button(ventana, text="7",command= lambda :obtner_numero(7)).grid(row=4,column=0,padx=5,pady=5,sticky=W+E)
Button(ventana, text="8",command= lambda :obtner_numero(8)).grid(row=4,column=1,padx=5,pady=5,sticky=W+E)
Button(ventana, text="9",command= lambda :obtner_numero(9)).grid(row=4,column=2,padx=5,pady=5,sticky=W+E)

Button(ventana, text="AC",command= lambda : limpiar()).grid(row=5,column=0,padx=5,pady=5,sticky=W+E)
Button(ventana, text="0",command= lambda :obtner_numero(0)).grid(row=5,column=1,padx=5,pady=5,sticky=W+E)
Button(ventana, text="=",command= lambda : calcular()).grid(row=5,column=2,padx=5,pady=5,sticky=W+E)
# botones operadores 
Button(ventana, text="+",command= lambda :obtener_operador("+")).grid(row=2,column=3,padx=5,pady=5,sticky=W+E)
Button(ventana, text="-",command= lambda :obtener_operador("-")).grid(row=3,column=3,padx=5,pady=5,sticky=W+E)
Button(ventana, text="*",command= lambda :obtener_operador("*")).grid(row=4,column=3,padx=5,pady=5,sticky=W+E)
Button(ventana, text="/",command= lambda :obtener_operador("/")).grid(row=5,column=3,padx=5,pady=5,sticky=W+E)





ventana.mainloop()

