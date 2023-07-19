#Suma de numeros ingresados
def suma_numeros_ingresados():
    suma_total = 0

    while True:
        numero = int(input("Ingrese un número entero positivo (o un número negativo para salir): "))
        
        if numero < 0:
            break  

        suma_total += numero
        
    print("La suma total es:", suma_total)
    
print(suma_numeros_ingresados())