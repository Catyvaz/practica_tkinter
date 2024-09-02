from tkinter import *
from tkinter import messagebox
import random

class Programa(Frame):
    def __init__(self, master = None):
        super().__init__(master, width = 400, height = 300, bg = "sienna4")
        self.master = master
        self.pack_propagate(False) 
        self.pack(expand=True)
        self.menu()

    def numero_random(self):
        n1 = self.lim1.get()
        n2 = self.lim2.get()
        if n1 < n2:
            rta = random.randint(n1, n2)
            self.numR.set(rta)
        else:
            messagebox.showerror("Error", "El primer número debe ser menor que el segundo")
    
    def menu(self):
        contenedor_total = Frame(self, width= 300, height= 300, bg= "salmon2" )
        contenedor_total.pack(expand= True, ipadx= 10, ipady= 10)
        contenedor = Frame(contenedor_total, width= 200, height= 200, bg= "salmon2")
        contenedor.pack(expand=True)
        
        self.lim1 = IntVar()
        self.lim2 = IntVar()
        self.numR = StringVar(value= "")

        Label(contenedor, text="Número 1", font=("Times New Roman", 11), justify=LEFT, bg="salmon2").grid(row= 0, column= 0, pady= 14, padx= 10, sticky= W)
        Label(contenedor, text="Número 2", font=("Times New Roman", 11), justify= LEFT, bg="salmon2").grid(row= 1, column= 0, pady= 5, padx= 10, sticky= W)
        Label(contenedor, text="Número Generado", font=("Times New Roman", 11), justify= LEFT, bg="salmon2").grid(row= 2, column= 0, pady= 10, padx= 10, sticky= W)

        self.n1 = Spinbox(contenedor, textvariable= self.lim1, from_= 0, to=25, increment= 1, font= ("Times New Roman", 11), justify= CENTER)
        self.n1.grid(row= 0, column= 1, pady= 14, padx= 5, sticky= S)
        self.n2 = Spinbox(contenedor, textvariable= self.lim2, from_= 0, to=25, increment= 1, font= ("Times New Roman", 11), justify= CENTER)
        self.n2.grid(row= 1, column= 1, pady= 14, padx= 5, sticky= S)
        self.salida = Entry(contenedor)
        self.salida.config(textvariable= self.numR, font =("Times New Roman", 11), width= 18, state= "readonly", justify= CENTER)
        self.salida.grid(row= 2, column= 1)

        self.generar = Button(contenedor, text="Generar", justify= CENTER, font =("Times New Roman", 11), command= self.numero_random)
        self.generar.grid(row= 3, column= 1, pady= 10)

ventana = Tk()
ventana.wm_title("Generador de Números")
ventana.wm_resizable(0,0)
entradas = Programa(ventana)
entradas.mainloop()