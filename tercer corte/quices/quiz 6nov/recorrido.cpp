#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

const int N = 9;
std::vector<std::string> NOMBRES = {"CENTRO", "NORTE", "SUR", "ORIENTE", "OCCIDENTE", "CHAPINERO", "USAQUEN", "BOSA", "VEREDA"};
std::vector<std::pair<int, int>> ARISTAS = {
    {0,1}, {1,4}, {0,2}, {0,3}, {1,5}, {2,7}, {3,6}, {5,6}, 
    {4,7}, {7,8}, {8,1}, {7,5}, {5,8}, {2,6}, {6,8}, {1,8}, 
    {5,7}, {5,3}
};
std::vector<std::vector<int>> lista(N);

void dfs_rec(int u, std::vector<bool>& visitado, std::vector<int>& orden, int prof = 0, std::vector<std::string>* traza = nullptr) {
    visitado[u] = true;
    orden.push_back(u);
    if (traza != nullptr) {
        std::string spaces(prof * 2, ' ');
        traza->push_back(spaces + "entra " + NOMBRES[u]);
    }
    for (int v : lista[u]) {
        if (!visitado[v]) {
            dfs_rec(v, visitado, orden, prof + 1, traza);
        } else if (traza != nullptr) {
            std::string spaces((prof + 1) * 2, ' ');
            traza->push_back(spaces + NOMBRES[v] + " ya visitado, no entra");
        }
    }
    if (traza != nullptr) {
        std::string spaces(prof * 2, ' ');
        traza->push_back(spaces + "sale  " + NOMBRES[u]);
    }
}

std::vector<std::vector<std::string>> componentes() {
    std::vector<bool> visitado(N, false);
    std::vector<std::vector<std::string>> comps;
    for (int s = 0; s < N; ++s) {
        if (!visitado[s]) {
            std::vector<int> o;
            dfs_rec(s, visitado, o, 0, nullptr);
            std::vector<std::string> comp_nombres;
            for (int i : o) {
                comp_nombres.push_back(NOMBRES[i]);
            }
            comps.push_back(comp_nombres);
        }
    }
    return comps;
}

std::vector<int> dfs_iter(int inicio) {
    std::vector<bool> visitado(N, false);
    std::vector<int> pila = {inicio};
    std::vector<int> orden;
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
    return orden;
}

bool hay_ciclo() {
    std::vector<bool> visitado(N, false);
    auto explorar = [&](auto& self, int u, int padre) -> bool {
        visitado[u] = true;
        for (int v : lista[u]) {
            if (!visitado[v]) {
                if (self(self, v, u)) return true;
            } else if (v != padre) {
                return true;
            }
        }
        return false;
    };
    for (int s = 0; s < N; ++s) {
        if (!visitado[s] && explorar(explorar, s, -1)) return true;
    }
    return false;
}

int main() {
    for (const auto& arista : ARISTAS) {
        int u = arista.first;
        int v = arista.second;
        lista[u].push_back(v);
        lista[v].push_back(u);
    }
    for (auto& v : lista) {
        std::sort(v.begin(), v.end());
    }

    std::vector<bool> vis(N, false);
    std::vector<int> orden;
    std::vector<std::string> traza;
    dfs_rec(0, vis, orden, 0, &traza);
    std::cout << "DFS RECURSIVO desde CENTRO\n";
    for (const auto& t : traza) {
        std::cout << "  " << t << "\n";
    }
    std::cout << "  orden de visita: ";
    for (size_t i = 0; i < orden.size(); ++i) {
        std::cout << NOMBRES[orden[i]] << (i + 1 < orden.size() ? " -> " : "");
    }
    std::cout << "\n\nDFS ITERATIVO (con pila explicita) desde CENTRO\n";
    std::cout << "  orden de visita: ";
    std::vector<int> orden_iter = dfs_iter(0);
    for (size_t i = 0; i < orden_iter.size(); ++i) {
        std::cout << NOMBRES[orden_iter[i]] << (i + 1 < orden_iter.size() ? " -> " : "");
    }
    std::cout << "\n";

    auto print_comps = [](const std::vector<std::vector<std::string>>& comps) {
        std::cout << "[";
        for (size_t i = 0; i < comps.size(); ++i) {
            std::cout << "[";
            for (size_t j = 0; j < comps[i].size(); ++j) {
                std::cout << "\"" << comps[i][j] << "\"" << (j + 1 < comps[i].size() ? ", " : "");
            }
            std::cout << "]" << (i + 1 < comps.size() ? ", " : "");
        }
        std::cout << "]";
    };

    std::cout << "\nCOMPONENTES CONEXAS de la red completa: ";
    print_comps(componentes());
    std::cout << "\n";

    std::vector<std::vector<int>> lista_rota(N);
    std::vector<std::pair<int, int>> aristas_rotas = {{0,1},{0,2},{3,6}};
    for (const auto& arista : aristas_rotas) {
        int u = arista.first;
        int v = arista.second;
        lista_rota[u].push_back(v);
        lista_rota[v].push_back(u);
    }
    for (auto& v : lista_rota) {
        std::sort(v.begin(), v.end());
    }

    std::vector<std::vector<int>> lista_orig = lista;
    lista = lista_rota;
    std::cout << "COMPONENTES de una red con tramos cortados: ";
    print_comps(componentes());
    std::cout << "\n";
    lista = lista_orig;

    std::cout << "¿La red tiene algun circuito?: " << (hay_ciclo() ? "true" : "false") << "\n";

    return 0;
}