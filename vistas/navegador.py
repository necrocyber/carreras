# Importamos librerias GUI
from tkinter import *
from tkinter import ttk
from vistas.frame_registro import *

class App(ttk.Frame):
    def __init__(self, ventana):
        super().__init__(ventana) # herencias
        self.mi_ventana = ventana
        self.mi_ventana.title("System Form")
        self.mi_ventana.iconbitmap("img/bt.ico")

        # Creamos el navegador
        self.navegador = ttk.Notebook(self)

        # Creamos la primera pestaña
        # Inicio
        self.inicio = Label(self.navegador, text = "Pagina de Inicio")
        self.navegador.add(self.inicio, text = "Inicio")

        # Registros
        self.registro = Registro(self.navegador)
        self.navegador.add(self.registro, text = "Registro")

        self.navegador.pack()
        self.pack()