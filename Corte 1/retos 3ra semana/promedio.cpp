#include <iostream>
using namespace std;

double media(double notas[3][10], int i) {
    double suma = 0;
    for (int j = 0; j < 10; j++) suma += notas[i][j];
    return suma / 10.0;
}

int main() {
    double notas[3][10] = {
        {4.0, 3.5, 4.5, 2.0, 5.0, 3.8, 4.2, 3.0, 4.0, 4.5},
        {3.0, 4.0, 3.0, 3.5, 4.5, 2.5, 3.5, 4.0, 5.0, 4.0},
        {5.0, 4.8, 4.2, 3.9, 4.0, 3.5, 4.5, 4.0, 3.8, 4.1}
    };

    for (int i = 0; i < 3; i++) {
        cout << "media asignatura " << i + 1 << ": " << media(notas, i) << "\n";
    }
    return 0;
}