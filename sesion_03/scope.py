resultado = "hola"  # Alcance global

def suma(x, y):
    resultado = x + y  # Shadowing (ofuscar)
    print(f"El resultado es {resultado}")

suma(7, 8)
print(resultado)

edad = 24  # Alcance global


def funcion():
    edad = 23  # Alcance local
    print(edad)


print(edad)  # 24