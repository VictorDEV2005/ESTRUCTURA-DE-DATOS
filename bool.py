# Programa interactivo para entender booleanos en Python

def interactuar_booleanos():
    # Comparación interactiva
    numero1 = int(input("Ingresa el primer número: "))
    numero2 = int(input("Ingresa el segundo número: "))
    
    print(f"\n¿{numero1} es mayor que {numero2}? {numero1 > numero2}")
    print(f"¿{numero1} es menor que {numero2}? {numero1 < numero2}")
    print(f"¿{numero1} es igual a {numero2}? {numero1 == numero2}\n")
    
    # Convertir a booleano
    #para convertir un string a bool, si la cadena de caracter esta vacia es false pero si hay caracteres es True
    valor = input("Ingresa un valor (número o texto) para convertir a booleano: ")
    print(f"El valor booleano de '{valor}' es:", bool(valor))

if __name__ == "__main__":
    interactuar_booleanos()
