class Calculadora:
    
    def suma(self, a, b):
        return a + b
    
    def resta(self, a, b):
        return a - b
    
    def multiplicacion(self, a, b):
        return a * b
    
    def division(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error: División por cero"
    
    def division_entera(self, a, b):
        if b != 0:
            return a // b
        else:
            return "Error: División por cero"
    
    def exponente(self, a, b):
        return a ** b
    
    def modulo(self, a, b):
        if b != 0:
            return a % b
        else:
            return "Error: División por cero"

    def menu(self):
        print("CALCULADORA")
        print("****")
        print("MENU DE OPCIONES")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. División Entera")
        print("6. Exponente")
        print("7. Módulo")
        print("****")
        return int(input("Introduce la opción: "))
    
    def ejecutar(self):
        opcion = self.menu()
        if 1 <= opcion <= 7:
            a = float(input("Introduce el primer número: "))
            b = float(input("Introduce el segundo número: "))
            
            if opcion == 1:
                print(f"Resultado: {self.suma(a, b)}")
            elif opcion == 2:
                print(f"Resultado: {self.resta(a, b)}")
            elif opcion == 3:
                print(f"Resultado: {self.multiplicacion(a, b)}")
            elif opcion == 4:
                print(f"Resultado: {self.division(a, b)}")
            elif opcion == 5:
                print(f"Resultado: {self.division_entera(a, b)}")
            elif opcion == 6:
                print(f"Resultado: {self.exponente(a, b)}")
            elif opcion == 7:
                print(f"Resultado: {self.modulo(a, b)}")
        else:
            print("Opción inválida")

# Crear una instancia de la clase Calculadora y ejecutar
calculadora = Calculadora()
calculadora.ejecutar()