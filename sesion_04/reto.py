class Vehiculo:
    def __init__(self, tipo, ruedas):
        self.tipo = tipo
        self.ruedas = ruedas

    def manejar(self):
        print(f"Manejando un vehículo {self.tipo}...")


class VehiculoTerrestre(Vehiculo):

    def __init__(self, ruedas):
        super().__init__("terrestre", ruedas)

    def moverse_por_tierra(self):
        print("Moviéndose por tierra...")


class VehiculoAcuatico(Vehiculo):

    def __init__(self):
        super().__init__("acuático", 0)


    def nadar(self):
        print("Nadando...")


terrestre = VehiculoTerrestre(4)
terrestre.manejar()
terrestre.moverse_por_tierra()

acuatico = VehiculoAcuatico()
acuatico.manejar()
acuatico.nadar()
