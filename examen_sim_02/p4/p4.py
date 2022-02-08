# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 09:54:06 2022

@author: HP-2016
"""
# 4.- Crear una funcion que muestre un numero entero digito por digito
entrada=int(input("ingrese la entrada : "))
while entrada >0:
    digito=entrada % 10
    print (digito)
    entrada=int(entrada/10)
