#include <iostream>
#include <cmath>
using namespace std;

int main() {
    double n1, n2;
    
    cout << "ingresa el primer numero: ";
    cin >> n1;
    cout << "ingresa el segundo numero: ";
    cin >> n2;

    cout << "\nresultados:\n";
    cout << "suma: " << n1 + n2 << "\n";
    cout << "resta: " << n1 - n2 << "\n";
    cout << "mult: " << n1 * n2 << "\n";

    if (n2 != 0) cout << "div: " << n1 / n2 << "\n";
    else cout << "div: error (division por cero)\n";

    if (n1 >= 0) cout << "raiz 1: " << sqrt(n1) << "\n";
    else cout << "raiz 1: error (numero negativo)\n";

    if (n2 >= 0) cout << "raiz 2: " << sqrt(n2) << "\n";
    else cout << "raiz 2: error (numero negativo)\n";

    cout << "potencia: " << pow(n1, n2) << "\n";

    return 0;
}