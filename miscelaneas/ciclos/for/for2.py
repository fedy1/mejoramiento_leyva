def obtener_multiplos_5(N):
    multiplos = []
    for num in range(1, N + 1):
        if num % 5 == 0:
            multiplos.append(num)
    return multiplos

def main_multiplos_5():
    N = int(input("Ingrese un número para determinar los múltiplos de 5: "))
    if N < 1:
        print("El número debe ser mayor o igual a 1.")
        return
    multiplos = obtener_multiplos_5(N)
    print(f"Los múltiplos de 5 comprendidos entre 1 y {N} son: {multiplos}")

print(main_multiplos_5())