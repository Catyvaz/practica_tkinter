from tkinter import *
from tkinter import messagebox

class Programa(Frame):
    def __init__(self, master = None):
        super().__init__(master, width = 400, height = 350, bg = "NavajoWhite4")
        self.master = master
        self.pack_propagate(False) 
        self.pack(expand=True)
        self.ingresos()
        self.botones()
    
    def suma(self):
        try:
            a = float(self.num1.get())
            b = float(self.num2.get())
            total = a + b
            self.resultado.set(total)
        except ValueError:
            messagebox.showwarning("Error", "Ingrese valores numéricos")
    def resta(self):
        try:
            a = float(self.num1.get())
            b = float(self.num2.get())
            total = a - b
            self.resultado.set(total)
        except ValueError:
            messagebox.showwarning("Error", "Ingrese valores numéricos")
    def multiplicacion(self):
        try:
            a = float(self.num1.get())
            b = float(self.num2.get())
            total = a * b
            self.resultado.set(total)
        except ValueError:
            messagebox.showwarning("Error", "Ingrese valores numéricos")
    def division(self):
        try:
            a = float(self.num1.get())
            b = float(self.num2.get())
            total = a / b
            self.resultado.set(total)
        except ValueError:
            messagebox.showwarning("Error", "Ingrese valores numéricos")
    def porcent(self):
        try:
            a = float(self.num1.get())
            b = float(self.num2.get())
            total = a % b
            self.resultado.set(total)
        except ValueError:
            messagebox.showwarning("Error", "Ingrese valores numéricos")
    def borrar(self):
        self.num1.set("")
        self.num2.set("")
        self.resultado.set("")

    def ingresos(self):
        contenedor1 = Frame(self, width= 300, height= 250, bg= "NavajoWhite3")
        contenedor1.pack(pady= 20)
        
        self.num1 = StringVar(value="")
        self.num2 = StringVar(value="")
        self.resultado = StringVar(value="")

        self.primer = Label(contenedor1, text= "Primer Número", font =("Times New Roman", 11), bg= "NavajoWhite3",anchor= W)
        self.entrada_primer = Entry(contenedor1, justify='center')
        self.entrada_primer.config(textvariable= self.num1, font =("Times New Roman", 11))
        self.segundo = Label(contenedor1, text="Segundo Número", font =("Times New Roman", 11), bg= "NavajoWhite3", anchor= W)
        self.entrada_segundo = Entry(contenedor1, justify='center', textvariable= self.num2)
        self.entrada_segundo.config(font =("Times New Roman", 11))
        self.resultado_rta = Label(contenedor1, text="Resultado", font =("Times New Roman", 11), bg= "NavajoWhite3", anchor= W)
        self.salida_resultado = Entry(contenedor1, state='readonly', justify='center')
        self.salida_resultado.config(text = self.resultado, font =("Times New Roman", 11))

        self.primer.grid(row = 0, column = 0, padx= 8, pady=8, ipadx= 10, sticky= W)
        self.entrada_primer.grid(row = 0, column = 1, padx= 8, pady=8)
        self.segundo.grid(row = 1, column = 0, padx= 8, pady=8, ipadx= 10, sticky= W)
        self.entrada_segundo.grid(row = 1, column = 1, padx= 8, pady=8)
        self.resultado_rta.grid(row = 2, column = 0, padx= 8, pady=8, ipadx= 10, sticky= W) 
        self.salida_resultado.grid(row = 2, column = 1, padx= 8, pady=8)
    
    def botones(self):
        contenedor2 = Frame(self, width= 350, height= 250, bg= "NavajoWhite3")
        contenedor2.pack(pady= 5)

        self.suma = Button(contenedor2, text="+", font =("Times New Roman", 11), command= self.suma)
        self.resta = Button(contenedor2, text="-", font =("Times New Roman", 11), command= self.resta)
        self.multiplicar = Button(contenedor2, text="*", font =("Times New Roman", 11), command= self.multiplicacion)
        self.dividir = Button(contenedor2, text="/", font =("Times New Roman", 11), command= self.division)
        self.porcentaje = Button(contenedor2, text="%", font =("Times New Roman", 11), command = self.porcent)
        self.limpiar = Button(contenedor2, text="CLEAR", font =("Times New Roman", 11), command= self.borrar)

        self.suma.grid(row = 4, column = 0, padx= 10, pady=10, ipadx= 55)
        self.resta.grid(row = 4, column = 1, padx= 10, pady=10, ipadx= 55)
        self.multiplicar.grid(row = 5, column = 0, padx= 10, pady=10, ipadx= 56)
        self.dividir.grid(row = 5, column = 1, padx= 10, pady=10, ipadx= 56)
        self.porcentaje.grid(row = 6, column = 0, padx= 10, pady=10, ipadx= 54)
        self.limpiar.grid(row = 6, column = 1, padx= 10, pady=10, ipadx= 33)

ventana = Tk()
ventana.wm_title("Calculadora")
ventana.wm_resizable(0,0)
entradas = Programa(ventana)
entradas.mainloop()