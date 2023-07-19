#Usar un condicional para verificar si es menor o mayor de edad.
def menor_o_mayor():
    edad = int(input("Ingrese su edad: "))

    if edad < 18:
        print("Eres menor de edad.")
    else:
        print("Eres mayor de edad.")
print(menor_o_mayor())