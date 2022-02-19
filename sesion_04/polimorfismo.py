datos = ["hola", 1, 7, "7.5", 7.5]

for dato in datos:
    print(dato + dato)


class Persona:
    def saludar(self):
        print("Hola...")


class Perro:
    def saludar(self):
        print("*dando vueltas en círculo*")



x1 = Persona()
y1 = Perro()
x2 = Persona()
y2 = Perro()
x3 = Persona()
y3 = Perro()


for lo_que_sea in [x1, y1, x2, y2, x3, y3]:
    lo_que_sea.saludar()
