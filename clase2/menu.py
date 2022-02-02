# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 08:51:36 2022

@author: HP-2016
"""
"""
crear un programa que registre nuyevos alumnos, liste los actuales alumnos,
borre un alumno , el alumno tiene nombre y apellido 
"""

# crear una list

list=[]     #creamos la lista en BLANCO 

salir=False #creamos una variable para salir del programa
while salir!= True :  # while=ciclos, dado concluida la opccion elegida nos vuelve a mostrar las opciones principales hasta decidamos salir del programa
    print("----------MENU----------")
    print("1.- LISTA ALUMNOS ")
    print("2.- REGISTAR ALUMNOS")
    print("3.- SALIR ")
    print("4.- QUITAR A ALUMNO DE LA LISTA")
    print("------------------------")
    # elegir opccion
    option=int(input("seleccione una opccion [1.2.3] :"))     # int=entero , input = entarda standar
    ## ejecutamos la opccion que se eligio
    # opccion 1 lista de alumnos
    if option ==1 : # if = si 
       print(" LA LISTA DE ALUMNOS ES : ")#imprimimos un titulo
       for alumno in list: # for=iteramos la lista 
         print(alumno) # imprimimos la lista de los alumnos 
    # opccion 2 registramos un alumno nuevo
    elif option==2:   # elif=sino (referente a una condicion)
      nuevo_alumno=input("ingrese NOMBRE COMPLETO :") # pedimos el nombre del alumno
      list.append(nuevo_alumno) #registramos en nombre en la lista 
  # opccion3 salimos de la app
    elif option==3:
        print("GRACIAS POR USAR MI APP")
        salir = True
   # opccion 4 quitamos un alumno de la lista
    elif option==4:
        elim_alumno=input("ingrese el NOMBRE COMPLETO del alumno que quiere quitar de la lista :")
        list.remove(elim_alumno)   #list.remove=quitar a alguien de la lista
    else:
        print("por favor ingrese una opccion valida [1,2,3]")

    
        
        