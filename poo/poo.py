# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 16:31:12 2022

@author: HP-2016
"""

salir=False
while salir !=True:
    print("------------ FIGURAS INFORMACION --------------")
    print(" 1.- CIRCULO")
    print(" 2.- CUADRADO")
    print(" 3.- RECTANGULO")
    print(" 4.- SALIR ")
    opcion=int(input("ingrese la opccion [ 1 , 2 , 3 ,4 ] :"))
    if opcion==1:
        
        class figura:
        # definimos el metodo constructor 
           def __init__(self,linea,dimension):
            ## definimos atributos
            self.linea=linea 
            self.dimension=dimension
            
        # definimos metodos
           def angulo(self):
            pass
           def lados(self):
            pass
           def area(self):
            pass
           def describirse(self):
            print(f"es una figura {self.linea} de dimension {self.dimension}")
         
        class circulo(figura):
           def __init__(self, linea, dimension):
            self.linea=linea
            self.dimension=dimension
            
        # definimos metodos
           def angulo(self):
            print("tiene un agulo de 360°")
           def lados(self):
            print("no tiene lados ")
           def area(self):
            print("pi*(radio)^2")
           def describirse(self):
            print(f"es una figura de tipo de linea {self.linea} de dimension {self.dimension}")
        circulo=circulo("curva", "2D")
        circulo.angulo()
        circulo.lados()
        circulo.area()
        circulo.describirse()  
       
    elif opcion ==2:
        class figura:
        # definimos el metodo constructor 
           def __init__(self,linea,dimension):
            ## definimos atributos
            self.linea=linea 
            self.dimension=dimension
            
        # definimos metodos
           def angulo(self):
            pass
           def lados(self):
            pass
           def area(self):
            pass
           def describirse(self):
            print(f"es una figura {self.linea} de dimension {self.dimension}")
   
        class cuadrado(figura):
           def __init__(self, linea, dimension):
               self.linea=linea
               self.dimension=dimension
               
           # definimos metodos
           def angulo(self):
               print("tiene un agulo entre sus vertices de 90°")
           def lados(self):
               print("tiene cuatro lados  ")
           def area(self):
               print("el area es :lado * lado")
           def describirse(self):
               print(f"es una figura de tipo de linea {self.linea} de dimension {self.dimension}")          
        cuadrado=cuadrado("recta", "2D")
        cuadrado.angulo()
        cuadrado.lados()
        cuadrado.area()
        cuadrado.describirse()           

   

    elif opcion ==3:
        class figura:
        # definimos el metodo constructor 
           def __init__(self,linea,dimension):
            ## definimos atributos
            self.linea=linea 
            self.dimension=dimension
            
        # definimos metodos
           def angulo(self):
            pass
           def lados(self):
            pass
           def area(self):
            pass
           def describirse(self):
            print(f"es una figura {self.linea} de dimension {self.dimension}")
        class rectangulo(figura):
            def __init__(self, linea, dimension):
                self.linea=linea
                self.dimension=dimension
                
            # definimos metodos
            def angulo(self):
                print("tiene un agulo entre sus vertices de 90°")
            def lados(self):
                print("tiene cuatro lados  ")
            def area(self):
                print("el area es : base  * altura")
            def describirse(self):
                print(f"es una figura de tipo de linea {self.linea} de dimension {self.dimension}")          
        rectangulo=rectangulo("recta", "2D")
        rectangulo.angulo()
        rectangulo.lados()
        rectangulo.area()
        rectangulo.describirse()  
        
    elif opcion==4:
       salir=True
    else:
        print("ingrese la opcciom valida [ 1,2,3,4 ] :")
        
            
            
            
            
            
            
            
            
            
            
            
            
            
            