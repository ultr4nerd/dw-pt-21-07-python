# Los diccionarios son "desordenados" y dinámico

# Lectura lineal

# Definición
vacio = {}
vacio = dict()
capitales = {"jalisco": "guadalajara", "nuevo leon": "monterrey"}
usuario = {
    "correo": "team@bedu.org",
    "nombre": "Miguel",
    "edad": 34,
    "objecto": "entidad que posee propiedades y habilidades",
}

# Lectura
edad = usuario["edad"]  # Si no existe, lanza una excepción
edad = usuario.get("edad")  # Si no existe, devuelve None

# Escritura
usuario["edad"] = 35  # Si la llave ya existe, se actualiza
usuario["apellido"] = "Jimenez"  # Si la llave NO existe, se agrega

# Eliminar elementos
eliminado = usuario.pop("apellido")
del usuario["edad"]

# Búsqueda
"edad" in usuario
