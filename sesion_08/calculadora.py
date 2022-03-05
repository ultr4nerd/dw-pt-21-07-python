class Calculadora:
    def suma(self, a, b):
        return a + b

    def multiplicacion(self, a, b):
        suma = 0
        for _ in range(b):
            suma = self.suma(suma, a)
        return suma

