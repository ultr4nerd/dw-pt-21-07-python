numero1_texto = input("Dame el primer número: ")
numero2_texto = input("Dame el segundo: ")

numero1 = int(numero1_texto)
numero2 = int(numero2_texto)

resultado_resta = numero1 - numero2
resultado_modulo = numero1 % numero2

mensaje = "El resultado de la resta es {} y el resultado del módulo es {}".format(resultado_resta, resultado_modulo)
print(mensaje)
