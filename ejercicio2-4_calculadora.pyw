from tkinter import *

class Contenedor_ingresos(Frame):
    def __init__(self, master):
        super().__init__(master, width = 200, height = 500, bg = "NavajoWhite3", padx=10, pady=15)
        self.master = master
        self.pack(expand = True)
        self.ingresos()
    
    def ingresos(self):
        self.primer = Label(self, text= "Primer Número", font =("Times New Roman", 10))
        self.entrada_primer = Entry(self, justify='center')
        self.entrada_primer.config( font =("Times New Roman", 10))
        self.segundo = Label(self, text="Segundo Número", font =("Times New Roman", 10))
        self.entrada_segundo = Entry(self, justify='center')
        self.entrada_segundo.config(font =("Times New Roman", 10))
        self.resultado = Label(self, text="Resultado", font =("Times New Roman", 10))
        self.salida_resultado = Entry(self, state='readonly', justify='center')
        self.salida_resultado.config(font =("Times New Roman", 10))

        self.primer.grid(row = 0, column = 0, padx= 8, pady=8, ipadx= 23)
        self.entrada_primer.grid(row = 0, column = 1, padx= 8, pady=8)
        self.segundo.grid(row = 1, column = 0, padx= 8, pady=8, ipadx= 16)
        self.entrada_segundo.grid(row = 1, column = 1, padx= 8, pady=8)
        self.resultado.grid(row = 2, column = 0, padx= 8, pady=8, ipadx= 35) 
        self.salida_resultado.grid(row = 2, column = 1, padx= 8, pady=8)

class Contenedor_botones(Frame):
    def __init__(self, master):
        super().__init__(master, width = 200, height = 500, bg = "NavajoWhite3", padx=10, pady=15)
        self.master = master
        self.pack(expand = True)
        self.botones()
    
    def botones(self):
        self.suma = Button(self, text="+", font =("Times New Roman", 12))
        self.resta = Button(self, text="-", font =("Times New Roman", 12))
        self.multiplicar = Button(self, text="*", font =("Times New Roman", 12))
        self.dividir = Button(self, text="/", font =("Times New Roman", 12))
        self.porcentaje = Button(self, text="%", font =("Times New Roman", 12))
        self.limpiar = Button(self, text="CLEAR", font =("Times New Roman", 12))

        self.suma.grid(row = 0, column = 0)
        self.resta.grid(row = 1, column = 0)
        self.multiplicar.grid(row = 1, column = 1)
        self.dividir.grid(row = 1, column = 2)
        self.porcentaje.grid(row = 2, column = 1)
        self.limpiar.grid(row = 2, column = 2)

ventana = Tk()
ventana.wm_title("Calculadora")
ventana.wm_geometry("400x450")
ventana.wm_resizable(0,0)
ventana.configure(bg="navajowhite4",)
entradas = Contenedor_ingresos(ventana)
entradas.mainloop()
