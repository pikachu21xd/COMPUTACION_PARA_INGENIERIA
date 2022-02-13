# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 20:47:30 2022

@author: HP-2016
"""

class Atm:
    
    def __init__(self, ubicacion):
        self.ubicacion = ubicacion
    def showATM(self):
        print("cajero ubicado en ", self.ubicacion)