# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 14:18:31 2022

@author: HP-2016
"""

print("-------ejercicio 1 --------------")
print("Escribir un Archivo llamado archivo.txt con el siguiente contenido")

# creamos un archivo 
f_1=open("archivo.txt","w+")
f_1.write("nombre : javier david pacheco\n")
f_1.write("cod. SIS : 201900690\n")
f_1.write("edad : 21\n")
f_1.write("nota : 100\n")
f_1.close()

print("-------ejercicio 2 --------------")
print("dado el archivo multilinea.txt Contar el numero de lineas que tiene un Achivo")
 
f_2=open("multilinea.txt","r")
res=f_2.readlines() # convertimos en una lista 
contador=0
for i in res:
    contador=contador+1 # contamos los elementos 

print("el numero de lineas es :",contador)

f_2.close()


print("-------ejercicio 3 --------------")
print("Leer un Archivo con el siguiente contenido y convertirlo en una lista")
f_3=open("ejercicio 3.txt","w+")
f_3.write("1\n")
f_3.write("0\n")
f_3.write("3\n")
f_3.write("4\n")
f_3.write("5\n")
f_3.close()

f_4=open("ejercicio 3.txt","r")
listado=f_4.readlines()
print(listado)
f_4.close()

print("-------ejercicio 4 --------------")
print("dado la list Alumnos [“jhonny”, “jose”, “Rither”] escribir en un archivo llamado almunos.txt")
f_5=open("alumnos.txt","w+")
list_alumnos=["jhonny","jose","Rither"]
for i in list_alumnos:
    f_5.write('{}\n'.format(i))
    
f_5.close()

print("-------ejercicio 5 --------------")
print("Dado el archivo frase.txt contar el número de caracteres sin contar los espacios:La programacion en python genial!")

f_6=open("frase.txt","r")
leer=f_6.readline()
def contar(leer):
    caracter=0
    espacio=0
    for i  in leer:
        if i==" ":
            espacio=espacio+1
            continue
        caracter=caracter+1
    return caracter,espacio 
print("(numero de caracteres , numero de espacios): ",contar(leer))
f_6.close()
   
    
