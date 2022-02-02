# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 22:56:35 2022

@author: HP-2016
"""
print("listar numeros primos dentro de un intervalo")

def encontrar_primos (inicial,final): # definimos la funcion encontrar primos dentro un intervalo 

    primos=[] # creamos una lista en blanco 
    for numero in range(inicial,final+1):  # iteramos desde el numero inicial hasta el final
        contador=0
        for i in range(1,numero+1):
            if numero % i == 0:
                contador +=1
        if  contador == 2:
            primos.append(numero)
    return primos 
a= int(input("numero inicial : "))
b= int(input("numero final : "))
print(encontrar_primos (a,b))       