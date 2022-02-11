# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 17:41:26 2022

@author: HP-2016
"""

# import 
import matematica.aritmetrica

print(matematica.aritmetrica.sumar(2,4))
# import
from matematica import aritmetrica
print(aritmetrica.sumar(6, 6))

from matematica.aritmetrica import sumar

print(sumar(2,3))

# importamos gemetria
from matematica.geometria import calcularArea
print(calcularArea())