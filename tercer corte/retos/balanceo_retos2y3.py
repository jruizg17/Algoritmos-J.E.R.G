import random

class nodo:
    def __init__(self, c):
        self.clave = c; self.izq = None; self.der = None; self.alt = 0

def alt(n):  return -1 if n is None else n.alt
def fe(n):   return 0 if n is None else alt(n.izq) - alt(n.der)
def recalc(n): n.alt = 1 + max(alt(n.izq), alt(n.der))

def rotar_derecha(y):
    x = y.izq; b = x.der
    x.der = y; y.izq = b
    recalc(y); recalc(x)
    return x

def rotar_izquierda(x):
    y = x.der; b = y.izq
    y.izq = x; x.der = b
    recalc(x); recalc(y)
    return y

def insertar(n, c):
    if n is None: return nodo(c)
    if c < n.clave: n.izq = insertar(n.izq, c)
    elif c > n.clave: n.der = insertar(n.der, c)
    recalc(n)
    return n

def minimo(n):
    while n.izq is not None: n = n.izq
    return n

def eliminar(n, c):
    if n is None: return None
    if c < n.clave: n.izq = eliminar(n.izq, c)
    elif c > n.clave: n.der = eliminar(n.der, c)
    else:
        if n.izq is None: return n.der
        if n.der is None: return n.izq
        suc = minimo(n.der)
        n.clave = suc.clave
        n.der = eliminar(n.der, suc.clave)
    recalc(n)
    return n

def altura_de_orden(orden):
    raiz = None
    for c in orden: raiz = insertar(raiz, c)
    return alt(raiz)

def reto2():
    print("=" * 66)
    print("reto 2 - el orden maldito (claves 1 a 7)")
    print("=" * 66)

    bueno = [4, 2, 6, 1, 3, 5, 7]
    malo = [1, 2, 3, 4, 5, 6, 7]
    print(f"un orden equilibrado : {bueno}  -> altura {altura_de_orden(bueno)}")
    print(f"el peor orden        : {malo}  -> altura {altura_de_orden(malo)}")

    alturas = {}
    ordenes_h2 = []
    for p in range(1, 8):
        h = altura_de_orden(p)
        alturas[h] = alturas.get(h, 0) + 1
        if h == 2: ordenes_h2.append(p)
    print("\naltura del bst segun el orden de insercion (las 5040 permutaciones):")
    for h in sorted(alturas):
        print(f"  altura {h}: {alturas[h]:>4} ordenes")
    print(f"\nordenes que dan altura 2 (sin rotar): {len(ordenes_h2)}")
    print(f"ordenes que dan altura 6 (el peor)  : {alturas[6]}  (= 2^6: en cada paso se elige el minimo o el maximo restante)")

    todos_con_4 = all(p[0] == 4 for p in ordenes_h2)
    padre = {2: 4, 6: 4, 1: 2, 3: 2, 5: 6, 7: 6}
    padre_antes = all(p.index(padre[k]) < p.index(k) for p in ordenes_h2 for k in padre)
    print("\n¿todos empiezan por 4?                         ", todos_con_4)
    print("¿en todos cada nodo llega despues de su padre? ", padre_antes)

def rebalancear(n):
    if fe(n) > 1:
        if fe(n.izq) < 0: n.izq = rotar_izquierda(n.izq)
        return rotar_derecha(n)
    if fe(n) < -1:
        if fe(n.der) > 0: n.der = rotar_derecha(n.der)
        return rotar_izquierda(n)
    return n

def avl_insertar(n, c):
    if n is None: return nodo(c)
    if c < n.clave: n.izq = avl_insertar(n.izq, c)
    elif c > n.clave: n.der = avl_insertar(n.der, c)
    else: return n
    recalc(n)
    return rebalancear(n)

def reparar_mas_profundo(n):
    if n is None: return None, False
    n.izq, hecho = reparar_mas_profundo(n.izq)
    if not hecho: n.der, hecho = reparar_mas_profundo(n.der)
    recalc(n)
    if not hecho and abs(fe(n)) > 1:
        return rebalancear(n), True
    return n, hecho

def desbalanceados(n, lista=None):
    if lista is None: lista = []
    if n is None: return lista
    desbalanceados(n.izq, lista); desbalanceados(n.der, lista)
    if abs(fe(n)) > 1: lista.append((n.clave, fe(n)))
    return lista

