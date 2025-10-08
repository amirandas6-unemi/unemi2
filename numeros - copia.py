# Lista original
numeros = list(range(1, 11))  # del 1 al 10

# Usamos map con una función lambda para filtrar los pares
pares = list(filter(lambda x: x % 2 == 0, numeros))

print(pares)  # Resultado: [2, 4, 6, 8, 10]
