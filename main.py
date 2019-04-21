# Developer by Antonio Medel 2019

# Importamos Librerias GUI
from tkinter import *
from tkinter import ttk
# Importamos el Modulo de Navegador
from vistas.navegador import *

if __name__ == "__main__":
    ventana = Tk()
    App = App(ventana)
    ventana.mainloop()