print("""Menú:

1. Helado con oreo
2. Helado con m&m
3. Helado con fresas
4. Helado con brownie
""")

opcion = int(input("Selecciona una opción: "))

if opcion == 1:
    print("El precio es de $19")
elif opcion == 2:
    print("El precio es de $25")
elif opcion == 3:
    print("El precio es de $22")
elif opcion == 4:
    print("El precio es de $28")
else:
    print("Opción no disponible")
