# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 09:04:10 2022

@author: HP-2016
"""

# 2.- Dada la Lista [12,1, 3, 5 , 15, 24] separar en dos listas de pares e impares

Lista = [12,1, 3, 5 , 15, 24]
lista_1=[]
lista_2=[]

for impar in Lista:
    if impar % 2 == 1 :
     lista_1.append(impar)
print("numeros impares son:",lista_1)
   
for par in Lista:
    if par % 2 == 0 :
     lista_2.append(par)
print("numeros pares son:",lista_2)
      