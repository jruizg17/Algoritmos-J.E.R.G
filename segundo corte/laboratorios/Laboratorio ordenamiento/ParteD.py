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

#include <iostream>
#include <vector>
#include <chrono>
#include <cstdlib>
using namespace std;

void quickSort(vector<int>& a, int ini, int fin) {
    if (ini >= fin) return;
    int pivote = a[fin];
    int i = ini;
    for (int j = ini; j < fin; j++) {
        if (a[j] < pivote) {
            swap(a[i], a[j]);
            i++;
        }
    }
    swap(a[i], a[fin]);
    quickSort(a, ini, i - 1);
    quickSort(a, i + 1, fin);
}

double medir(const vector<int>& datos, int repeticiones) {
    int suma = 0;
    auto inicio = chrono::high_resolution_clock::now();
    for (int r = 0; r < repeticiones; r++) {
        vector<int> copia = datos;
        quickSort(copia, 0, (int)copia.size() - 1);
        suma += copia[0];
    }
    auto fin = chrono::high_resolution_clock::now();
    if (suma == -999999) cout << "";   // evita que el compilador elimine el trabajo
    chrono::duration<double, micro> total = fin - inicio;
    return total.count() / repeticiones;
}

int main() {
    srand(42);
    int tamanos[3] = {5, 15, 30};
    int repeticiones = 200000;

    cout << "n,tiempo_us\n";
    for (int t = 0; t < 3; t++) {
        int n = tamanos[t];
        vector<int> datos(n);
        for (int i = 0; i < n; i++) datos[i] = rand() % 1000;
        double tiempo = medir(datos, repeticiones);
        cout << n << "," << tiempo << "\n";
    }
    return 0;
}
