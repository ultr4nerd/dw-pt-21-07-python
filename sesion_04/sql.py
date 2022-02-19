import sqlite3


def crear_conexion():
    try:
        return sqlite3.connect(":memory:")
    except sqlite3.Error as e:
        print(e)


def crear_tabla(conn):
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE employees(id integer PRIMARY KEY, name text, salary real, department text, position text, hireDate text)")
    conn.commit()


def insertar(conn, entities):
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO employees(id, name, salary, department, position, hireDate) VALUES(?, ?, ?, ?, ?, ?)', entities)
    conn.commit()


def leer(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM employees')
    rows = cursor.fetchall()
    for row in rows:
        print(row)


conn = crear_conexion()
crear_tabla(conn)
entities = (2, 'Andrew', 800, 'IT', 'Tech', '2018-02-06')
insertar(conn, entities)
entities = (3, 'Mauricio', 100, 'IT', 'Tech', '2018-02-06')
insertar(conn, entities)
leer(conn)
conn.close()
