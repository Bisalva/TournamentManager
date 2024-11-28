from database import database

def main():
    #Crea la tabla si es que no existe
    database.createTable()

    #input a la tabla
    #Newgroup = () INPUTNAME, VICTORY = 0, DEFEAT = 0 
    database.insertNewGroup("Raix")

    #Oldgroup = () INPUTNAME, INPUTVICTORIES, INPUTDEFEATS
    database.insertOldGroup("Mandragora",4,2)

    conexion = database.conexionDB()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM grupos")

    grupos = cursor.fetchall()

    conexion.close()

    print("Grupos : ")
    for grupo in grupos:
        print(grupo)

if __name__ == "__main__":
    main()




