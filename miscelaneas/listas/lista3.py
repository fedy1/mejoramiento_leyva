#Ver los numeros negativos

import random

numeros_lista = [random.randint(-100, 100) for _ in range(10)]

numeros_negativos = [num for num in numeros_lista if num < 0]

print("Resultados de la lista: ", numeros_lista)
print("Números negativos en la lista: ", numeros_negativos)