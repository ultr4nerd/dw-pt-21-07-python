import time

def monitorear(funcion_decorada):
    def wrapper(a, b):
        print(f"El valor de a es: {a}")
        print(f"El valor de b es: {b}")
        value = funcion_decorada(a, b)
        print(f"El resultado de {a} + {b} es: {value}")
        return

    return wrapper

def cronometrar(funcion):
    def wrapper(*args, **kwargs):
        start = time.time()
        value = funcion(*args, *kwargs)
        end = time.time()
        print(f"La función tardó: {end - start}")
        return value
    return wrapper


@cronometrar
def suma(a, b):
    return a + b

@cronometrar
def multiplicacion(a, b):
    return a * b


suma(1, 2)
multiplicacion(3, 4)
