import datetime

# Valores
verdadero = True
falso = False

# Operaciones lógicas

p = True
q = False

# AND
resultado = p and q

# OR
resultado = p or q

# NOT
resultado = not p


# Operaciones de comparación

comparacion = 7 <= 8  # Diferencia
comparacion = 9 == 9  # Igualdad


# Operaciones de búsqueda

busqueda = 7 in [1, 2, 3, 4, 5, 6, 7]

diccionario = {"llave": "valor"}
busqueda = "llave" in diccionario

# Comparación de objetos
fecha1 = datetime.datetime(2022, 2, 5)
fecha2 = datetime.datetime(2022, 2, 5)
fecha3 = fecha1

fecha1 == fecha2  # True
fecha1 is fecha2  # False
fecha1 is fecha3  # True

# Valores truthy y falsy

# Truthy (números diferentes a 0, cadenas NO vacías, iterables no vacíos, objetos)
truthy = bool(7)

# Falsy (el 0, cadenas vacías, iterables vacíos, None)
falsy = bool(0)

# Tipo None
variable = None
