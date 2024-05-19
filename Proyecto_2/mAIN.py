import math
import numpy as np
from scipy.optimize import fsolve
def Metodo_Secante():
    def f(x):
        return 4*x**3 - 3.8*x**2 - 2*x

    x0 = 2
    x1 =  3  
    Error = 0.05
    i=0
    opc = True

    while(opc):
       
        if(i == 0):
            
            x = x1 - (( f(x1)*(x0 - x1)) / (f(x0) - f(x1) ))
            ErrorAbs = 0
            fx1 = f(x1)
            fx0 = f(x0)
            fx = f(x)
            
            print(f"\nIteracion = {i}")
            print(f"Valores de x0 = {x0},\nValores de x1 = {x1}, \nValores de f(x0) = {fx0},\nValores de f(x1) = {fx1},\nValores de f(x) ={fx} ,\nValores de x = {x}")
            print(f"ERROR = {ErrorAbs}")
            x0 = x1
            x1 = x
            
            i = i + 1

        if(i > 0 ):

            
            x = x1 - (( f(x1)*(x0 - x1)) / (f(x0) - f(x1) ))
            ErrorAbs = ((abs(x -x1)/x))*100
            fx1 = f(x1)
            fx0 = f(x0)
            fx = f(x)
            print(f"\nIteracion = {i}")
            print(f"Valores de x0 = {x0},\nValores de x1 = {x1}, \nValores de f(x0) = {fx0},\nValores de f(x1) = {fx1},\nValores de f(x) ={fx} ,\nValores de x = {x}")
            print(f"ERROR = {ErrorAbs}")
            x0 = x1
            x1 = x
            i= i+1 
            
            if(ErrorAbs<= Error):
                i= i+1 
                opc = False
def Metodo_Punto_Fijo(tol = 1e-5):
    # Define la función
    def g(x):
        return x**2 - 4
    x0 = 0.5
    
   

    
def Menu():
    
    while(True):
        print("[1]Metodo secante\n[2]Metodo de punto fijo\n[3]Salir")
        opc = input("Que desea escoger? ")

        match(opc):
            case "1":
                Metodo_Secante()
                
            case "2":
                Metodo_Punto_Fijo()
            
            case "3":
                exit()
                
        


Menu()