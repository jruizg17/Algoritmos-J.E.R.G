#include <iostream>
#include <vector>
#include <list>
#include <string>
#include <chrono>
using namespace std;

class TablaHash{
private:
    int cap;
    int n;
    vector<list<pair<string,string>>> cubetas;

public:
    TablaHash(int capacidad=8):cap(capacidad),n(0),cubetas(cap
acidad){}
    int hashear(const string & clave) const {
        unsigned long long h = 0;
        for (unsigned char c : clave) h = (h * 31 + c) % cap;
        return (int)h;
    }
    void insertar(const string& clave, const string& valor) {
        int i = hashear(clave);
        for (auto& par : cubetas[i]) {
            if (par.first == clave) { par.second = valor; return; }   // ACTUALIZA
        }
        cubetas[i].push_back({clave, valor});
        n++;
    }

    bool buscar(const string& clave, string& salida) const {
        int i = hashear(clave);
        for (const auto& par : cubetas[i]) {
            if (par.first == clave) { salida = par.second; return true; }
        }
        return false;
    }
    
    
