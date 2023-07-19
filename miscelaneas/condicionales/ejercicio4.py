#Usar un condicional para verificar si el usuario es "Fredy" o no.
def verificar_nombre():
    nombre = input("Ingrese su nombre: ")

    if nombre.lower() == "fredy":
        print("¡Hola Fredy! Bienvenido.")
    else:
        print("Hola, tu no eres el dueño del codigo.")
print(verificar_nombre())