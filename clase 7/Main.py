# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 20:45:27 2022

@author: HP-2016
"""

from banco.ATM import Atm
from banco.clientes import Cliente

atm = Atm("calle oquendo")
atm.showATM()

client = Cliente("jhonny")
client.showCLient()