#include <iostream>
#include <string>
using namespace std;

class persona {
protected:
    string doctipo, doc, nombre, apellido, sexo;
    double peso, estatura;
    int edad;

public:
    void pedirdatos() {
        cin >> doctipo >> doc >> nombre >> apellido >> peso >> estatura >> edad >> sexo;
    }

    void mostrarpersona() {
        cout << nombre << " " << apellido << " - " << doctipo << ": " << doc << "\n";
    }

    string calcularimc() {
        double imc = peso / (estatura * estatura);
        if (imc < 20) return "pesobajo";
        if (imc <= 25) return "pesoideal";
        return "sobrepeso";
    }

    bool mayoredad() { return edad >= 18; }
};

class empleado : public persona {
private:
    string cargo, departamento;
    double valorhora, horastrabajadas;

public:
    void calcularhonorarios() {
        pedirdatos();
        cin >> cargo >> valorhora >> horastrabajadas >> departamento;

        double total = valorhora * horastrabajadas;
        double pago = total - (total * 0.00966);

        cout << "\ndoc: " << doctipo << " " << doc << "\n";
        cout << "nombre: " << nombre << " " << apellido << "\n";
        cout << "cargo: " << cargo << " | horas: " << horastrabajadas << " | valor hr: " << valorhora << "\n";
        cout << "pago total: " << pago << "\n";
    }
};

int main() {
    empleado e;
    e.calcularhonorarios();

    string imc = e.calcularimc();
    if (imc == "pesobajo") cout << "el peso esta por debajo del ideal\n";
    else if (imc == "pesoideal") cout << "el peso es ideal\n";
    else cout << "tiene sobrepeso\n";

    return 0;
}