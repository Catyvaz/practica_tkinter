#Ejercicio 1.1 - Contador Creciente.
import tkinter as tk

ventana = tk.Tk()
ventana.title("Contador Creciente")
ventana.geometry("600x400")
ventana.resizable(False, False)
ventana.configure(bg="PeachPuff4")

numero = tk.IntVar(value=0)

def subir():
    valor = numero.get()
    valor += 1
    numero.set(valor)

contenedor = tk.Frame(ventana)
contenedor.configure(width="550", height="400", bg="PeachPuff3", bd= 50)

texto1 = tk.Label(contenedor, text= "Contador", padx= 10, pady=10)
texto1.config(fg="black", bg= "PeachPuff3", font=("TimesNewRoman", 15))
texto1.grid(row=2, column=1)

entrada = tk.Entry(contenedor)
entrada.config(fg="Black", bg="White", font=("TimesNewRoman", 15))
entrada.config(text = numero)

entrada.grid(row=2, column= 2)

boton = tk.Button(contenedor, text= "+", width= "5", command= subir)
boton.config(fg= "Black", bg= "DarkOliveGreen3", font=("TimesNewRoman", 14))
boton.grid(row=2, column=3, padx= 5, pady= 5)

contenedor.pack(expand=True)
ventana.mainloop()