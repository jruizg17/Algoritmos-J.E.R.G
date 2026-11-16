import random
import sys
import time
from grafo_base import nombres, aristas_base, num_zonas

sys.setrecursionlimit(10000)

def lista_de(n, aristas):
    l = [[] for _ in range(n)]
    for u, v in aristas:
        l[u].append(v); l[v].append(u)
    for x in l: x.sort()
    return l

lista = lista_de(num_zonas, aristas_base)

def bfs(lista, inicio):
    n = len(lista)
    visitado = [False] * n
    dist = [-1] * n
    padre = [-1] * n
    cola = [inicio]
    visitado[inicio] = True
    dist[inicio] = 0
    orden = []
    while cola:
        u = cola.pop(0)
        orden.append(u)
        for v in lista[u]:
            if not visitado[v]:
                visitado[v] = True
                dist[v] = dist[u] + 1
                padre[v] = u
                cola.append(v)
    return orden, dist, padre

asignaturas = ["programacion i", "estructuras de datos", "algoritmos", "bases de datos",
               "calculo i", "algebra lineal", "aprendizaje automatico"]
prerrequisitos = [
    (0, 1),
    (1, 2),
    (1, 3),
    (4, 5),
    (2, 6),
    (5, 6),
    (6, 1),
]

def lista_dirigida(n, aristas):
    l = [[] for _ in range(n)]
    for u, v in aristas: l[u].append(v)
    return l

def detectar_ciclos(ld):
    n = len(ld)
    estado = [0] * n
    camino = []
    ciclos = []
    def visitar(u):
        estado[u] = 1
        camino.append(u)
        for v in ld[u]:
            if estado[v] == 0:
                visitar(v)
            elif estado[v] == 1:
                i = camino.index(v)
                ciclos.append(camino[i:] + [v])
        camino.pop()
        estado[u] = 2
    for s in range(n):
        if estado[s] == 0: visitar(s)
    return ciclos

def hay_ciclo_regla_del_padre(ld):
    n = len(ld); vis = [False] * n
    def explorar(u, padre):
        vis[u] = True
        for v in ld[u]:
            if not vis[v]:
                if explorar(v, u): return True
            elif v != padre: return True
        return False
    return any(not vis[s] and explorar(s, -1) for s in range(n))

def reto2_dfs():
    print("=" * 66)
    print("dfs - reto 2: el plan de estudios imposible")
    print("=" * 66)
    n = len(asignaturas)
    print("prerrequisitos (u -> v: u debe aprobarse antes que v):")
    for u, v in prerrequisitos:
        marca = "   <-- error intencional" if (u, v) == (6, 1) else ""
        print(f"  {asignaturas[u]} -> {asignaturas[v]}{marca}")

    ld = lista_dirigida(n, prerrequisitos)
    ciclos = detectar_ciclos(ld)
    print(f"\nciclos encontrados: {len(ciclos)}")
    for c in ciclos:
        print("  ciclo:", " -> ".join(asignaturas[i] for i in c))
        print("  asignaturas que lo forman:", ", ".join(sorted(asignaturas[i] for i in set(c))))
    print("  ninguna de ellas se puede cursar primero: cada una espera a otra del ciclo.")

    ld2 = lista_dirigida(n, [e for e in prerrequisitos if e != (6, 1)])
    print("\nsin la arista erronea el plan queda valido. ciclos:", detectar_ciclos(ld2) or "ninguno")

    print("un auto-ciclo (a -> a):", [" -> ".join(map(str, c)) for c in detectar_ciclos([[0]])])

    print("\npor que la regla del padre no sirve en grafos dirigidos:")
    rombo = lista_dirigida(4, [(0, 1), (0, 2), (1, 3), (2, 3)])
    print("  rombo 0->1->3, 0->2->3 (sin ciclo). regla del padre dice ciclo?:",
          hay_ciclo_regla_del_padre(rombo), "(falso positivo)  | tres estados:", bool(detectar_ciclos(rombo)))
    dos = lista_dirigida(2, [(0, 1), (1, 0)])
    print("  ciclo 0->1->0 (si hay ciclo).      regla del padre dice ciclo?:",
          hay_ciclo_regla_del_padre(dos), "(falso negativo)  | tres estados:", bool(detectar_ciclos(dos)))

def camino_mas_largo(lista, origen, destino, limite_seg=60):
    n = len(lista)
    visitado = [False] * n
    camino = [origen]
    visitado[origen] = True
    mejor = {"len": -1, "camino": None}
    llamadas = [0]
    t0 = time.perf_counter()

    corte = [False]

    def explorar(u):
        if corte[0]: return
        llamadas[0] += 1
        if llamadas[0] % 50000 == 0 and time.perf_counter() - t0 > limite_seg:
            corte[0] = True
            return
        if u == destino:
            if len(camino) - 1 > mejor["len"]:
                mejor["len"] = len(camino) - 1
                mejor["camino"] = camino[:]
            return
        for v in lista[u]:
            if not visitado[v]:
                visitado[v] = True
                camino.append(v)
                explorar(v)
                camino.pop()
                visitado[v] = False

    explorar(origen)
    return mejor["len"], mejor["camino"], llamadas[0], not corte[0]

