class nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izq = None
        self.der = None

def inorden(n, salida):
    if n is None: return
    inorden(n.izq, salida)
    salida.append(n.dato)
    inorden(n.der, salida)

def construir():
    raiz = nodo("catalogo")
    raiz.izq = nodo("herramienta"); raiz.der = nodo("libro")
    raiz.izq.izq = nodo("taladro");  raiz.izq.der = nodo("sierra")
    raiz.der.izq = nodo("arte");     raiz.der.der = nodo("tecnico")
    raiz.der.der.der = nodo("redes")
    return raiz

def imprimir_jerarquia(n, nivel=0):
    if n is None: return
    print("  " * nivel + str(n.dato))
    imprimir_jerarquia(n.izq, nivel + 1)
    imprimir_jerarquia(n.der, nivel + 1)

def espejo(n):
    if n is None: return
    n.izq, n.der = n.der, n.izq
    espejo(n.izq)
    espejo(n.der)

def son_iguales(a, b):
    if a is None and b is None: return True
    if a is None or b is None: return False
    if a.dato != b.dato: return False
    return son_iguales(a.izq, b.izq) and son_iguales(a.der, b.der)


if __name__ == "__main__":
    print("=== reto 1: imprimir_jerarquia ===")
    raiz = construir()
    imprimir_jerarquia(raiz)

    print("\n  otro arbol (prueba de que funciona con cualquiera):")
    t = nodo("a"); t.izq = nodo("b"); t.der = nodo("c")
    t.izq.izq = nodo("d"); t.izq.izq.der = nodo("e")
    imprimir_jerarquia(t)

    print("\n=== reto 2: espejo ===")
    original = construir()
    s = []; inorden(original, s)
    print("inorden original:", " -> ".join(s))
    espejo(original)
    s = []; inorden(original, s)
    print("inorden espejado:", " -> ".join(s))
    print("(el inorden del espejo es el inorden original al reves)")

    print("\n=== reto 3: son_iguales ===")
    a = construir()
    b = construir()
    c = construir(); espejo(c)
    print("original vs copia identica :", son_iguales(a, b))
    print("original vs su espejo      :", son_iguales(a, c))
    d = construir(); d.der.izq.dato = "arte2"
    print("misma forma, un dato distinto:", son_iguales(a, d))
    e = nodo(1); e.izq = nodo(2)
    f = nodo(1); f.der = nodo(2)
    print("mismos datos, forma distinta :", son_iguales(e, f))
    g = nodo(1); g.izq = nodo(2); g.der = nodo(2)
    h = nodo(1); h.izq = nodo(2); h.der = nodo(2); espejo(h)
    print("arbol simetrico vs su espejo :", son_iguales(g, h))
    print("dos arboles vacios           :", son_iguales(None, None))
