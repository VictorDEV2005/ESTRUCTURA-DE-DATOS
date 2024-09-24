# Función recursiva para calcular el factorial de un número
def factorial(n):
    # Caso base: el factorial de 0 o 1 es 1
    if n == 0 or n == 1:
        return 1
    else:
        # Llamada recursiva: n * factorial de n-1
        return n * factorial(n - 1)

# Solicitar un número al usuario
numero = int(input("Ingresa un número para calcular su factorial: "))

# Llamar a la función recursiva e imprimir el resultado
resultado = factorial(numero)
print(f"El factorial de {numero} es: {resultado}")
