"""
Objetos (perros): Firulais, Pluto
Molde: Perro
Método: habilidad - función de un objecto
Constructor: el primer método que se manda a llamar (__init__)
"""

# Declaración

class Perro:
    """Es un molde que crea perros"""

    def __init__(self, nombre):
        """Crea un nuevo perro con un nombre"""
        self.nombre = nombre

    def ladrar(self):
        """Es un perro ladrando"""
        print(f"{self.nombre} está ladrando...")

    def __str__(self):
        """Regresa la representación en cadena de un perro"""
        return self.nombre

    def __add__(self, otro):
        """Crea un nuevo perro"""
        primer_mitad = self.nombre[:len(self.nombre) // 2]
        segunda_mitad = otro.nombre[len(otro.nombre) // 2:]
        return Perro(primer_mitad + segunda_mitad)
    


# Instanciación

firulais = Perro("Firulais")
fido = Perro("Fido")
nuevo_perro = firulais + fido
print(nuevo_perro)
