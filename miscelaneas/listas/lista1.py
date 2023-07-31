def main():

    cantidad_numeros = int(input("Ingresa la cantidad de números para la serie de Fibonacci: "))

    if cantidad_numeros < 1:
        print("Error: La cantidad de números debe ser al menos 1.")
        return

    fibonacci = [0, 1]

    while len(fibonacci) < cantidad_numeros:
        next_fibo = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(next_fibo)

    print(f"Los {cantidad_numeros} primeros números de la serie de Fibonacci:")
    for num in fibonacci:
        print(num)

print(main())