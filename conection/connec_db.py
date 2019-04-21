import sqlite3

class Conectar():
    nombre_bd = "db/sistema.db"

    def run_db(self, query, params = ()):
        with sqlite3.connect(self.nombre_bd) as conn:
            cursor = conn.cursor()
            datos = cursor.execute(query, params)
            conn.commit()
        return datos