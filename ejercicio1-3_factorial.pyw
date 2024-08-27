#Ejercicio 1.3 - Factorial.
import tkinter as tk

ventana = tk.Tk()
ventana.title("Factorial")
ventana.geometry("600x400")
ventana.resizable(False, False)
ventana.configure(bg="GREY38")

numero = tk.IntVar(value= 0)
rta = tk.StringVar(value= "")

def factorial(valor):
    valor = int(valor)
    if valor == 0 or valor == 1:
        return 1
    return valor * factorial(valor - 1)

def mostrar():
    n = numero.get()
    resultado = factorial(n)
    rta.set(resultado)

#Contenedor de todito
contenedor = tk.LabelFrame(ventana, text= "Factorial")
contenedor.configure(width= 500, height= 300, bg="grey52")
contenedor.configure(padx= 50, pady=50)

#Etiqueta que tiene la n para le número
etiqueta_numero = tk.Label(contenedor, text="N")
etiqueta_numero.grid(row=1, column= 2, padx= 10, pady=10)

#Entry donde se va a poner el número
entrada_numero = tk.Entry(contenedor)
entrada_numero.config( text = numero, justify='center')
entrada_numero.grid(row=1, column=3, padx= 10, pady=10)

#Etiqueta que denota donde se va a mostrar el factorial
etiqueta_factorial = tk.Label(contenedor, text="Factorial (n)")
etiqueta_factorial.grid(row=2, column= 2, padx= 10, pady=10)

#Entry donde se va a ver el factorial, no editable
entrada_factorial = tk.Entry(contenedor)
entrada_factorial.config(text = rta, state='readonly', justify='center')
entrada_factorial.grid(row=2, column=3, padx= 10, pady=10)

#Botorn que calcula
boton_calcular = tk.Button(contenedor, text="siguiente", padx= 10, pady=8, command= mostrar)
boton_calcular.grid(row=3, column=3)

numero.set(int(numero.get()) + 1)

contenedor.pack(expand=True)
ventana.mainloop()