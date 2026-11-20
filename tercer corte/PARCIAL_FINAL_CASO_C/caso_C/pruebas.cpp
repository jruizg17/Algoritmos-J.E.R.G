// NO MODIFIQUE ESTE ARCHIVO. Alterarlo se considera fraude academico
// segun la seccion 13 de la guia de asignatura.
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <utility>
#include "sistema.h"
using namespace std;

// ---- datos del caso C ----
static int          COD[8]  = {754, 981, 438, 580, 649, 888, 793, 491};
static const char*  NOM[8]  = {"CENTRAL", "BLOQUE1", "BLOQUE2", "BIBLIOTECA", "BIENESTAR", "DEPORTES", "SALUD", "ANEXO"};
static int          NME[8]  = {3, 3, 6, 5, 6, 6, 5, 3};
static int          MED[][3] = {{0, 0, 31}, {0, 1, 3}, {0, 2, 23}, {1, 0, 6}, {1, 1, 10}, {1, 2, 33}, {2, 0, 32}, {2, 1, 33}, {2, 2, 6}, {2, 3, 20}, {2, 4, 26}, {2, 5, 23}, {3, 0, 23}, {3, 1, 15}, {3, 2, 22}, {3, 3, 10}, {3, 4, 19}, {4, 0, 9}, {4, 1, 5}, {4, 2, 34}, {4, 3, 39}, {4, 4, 27}, {4, 5, 11}, {5, 0, 26}, {5, 1, 9}, {5, 2, 38}, {5, 3, 8}, {5, 4, 26}, {5, 5, 37}, {6, 0, 11}, {6, 1, 15}, {6, 2, 6}, {6, 3, 21}, {6, 4, 10}, {7, 0, 39}, {7, 1, 40}, {7, 2, 5}};
static const int    NMED = 37;
static vector<pair<int,int>> VIAS = {{0, 1}, {0, 2}, {0, 3}, {1, 2}, {1, 4}, {2, 5}, {3, 6}, {4, 5}, {6, 7}};
static const int    VERT = 8;
static const int    CAPV = 14;
static const int    COLA = 4;

static void cargar(Sistema& S) {
    for (int i = 0; i < 8; i++) S.registrar(COD[i], NOM[i], NME[i]);
    for (int i = 0; i < NMED; i++) S.medir(COD[MED[i][0]], MED[i][1], MED[i][2]);
}

static int fallas = 0;
static string lista2s(const vector<int>& v) {
    string r; for (size_t i=0;i<v.size();i++) { if(i) r+=","; r+=to_string(v[i]); } return r;
}
static void chkS(const string& n, const string& o, const string& e) {
    bool ok = (o == e);
    cout << "  [" << (ok ? "OK " : "FALLA") << "] " << n << ": obtuvo \"" << o << "\"";
    if (!ok) cout << "\n          esperaba \"" << e << "\"";
    cout << endl; if (!ok) fallas++;
}
static void chkI(const string& n, int o, int e) {
    bool ok = (o == e);
    cout << "  [" << (ok ? "OK " : "FALLA") << "] " << n << ": obtuvo " << o;
    if (!ok) cout << "  (esperaba " << e << ")";
    cout << endl; if (!ok) fallas++;
}

