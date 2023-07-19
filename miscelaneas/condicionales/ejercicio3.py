#El programa debera determinar si el usuario tiene una familia grande o pequeña.
def familia_grande():
    edad = int(input("Ingrese su edad: "))

    hermanos = int(input("Ingrese el número de hermanos que tiene: "))

    if hermanos > 3:
        print("Tienes una familia grande.")
    else:
        print("Tienes una familia pequeña.")
print(familia_grande())