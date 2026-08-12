#include <iostream>
using namespace std;

int main() {
    int edades[] = {17,21,15,19,14,25,18};
    int n = 8;

    int mayor = edades[0];
    int menor = edades[0];
    int suma = 0;

    for (int i = 0; i < n; i++) {
        suma += edades[i];

        if (edades[i] > mayor) {
            mayor = edades[i];
        }

        if (edades[i] < menor) {
            menor = edades[i];
        }
    }

    double promedio = (double)suma / n;

    cout << "Edad mayor: " << mayor << endl;
    cout << "Edad menor: " << menor << endl;
    cout << "Promedio: " << promedio << endl;

    return 0;
}