# Creamos la vista de Registro
from tkinter import *
from tkinter import ttk
from conection.connec_db import *

class Registro(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Funciones para los botones
        def nuevo():
            self.entry_nombre.config(state = "normal")
            self.entry_costo.config(state = "normal")
            self.entry_categoria.config(state = "normal")

        def guardar():
            self.entry_nombre.config(state = "readonly")
            self.entry_costo.config(state = "readonly")
            self.entry_categoria.config(state = "readonly")

        # Titutlo de la ventana
        self.titulo = Label(self, text = "Pagina de Registro")
        self.titulo.grid(row = 0, column = 0, columnspan = 2, pady = 10, padx = 10)
        self.titulo.config(anchor = "e")
        # Input del nombre de la carrera
        Label(self, text = "Nombre Carrera").grid(row = 1, column = 0 ,pady = 10, padx = 10)
        self.entry_nombre = Entry(self, state = "readonly")
        self.entry_nombre.grid(row = 1, column = 1, pady = 10, padx = 10) 
        # Input del costo anual
        Label(self, text = "Costo Anual").grid(row = 2, column = 0, pady = 10, padx = 10)
        self.entry_costo = Entry(self, state = "readonly")
        self.entry_costo.grid(row = 2, column = 1, pady = 10, padx = 10)
        # categoria
        Label(self, text = "Categoria").grid(row = 3, column = 0, pady = 10, padx = 10)
        self.entry_categoria = Entry(self, state = "readonly")
        self.entry_categoria.grid(row = 3, column = 1, pady = 10, padx = 10)

        # Botones con acciones
        Button(self, text = "Nuevo", command = nuevo).grid(row = 4, column = 0, pady = 10, padx = 10)
        Button(self, text = "Guardar", command = guardar).grid(row = 4, column = 1, pady = 10, padx = 10)


        # Tabla de registros
        self.tabla = ttk.Treeview(self, columns = ("",""))
        self.tabla.grid(row = 5, column = 0, columnspan = 3, pady = 10, padx = 10)
        self.tabla.heading("#0", text = "Nombre Carrera")
        self.tabla.heading("#1", text = "Costo Anual")
        self.tabla.heading("#2", text = "Categoria")

        # Funciones de botones Editar y Eliminar
        def Editar():
            pass

        def Eliminar():
            pass    

        # Botones con acciones
        Button(self, text = "Editar").grid(row = 6, column = 0, pady = 10, padx = 10)
        Button(self, text = "Eliminar").grid(row = 6, column = 1, pady = 10, padx = 10)

        # Listar los datos en la tabla desde sqlite3
        def listar_datos():
            query = "SELECT * FROM carreras"
            conn = Conectar()
            datos = conn.run_db(query)
            for carrera in datos:
                self.tabla.insert('', 0, text = carrera[0], value=(carrera[1], carrera[2]))

        listar_datos()        