# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 17:03:30 2022

@author: HP-2016
"""

# importar modulo
import aritmetrica
print(aritmetrica.sumar(1,1))
print(aritmetrica.div(1,1))
print(aritmetrica.restar(1,1))

# otra menera de import solo funciones especificas
"""
from aritmetica import sumar, div
print(sumar(1,1))
print(div(1,1))
"""
# importar todas las funciones de la libreria
from aritmetrica import *
print(sumar(1,1))