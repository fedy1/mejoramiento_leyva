def encontrar_medio(num1, num2, num3):
    if num1 <= num2 <= num3 or num3 <= num2 <= num1:
        return num2
    elif num2 <= num1 <= num3 or num3 <= num1 <= num2:
        return num1
    else:
        return num3

def main():
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    num3 = float(input("Ingresa el tercer número: "))

    medio = encontrar_medio(num1, num2, num3)
    print("El valor del medio es: ", medio)

print(main())