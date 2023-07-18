#Lista de nombres mas largos y cortos

nombres_str = input("Ingrese una lista de nombres separados por espacios: ")

nombres_lista = nombres_str.split()

nombres_mas_largos = [nombre for nombre in nombres_lista if len(nombre) >5]

nombres_mas_cortos = [nombre for nombre in nombres_lista if len(nombre) <=5]

print("Los nombres más largos son:", nombres_mas_largos)

print("Los nombres más cortos son:", nombres_mas_cortos)