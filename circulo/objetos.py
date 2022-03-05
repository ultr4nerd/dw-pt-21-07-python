class Perro:
    def __init__(self, nombre):
        """Constructor"""
        self.nombre = nombre

    def ladrar(self):
        """Método"""
        print(f"{self.nombre} está ladrando...")

    def __str__(self):
        """Método mágico"""
        return self.nombre


pluto = Perro("Pluto")
fido = Perro("Fido")
pluto.ladrar()
fido.ladrar()
print(pluto)
print(fido)