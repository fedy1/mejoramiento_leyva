import random

def generar_arreglo(n):
    arreglo = []
    for _ in range(n):
        num = random.randint(1, 100)
        arreglo.append(num)
    return arreglo

def suma_mas_alta(arreglo1, arreglo2):
    suma_arreglo1 = sum(arreglo1)
    suma_arreglo2 = sum(arreglo2)

    if suma_arreglo1 > suma_arreglo2:
        return "El arreglo 1 tiene la suma más alta."
    elif suma_arreglo1 < suma_arreglo2:
        return "El arreglo 2 tiene la suma más alta."
    else:
        return "Ambos arreglos tienen la misma suma."

def numero_mayor(arreglo1, arreglo2):
    max_arreglo1 = max(arreglo1)
    max_arreglo2 = max(arreglo2)

    if max_arreglo1 > max_arreglo2:
        return f"El arreglo 1 tiene el número mayor: {max_arreglo1}"
    elif max_arreglo1 < max_arreglo2:
        return f"El arreglo 2 tiene el número mayor: {max_arreglo2}"
    else:
        return "Ambos arreglos tienen el mismo número mayor."

def numero_menor(arreglo1, arreglo2):
    min_arreglo1 = min(arreglo1)
    min_arreglo2 = min(arreglo2)

    if min_arreglo1 < min_arreglo2:
        return f"El arreglo 1 tiene el número menor: {min_arreglo1}"
    elif min_arreglo1 > min_arreglo2:
        return f"El arreglo 2 tiene el número menor: {min_arreglo2}"
    else:
        return "Ambos arreglos tienen el mismo número menor."

def promedio_conjunto(arreglo1, arreglo2):
    promedio_calc = (sum(arreglo1) + sum(arreglo2)) / (len(arreglo1) + len(arreglo2))
    return promedio_calc

def promedio_por_encima_o_debajo(arreglo, promedio_conjunto):
    promedio_arreglo = sum(arreglo) / len(arreglo)

    if promedio_arreglo > promedio_conjunto:
        return "Está por encima del promedio conjunto."
    elif promedio_arreglo < promedio_conjunto:
        return "Está por debajo del promedio conjunto."
    else:
        return "Es igual al promedio conjunto."

def cantidad_pares(arreglo):
    return sum(1 for num in arreglo if num % 2 == 0)

def cantidad_impares(arreglo):
    return sum(1 for num in arreglo if num % 2 != 0)

def main():
    n = int(input("Ingrese la cantidad de elementos para los arreglos: "))

    if n < 1:
        print("Error: La cantidad de elementos debe ser al menos 1.")
        return

    arreglo1 = generar_arreglo(n)
    arreglo2 = generar_arreglo(n)

    print(suma_mas_alta(arreglo1, arreglo2))
    print(numero_mayor(arreglo1, arreglo2))
    print(numero_menor(arreglo1, arreglo2))

    promedio_conjunto_val = promedio_conjunto(arreglo1, arreglo2)
    print(f"El promedio conjunto de los dos arreglos es: {promedio_conjunto_val}")

    print("El promedio del arreglo 1", promedio_por_encima_o_debajo(arreglo1, promedio_conjunto_val))
    print("El promedio del arreglo 2", promedio_por_encima_o_debajo(arreglo2, promedio_conjunto_val))

    print("El arreglo 1 tiene", cantidad_pares(arreglo1), "números pares.")
    print("El arreglo 2 tiene", cantidad_pares(arreglo2), "números pares.")

    print("El arreglo 1 tiene", cantidad_impares(arreglo1), "números impares.")
    print("El arreglo 2 tiene", cantidad_impares(arreglo2), "números impares.")

print(main())