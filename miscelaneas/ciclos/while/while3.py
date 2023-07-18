#mostrar X cantidad de numeros pares

n = int(input("Ingrese un número positivo: "))

contador = 0

print("Los primeros", n, "números pares son:")
while contador < n:
    print(contador * 2)
    contador += 1