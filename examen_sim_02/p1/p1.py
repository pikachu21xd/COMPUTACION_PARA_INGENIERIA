# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 09:10:39 2022

@author: HP-2016
"""

# 1.- Pedir un parrafo al usuario y contar los espacios en el parrafo

frase=input("ingrese la frase :")

def contar(frase):
    caracter=0
    espacio=0
    for i  in frase:
        if i==" ":
            espacio=espacio+1
            continue
        caracter=caracter+1
    return espacio 
        
print("numero de espacios: ",contar(frase))
