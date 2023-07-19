#Enseñar los numeros pares en un rango X
def numeros_pares_x():
    for numero in range(1, 10):
        if numero % 2 == 0:
            print(numero)
print(numeros_pares_x())