from tkinter import *
from tkinter import messagebox

class Programa(Frame):
    def __init__(self, master = None):
        super().__init__(master, width = 450, height = 350, bg = "DeepSkyBlue3")
        self.master = master
        self.pack_propagate(False) 
        self.pack(expand=True)
        self.ingreso_peliculas()
        self.lista_peliculas()
    
    def validar(self):
        oracion = str((self.ingreso.get()).lower()).split()
        peliculas_listadas = self.lista.get(0, END)
        for peliculas in peliculas_listadas:
            if (peliculas.lower()).split() == oracion:
                return False
        return True

    def agregar_peliculas(self):
        valor = self.ingreso.get()
        valid = self.validar()
        if valid:
            self.ingreso.set("")
            self.lista.insert(0, valor)
        else:
            messagebox.showwarning("Repetido", "Ya existe esa pelicula en la lista")
            self.ingreso.set("")

    def ingreso_peliculas(self):
        contenedor_ingreso = Frame(self, width= 300, height= 300, bg= "SkyBlue2")
        contenedor_ingreso.grid(row = 0, column = 0, pady= 20, padx=18, ipadx= 20, ipady= 65)
        contenedor = Frame(contenedor_ingreso, bg= "SkyBlue2")
        contenedor.pack(expand=True)

        self.ingreso= StringVar()

        Label(contenedor, text="Escribe el titulo de una pelicula", font=("Times New Roman", 11), justify= CENTER, bg="SkyBlue2").pack(padx= 10, pady= 10)
        self.pelicula = Entry(contenedor)
        self.pelicula.config(textvariable= self.ingreso, font =("Times New Roman", 11), width= 30)
        self.pelicula.pack(padx= 10, pady= 10)
        self.boton_entrada = Button(contenedor, text= "Añadir", justify= CENTER, font =("Times New Roman", 11), command= self.agregar_peliculas)
        self.boton_entrada.pack(padx= 10, pady= 10)

    def lista_peliculas(self):
        contenedor_lista = Frame(self, width= 250, height= 300, bg= "SkyBlue2")
        contenedor_lista.grid(row = 0, column = 1,pady= 20, padx=18, ipadx= 20, ipady= 20)
        contenedor1 =Frame(contenedor_lista, bg= "SkyBlue2")
        contenedor1.pack(expand=True)

        Label(contenedor1, text="Peliculas", font =("Times New Roman", 15, "bold"), justify= CENTER, bg="SkyBlue2").pack(padx= 10, pady= 6)
        self.lista = Listbox(contenedor1, width= 30, height= 10, font= ("Times New Roman", 11))
        self.lista.pack(padx= 10, pady= 6)

ventana = Tk()
ventana.wm_title("Lista de Peliculas")
ventana.wm_resizable(0,0)
entradas = Programa(ventana)
entradas.mainloop()