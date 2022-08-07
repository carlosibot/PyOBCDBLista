import sqlite3

conn = sqlite3.connect('Alumnos-lista.db')
cursor = conn.cursor()
def crear_tabla():
    cursor.execute("CREATE TABLE IF NOT EXISTS tabla_alumnos(id INT , Nombre TEXT, Apellido TEXT)")
def entrada_informacion():
    cursor.execute("INSERT INTO tabla_alumnos VALUES(1 ,'Juan' ,'Morales')")
    cursor.execute("INSERT INTO tabla_alumnos VALUES(2 ,'Pedro' ,'Perez')")
    cursor.execute("INSERT INTO tabla_alumnos VALUES(3 ,'Miguel' ,'Millan')")
    cursor.execute("INSERT INTO tabla_alumnos VALUES(4 ,'Jessica' ,'Pillar')")
    cursor.execute("INSERT INTO tabla_alumnos VALUES(5,'Diego','Montaner')")
    cursor.execute("INSERT INTO tabla_alumnos VALUES(6 ,'Edison' ,'Ramirez')")
    cursor.execute("INSERT INTO tabla_alumnos VALUES(7,'Maria' ,'Miranda')")
    cursor.execute("INSERT INTO tabla_alumnos VALUES(8 ,'Pilar' ,'Montoya')")
    
def consulta():
    query = cursor.execute("SELECT Nombre FROM tabla_alumnos WHERE id=2")
    for alumno in query:
        print("Nombre del alumno", alumno)
        break
    conn.commit()
crear_tabla()
entrada_informacion()
consulta()
cursor.close()
conn.close()