# Argumentos posicionales

def suma(a, b):
    return a + b

# Argumentos posicionales arbitratios (args)


def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    return resultado

# Argumentos opcionales


def potencia(base, n=2):
    return base ** n


# Argumentos opcionales arbitrarios (kwargs)
def crear_usuario(**atributos):
    usuario = {
        "fecha_creacion": "12-02-2022"
    }

    for key, value in atributos.items():
        usuario[key] = value

    return usuario


usuario = crear_usuario(
    nombre="Mauricio", apellido="Chávez", email="mauricio@bedu.org",
)
print(usuario)


# Regla para argumentos

def regla(posicional1, posicional2, opcional=True, *args, **kwargs):
    print(posicional1)
    print(posicional2)
    print(opcional)
    print(args)
    print(kwargs)


# Regla para parámetros
regla(1, 2, 3, 4, 5, key="value")
