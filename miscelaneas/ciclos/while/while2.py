#Utilizar un bucle while para que el usuario adivine el número
def adivinar_numero():
    import random
    numero_secreto = random.randint(1, 100)

    while True:
        intento = int(input("Adivina el número secreto (entre 1 y 100): "))
        

        if intento == numero_secreto:
            print("¡Felicitaciones! Adivinaste el número secreto.")
            break  
        elif intento < numero_secreto:
            print("El número secreto es mayor. Sigue intentando.")
        else:
            print("El número secreto es menor. Sigue intentando.")
print(adivinar_numero())