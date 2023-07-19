#Lanzamiento de dados
def dados():
    import random

    cantidad_dados = int(input("Ingrese la cantidad de dados a lanzar: "))

    resultados_dados = [random.randint(1, 6) for _ in range(cantidad_dados)]

    suma_total = sum(resultados_dados)

    print("Resultados de lanzar los dados:", resultados_dados)
    print("La suma total de los resultados es:", suma_total)
print(dados())