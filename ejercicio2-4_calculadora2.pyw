from tkinter import *
from tkinter import messagebox

class Programa(Frame):
    def __init__(self, master = None):
        super().__init__(master, width = 500, height = 350, bg = "MediumPurple4")
        self.master = master
        self.pack_propagate(False) 
        self.pack(expand=True)
        self.menu()
    
    def suma(self):
        try:
            a = float(self.num1.get())
            b = float(self.num2.get())
            total = a + b
            self.resul.set(total)
        except ValueError:
            messagebox.showwarning("Error", "Ingrese valores numéricos")
    def resta(self):
        try:
            a = float(self.num1.get())
            b = float(self.num2.get())
            total = a - b
            self.resul.set(total)
        except ValueError:
            messagebox.showwarning("Error", "Ingrese valores numéricos")
    def multiplicacion(self):
        try:
            a = float(self.num1.get())
            b = float(self.num2.get())
            total = a * b
            self.resul.set(total)
        except ValueError:
            messagebox.showwarning("Error", "Ingrese valores numéricos")
    def division(self):
        try:
            a = float(self.num1.get())
            b = float(self.num2.get())
            if b == 0:
                messagebox.showwarning("Error", "No se puede dividir por 0")
            else:
                total = a / b
                self.resul.set(total)
        except ValueError:
            messagebox.showwarning("Error", "Ingrese valores numéricos")
    
    def funciones(self):
        # diccionario con clave, valor
        operaciones = {
            1: self.suma,
            2: self.resta,
            3: self.multiplicacion,
            4: self.division
        }

        # llama a las funciones
        operacion = self.rta_opcion.get()
        if operacion in operaciones:
            operaciones[operacion]()
        else:
            messagebox.showwarning("Error", "Seleccione una operación")

    def menu(self):
        contenedor_total = Frame(self, width= 300, height= 300, bg= "MediumPurple3" )
        contenedor_total.pack(expand= True, ipadx= 10, ipady= 10)
        contenedor = Frame(contenedor_total, width= 200, height= 200, bg= "MediumPurple3")
        contenedor.pack(expand=True)
        contenedor_radio = Frame(contenedor, bg= "MediumPurple3")
        contenedor_radio.grid(row= 1, column= 3, rowspan= 3)

        self.num1 = StringVar(value= "")
        self.num2 = StringVar(value= "")
        self.resul = StringVar(value= "")

        Label(contenedor, text="Valor 1", font=("Verdana", 11), justify=LEFT, bg="MediumPurple3").grid(row= 1, column= 0, pady= 14, padx= 10, sticky= W)
        Label(contenedor, text="Valor 2", font=("Verdana", 11), justify= LEFT, bg="MediumPurple3").grid(row= 2, column= 0, pady= 5, padx= 10, sticky= W)
        Label(contenedor, text="Resultado", font=("Verdana", 11), justify= LEFT, bg="MediumPurple3").grid(row= 3, column= 0, pady= 10, padx= 10, sticky= W)
        Label(contenedor, text="Operaciones", font=("Verdana", 11), justify= LEFT, bg="MediumPurple3").grid(row= 0, column= 3, pady= 10, padx= 10, sticky= W)

        self.numero1 = Entry(contenedor)
        self.numero1.config(textvariable= self.num1, font =("Verdana", 11), width= 14, justify= CENTER)
        self.numero1.grid(row= 1, column= 2)
        self.numero2 = Entry(contenedor)
        self.numero2.config(textvariable= self.num2, font =("Verdana", 11), width= 14, justify= CENTER)
        self.numero2.grid(row= 2, column= 2)
        self.resultado = Entry(contenedor)
        self.resultado.config(textvariable= self.resul, font =("Verdana", 11), width= 14, state= "readonly", justify= CENTER)
        self.resultado.grid(row= 3, column= 2)
        self.boton = Button(contenedor, text="Calcular", justify= CENTER, font =("Verdana", 11), command= self.funciones)
        self.boton.grid(row= 4, column = 2, pady= 8)

        self.rta_opcion = IntVar()
        self.opcion1 = Radiobutton(contenedor_radio, text="Sumar", variable= self.rta_opcion, value= 1, bg= "MediumPurple3").pack(anchor= W)
        self.opcion2 = Radiobutton(contenedor_radio, text="Restar", variable= self.rta_opcion, value= 2, bg= "MediumPurple3").pack(anchor= W)
        self.opcion3 = Radiobutton(contenedor_radio, text="Multiplicar", variable= self.rta_opcion, value= 3, bg= "MediumPurple3").pack(anchor= W)
        self.opcion4 = Radiobutton(contenedor_radio, text="Dividir", variable= self.rta_opcion, value= 4, bg= "MediumPurple3").pack(anchor= W)

ventana = Tk()
ventana.wm_title("Calculadora 2")
ventana.wm_resizable(0,0)
entradas = Programa(ventana)
entradas.mainloop()