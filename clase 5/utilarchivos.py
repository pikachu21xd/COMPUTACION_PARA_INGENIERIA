# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 12:58:19 2022

@author: HP-2016
"""

#Manejar archivos

numeros=open("ListaNumeros compu.txt","r")
print(numeros.readline())
print(numeros.readline())
print(numeros.readline())


# leer lineas de un archivo (kista tranfor.)
res=numeros.readlines() # restor un arary con el contenidos de archivo
print(res)


# anexar archivos

archivo=open('lista profes.txt','a') # a = anexo
archivo.write('nuevo docente')  # agregamos nueva linea 
archivo.close()