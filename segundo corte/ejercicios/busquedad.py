# búsqueda binaria y búsqueda secuencial

def busqueda_binaria(arr, x, comparaciones=0):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        comparaciones += 1
        if arr[mid] == x:
            return mid, comparaciones
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1, comparaciones


def busqueda_secuencial(arr, x, comparaciones=0):
    for i in range(len(arr)):
        comparaciones += 1
        if arr[i] == x:
            return i, comparaciones
    return -1, comparaciones


arr = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
x = 5

result_binaria, comparaciones_binaria = busqueda_binaria(arr, x)
result_secuencial, comparaciones_secuencial = busqueda_secuencial(arr, x)

if result_binaria != -1:
    print(f"Elemento encontrado en el índice {result_binaria} con {comparaciones_binaria} comparaciones (búsqueda binaria).")
else:
    print(f"Elemento no encontrado con {comparaciones_binaria} comparaciones (búsqueda binaria).")

if result_secuencial != -1:
    print(f"Elemento encontrado en el índice {result_secuencial} con {comparaciones_secuencial} comparaciones (búsqueda secuencial).")
else:
    print(f"Elemento no encontrado con {comparaciones_secuencial} comparaciones (búsqueda secuencial).")

print(f"Comparaciones totales: {comparaciones_binaria + comparaciones_secuencial}")

#imprimir el tiempo de ejecución de cada búsqueda
import time

start_time = time.time()
busqueda_binaria(arr, x)
end_time = time.time()
print(f"Tiempo de ejecución de la búsqueda binaria: {end_time - start_time} segundos")

start_time = time.time()
busqueda_secuencial(arr, x)
end_time = time.time()
print(f"Tiempo de ejecución de la búsqueda secuencial: {end_time - start_time} segundos")

x = 30
result_binaria, comparaciones_binaria = busqueda_binaria(arr, x)
result_secuencial, comparaciones_secuencial = busqueda_secuencial(arr, x)

if result_binaria != -1:
    print(f"Elemento encontrado en el índice {result_binaria} con {comparaciones_binaria} comparaciones (búsqueda binaria).")
else:
    print(f"Elemento no encontrado con {comparaciones_binaria} comparaciones (búsqueda binaria).")
if result_secuencial != -1:
    print(f"Elemento encontrado en el índice {result_secuencial} con {comparaciones_secuencial} comparaciones (búsqueda secuencial).")
else:
    print(f"Elemento no encontrado con {comparaciones_secuencial} comparaciones (búsqueda secuencial).")
    
