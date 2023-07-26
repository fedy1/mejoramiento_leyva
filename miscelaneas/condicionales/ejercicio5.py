def main():
    
    hora = int(input("Ingresa la hora (0-23): "))
    minutos = int(input("Ingresa los minutos (0-59): "))
    segundos = int(input("Ingresa los segundos (0-59): "))

    segundos += 1
    
    if segundos >= 60:
        segundos = 0
        minutos += 1

    if minutos >= 60:
        minutos = 0
        hora += 1

    if hora >= 24:
        hora = 0
        
    print(f"La hora dentro de 1 segundo será: {hora:02d}:{minutos:02d}:{segundos:02d}")
    
print(main())