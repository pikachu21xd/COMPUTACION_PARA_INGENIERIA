# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 21:14:31 2022

@author: HP-2016
"""
"""
ejercicio n° 1 contador del 1 al 10 
"""
# contadores de 1 en 1
print("------ejercicio 1 CONTADORES ------")
print("------- manera 1 ------------")
# manera 1 de resolver
cont=range(1,11) #creamos una variable con valor neutro
for numero in cont :
    print(numero)
print("------ manera 2 ---------------")
# manera 2 de resolver
contador=0
while contador < 10:
    contador=contador + 1
    print (contador)


"""
ejercicio n° 2
SUMADORES : sumar numeros del 1 al 10
"""
print("--- ejerccio 2  SUMADORES ---- ")
suma=0
for num in range(1,11):
   suma = suma + num
print(f'la suma total es : {suma}')



"""
ejercicicio N° 3 
MULTIPLICADORES: multiplicar del 1 al 10
"""
print("---ejercicio 3  MULTIPLICADORES ----")
multi=1
for multiplicado in range(1,11):
    multi = multi * multiplicado
print(f' la multiplicacion total es . {multi}')




"""
EJERCICIO 4 
MODULO : mostrar los  pares e impares del 1 al 10
"""
print("----ejercicio 4 mostrar los pares e impares del 1 al 10--------")
print("----numeros pares del 1 al 10 -----")
for par in range(1,11):
    if par % 2 == 0:
        print("numero par es:",par)
print("-------numeros impares del 1 al 10--------")
for impar in range(1,11):
    if impar % 2 == 1 :
        print("el numero impar es :",impar)


print("----otra manera de resolver ---")
for par in range (100,401):
    if par % 2 == 0:
        print("el numero par es  :",par)
    else :
         print("el numero impar es :", par)
        