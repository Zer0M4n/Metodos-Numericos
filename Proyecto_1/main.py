import numpy as np
import math
from scipy.interpolate import interp1d# Librerias para hacer la interpolacion


def Interpolacion():
    X = [7,10,13,16,19] # Valores de x
    Y = [14,21,28,30,28] # Valores de y
    # Aproximacion
    Aproximacion_x = 9
    # Interpolamos
    y_interpolacion = interp1d(X, Y)
    print("DATOS:")
    print("X = ")
    print(X)
    print("Y = ")
    print(Y)
    print("Resulltado f(x) = {} es".format(Aproximacion_x),
      y_interpolacion(Aproximacion_x))


def Newton_Raphson():
    # INGRESO 
    fx  = lambda x: 5*(x**4) - 2*(x**2) - 11
    dfx = lambda x: 20*(x**3) - 4*x
    
    x0 = 2.
    tolera = 0.01
    # PROCEDIMIENTO
    tabla = []
    tramo = abs(2*tolera)
    xi = x0
    while (tramo>=tolera):
        xnuevo = xi - fx(xi)/dfx(xi)
        tramo  = abs(xnuevo - xi)/xnuevo
        tabla.append([xi,xnuevo,tramo*100])
        xi = xnuevo
    
    # convierte la lista a un arreglo.
    tabla = np.array(tabla)
    n = len(tabla)
    
    # SALIDA
    print("f(x) = 5x^4 - 2x^2 - 11")
    print(['xi', 'xnuevo', 'tramo'])
    np.set_printoptions(precision = 4)
    print(tabla)
    print('raiz en: ', xi)
    print('con error de: ',tramo)


def Newton_Raphson_Modificado():
    # INGRESO 
    fx  = lambda x: 19*(x**7) - 6*(x**2) - 19
    dfx = lambda x: 133*(x**6) - 12*x
    ddfx = lambda x: 798*(x**5) -12
    
    x0 = 3.
    tolera = 0.01
    # PROCEDIMIENTO
    tabla = []
    tramo = abs(2*tolera)
    xi = x0
    while (tramo>=tolera):
        xnuevo = xi - ( (fx(xi) * dfx(xi)) / ( (math.pow( dfx(xi) , 2 )) -(fx(xi) * ddfx(xi))))
        tramo  = abs(xnuevo - xi)/xnuevo
        tabla.append([xi,xnuevo,tramo*100])
        xi = xnuevo
    
    # convierte la lista a un arreglo.
    tabla = np.array(tabla)
    n = len(tabla)
    
    # SALIDA
    print("f(x) = 19x^7) - 6x^2 - 19")
    print(['xi', 'xnuevo', 'tramo'])
    np.set_printoptions(precision = 4)
    print(tabla)
    print('raiz en: ', xi)
    print('con error de: ',tramo)

opc2 = True
while(opc2):
    print("[1]Interpolacion\n[2]Newton_Raphson\n[3]Newton_Raphson Mejorado\n[4]Salir")
    opc = input("Que desea escoger? ")
    match(opc):
        case "1":
            Interpolacion()
        case "2":
            Newton_Raphson()
        case "3":
            Newton_Raphson_Modificado()
        case "4":
            exit()
    



