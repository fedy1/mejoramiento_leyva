import random

def generar_arreglo(n):
    arr = []
    for _ in range(n):
        num = random.randint(1, 100)
        arr.append(num)
    return arr

def imprimir_arreglo(arreglo):
    print("Arreglo original:", arreglo)

def suma_arreglo(arreglo):
    return sum(arreglo)

def promedio_arreglo(arreglo):
    return sum(arreglo) / len(arreglo)

def mayor_arreglo(arreglo):
    return max(arreglo)

def menor_arreglo(arreglo):
    return min(arreglo)

def ordenar_ascendente(arreglo):
    return sorted(arreglo)

def ordenar_descendente(arreglo):
    return sorted(arreglo, reverse=True)

def moda_arreglo(arreglo):
    frecuencias = {}
    for num in arreglo:
        frecuencias[num] = frecuencias.get(num, 0) + 1

    max_frecuencia = max(frecuencias.values())
    moda = [num for num, frecuencia in frecuencias.items() if frecuencia == max_frecuencia]

    return moda

def mediana_arreglo(arreglo):
    sorted_arr = sorted(arreglo)
    n = len(sorted_arr)

    if n % 2 == 0:
        return (sorted_arr[n//2 - 1] + sorted_arr[n//2]) / 2
    else:
        return sorted_arr[n//2]

def buscar_arreglo(arreglo, numero):
    posiciones = [pos for pos, num in enumerate(arreglo) if num == numero]
    veces = len(posiciones)

    return posiciones, veces

def main():
    n = int(input("Ingrese la cantidad de elementos para el arreglo: "))

    if n < 1:
        print("Error: La cantidad de elementos debe ser al menos 1.")
        return

    arreglo = generar_arreglo(n)
    arreglo_original = arreglo.copy()

    while True:
        print("\n------ Menú ------")
        print("a. Imprimir arreglo original")
        print("b. Suma")
        print("c. Promedio")
        print("d. Mayor")
        print("e. Menor")
        print("f. Ordenar ascendente")
        print("g. Ordenar descendente")
        print("h. Moda")
        print("i. Mediana")
        print("j. Buscar")
        print("k. Salir")

        opcion = input("Seleccione una opción (a-k): ")

        if opcion == 'a':
            imprimir_arreglo(arreglo_original)
        elif opcion == 'b':
            print("Suma del arreglo:", suma_arreglo(arreglo))
        elif opcion == 'c':
            print("Promedio del arreglo:", promedio_arreglo(arreglo))
        elif opcion == 'd':
            print("Mayor del arreglo:", mayor_arreglo(arreglo))
        elif opcion == 'e':
            print("Menor del arreglo:", menor_arreglo(arreglo))
        elif opcion == 'f':
            print("Arreglo ordenado ascendente:", ordenar_ascendente(arreglo))
        elif opcion == 'g':
            print("Arreglo ordenado descendente:", ordenar_descendente(arreglo))
        elif opcion == 'h':
            print("Moda del arreglo:", moda_arreglo(arreglo))
        elif opcion == 'i':
            print("Mediana del arreglo:", mediana_arreglo(arreglo))
        elif opcion == 'j':
            numero_buscar = int(input("Ingrese el número que desea buscar: "))
            posiciones, veces = buscar_arreglo(arreglo, numero_buscar)
            if veces > 0:
                print(f"El número {numero_buscar} está en las posiciones: {posiciones} y aparece {veces} veces.")
            else:
                print(f"El número {numero_buscar} no se encuentra en el arreglo.")
        elif opcion == 'k':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

print(main())