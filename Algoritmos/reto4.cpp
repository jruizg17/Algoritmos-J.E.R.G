#include <iostream>

using namespace std;

int main() {
    int usuario, maquina = 1; 

    cout << "1. Piedra\n2. Papel\n3. Tijera\n";
    cout << "Elige tu opcion (1-3): ";
    cin >> usuario;

    cout << "La maquina eligio: Piedra\n";

    if (usuario == maquina) {
        cout << "¡Es un empate!" << endl;
    } 
    else if ((usuario == 1 && maquina == 3) || 
             (usuario == 2 && maquina == 1) || 
             (usuario == 3 && maquina == 2)) {
        cout << "ganaste" << endl;
    } 
    else {
        cout << "perdiste" << endl;
    }

    return 0;
}
