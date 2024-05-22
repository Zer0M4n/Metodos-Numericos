import math as m
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
def Metodo_Punto_Fijo():
    
    # Define la función
    def g(x):
        return m.sqrt(m.e**x/3)
    #Variables
    x0 = 0
    n = 5

    tol = 6
    for k in range(n):
        x1 = g(x0)
        error = abs((x1-x0)/x1 )*100
        if(abs((x1-x0)/x1 )*100 < tol):
            print(f"x {k +1}, = {x1}, Es punto fijo ")
            error = abs((x1-x0)/x1 )*100
            print(f"Error {error}") 
           

            return
        
        x0 = x1
        print(f"x {k +1}, = {x1}") 
        print(f"Error {error}") 
           
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