int main() {
    cout << "PARTE C++ · sistema integrado · caso C" << endl;
    cout << "----------------------------------------------------------" << endl;
    Sistema S(COLA, VIAS, VERT);
    cargar(S);

    cout << " A · memoria, lista e indice" << endl;
    chkS("la lista queda ordenada por codigo", S.codigos(), "438 491 580 649 754 793 888 981");
    chkI("cuantos puntos registrados", S.cuantos(), 8);
    chkI("altura del indice", S.alturaIndice(), 3);
    chkI("un codigo repetido no se registra", S.registrar(COD[0], "OTRO", 3) ? 1 : 0, 0);
    chkI("el repetido no altero la cantidad", S.cuantos(), 8);
    chkI("suma de todas las mediciones", S.sumaTotales(), 751);

    cout << " B · consultas sobre el indice" << endl;
    Punto* p = S.buscar(COD[3]);
    chkS("buscar devuelve el punto correcto", p ? p->nombre : string("NULO"), "BIBLIOTECA");
    chkI("el indice apunta al MISMO punto de la lista", p ? p->total() : -1, 89);
    chkI("buscar un codigo ausente devuelve nulo", S.buscar(1) == nullptr ? 1 : 0, 1);
    chkS("rango amplio: todos en orden", lista2s(S.enRango(0, 1000)), "438,491,580,649,754,793,888,981");
    chkS("rango acotado [580, 793]", lista2s(S.enRango(580, 793)), "580,649,754,793");
    chkS("rango sin resultados", lista2s(S.enRango(1, 2)), "");

    cout << " C · cola circular" << endl;
    for (int i = 0; i < COLA; i++) S.encolar(COD[i]);
    chkI("encolar en cola llena devuelve false", S.encolar(COD[5]) ? 1 : 0, 0);
    chkS("cola llena", S.enEspera(), "754 981 438 580");
    int x;
    S.siguiente(x); chkI("siguiente devuelve el frente", x, 754);
    S.siguiente(x);
    S.encolar(COD[6]); S.encolar(COD[7]);
    chkS("los datos dieron la vuelta", S.enEspera(), "438 580 793 491");
    chkI("capacidad antes de ampliar", S.cap, 4);
    S.ampliarCola();
    chkI("capacidad duplicada", S.cap, 8);
    chkI("frente reubicado en 0", S.frente, 0);
    chkS("orden conservado tras ampliar", S.enEspera(), "438 580 793 491");
    S.encolar(COD[0]);
    chkS("sigue funcionando tras ampliar", S.enEspera(), "438 580 793 491 754");

    cout << " D · la red de puntos" << endl;
    chkS("ruta minima 0 -> 7", lista2s(S.rutaMinima(0, 7)), "0,3,6,7");
    chkS("ruta minima 0 -> 5", lista2s(S.rutaMinima(0, 5)), "0,2,5");
    chkS("ruta de un vertice a si mismo", lista2s(S.rutaMinima(3, 3)), "3");
    vector<string> vc = S.viasCriticas();
    string sc; for (size_t i=0;i<vc.size();i++) { if(i) sc+=","; sc+=vc[i]; }
    chkS("vias criticas", sc, "0-3,3-6,6-7");

    cout << " E · seleccion optima" << endl;
    vector<int> sel = S.mejorSeleccion(CAPV);
    chkS("mejor seleccion con capacidad 14", lista2s(sel), "491,580,888");
    int aporte = 0, peso = 0;
    for (size_t i=0;i<sel.size();i++) { Punto* q=S.buscar(sel[i]); aporte+=q->total(); peso+=q->nm; }
    chkI("aporte total de la seleccion", aporte, 317);
    chkI("la seleccion cabe en la capacidad", peso <= CAPV ? 1 : 0, 1);
    chkS("seleccion con capacidad 0", lista2s(S.mejorSeleccion(0)), "");

    cout << "----------------------------------------------------------" << endl;
    if (fallas == 0) {
        // Se entrega a la PARTE F lo necesario para la verificacion cruzada.
        ofstream f("cruce.txt");
        f << "cuantos=" << S.cuantos() << "\n";
        f << "suma="    << S.sumaTotales() << "\n";
        f << "altura="  << S.alturaIndice() << "\n";
        f << "capacidad=" << CAPV << "\n";
        string cods, pes, vals;
        for (Punto* a = S.lista; a != nullptr; a = a->sig) {
            if (!cods.empty()) { cods += ","; pes += ","; vals += ","; }
            cods += to_string(a->codigo);
            pes  += to_string(a->nm);
            vals += to_string(a->total());
        }
        f << "codigos="  << cods << "\n";
        f << "pesos="    << pes  << "\n";
        f << "valores="  << vals << "\n";
        f << "seleccion=" << lista2s(sel) << "\n";
        f << "aporte="   << aporte << "\n";
        f.close();
        cout << "  PARTE C++ COMPLETA. Ahora ejecute la PARTE F:  python3 pruebas.py" << endl;
    } else {
        remove("cruce.txt");
        cout << "  PARTE C++ INCOMPLETA (" << fallas << " falla(s))." << endl;
        cout << "  Corrija y vuelva a ejecutar. El codigo de cierre sale al final," << endl;
        cout << "  cuando las dos partes del sistema funcionen." << endl;
    }
    return 0;
}
