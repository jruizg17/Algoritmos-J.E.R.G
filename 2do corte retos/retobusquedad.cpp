#include <iostream>
using namespace std;

int busqueda_binaria(int arr[], int objetivo, int inicio, int fin){
    if (inicio == fin){
        return inicio;
    }
    int mitad = inicio + (fin - inicio) / 2;
    if (arr[mitad] < objetivo){
        return busqueda_binaria(arr, objetivo, mitad + 1, fin);
    }
    return busqueda_binaria(arr, objetivo, inicio, mitad);
}

int main(){
    int datos[] = {2, 4, 4, 4, 7, 9, 12};
    int n = sizeof(datos) / sizeof(datos[0]);
    int objetivo = 4;

    int resultado = busqueda_binaria(datos, objetivo, 0, n);

    if (resultado < n && datos[resultado] == objetivo){
        cout << "encontrado en la posicion " << resultado << endl;
    } else {
        cout << "no encontrado, deberia ir en la posicion " << resultado << endl;
    }

    return 0;
}