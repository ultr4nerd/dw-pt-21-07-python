class Animal:

    def __init__(self, tipo, clase, vertebrado=True):
        self.tipo = tipo
        self.clase = clase
        self.vertebrado = vertebrado

    def comer(self):
        print(f"{self.tipo.capitalize()} está comiendo...")


class Perro(Animal):

    def __init__(self, nombre):
        super().__init__("perro", "mamífero")
        self.nombre = nombre

    def comer(self):
        print(f"{self.nombre} está comiendo...")

    def ladrar(self):
        print(f"{self.nombre} está ladrando...")


class Mascota:
    def __init__(self, nombre):
        self.nombre = nombre

    def pasear(self):
        print(f"{self.nombre} está paseando...")


class Gato(Animal, Mascota):

    def __init__(self, nombre):
        # De izquierda a derecha hasta que encuentre el método en alguno de los padres
        super().__init__("gato", "mamífero")
        # Manda a llamar directamente a __init__ en mascota
        Mascota.__init__(self, nombre)

    def comer(self):
        print(f"{self.nombre} está comiendo...")

    def maullar(self):
        print(f"{self.nombre} está maullando...")


animal = Animal("perro", "mamífero")
perro = Perro("Fido")
gato = Gato("Garfield")
animal.comer()
perro.comer()
perro.ladrar()
gato.maullar()
