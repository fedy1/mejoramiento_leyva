def calcular_potencia(base, exponente):
    resultado = 1
    for _ in range(exponente):
        resultado *= base
    return resultado

def main_calcular_potencia():
    base = int(input("Ingrese la base (x): "))
    exponente = int(input("Ingrese el exponente (n): "))
    if exponente < 0:
        print("El exponente debe ser mayor o igual a 0.")
        return
    potencia = calcular_potencia(base, exponente)
    print(f"El resultado de {base}^{exponente} es: {potencia}")

print(main_calcular_potencia())