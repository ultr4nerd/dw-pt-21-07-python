# Las listas son ordenadas y dinámicas
numeros = [1, 2, 3, 4, 5]
cadenas = ["hola", "mundo"]

lista_vacia_1 = []
lista_vacia_2 = list()

# Operaciones

# Concatenación
x = [1, 2, 3] + [4, 5, 6]

# Lectura
hola = cadenas[0]
mundo = cadenas[1]
ultimo = cadenas[-1]
penultimo = cadenas[-2]

# Escritura
cadenas.append("cruel")
cadenas.insert(1, "mi")

# Eliminar
eliminado = cadenas.pop()  # Sin especificar índice (eliminando el último elemento)
eliminado = cadenas.pop(1)  # Especificando un índice
del cadenas[1]

# Convertir cadena de texto a lista
lista = list("hola")

# Slices
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# La primer parte es inclusiva y la segunda parte es exclusiva
lista2 = lista[3:5]
lista3 = lista[1:8:2]  # Podemos definir un salto (step)
lista4 = lista[8:1:-1]  # Recorrido al revés
lista4 = lista[:6]  # Se obvia que se empieza desde el primer elemento
lista5 = lista[2:]  # Se obvia que se acaba en el último elemento
copia = lista[:]  # Se obviaron el primero y el último

# Búsqueda
1 in [1, 2, 3, 4, 5]
