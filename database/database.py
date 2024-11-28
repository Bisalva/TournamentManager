# PROBANDO LO BASICO DE LA BD DEL GESTOR DE TORNEOS
import sqlite3

def conexionDB():
    conexion = sqlite3.connect("tournament.db")
    return conexion

def createTable():
    conexionToDB = conexionDB()
    cursor = conexionToDB.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS grupos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombreGrupo TEXT NOT NULL,
        victoriasGrupo INTEGER,
        derrotasGrupo INTEGER
        )
    """)
    
    conexionToDB.commit()
    conexionToDB.close()

def insertNewGroup(nombre):

    conexionToDB = conexionDB()
    cursor = conexionToDB.cursor()

    cursor.execute("INSERT INTO grupos (nombreGrupo, victoriasGrupo, derrotasGrupo) VALUES (?, 0, 0)",(nombre))
    
    conexionToDB.commit()
    conexionToDB.close()
    
def insertOldGroup(nombre,victorias,derrotas):

    conexionToDB = conexionDB()
    cursor = conexionToDB.cursor()

    cursor.execute("INSERT INTO grupos(nombreGrupo, victoriasGrupo, derrotasGrupo) VALUES (?, ?, ?)",(nombre,victorias,derrotas))

    conexionToDB.commit()
    conexionToDB.close()