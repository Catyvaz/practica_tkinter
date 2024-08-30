from tkinter import *

class Programa(Frame):
    def __init__(self, master):
        super().__init__(master, width = 400, height = 600, bg = "NavajoWhite4")
        self.master = master
        self.pack(expand = True)
        self.ingresos()
    
    def ingresos(self):
        contenedor1 = Frame(self, width= 300, height= 200, bg= "NavajoWhite3")

        self.primer = Label(contenedor1, text= "Primer Número", font =("Times New Roman", 11), bg= "NavajoWhite3")
        self.entrada_primer = Entry(contenedor1, justify='center')
        self.entrada_primer.config( font =("Times New Roman", 11))
        self.segundo = Label(contenedor1, text="Segundo Número", font =("Times New Roman", 11))
        self.entrada_segundo = Entry(contenedor1, justify='center')
        self.entrada_segundo.config(font =("Times New Roman", 11))
        self.resultado = Label(contenedor1, text="Resultado", font =("Times New Roman", 11))
        self.salida_resultado = Entry(contenedor1, state='readonly', justify='center')
        self.salida_resultado.config(font =("Times New Roman", 11))

        self.primer.grid(row = 0, column = 0, padx= 8, pady=8, ipadx= 23)
        self.entrada_primer.grid(row = 0, column = 1, padx= 8, pady=8)
        self.segundo.grid(row = 1, column = 0, padx= 8, pady=8, ipadx= 16)
        self.entrada_segundo.grid(row = 1, column = 1, padx= 8, pady=8)
        self.resultado.grid(row = 2, column = 0, padx= 8, pady=8, ipadx= 35) 
        self.salida_resultado.grid(row = 2, column = 1, padx= 8, pady=8)
    
    def botones(self):
        contenedor2 = Frame(self, width= 300, height= 300, bg= "NavajoWhite3")

        self.suma = Button(contenedor2, text="+", font =("Times New Roman", 11))
        self.resta = Button(contenedor2, text="-", font =("Times New Roman", 11))
        self.multiplicar = Button(contenedor2, text="*", font =("Times New Roman", 11))
        self.dividir = Button(contenedor2, text="/", font =("Times New Roman", 11))
        self.porcentaje = Button(contenedor2, text="%", font =("Times New Roman", 11))
        self.limpiar = Button(contenedor2, text="CLEAR", font =("Times New Roman", 11))

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