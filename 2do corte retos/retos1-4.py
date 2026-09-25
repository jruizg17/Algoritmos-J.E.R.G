def suma_elementos(datos, indice=0):
    if indice == len(datos):
        return 0
    return datos[indice] + suma_elementos(datos, indice + 1)

print(suma_elementos([1, 6, 8, 9, 10]))





base = int(input("ingresa la base de la potencia: "))
exponente = int(input("ingresa el exponente: "))

def elevar(exp):
    return base if exp == 1 else base * elevar(exp - 1)

print(elevar(exponente))




palabra = input("ingresa la palabra a invertir: ")

def voltear(cadena):
    return cadena if len(cadena) == 0 else voltear(cadena[1:]) + cadena[0]

print(voltear(palabra))





numeros = [1, 3, 4, 6, 7, 7]

def voltear_lista(datos):
    return datos if len(datos) == 0 else voltear_lista(datos[1:]) + [datos[0]]

print(voltear_lista(numeros))