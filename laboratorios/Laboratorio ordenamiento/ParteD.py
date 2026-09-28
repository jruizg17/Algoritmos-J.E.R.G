 #codigo hecho con IA para revisar mediciones de tiempo, por falta de tiempo
import random
import time

def bubble_sort(a):
    n = len(a)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

def merge_sort(a):
    if len(a) <= 1:
        return a
    medio = len(a) // 2
    izq = merge_sort(a[:medio])
    der = merge_sort(a[medio:])
    res = []
    i = j = 0
    while i < len(izq) and j < len(der):
        if izq[i] <= der[j]:
            res.append(izq[i])
            i += 1
        else:
            res.append(der[j])
            j += 1
    return res + izq[i:] + der[j:]

def quick_sort(a):
    if len(a) <= 1:
        return a
    pivote = a[0]
    menores = [x for x in a[1:] if x < pivote]
    mayores = [x for x in a[1:] if x >= pivote]
    return quick_sort(menores) + [pivote] + quick_sort(mayores)

def medir(funcion, datos, repeticiones):
    inicio = time.perf_counter()
    for _ in range(repeticiones):
        funcion(datos[:])          # se ordena una copia
    fin = time.perf_counter()
    return (fin - inicio) / repeticiones * 1_000_000   # microsegundos

REPETICIONES = 10000
print("   n    Bubble(us)   Merge(us)   Quick(us)")
for n in (5, 15, 30):
    datos = [random.randint(0, 1000) for _ in range(n)]
    tb = medir(bubble_sort, datos, REPETICIONES)
    tm = medir(merge_sort, datos, REPETICIONES)
    tq = medir(quick_sort, datos, REPETICIONES)
    print(f"{n:>4}{tb:>13.2f}{tm:>12.2f}{tq:>12.2f}")
    
    #codigo hecho con IA para revisar mediciones de tiempo, por falta de tiempo