# edad = 19

# while edad < 18:
#     print(f"No puedes entrar al bar, tienes {edad} años")
#     edad += 1

# print("Pásale")

# while False:
#     print("Nunca va a ocurrir")


# count = 0

# while True:  # Ciclo infinito
#     print("Ciclo infinito")
#     count += 1
#     if count == 5:
#         break  # Se puede romper el ciclo usando esto


# count = 0

# while count <= 10:
#     count += 1
#     if count % 2 != 0:
#         continue  # Rompe la iteración
#     print(count)


# frutas = ["Manzana", "Naranja", "Sandía"]

# for fruta in frutas:
#     print(fruta.upper())

# # Primer iteración
# fruta = "Manzana"

# # Segunda iteración
# fruta = "Naranja"

# # Tercera iteración
# fruta = "Sandía"


# for numero in range(5):
#     print(numero)

# for numero in range(1, 6):
#     print(numero)

# for numero in range(2, 11, 2):
#     print(numero)


## Diccionarios

usuario = {"nombre": "Mauricio", "apellido": "Chávez"}

for key in usuario: # Llaves
    print(key, usuario[key])

for key in usuario.keys(): # Es lo mismo que arriba
    print(key, usuario[key])

for value in usuario.values():  # Valores
    print(value)

for key, value in usuario.items():  # llave - valor
    print(key, value)
