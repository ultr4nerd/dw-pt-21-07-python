import sqlite3


class Database:
    def __init__(self):
        try:
            self.conn = sqlite3.connect(":memory:")
        except sqlite3.Error as e:
            print(e)

    def crear_tabla(self):
        cursorObj = self.conn.cursor()
        cursorObj.execute(
            "CREATE TABLE employees(id integer PRIMARY KEY, name text, salary real, department text, position text, hireDate text)"
        )
        self.conn.commit()

    def insertar(self, entities):
        cursor = self.conn.cursor()
        cursor.execute(
            'INSERT INTO employees(id, name, salary, department, position, hireDate) VALUES(?, ?, ?, ?, ?, ?)',
            entities
        )
        self.conn.commit()

    def leer(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM employees')
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    def cerrar_conexion(self):
        self.conn.close()


db = Database()
db.crear_tabla()
entities = (2, 'Andrew', 800, 'IT', 'Tech', '2018-02-06')
db.insertar(entities)
entities = (3, 'Mauricio', 100, 'IT', 'Tech', '2018-02-06')
db.insertar(entities)
db.leer()
db.cerrar_conexion()
