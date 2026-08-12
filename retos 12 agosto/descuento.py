import random

compra = float(input("Ingrese el valor de la compra: "))

if compra > 50000:

    numero = random.randint(1, 4)

    if numero == 1:
        descuento = 10
        color = "roja"

    elif numero == 2:
        descuento = 30
        color = "azul"

    elif numero == 3:
        descuento = 50
        color = "amarilla"

    else:
        descuento = 100
        color = "blanca"

    valor_descuento = compra * descuento / 100
    total = compra - valor_descuento

    print("Bolita:", color)
    print("Descuento:", descuento, "%")
    print("Valor del descuento:", valor_descuento)
    print("Total a pagar:", total)

else:
    print("La compra no supera los $50.000")
    print("No tiene descuento")
    print("Total a pagar:", compra)