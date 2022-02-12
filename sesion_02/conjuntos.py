# Los conjuntos son "desordenados" y dinámico
conjunto = {1, 2, 3}
conjunto_vacio = set()
invalido = {}  # Esto es un diccionario vacío

# Escritura
conjunto.add(2)  # Si ya está el elemento lo omite, si no, lo pone
conjunto.update([2, 3, 4])  # Mete todos los elementos de la lista

# Eliminar
conjunto.remove(10)  # Si no existe, tira un error KeyError
conjunto.discard(10)  # Si no existe, lo omite

# Operaciones
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Unión
union = A | B
union = A.union(B)

# Intersección
intersection = A & B
intersection = A.intersection(B)

# Nos puede ayudar a quitar repetidos
repetidos = [1, 2, 3, 1, 2, 3, 4]
sin_repetidos = list(set(repetidos))

# Búsqueda
1 in {1, 2, 3, 4, 5}
