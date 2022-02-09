# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 07:16:13 2022

@author: HP-2016
"""

# 3.Dado el archivo estudiantes.txt y notas.txt unir en un solo archivo llamado primer_parcial.txt que contendra los nombre seguido de su nota. (20pts)


Estudiantes=open("Estudiantes.txt","r")
Notas=open("Notas.txt","r")
Primer_Parcial=open("Primer_Parcial.txt","w+")
lineas = Estudiantes.readlines()

for linea in lineas:
    nota = Notas.readline()
    Primer_Parcial.write(linea +' '+ nota)
Estudiantes.close()
Notas.close()
Primer_Parcial.close()    
    
