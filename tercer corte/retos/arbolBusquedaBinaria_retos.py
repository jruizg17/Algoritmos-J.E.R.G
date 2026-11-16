import math

class nodo:
    def __init__(self, clave, nombre=""):
        self.clave = clave; self.nombre = nombre
        self.izq = None; self.der = None

def insertar(n, clave, nombre=""):
    if n is None: return nodo(clave, nombre)
    if clave < n.clave: n.izq = insertar(n.izq, clave, nombre)
    elif clave > n.clave: n.der = insertar(n.der, clave, nombre)
    return n

def inorden(n, s):
    if n is None: return
    inorden(n.izq, s); s.append(n.clave); inorden(n.der, s)

def contar(n):
    if n is None: return 0
    return 1 + contar(n.izq) + contar(n.der)

def en_rango(n, a, b, visitados, salida):
    if n is None: return
    visitados[0] += 1
    if n.clave > a:
        en_rango(n.izq, a, b, visitados, salida)
    if a <= n.clave <= b:
        salida.append(n.clave)
    if n.clave < b:
        en_rango(n.der, a, b, visitados, salida)

def es_bst(n, minimo=-math.inf, maximo=math.inf):
    if n is None: return True
    if not (minimo < n.clave < maximo): return False
    return (es_bst(n.izq, minimo, n.clave) and
            es_bst(n.der, n.clave, maximo))

def es_bst_ingenuo(n):
    if n is None: return True
    if n.izq is not None and n.izq.clave >= n.clave: return False
    if n.der is not None and n.der.clave <= n.clave: return False
    return es_bst_ingenuo(n.izq) and es_bst_ingenuo(n.der)


if __name__ == "__main__":
    raiz = None
    for c in [50, 30, 70, 20, 40, 60, 80, 35]:
        raiz = insertar(raiz, c)
    total = contar(raiz)
    s = []; inorden(raiz, s)
    print("arbol del ejemplo, inorden:", s, f"({total} nodos)")

    print("\n=== reto 2: en_rango ===")
    for a, b in [(35, 65), (20, 80), (45, 55), (0, 10), (60, 60)]:
        vis = [0]; out = []
        en_rango(raiz, a, b, vis, out)
        esperado = [x for x in s if a <= x <= b]
        ok = "ok" if out == esperado else "error"
        print(f"  en_rango [{a:>2},{b:>2}] -> {out}  visitados={vis[0]} de {total}  [{ok}]")
    vis = [0]; out = []
    en_rango(raiz, 35, 65, vis, out)
    assert out == [35, 40, 50, 60] and vis[0] < 8
    print("  reto: [35,65] imprime 35, 40, 50, 60 y visita", vis[0], "< 8 nodos  -> cumplido")

    print("\n=== reto 3: es_bst ===")
    print("  bst valido (el del ejemplo)        :", es_bst(raiz))

    malo = nodo(50)
    malo.izq = nodo(30)
    malo.izq.der = nodo(60)
    print("  contraejemplo 50 / 30 / (der 30)=60:", es_bst(malo), " <- debe ser false")
    print("  version ingenua (solo hijos)       :", es_bst_ingenuo(malo),
          " <- dice true: por eso no basta comparar con los hijos")

    otro = nodo(10); otro.der = nodo(20); otro.der.izq = nodo(5)
    print("  5 colgando a la derecha del 10     :", es_bst(otro), " <- debe ser false")
    dup = nodo(10); dup.izq = nodo(10)
    print("  clave repetida (10 con hijo izq 10):", es_bst(dup), " <- false (sin duplicados)")
    print("  arbol vacio                        :", es_bst(None))
    print("  un solo nodo                       :", es_bst(nodo(7)))
