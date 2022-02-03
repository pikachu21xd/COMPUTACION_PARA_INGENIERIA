# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 15:24:57 2022

@author: HP-2016
"""
class ATM:
    def __init__(self,ubicacion,banco,tipodemoneda):
        self.ubicacion=ubicacion
        self.banco=banco
        self.tipodemoneda=tipodemoneda
    
    # metodos de clase 
    
    def pedirtarjeta(self):
        print(f"tarjeta insertada correctamente del banco:{self.banco} y ubicacion : {self.ubicacion} ")
    def perdirpin(self):
        pin=input("ingrese el codigo pin : ")
        print(f"el codigo  {pin} es valido ")
    def retirar(self):
        cantidad=input("que cantidad quiere retirar ? :")
        print(f"RETIRO EXITOSO!!!,cantidad :{cantidad} {self.tipodemoneda}")

# crear objetos para los banco BNB, SOL,BCP

tarjBNB=ATM('planeta namecusein','BNB','BOS')
tarjBCP=ATM('planeta vegueta', 'BCP', 'USD') 
tarjSOL=ATM('templo kamisama', 'SOL', 'USD') 
"""
 # acciones ATM BNB     

tarjBNB.pedirtarjeta() 
tarjBNB.perdirpin()  
tarjBNB.retirar()
"""

"""
 # acciones ATM BCP     

tarjBCP.pedirtarjeta() 
tarjBCP.perdirpin()  
tarjBCP.retirar()
"""


 # acciones ATM SOL
tarjSOL.pedirtarjeta() 
tarjSOL.perdirpin()  
tarjSOL.retirar()
 