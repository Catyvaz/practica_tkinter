from tkinter import *

def Contenedor_ingresos(Frame):
    def __init__(self, master):
        super().__init__(master, width = 300, height = 400, bg = "NavajoWhite3", padx= 50, pady=15)
        self.master = master
        self.pack(expand = True)
        self.ingresos()
    
    def ingresos(self):
        self.primer = Label(self, text= "Primer Número")
        self.entrada_primer = Entry(self)
        self.segundo = Label(self, text="Segundo Número")
        self.entrada_segundo = Entry(self)
        self.resultado = Label(self, text="Resultado")
        self.salida_resultado = Entry(self)

        self.primer.grid(row = 0, column = 0)
        self.entrada_primer.grid(row = 0, column = 1)
        self.segundo.grid(row = 1, column = 0)
        self.entrada_segundo.grid(row = 1, column = 1)
        self.resultado.grid(row = 2, column = 1)
        self.salida_resultado.grid(row = 2, column = 1)

ventana = Tk()
ventana.wm_title("Calculadora")
ventana.wm_geometry("350x450")
ventana.wm_resizable(0,0)
ventana.configure(bg="navajowhite4")
entradas = Contenedor_ingresos(ventana)
ventana.mainloop()
