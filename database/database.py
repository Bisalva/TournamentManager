# PROBANDO LO BASICO DE LA BD DEL GESTOR DE TORNEOS
import sqlite3

conexion = sqlite3.connect("tournament.db")

cursor = conexion.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS grupos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombreGrupo TEXT NOT NULL,
    victoriasGrupo INTEGER,
    derrotasGrupo INTEGER
    )
""")

cursor.execute("INSERT INTO grupos (nombreGrupo, victoriasGrupo, derrotasGrupo ) VALUES ('Titanes', 0, 0)")

conexion.commit()

cursor.execute("SELECT * FROM grupos")

gruposQuary = cursor.fetchall()

print("Grupos y Estadisticas")
for grupo in gruposQuary:
    print(f"ID: {grupo[0]}, Grupo: {grupo[1]}, Victorias: {grupo[2]}, Derrotas: {grupo[3]}")

# Cerrar el cursor y la conexión
cursor.close()
conexion.close()
