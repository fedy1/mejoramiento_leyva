#Usar condicionales para determinar si es positivo, negativo o cero.
def positivo_negativo():
    numero = float(input("Ingrese un número: "))

    if numero > 0:
        print("El número ingresado es positivo.")
    elif numero < 0:
        print("El número ingresado es negativo.")
    else:
        print("El número ingresado es igual a cero.")
print(positivo_negativo())