def suma(a, b):
    return a + b


def multiplicacion(a, b):
    acumulador = 0
    for _ in range(b):
        acumulador = suma(acumulador, a)
    return acumulador
