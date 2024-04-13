# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
'''UC
  ISI'''


class CalculadoraMCD:
    def __init__(self):
        pass

    def calcular_mcd(self, a, b):
        while b:
            a, b = b, a % b
        return a


# Crear una instancia de la clase CalculadoraMCD
calculadora = CalculadoraMCD()

# Solicitar al usuario que ingrese los números
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

# Calcular y mostrar el máximo común divisor utilizando el método de la instancia
print("El máximo común divisor de", num1, "y", num2, "es:", calculadora.calcular_mcd(num1, num2))
