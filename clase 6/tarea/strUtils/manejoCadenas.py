# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 18:02:05 2022

@author: HP-2016
"""
"""
contar palabras

"""
def contar_Palabras(palabras):
   contadorPalabras = 0
   palabrasList = []
   palabra=''
   index = 0
   
   for character in palabras:
           
        
        if character == ' ':
            palabrasList.append(palabra)
            # reinicializamos todo
            palabra=''
        else:
            palabra += character
        
        # final del array de caracteres
        if index + 1 == len(palabrasList) :
            palabrasList.append(palabra)
            
   return len(palabrasList)
parrafo=input("ingrese el texto : ")
print ( "el numero de palabras es :",contar_Palabras(parrafo)) #retorna 4
           
"""
contar palabras
"""
#frase=input("ingrese la frase :")

def contar_espacios(parrafo):
    caracter=0
    espacio=0
    for i  in parrafo:
        if i==" ":
            espacio=espacio+1
            continue
        caracter=caracter+1
    return espacio 
        
print("numero de espacios: ",contar_espacios(parrafo))









