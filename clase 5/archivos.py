# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 07:19:27 2022

@author: HP-2016
"""
print("---------------------------------")
 # leer archivos 
 
f=open('lista de alumnos xd.txt','r+')
print(f.read())
f.close()

# propiedades del archivo ( f es un objeto file)
# estado de un archivo (descripcion)
print("nombre de archivo",f.name)
print("mode de archivo",f.mode)
print("estado de archivo : closed ",f.closed)
f.close()
print("estado de archivo : closed ",f.closed)

print("---------------------------------")


# crear un archivo
f_2=open("lista profes.txt","w+")
f_2.write("javi\n") #  \n = salto de linea 
f_2.write("goku\n")
f_2.close()

print("---------------------------------")


# iterar un archivo  y copiar archivo a otro archivo

f_3=open("ListaNumeros compu.txt","r")
f_3_copi=open("salida.txt","w+") #copia archivos

for linea in f_3:
    print(linea)
    f_3_copi.write(linea)
f_3.close()
f_3_copi.close()    

print("---------------------------------")












