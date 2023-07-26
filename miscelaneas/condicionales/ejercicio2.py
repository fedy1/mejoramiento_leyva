def contar_cifras(numero):
    return len(str(numero))

def main():
    numero = input("Ingresa un número entre 0 y 9999: ")

    if numero.isdigit():
        numero = int(numero)
        if 0 <= numero <= 9999:
            cifras = contar_cifras(numero)
            print("El número ",numero, "tiene ",cifras, "cifras.")
        else:
            print("Error: El número debe estar entre 0 y 9999.")
    else:
        print("Error: Ingresa un número válido.")

print(main())