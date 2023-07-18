#contar vocales

palabra = input("Ingrese una palabra: ")

contador_vocales = 0

for caracter in palabra:
    if caracter.lower() in 'aeiou':
        contador_vocales += 1

print("La palabra contiene", contador_vocales, "vocales.")