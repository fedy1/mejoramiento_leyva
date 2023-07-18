#contador de numeros pares e impares de una lista

numeros = [13, 7, 33, 46, 21, 18, 9, 22]

contador_pares = 0
contador_impares = 0

for numero in numeros:
    if numero % 2 == 0:
        contador_pares += 1
    else:
        contador_impares += 1

print("Cantidad de números pares:", contador_pares)
print("Cantidad de números impares:", contador_impares)