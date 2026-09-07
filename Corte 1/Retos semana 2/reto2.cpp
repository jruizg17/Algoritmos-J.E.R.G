#include <iostream>

using namespace std;

int main() {
    float peso, dosis;
    int meses;

    cout << "Ingrese el peso del bebe (en kg): ";
    cin >> peso;

    cout << "Ingrese la edad del bebe (en meses): ";
    cin >> meses;

    dosis = ((peso + 10.0) / (meses * 10.0)) * 8.0;

    cout << "La dosis de vacuna a aplicar es: " << dosis << endl;

    return 0;
}