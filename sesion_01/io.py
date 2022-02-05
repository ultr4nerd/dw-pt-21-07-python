# print - salida (output) de datos
# input - entrada (input) de datos

message = "Ingresa el texto"
print(message)
texto = input()
resultado = "Ingresaste: {}".format(texto)
print(resultado)

# Nos ahorramos el print y espera en la misma línea
respuesta = input("¿Cúal es la capital de Jalisco? ")
print(respuesta == "Guadalajara")

# input SIEMPRE regresa str
numero = input("Ingresa el número a sumar: ")
resultado = 10 + numero  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
print("El resultado es: {}".format(resultado))
