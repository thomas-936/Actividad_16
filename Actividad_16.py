import tkinter as tk

ventana = tk.Tk()
ventana.title("Calculadora ;)")
ventana.geometry("300x300")

etiqueta1 = tk.Label(ventana, text="Escribe el primer número: ")
etiqueta1.pack(pady=5)
entrada1= tk.Entry(ventana)
entrada1.pack(pady=5)
etiqueta2 = tk.Label(ventana, text="Escribe el segundo número: ")
etiqueta2.pack(pady=5)
entrada2 = tk.Entry(ventana)
entrada2.pack(pady=5)

resultado = tk.Label(ventana, text="Resultado: ")
resultado.pack(pady=10)

def Sumar():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        resultado.config(text=f"Resultado:{num1+num2} ")
    except ValueError:
        resultado.config(text="Error... Ingresa números validos")

def Restar():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        resultado.config(text=f"Resultado: {num1-num2}")
    except ValueError:
        resultado.config(text="Error... Ingresa números validos")

def Multiplicar():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        resultado.config(text=f"Resultado: {num1*num2}")
    except ValueError:
        resultado.config(text="Error... Ingresa números validos")