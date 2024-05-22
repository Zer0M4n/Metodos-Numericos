import tkinter as tk
import numpy as np
import math as m
from scipy.interpolate import interp1d

def Interpolacion():
    new_window = tk.Toplevel(root)
    new_window.title("Interpolación")
    output_text = tk.Text(new_window, wrap=tk.WORD, height=20, width=80)
    output_text.pack(pady=10)
    
    X = [7, 10, 13, 16, 19]
    Y = [14, 21, 28, 30, 28]
    Aproximacion_x = 9
    y_interpolacion = interp1d(X, Y)
    result = y_interpolacion(Aproximacion_x)
    
    output_text.insert(tk.END, "Interpolación\n")
    output_text.insert(tk.END, f"f({Aproximacion_x}) = {result}\n\n")

def Newton_Raphson():
    new_window = tk.Toplevel(root)
    new_window.title("Newton-Raphson")
    output_text = tk.Text(new_window, wrap=tk.WORD, height=20, width=80)
    output_text.pack(pady=10)
    
    fx = lambda x: 5*(x**4) - 2*(x**2) - 11
    dfx = lambda x: 20*(x**3) - 4*x
    
    x0 = 2.
    tolera = 0.01
    tabla = []
    tramo = abs(2 * tolera)
    xi = x0
    while tramo >= tolera:
        xnuevo = xi - fx(xi) / dfx(xi)
        tramo = abs(xnuevo - xi) / xnuevo
        tabla.append([xi, xnuevo, tramo * 100])
        xi = xnuevo
    
    tabla = np.array(tabla)
    result = f"Raíz en: {xi}\nError: {tramo}"
    output_text.insert(tk.END, "Newton-Raphson\n")
    output_text.insert(tk.END, f"{result}\n\n")

def Newton_Raphson_Modificado():
    new_window = tk.Toplevel(root)
    new_window.title("Newton-Raphson Modificado")
    output_text = tk.Text(new_window, wrap=tk.WORD, height=20, width=80)
    output_text.pack(pady=10)
    
    fx = lambda x: 19*(x**7) - 6*(x**2) - 19
    dfx = lambda x: 133*(x**6) - 12*x
    ddfx = lambda x: 798*(x**5) - 12
    
    x0 = 3.
    tolera = 0.01
    tabla = []
    tramo = abs(2 * tolera)
    xi = x0
    while tramo >= tolera:
        xnuevo = xi - (fx(xi) * dfx(xi)) / ((m.pow(dfx(xi), 2)) - (fx(xi) * ddfx(xi)))
        tramo = abs(xnuevo - xi) / xnuevo
        tabla.append([xi, xnuevo, tramo * 100])
        xi = xnuevo
    
    tabla = np.array(tabla)
    result = f"Raíz en: {xi}\nError: {tramo}"
    output_text.insert(tk.END, "Newton-Raphson Modificado\n")
    output_text.insert(tk.END, f"{result}\n\n")

def Metodo_Secante():
    new_window = tk.Toplevel(root)
    new_window.title("Método de la Secante")
    output_text = tk.Text(new_window, wrap=tk.WORD, height=20, width=80)
    output_text.pack(pady=10)
    
    def f(x):
        return 4*x**3 - 3.8*x**2 - 2*x
    
    x0 = 2
    x1 = 3  
    Error = 0.05
    i = 0
    opc = True
    results = ""
    
    while opc:
        if i == 0:
            x = x1 - ((f(x1) * (x0 - x1)) / (f(x0) - f(x1)))
            ErrorAbs = 0
            fx1 = f(x1)
            fx0 = f(x0)
            fx = f(x)
            results += f"Iteración {i}\nValores: x0 = {x0}, x1 = {x1}, f(x0) = {fx0}, f(x1) = {fx1}, f(x) = {fx}, x = {x}\nError = {ErrorAbs}\n\n"
            x0 = x1
            x1 = x
            i += 1
        else:
            x = x1 - ((f(x1) * (x0 - x1)) / (f(x0) - f(x1)))
            ErrorAbs = ((abs(x - x1) / x)) * 100
            fx1 = f(x1)
            fx0 = f(x0)
            fx = f(x)
            results += f"Iteración {i}\nValores: x0 = {x0}, x1 = {x1}, f(x0) = {fx0}, f(x1) = {fx1}, f(x) = {fx}, x = {x}\nError = {ErrorAbs}\n\n"
            x0 = x1
            x1 = x
            i += 1
            if ErrorAbs <= Error:
                opc = False
    
    output_text.insert(tk.END, "Método de la Secante\n")
    output_text.insert(tk.END, f"{results}\n\n")

def Metodo_Punto_Fijo():
    new_window = tk.Toplevel(root)
    new_window.title("Método del Punto Fijo")
    output_text = tk.Text(new_window, wrap=tk.WORD, height=20, width=80)
    output_text.pack(pady=10)
    
    def g(x):
        return m.sqrt(m.e**x / 3)
    
    x0 = 0
    n = 5
    tol = 6
    results = ""
    
    for k in range(n):
        x1 = g(x0)
        error = abs((x1 - x0) / x1) * 100
        results += f"x{k + 1} = {x1}\nError = {error}\n\n"
        if error < tol:
            results += "Es punto fijo\n"
            break
        x0 = x1
    
    output_text.insert(tk.END, "Método del Punto Fijo\n")
    output_text.insert(tk.END, f"{results}\n\n")

# Crear ventana principal de Tkinter
root = tk.Tk()
root.title("Métodos Numéricos")

# Crear botones para cada método
button_interpolacion = tk.Button(root, text="Interpolación", command=Interpolacion)
button_interpolacion.pack(pady=5)

button_newton_raphson = tk.Button(root, text="Newton-Raphson", command=Newton_Raphson)
button_newton_raphson.pack(pady=5)

button_newton_raphson_modificado = tk.Button(root, text="Newton-Raphson Modificado", command=Newton_Raphson_Modificado)
button_newton_raphson_modificado.pack(pady=5)

button_secante = tk.Button(root, text="Método de la Secante", command=Metodo_Secante)
button_secante.pack(pady=5)

button_punto_fijo = tk.Button(root, text="Método del Punto Fijo", command=Metodo_Punto_Fijo)
button_punto_fijo.pack(pady=5)

# Crear botón para salir
button_exit = tk.Button(root, text="Salir", command=root.quit)
button_exit.pack(pady=5)

# Iniciar el bucle principal de Tkinter
root.mainloop()