def crecer_red(n_obj, vecinos=4, semilla=3):
    random.seed(semilla)
    aristas = set(aristas_base)
    for v in range(num_zonas, n_obj):
        for u in random.sample(range(v), min(v, vecinos)):
            aristas.add((min(u, v), max(u, v)))
    return sorted(aristas)

def reto3_dfs():
    print("\n" + "=" * 66)
    print("dfs - reto 3: el camino mas largo")
    print("=" * 66)

    long_, cam, _, _ = camino_mas_largo(lista, 0, 8)
    print("en la red de 9 zonas, de centro a vereda:")
    print(f"  mas largo ({long_} tramos): " + " -> ".join(nombres[i] for i in cam))
    _, dist, padre = bfs(lista, 0)
    corto = []
    x = 8
    while x != -1: corto.append(x); x = padre[x]
    corto.reverse()
    print(f"  mas corto ({dist[8]} tramos): " + " -> ".join(nombres[i] for i in corto) + "   (bfs)")

    print("\ntiempos (red ampliada: cada zona nueva se conecta con 4 existentes; origen = 0, destino = ultimo):")
    print(f"  {'v':>3} {'e':>4} {'tramos':>7} {'llamadas dfs':>14} {'dfs mas largo':>15} {'bfs mas corto':>15}")
    for n in (9, 15, 18, 20):
        aristas = aristas_base if n == 9 else crecer_red(n)
        l = lista_de(n, aristas)
        destino = 8 if n == 9 else n - 1
        t0 = time.perf_counter()
        longitud, _, llamadas, terminado = camino_mas_largo(l, 0, destino, limite_seg=120)
        t_dfs = time.perf_counter() - t0
        t0 = time.perf_counter()
        bfs(l, 0)
        t_bfs = time.perf_counter() - t0
        txt = f"{t_dfs:>13.3f} s" if terminado else "     > limite"
        print(f"  {n:>3} {len(aristas):>4} {longitud:>7} {llamadas:>14,} {txt} {t_bfs * 1000:>12.3f} ms")
    print("  (los tiempos exactos dependen del computador; lo importante es como crecen)")
def todas_las_distancias(lista):
    return [bfs(lista, s)[1] for s in range(len(lista))]

def reto2_bfs():
    print("\n" + "=" * 66)
    print("bfs - reto 2: los grados de separacion")
    print("=" * 66)
    distancias = todas_las_distancias(lista)
    print("matriz de distancias minimas (en tramos):")
    print("             " + " ".join(f"{n[:4]:>4}" for n in nombres))
    for i in range(num_zonas):
        print(f"  {nombres[i]:>10} " + " ".join(f"{d:>4}" for d in distancias[i]))

    alcanzables = [distancias[i][j] for i in range(num_zonas) for j in range(i + 1, num_zonas) if distancias[i][j] >= 0]
    diametro = max(alcanzables)
    pares = [(i, j) for i in range(num_zonas) for j in range(i + 1, num_zonas) if distancias[i][j] == diametro]
    desconectados = sum(1 for i in range(num_zonas) for j in range(i + 1, num_zonas) if distancias[i][j] < 0)
    print(f"\ndiametro de la red = {diametro} tramos")
    for i, j in pares:
        print(f"  par que lo produce: {nombres[i]} - {nombres[j]}")
        _, _, padre = bfs(lista, i)
        ruta = []; x = j
        while x != -1: ruta.append(x); x = padre[x]
        print("  una ruta minima entre ellos:", " -> ".join(nombres[k] for k in reversed(ruta)))
    if desconectados: print(f"  (hay {desconectados} pares sin conexion; se ignoran para el diametro)")
    promedio = sum(alcanzables) / len(alcanzables)
    print(f"distancia promedio entre zonas: {promedio:.2f} tramos")

def propagacion(lista, origen):
    _, dist, _ = bfs(lista, origen)
    alcanzados = [d for d in dist if d >= 0]
    return dist, max(alcanzados), len(alcanzados) == len(lista)

def reto3_bfs():
    print("\n" + "=" * 66)
    print("bfs - reto 3: la propagacion por olas")
    print("=" * 66)
    for origen in (0, 8):
        dist, total, todos = propagacion(lista, origen)
        print(f"\nfalla que se origina en {nombres[origen]}:")
        for minuto in range(total + 1):
            puntos = [nombres[v] for v in range(num_zonas) if dist[v] == minuto]
            print(f"  minuto {minuto}: {', '.join(puntos)}")
        print(f"  -> toda la red cae en {total} minutos" +
              ("" if todos else " (y hay puntos que nunca caen: no estan conectados)"))

    exc = []
    for s in range(num_zonas):
        _, total, _ = propagacion(lista, s)
        exc.append(total)
    print("\nexcentricidad (minutos que tarda en caer toda la red segun donde empiece la falla):")
    for v in sorted(range(num_zonas), key=lambda v: (exc[v], v)):
        print(f"  {nombres[v]:>10}: {exc[v]} min  " + "#" * exc[v])

    menor, mayor = min(exc), max(exc)
    centro = [nombres[v] for v in range(num_zonas) if exc[v] == menor]
    periferia = [nombres[v] for v in range(num_zonas) if exc[v] == mayor]
    print(f"\npunto(s) con menor excentricidad ({menor} min):  {', '.join(centro)}")
    print(f"punto(s) con mayor excentricidad ({mayor} min):  {', '.join(periferia)}")
