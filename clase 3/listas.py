# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 07:11:03 2022

@author: HP-2016
"""
#lista en blanco
lista=[]

print("--------------------------------")
#lista con elementos
lista_elementos=[1,2,3,4,5]


print("--------------------------------")
# accerder a los elementos de la lista
 #posicion     0        1          2    ...
listalumnos= ["javi","pikachu","charman"]
alumno_pos_1=listalumnos[1]
print(alumno_pos_1)
 
print("--------------------------------")

# el tamaño de la lista 
tamaño_lista= len(listalumnos)
print("el tamaño de la lista es:",tamaño_lista)

print("--------------------------------")
# insertar elemento a una lista 
lista_blanco=[]  # lista en blsnco
lista_blanco.append(1) # insertamos un numero o texto en la lista
lista_blanco.append(3)
lista_blanco.append("goku")
print(lista_blanco) # imprimimos la lista 

print("--------------------------------")
# insertamos en una posicion expecifica un numero o texto
 # nom-lista  insertamos (posicion,num o "texto")
lista_blanco.insert(2, 7)
lista_blanco.insert(4,"vegueta")
print(lista_blanco)


print("--------------------------------")


# eliminar elementos de una lista
print(lista_blanco)
lista_blanco.pop()
print("se elimino al ultimo de la lista,la nueva lista es :",lista_blanco)

#eliminamos segun la posicion que eligas 
lista_blanco.pop(0)
print(lista_blanco)

# otra manera de eliminar
print(lista_blanco)

lista_blanco.remove(7)
print(lista_blanco)
lista_blanco.remove('goku')
print(lista_blanco)
 


print("--------------------------------")

#  iterar listas
lista_docentes=["mia","kalifla","crilin"]
for docente in lista_docentes:
    print(docente)
# otra manera de iterar
tamanño_lista_docentes= len(lista_docentes)

for posicion in range(0,tamanño_lista_docentes):
   print(lista_docentes[posicion])
   


print("--------------------------------")



    