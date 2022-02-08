# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 07:41:35 2022

@author: HP-2016
"""

#Dada la lista [10,20,30,10,5, 1, 3, 5, 4] separar en dos listas una lista debe contener solo los pares y la segunda lista solo debe contener los impares

listaDeNumeros=[10,20,30,11,5, 1, 3, 5, 4]
lista_1=[]
lista_2=[]

for impar in listaDeNumeros:
    if impar % 2 == 1 :
     lista_1.append(impar)
    print("numeros impares son:",lista_1)
   
for par in listaDeNumeros:
    if par % 2 == 0 :
     lista_2.append(par)
    print("numeros pares son:",lista_2)
      