# Función para manipular una cadena de texto
def manipular_cadena(texto):
    print("Texto original:", texto)
    
    # Convertir todo el texto a mayúsculas
    mayusculas = texto.upper()
    print("Texto en mayúsculas:", mayusculas)
    
    # Convertir todo el texto a minúsculas
    minusculas = texto.lower()
    print("Texto en minúsculas:", minusculas)
    
    # Reemplazar una palabra en el texto
    reemplazado = texto.replace("Python", "programación")
    print("Texto con reemplazo:", reemplazado)
    
    # Contar las veces que aparece una letra o palabra
    contar_a = texto.count("a")
    print("Número de veces que aparece la letra 'a':", contar_a)
    
    # Invertir la cadena de texto
    invertido = texto[::-1]
    print("Texto invertido:", invertido)

# Llamar a la función con un ejemplo de texto
cadena = "Aprender Python es divertido"
manipular_cadena(cadena)
