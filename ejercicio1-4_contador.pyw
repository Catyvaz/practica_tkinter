#Ejercicio 1.4 Contador.
from tkinter import *

def subir():
    valor = numero.get()
    valor += 1
    numero.set(valor)

def bajar():
    valor = numero.get()
    valor -= 1
    numero.set(valor)

def cero():
    valor = 0
    numero.set(valor)

ventana = Tk()
ventana.title("Contador")
ventana.geometry("600x400")
ventana.resizable(False, False)
ventana.configure(bg="slate gray")

numero = IntVar(value=0)

#Contenedor de todito
contenedor = LabelFrame(ventana, text= "Contador")
contenedor.configure(width= 500, height= 340, bg="light grey")
contenedor.configure(padx= 50, pady=50)

texto_contador = Label(contenedor, text= "Contador")
texto_contador.grid(row=1, column= 1, padx= 10, pady=10, ipadx= 15, ipady=10)

entrada_contador = Entry(contenedor)
entrada_contador.config(text = numero, state='readonly', justify='center')
entrada_contador.grid(row=2, column= 1, padx= 10, pady=10, ipadx=4, ipady= 2)

boton_subir = Button(contenedor, text= "Count Up", bd= 3, command=subir)
boton_subir.grid(row=1, column= 4, padx= 10, pady=10)

boton_bajar = Button(contenedor, text= "Count Down", bd= 3, command= bajar)
boton_bajar.grid(row=2, column= 4, padx= 10, pady=10)

boton_reset = Button(contenedor, text="Reset", bd= 3, command= cero)
boton_reset.grid(row=3, column= 4, padx= 10, pady=10) 

contenedor.pack(expand=True)
ventana.mainloop()