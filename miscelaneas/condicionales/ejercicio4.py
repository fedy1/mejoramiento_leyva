from datetime import datetime

def calcular_tiempo_desde_fecha(fecha):
    fecha_actual = datetime.now().date()
    diferencia = fecha - fecha_actual
    return diferencia.days

def obtener_fecha_valida():
    while True:
        fecha_str = input("Ingresa una fecha (dd/mm/aaaa): ")
        try:
            fecha = datetime.strptime(fecha_str, "%d/%m/%Y").date()
            return fecha
        except ValueError:
            print("Error: Ingresa una fecha válida en el formato dd/mm/aaaa.")

def main():
    fecha = obtener_fecha_valida()
    fecha_actual = datetime.now().date()
    diferencia = fecha - fecha_actual

    if fecha <= fecha_actual:
        tiempo_pasado = diferencia.days
        mensaje = "han pasado"
    else:
        tiempo_faltante = diferencia.days
        mensaje = "faltan"

    print(f"Desde la fecha ingresada {mensaje} {abs(diferencia.days)} días.")

print(main())