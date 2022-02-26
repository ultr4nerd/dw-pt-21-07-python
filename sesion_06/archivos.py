archivo = open("notas.txt")

for line in archivo.readlines():
    print(line, end="")

archivo.close()

message = input("Ingresa el texto a escribir en el archivo: ")
archivo = open("notas.txt", "w")

archivo.writelines(["CABECERA\n", "El texto abajo de esto\n"])
archivo.write(message)
archivo.write("\n")
archivo.close()

archivo = open("notas.txt")

for line in archivo:
    print(line)

archivo.close()

# Para no olvidar cerrar un archivo
with open("notas.txt") as f:
    print(f.readlines())
