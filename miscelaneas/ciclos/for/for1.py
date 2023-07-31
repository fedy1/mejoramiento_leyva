def encontrar_n_suma(maximo):
    suma = 0
    for n in range(1, maximo + 1):
        suma += n
        if suma > maximo:
            return n

def main_encontrar_n_suma():
    maximo = int(input("Ingrese el número máximo para la suma: "))
    if maximo < 1:
        print("El número máximo debe ser mayor o igual a 1.")
        return
    n = encontrar_n_suma(maximo)
    print(f"El número más pequeño de la serie para superar el dato máximo es: {n}")

print(main_encontrar_n_suma())