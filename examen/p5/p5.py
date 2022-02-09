# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 07:18:34 2022

@author: HP-2016
"""

#   5.- Crear un Menu que permita registrar estudiantes y sus notas en dos listas: lista_alumnos y lista_notas con los siguientes requerimientos . (30pts)

lista_alumnos=[]
lista_notas=[]
     

salir=False 
while salir!= True : 
    print("----------MENU----------")
    print("1.- LISTA ALUMNOS  Y SU NOTA  ")
    print("2.- REGISTAR ALUMNOS Y SU NOTA ")
    print("3.- SALIR ")
    print("------------------------")
    # elegir opccion
    option=int(input("seleccione una opccion [1.2.3] :"))         
    # opccion 1 lista de alumnos
    if option ==1 : # if = si 
       print(" LA LISTA DE ALUMNOS  Y SU NOTA ES : ")
       i=0
       print("{:<15} {:<15}".format(" ALUMNO","NOTA"))
       
       while i<1 :
           maxi=max(lista_notas)
           posMax=lista_notas.index(maxi)
           est=lista_alumnos[posMax]
           print("{:<15} {:<15}".format(est,maxi))
           del lista_alumnos[posMax]
           del lista_notas[posMax]
           i += 1
    # opccion 2 registramos un alumno nuevo
    elif option==2:   
      nuevo_alumno=input("ingrese NOMBRE COMPLETO :") 
      lista_alumnos.append(nuevo_alumno) 
      nueva_nota=input("ingrese la nota: ")
      lista_notas.append(nueva_nota)
  # opccion3 salimos de la app
    elif option==3:
        print("GRACIAS POR USAR MI APP")
        salir = True
  
    else:
        print("por favor ingrese una opccion valida [1,2,3]")

