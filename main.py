class CalculadoraMCD_MCM:
    def __init__(self):
        pass

    def calcular_mcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def calcular_mcm(self, a, b):
        mcd = self.calcular_mcd(a, b)
        mcm = (a * b) // mcd
        return mcm


# Crear una instancia de la clase CalculadoraMCD_MCM
calculadora = CalculadoraMCD_MCM()

# Solicitar al usuario que ingrese los números
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

# Calcular y mostrar el mínimo común múltiplo utilizando el método de la instancia
print("El mínimo común múltiplo de", num1, "y", num2, "es:", calculadora.calcular_mcm(num1, num2))
