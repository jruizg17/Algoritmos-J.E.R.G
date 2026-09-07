import math

def calculadora():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    
    print(f"Suma: {num1 + num2}")
    print(f"Resta: {num1 - num2}")
    print(f"Multiplicación: {num1 * num2}")
    print(f"División: {num1 / num2 if num2 != 0 else 'Indefinida (División por cero)'}")
    print(f"Raíz cuadrada de {num1}: {math.sqrt(num1) if num1 >= 0 else 'No real'}")
    print(f"Raíz cuadrada de {num2}: {math.sqrt(num2) if num2 >= 0 else 'No real'}")
    print(f"Potenciación ({num1}^{num2}): {math.pow(num1, num2)}")

if __name__ == "__main__":
    calculadora()