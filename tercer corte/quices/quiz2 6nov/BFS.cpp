#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;
vector<string> NOMBRES = {"CENTRO", "NORTE", "SUR", "ORIENTE", "OCCIDENTE", "CHAPINERO", "USAQUEN", "BOSA", "VEREDA"};
vector<vector<int>> CAMINOS;
vector<vector<int>> lista(NOMBRES.size());
void bfs(int inicio, const vector<vector<int>>& lista, const vector<string>& NOMBRES) {
    int N = lista.size();
    vector<bool> visitado(N, false);
    vector<int> cola = {inicio};
    vector<int> orden;
    while (!cola.empty()) {
        int u = cola.front();
        cola.erase(cola.begin());
        if (visitado[u]) continue;
        visitado[u] = true;
        orden.push_back(u);
        for (int v : lista[u]) {
            if (!visitado[v]) cola.push_back(v);
        }
    }
    cout << "BFS desde " << NOMBRES[inicio] << "\n";
    cout << "  orden de visita: ";
    for (size_t i = 0; i < orden.size(); ++i) {
        cout << NOMBRES[orden[i]] << (i + 1 < orden.size() ? " -> " : "");
    }
    cout << "\n";
    int total_tramos = orden.size() - 1;
    cout << "  total de tramos: " << total_tramos << "\n";
}
void dfs(int inicio, const vector<vector<int>>& lista, const vector<string>& NOMBRES) {
    int N = lista.size();
    vector<bool> visitado(N, false);
    vector<int> pila = {inicio};
    vector<int> orden;
    while (!pila.empty()) {
        int u = pila.back();
        pila.pop_back();
        if (visitado[u]) continue;
        visitado[u] = true;
        orden.push_back(u);
        for (auto it = lista[u].rbegin(); it != lista[u].rend(); ++it) {
            int v = *it;
            if (!visitado[v]) pila.push_back(v);
        }
    }
    cout << "DFS desde " << NOMBRES[inicio] << "\n";
    cout << "  orden de visita: ";
    for (size_t i = 0; i < orden.size(); ++i) {
        cout << NOMBRES[orden[i]] << (i + 1 < orden.size() ? " -> " : "");
    }
    cout << "\n";
    int total_tramos = orden.size() - 1;
    cout << "  total de tramos: " << total_tramos << "\n";
}
string unir(const vector<int>& camino, const vector<string>& NOMBRES) {
    string s;
    for (size_t i = 0; i < camino.size(); ++i)
        s += NOMBRES[camino[i]] + (i + 1 < camino.size() ? " -> " : "");
    return s;
}
void niveles_y_caminos(int inicio, const vector<vector<int>>& lista, const vector<string>& NOMBRES) {
    int N = lista.size();
    vector<int> dist(N, -1), padre(N, -1);
    vector<int> cola = {inicio};
    dist[inicio] = 0;
    for (size_t i = 0; i < cola.size(); ++i) {
        int u = cola[i];
        for (int v : lista[u]) {
            if (dist[v] == -1) {
                dist[v] = dist[u] + 1;
                padre[v] = u;
                cola.push_back(v);
            }
        }
    }
    int maxd = *max_element(dist.begin(), dist.end());
    cout << "NIVELES desde " << NOMBRES[inicio] << "\n";
    for (int d = 0; d <= maxd; ++d) {
        cout << "  nivel " << d << ": ";
        bool primero = true;
        for (int i = 0; i < N; ++i) {
            if (dist[i] == d) {
                cout << (primero ? "" : ", ") << NOMBRES[i];
                primero = false;
            }
        }
        cout << "\n";
    }
    cout << "CAMINO MAS CORTO desde " << NOMBRES[inicio] << "\n";
    for (int i = 0; i < N; ++i) {
        if (i == inicio) continue;
        if (dist[i] == -1) {
            cout << "  hacia " << NOMBRES[i] << ": sin camino\n";
            continue;
        }
        vector<int> camino;
        for (int x = i; x != -1; x = padre[x]) camino.push_back(x);
        reverse(camino.begin(), camino.end());
        cout << "  hacia " << NOMBRES[i] << ": " << unir(camino, NOMBRES)
             << "   (" << dist[i] << " tramos)\n";
    }
}
bool dfs_camino(int u, int destino, const vector<vector<int>>& lista,
                vector<bool>& visitado, vector<int>& camino) {
    visitado[u] = true;
    camino.push_back(u);
    if (u == destino) return true;
    for (int v : lista[u])
        if (!visitado[v] && dfs_camino(v, destino, lista, visitado, camino)) return true;
    camino.pop_back();
    return false;
}
int main() {
    lista[0] = {1, 2, 3};
    lista[1] = {0, 4};
    lista[2] = {0, 7};
    lista[3] = {0, 6, 5};
    lista[4] = {1, 7};
    lista[5] = {3, 8};
    lista[6] = {3};
    lista[7] = {2, 4};
    lista[8] = {5};
    bfs(0, lista, NOMBRES);
    dfs(0, lista, NOMBRES);
    niveles_y_caminos(0, lista, NOMBRES);

    vector<bool> vis(NOMBRES.size(), false);
    vector<int> camino;
    dfs_camino(0, 7, lista, vis, camino);
    cout << "DFS hacia BOSA: " << unir(camino, NOMBRES)
         << "   (" << camino.size() - 1 << " tramos)\n";

    return 0;
}
