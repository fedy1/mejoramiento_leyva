    #Diccionario de frutas 
def frutas():
    frutas ={
        "manzana": "apple",
        "platano": "banana",
        "naranja": "orang",
        "uva": "grape",
        "sandia": "watermelon",
        "coco": "coconut",
        "pera":"pear"
        
    }

    fruta_español = input("Ingrese el nombre de una fruta en español: ")

    fruta_español = fruta_español.lower()

    if fruta_español in frutas:
        fruta_ingles = frutas[fruta_español]
        print("En ingles ", fruta_español, "se dice: ",fruta_ingles)
    else:
        print("Lo siento, la traducción de esa fruta no está disponible.")
print(frutas())