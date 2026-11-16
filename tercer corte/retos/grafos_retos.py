import random
from grafo_base import nombres, aristas_base, num_zonas

def matriz_a_lista(m):
    n = len(m)
    return [[j for j in range(n) if m[i][j] == 1] for i in range(n)]

def lista_a_matriz(l):
    n = len(l)
    m = [[0] * n for _ in range(n)]
    for u in range(n):
        for v in l[u]:
            m[u][v] = 1
    return m

def ida_y_vuelta_matriz(m):
    return lista_a_matriz(matriz_a_lista(m)) == m

def ida_y_vuelta_lista(l):
    normal = [sorted(set(v)) for v in l]
    return matriz_a_lista(lista_a_matriz(l)) == normal

def matriz_aleatoria(n, p, simetrica):
    m = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if simetrica and j < i:
                m[i][j] = m[j][i]
            elif random.random() < p:
                m[i][j] = 1
    return m

def reto2():
    print("=" * 66)
    print("reto 2 - el converso")
    print("=" * 66)
    random.seed(7)

    m = [[0] * num_zonas for _ in range(num_zonas)]
    for u, v in aristas_base:
        m[u][v] = 1; m[v][u] = 1
    l = matriz_a_lista(m)
    print("grafo de las 9 zonas (no dirigido):")
    for i in range(num_zonas):
        print(f"  {nombres[i]:>10} -> {', '.join(nombres[j] for j in l[i])}")
    print("  matriz -> lista -> matriz es igual al original:", ida_y_vuelta_matriz(m))

    d = [[0] * 4 for _ in range(4)]
    d[0][1] = 1; d[1][2] = 1; d[2][3] = 1; d[3][1] = 1
    print("\ngrafo dirigido de 4 vertices:", matriz_a_lista(d), "| ida y vuelta:", ida_y_vuelta_matriz(d))

    casos = {
        "grafo vacio (0 vertices)": [],
        "un solo vertice": [[0]],
        "4 vertices sin aristas": [[0] * 4 for _ in range(4)],
        "completo k5 sin lazos": [[0 if i == j else 1 for j in range(5)] for i in range(5)],
        "todo unos (con lazos)": [[1] * 4 for _ in range(4)],
    }
    print("\ncasos borde:")
    for nombre, mm in casos.items():
        print(f"  {nombre:<28} -> {ida_y_vuelta_matriz(mm)}")

    ok_m = ok_l = 0
    pruebas = 2000
    for _ in range(pruebas):
        n = random.randint(0, 12)
        mm = matriz_aleatoria(n, random.random(), random.choice([True, False]))
        ok_m += ida_y_vuelta_matriz(mm)
        ll = [[random.randrange(n) for _ in range(random.randint(0, n))] for _ in range(n)] if n else []
        ok_l += ida_y_vuelta_lista(ll)
    print(f"\n{pruebas} matrices aleatorias (dirigidas y no dirigidas): {ok_m}/{pruebas} ida y vuelta correctas")
    print(f"{pruebas} listas aleatorias (con repetidos y desordenadas): {ok_l}/{pruebas} correctas tras normalizar")
    assert ok_m == pruebas and ok_l == pruebas
    print("-> lista_a_matriz(matriz_a_lista(m)) == m para toda matriz valida.")

def existe_regular(nv, k):
    if k < 0 or k > nv - 1: return False
    return (nv * k) % 2 == 0

def existe_por_fuerza_bruta(nv, k):
    pares = list(range(nv), 2))
    for mascara in range(1 << len(pares)):
        grado = [0] * nv
        for idx, (u, v) in enumerate(pares):
            if mascara >> idx & 1:
                grado[u] += 1; grado[v] += 1
        if all(g == k for g in grado): return True
    return False

def construir_regular(nv, k):
    aristas = set()
    for i in range(nv):
        for d in range(1, k // 2 + 1):
            aristas.add(frozenset((i, (i + d) % nv)))
        if k % 2 == 1:
            aristas.add(frozenset((i, (i + nv // 2) % nv)))
    return aristas

def reto3():
    print("\n" + "=" * 66)
    print("reto 3 - el grafo imposible")
    print("=" * 66)
    print("pregunta: ¿existe un grafo no dirigido de 5 vertices, todos de grado 3?")
    print("  suma de grados = 5 x 3 = 15.  pero la suma de grados = 2e (cada arista")
    print("  aporta 1 al grado de dos vertices), asi que debe ser par. 15 es impar.")
    print("  -> e = 15/2 = 7.5 aristas: absurdo. no existe.")
    print("  fuerza bruta (los 1024 grafos posibles de 5 vertices):",
          "existe" if existe_por_fuerza_bruta(5, 3) else "no existe, confirmado")

    print("\ngeneralizacion: tabla de existencia de grafos k-regulares")
    print("  (si = existe, no = imposible)   filas: v vertices, columnas: grado k")
    maxk = 7
    print("      k=" + "".join(f"{k:>4}" for k in range(maxk + 1)))
    for nv in range(1, 10):
        fila = "".join(f"{'si' if existe_regular(nv, k) else 'no':>4}" for k in range(maxk + 1))
        print(f"  v={nv}  " + fila)

    for nv in range(1, 7):
        for k in range(0, nv + 1):
            assert existe_regular(nv, k) == existe_por_fuerza_bruta(nv, k), (nv, k)
    print("\nla regla coincide con la fuerza bruta para todo v <= 6 y k <= v.")
    for nv in range(2, 15):
        for k in range(0, nv):
            if existe_regular(nv, k):
                a = construir_regular(nv, k)
                g = [0] * nv
                for e in a:
                    for x in e: g[x] += 1
                assert all(x == k for x in g) and len(a) == nv * k // 2, (nv, k)
    print("y para todo v <= 14 se construyo un ejemplo real en cada caso en que la regla dice si.")

    print("""
conclusion
  un grafo simple no dirigido de v vertices con todos los vertices de grado k
  existe si y solo si:
      (1)  k <= v - 1      (un vertice no puede tener mas vecinos que v-1), y
      (2)  v x k es par    (porque v x k = suma de grados = 2e).
  es imposible cuando k >= v, o cuando v y k son ambos impares.
  ejemplos imposibles: (5,3), (7,3), (9,5), (3,1)... y tambien (4,4), (3,3).
  siempre que v x k es par y k <= v-1 si existe (se construye uniendo cada
  vertice del anillo con sus vecinos mas cercanos; si k es impar, tambien con
  el vertice opuesto).""")


if __name__ == "__main__":
    reto2()
    reto3()
