#Usar un condicional para determinar si un numero es par o impar
def par_o_impar():
    numero = int(input("Ingrese un número entero: "))

    if numero % 2 == 0:
        print("El número ingresado es par.")
    else:
        print("El número ingresado es impar.")
print(par_o_impar())