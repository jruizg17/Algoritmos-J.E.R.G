#include <iostream>

using namespace std;

int main() {
    float fahrenheit, centigrados;

    cout << "Ingrese la temperatura en grados Fahrenheit: ";
    cin >> fahrenheit;

    centigrados = (fahrenheit - 32) / 1.8;

    cout << "La temperatura en grados Centigrados es: " << centigrados << " °C" << endl;

    return 0;
}