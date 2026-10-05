def temperaturas_diarias(temperaturas):
    n = len(temperaturas)
    resultado = [0] * n  
    pila = []  # pila para almacenar las temperaturas

    for i in range(n):
        # mientras la pila no esté vacía y la temperatura sea mayor que la temperatura de la cima de la pila
        while pila and temperaturas[i] > temperaturas[pila[-1]]:
            indice = pila.pop()  # sacamos el índice de la cima de la pila
            resultado[indice] = i - indice  # calculamos cuántos días hay que esperar
        pila.append(i)  # agregamos el índice a la pila

    return resultado
print(temperaturas_diarias([73, 74, 75, 71, 69, 72, 76, 73]))