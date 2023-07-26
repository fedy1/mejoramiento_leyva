
def verificar_numeros(num1, num2, num3):
    if num1 == num2 and num2 == num3:
        return "Los tres números son iguales."
    elif num1 == num2 or num1 == num3 or num2 == num3:
        return "Hay dos números iguales."
    else:
        return "Los tres números son distintos."

def main():
    num1 = input("Ingresa el primer número: ")
    num2 = input("Ingresa el segundo número: ")
    num3 = input("Ingresa el tercer número: ")

    if num1.isdigit() and num2.isdigit() and num3.isdigit():
        num1 = float(num1)
        num2 = float(num2)
        num3 = float(num3)
        resultado = verificar_numeros(num1, num2, num3)
        print(resultado)
    else:
        print("Error: Ingresa solo números.")

print(main())