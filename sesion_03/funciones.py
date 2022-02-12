# Declarar
def saludar():
    print("Hola, mundo")


# Llamar
saludar()


# Argumentos y parámetros

def suma(x, y):  # Argumentos
    resultado = x + y
    print(f"El resultado es {resultado}")


suma(5, 9)  # Parámetros

# Regresar valores


def resta(x, y):
    resultado = x - y
    return resultado


x = resta(5, 2)
print(x)


def divmod_v2(x, y):
    div = x // y
    mod = x % y
    return div, mod


div, mod = divmod_v2(7, 2)
print(div)
print(mod)
