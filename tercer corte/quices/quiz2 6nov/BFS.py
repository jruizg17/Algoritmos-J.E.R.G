def bfs(inicio, lista, NOMBRES):
    N = len(lista)
    visitado = [False] * N
    cola = [inicio]
    orden = []
    while cola:
        u = cola.pop(0)
        if visitado[u]:
            continue
        visitado[u] = True
        orden.append(u)
        for v in lista[u]:
            if not visitado[v]:
                cola.append(v)
    print(f"BFS desde {NOMBRES[inicio]}")
    print("  orden de visita: ", end="")
    print(" -> ".join(NOMBRES[i] for i in orden))
    total_tramos = len(orden) - 1
    print(f"  total de tramos: {total_tramos}")

def dfs(inicio, lista, NOMBRES):
    N = len(lista)
    visitado = [False] * N
    pila = [inicio]
    orden = []
    while pila:
        u = pila.pop()
        if visitado[u]:
            continue
        visitado[u] = True
        orden.append(u)
        for v in reversed(lista[u]):
            if not visitado[v]:
                pila.append(v)
    print(f"DFS desde {NOMBRES[inicio]}")
    print("  orden de visita: ", end="")
    print(" -> ".join(NOMBRES[i] for i in orden))
    total_tramos = len(orden) - 1
    print(f"  total de tramos: {total_tramos}")

def unir(camino, NOMBRES):
    return " -> ".join(NOMBRES[i] for i in camino)

def niveles_y_caminos(inicio, lista, NOMBRES):
    N = len(lista)
    dist = [-1] * N
    padre = [-1] * N
    cola = [inicio]
    dist[inicio] = 0
    i = 0
    while i < len(cola):
        u = cola[i]
        i += 1
        for v in lista[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                padre[v] = u
                cola.append(v)
    maxd = max(dist)
    print(f"NIVELES desde {NOMBRES[inicio]}")
    for d in range(maxd + 1):
        print(f"  nivel {d}: ", end="")
        primero = True
        for j in range(N):
            if dist[j] == d:
                print(("" if primero else ", ") + NOMBRES[j], end="")
                primero = False
        print()
    print(f"CAMINO MAS CORTO desde {NOMBRES[inicio]}")
    for j in range(N):
        if j == inicio:
            continue
        if dist[j] == -1:
            print(f"  hacia {NOMBRES[j]}: sin camino")
            continue
        camino = []
        x = j
        while x != -1:
            camino.append(x)
            x = padre[x]
        camino.reverse()
        print(f"  hacia {NOMBRES[j]}: {unir(camino, NOMBRES)}   ({dist[j]} tramos)")

def dfs_camino(u, destino, lista, visitado, camino):
    visitado[u] = True
    camino.append(u)
    if u == destino:
        return True
    for v in lista[u]:
        if not visitado[v] and dfs_camino(v, destino, lista, visitado, camino):
            return True
    camino.pop()
    return False

if __name__ == "__main__":
    NOMBRES = ["CENTRO", "NORTE", "SUR", "ORIENTE", "OCCIDENTE", "CHAPINERO", "USAQUEN", "BOSA", "VEREDA"]
    lista = [[] for _ in range(len(NOMBRES))]
    lista[0] = [1, 2, 3]
    lista[1] = [0, 4]
    lista[2] = [0, 7]
    lista[3] = [0, 6, 5]
    lista[4] = [1, 7]
    lista[5] = [3, 8]
    lista[6] = [3]
    lista[7] = [2, 4]
    lista[8] = [5]

    bfs(0, lista, NOMBRES)
    dfs(0, lista, NOMBRES)
    niveles_y_caminos(0, lista, NOMBRES)

    vis = [False] * len(NOMBRES)
    camino = []
    dfs_camino(0, 7, lista, vis, camino)
    print(f"DFS hacia BOSA: {unir(camino, NOMBRES)}   ({len(camino) - 1} tramos)")