#include <iostream>
using namespace std;

int main() {
    srand(time(0));

    int eleccion;
    cout << "Elige tu opcion:\n1. Cara\n2. Sello\n";
    cout << "Tu eleccion (1 o 2): ";
    cin >> eleccion;

    int resultado = (rand() % 2) + 1;

    if (resultado == 1) {
        cout << "La moneda cayo en: CARA\n";
    } else {
        cout << "La moneda cayo en: SELLO\n";
    }

    if (eleccion == resultado) {
        cout << "ganaste" << endl;
    } else {
        cout << "perdiste." << endl;
    }

    return 0;
}
