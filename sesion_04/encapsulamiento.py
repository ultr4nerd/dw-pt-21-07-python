class Contador:
    __cuenta = 0

    def contar(self):
        self.__proceso_contar()

    def __proceso_contar(self):
        self.__cuenta += 1

    def obtener(self):
        return self.__cuenta


contador = Contador()
contador.contar()
contador.contar()
contador.contar()
cuenta = contador.obtener()
print(cuenta)