def dibujar(n, prefijo="", etiqueta="", ultimo=True, raiz=True):
    if n is None: return
    conector = "" if raiz else ("└─ " if ultimo else "├─ ")
    print(f"  {prefijo}{conector}{etiqueta}{n.clave} (fe={fe(n)})")
    nuevo = prefijo if raiz else prefijo + ("   " if ultimo else "│  ")
    hijos = [(e, h) for e, h in (("izq: ", n.izq), ("der: ", n.der)) if h is not None]
    for i, (e, h) in enumerate(hijos):
        dibujar(h, nuevo, e, i == len(hijos) - 1, False)

def construir_ejemplo():
    def crear(c, izq=None, der=None):
        n = nodo(c); n.izq = izq; n.der = der; recalc(n); return n
    izquierda = crear(5, crear(3, crear(2, crear(1)), crear(4)), crear(6, None, crear(7)))
    derecha = crear(11, crear(10, crear(9)), crear(12))
    return crear(8, izquierda, derecha)

def reto3():
    print("\n" + "=" * 66)
    print("reto 3 - ¿cuando no alcanza una rotacion?")
    print("=" * 66)

    raiz = construir_ejemplo()
    print("arbol avl valido de partida (todos los |fe| <= 1):")
    dibujar(raiz)
    print("  nodos desbalanceados:", desbalanceados(raiz) or "ninguno")

    print("\n--- eliminacion: borrar el 12 (sin rebalancear) ---")
    raiz = eliminar(raiz, 12)
    print("  nodos desbalanceados:", desbalanceados(raiz))
    print("  el mas profundo es el 11 (fe=2, su hijo 10 tiene fe=+1 -> caso ll).")
    raiz, _ = reparar_mas_profundo(raiz)
    print("\n  tras una rotacion derecha en el 11, el subarbol de la derecha ya esta bien:")
    dibujar(raiz)
    print("  nodos desbalanceados:", desbalanceados(raiz))
    print("  -> ¡quedo otro nodo desbalanceado mas arriba (la raiz 8)!")
    print("     la rotacion en el 11 acorto en 1 la altura de ese subarbol (de 2 a 1),")
    print("     y el 8 paso de fe=+1 a fe=+2.")
    raiz, _ = reparar_mas_profundo(raiz)
    print("\n  segunda rotacion (derecha en el 8, caso ll):")
    dibujar(raiz)
    print("  nodos desbalanceados:", desbalanceados(raiz) or "ninguno")

    print("\n--- comprobacion experimental (arboles avl aleatorios) ---")
    random.seed(2026)
    intentos = 20000
    fallos_ins = 0
    fallos_del = 0
    ejemplo_del = None
    for _ in range(intentos):
        n = random.randint(1, 40)
        claves = random.sample(range(1, 200), n)
        nueva = random.choice([x for x in range(0, 201) if x not in claves])
        ti = None
        for c in claves: ti = avl_insertar(ti, c)
        ti = insertar(ti, nueva)
        ti, _ = reparar_mas_profundo(ti)
        if desbalanceados(ti): fallos_ins += 1

        borrar = random.choice(claves)
        td = None
        for c in claves: td = avl_insertar(td, c)
        td = eliminar(td, borrar)
        td, _ = reparar_mas_profundo(td)
        if desbalanceados(td):
            fallos_del += 1
            if ejemplo_del is None: ejemplo_del = (claves[:], borrar)
    print(f"  {intentos} inserciones con una rotacion: arbol aun desbalanceado en {fallos_ins} casos")
    print(f"  {intentos} eliminaciones con una rotacion: arbol aun desbalanceado en {fallos_del} casos")

    print("""
respuestas
  ¿es posible en una insercion?  no. una sola rotacion siempre basta.
    antes de insertar, el subarbol de x
    tenia altura h. la insercion lo dejo en h+1, y eso es lo que desbalancea a x.
    al aplicar la rotacion correcta, el subarbol que cuelga de
    la nueva raiz vuelve a tener altura h: la misma que tenia antes de insertar.
    para los ancestros de x nada cambio, asi que siguen equilibrados.

  ¿es posible en una eliminacion?  si.
    borrar acorta un subarbol, y al rotar la altura puede bajar de nuevo.
    cuando el hijo del lado pesado tiene fe distinto de 0, la rotacion deja el subarbol con altura h-1 en lugar de h. los
    ancestros ven un cambio de altura y pueden desbalancearse, y asi hacia
    arriba hasta la raiz: en el peor caso se necesitan o(log n) rotaciones.
    por eso el avl, despues de eliminar, revisa el camino completo hasta la raiz.""")
