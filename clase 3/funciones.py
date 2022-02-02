# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 09:00:23 2022

@author: HP-2016
"""
print("---------------------------------")

# declarar la funcion
def mi_funcion():
    print("hola mundo 1")
#llamar 1° funcion
mi_funcion()



def returholamundo()    :
    return "hola mundo 2"

# llamar la 2° funcion return
imprimir = returholamundo() # se lo llama dando una variable
print(imprimir)
 
print("---------------------------------")

# parametros de funciones

def mi_funcion_parametro(nombre,apellido):
    print(nombre,apellido)
#llamamos a la funcion que tiene parametros
mi_funcion_parametro("javi","goku")


def mi_funcion_parametro_2(nombre,apellido):
    return f'{nombre} - {apellido}'
# llamar funcion con parametro return 
nom_y_ape_conguion=mi_funcion_parametro_2('javi', 'vegueta')
print(nom_y_ape_conguion)


print("---------------------------------")
