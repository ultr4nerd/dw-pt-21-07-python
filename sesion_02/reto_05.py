# Primer forma
num1 = 0
num2 = 1

print(num1)

while num2 < 1000:
    print(num2)
    fib = num1 + num2
    num1 = num2
    num2 = fib


# Segunda forma
numeros = [0, 1]

print(numeros[0])

while numeros[-1] < 1000:
    print(numeros[1])
    fib = numeros[0] + numeros[1]
    numeros[0] = numeros[1]
    numeros[1] = fib

# Tercera forma
numeros = [0, 1]

while True:
    fib = numeros[-2] + numeros[-1]
    if fib < 1000:
        numeros.append(fib)
    else:
        break

print(numeros)

# texto = ', '.join([str(num) for num in numeros])
# print(texto)
