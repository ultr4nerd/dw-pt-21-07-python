try:
    number = int(input("Dame un número para dividir a 10: "))
    message = f"El resultado es {10 / number}"
    print(message)
except ZeroDivisionError:
    print("No puedo dividir entre cero...")
except ValueError:
    print("El valor que pasaste no es un número entero...")
except:
    print("\nLo siento, algo salió mal")


class DivisionEntreCero(Exception):
    pass


def division(a, b):
    if b == 0:
        raise DivisionEntreCero("No puedes dividir entre cero")
    return a / b


print(division(4, 0))
