import aritmeticas
from aritmeticas import suma
from aritmeticas import suma as mi_suma

resultado = aritmeticas.suma(1, 2)
print(resultado)

resultado = suma(1, 2)
print(resultado)

resultado = mi_suma(1, 2)
print(resultado)
