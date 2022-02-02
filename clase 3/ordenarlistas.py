# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 07:52:54 2022

@author: HP-2016
"""
print("--------met: BURBUJA --------------------")
A=[55,78,45,12,34,64] # dada la lista
#         i  j
#        i<=>j
#         j  i

#obtenemos el tamaño de la lista
num=len(A)
indice=0 #que comience en la posicion 0  
while indice < num:
    j=indice
    while j < num:
        if(A[indice] > A[j]):
            aux=A[indice]
            A[indice]=A[j]
            A[j]=aux
        j=j+1
    indice=indice+1
print("lista ordenada es :")
print(A)        


print("----------------------------")


lista_2=[2,3,5,1,6,9,4] # dada la lista 
lista_2.sort()

print("la lista ordena es :",lista_2)

print("----------------------------")
