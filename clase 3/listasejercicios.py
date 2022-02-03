# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 20:36:42 2022

@author: HP-2016
"""
print("------------------------------------------------------")


print("-----dado la lista encontar el elemento mayor --------")

lista=[2,1,5,100,-2] # creamos la lista 
mayor=None  # none=sin valor 
for numero in lista: #iteramos la lista
    if mayor==None: 
        mayor=numero
    else:
         if numero>mayor:
             mayor=numero
print("el numero mayor es : ",mayor)        
        

print("------------------------------------------------------")


print("-----dado la lista encontar el elemento menor --------")

lista=[2,1,5,100,-2] # creamos la lista 
menor=None  # none=sin valor 
for numero in lista: #iteramos la lista
    if menor==None: 
        menor=numero
    else:
         if numero<menor:
             menor=numero
print("el numero mayor es : ",menor)  


print("------------------------------------------------------")


print("-----dado la lista encontar el elemento mayor y menor --------")


lista=[2,1,5,100,-2] # creamos la lista 
menor_num=0
mayor_num=0
for elemento in lista:
    if menor_num==0 and mayor_num==0:
        menor_num=elemento
        mayor_num=elemento 
    else:
        if elemento<menor_num :
            menor_num=elemento 
        if elemento>mayor_num :
            mayor_num=elemento 
            
#  mostramos los resultados 
print(f'el numero mayor es: {mayor_num}')
print(f'el numero menor es: {menor_num}')

print("------------------------------------")

print("---------dado la lista mostrar el promedio -----------")


lista_2=[1,3,4,6,7]
suma=0
tamaño_lista_2=0
for elemento in lista_2:
    suma += elemento
    tamaño_lista_2 += 1
promedio = suma / tamaño_lista_2 
print("el promedio es . ",promedio) 
   
print("------------------------------------")
           
        
     
