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

def insertar_sin_balancear(n, c):
    if n is None: return nodo(c)
    if c < n.clave: n.izq = insertar_sin_balancear(n.izq, c)
    elif c > n.clave: n.der = insertar_sin_balancear(n.der, c)
    recalc(n)
    return n

def dibujar(n, prefijo="", etiqueta="", ultimo=True, raiz=True):
    if n is None: return
    conector = "" if raiz else ("└─ " if ultimo else "├─ ")
    print(f"  {prefijo}{conector}{etiqueta}{n.clave} (fe={fe(n)})")
    nuevo = prefijo if raiz else prefijo + ("   " if ultimo else "│  ")
    hijos = [(e, h) for e, h in (("izq: ", n.izq), ("der: ", n.der)) if h is not None]
    for i, (e, h) in enumerate(hijos):
        dibujar(h, nuevo, e, i == len(hijos) - 1, False)

def diagnosticar(raiz):
    f = fe(raiz)
    if f > 1:
        fh = fe(raiz.izq)
        return ("ll", f, fh) if fh >= 0 else ("lr", f, fh)
    if f < -1:
        fh = fe(raiz.der)
        return ("rr", f, fh) if fh <= 0 else ("rl", f, fh)
    return ("equilibrado", f, None)

def rotar(raiz, caso):
    if caso == "ll": return rotar_derecha(raiz)
    if caso == "rr": return rotar_izquierda(raiz)
    if caso == "lr":
        raiz.izq = rotar_izquierda(raiz.izq); recalc(raiz)
        return rotar_derecha(raiz)
    if caso == "rl":
        raiz.der = rotar_derecha(raiz.der); recalc(raiz)
        return rotar_izquierda(raiz)
    return raiz

accion = {
    "ll": "una rotacion derecha sobre la raiz",
    "rr": "una rotacion izquierda sobre la raiz",
    "lr": "izquierda sobre el hijo y luego derecha sobre la raiz",
    "rl": "derecha sobre el hijo y luego izquierda sobre la raiz",
}

def procesar(claves):
    raiz = None
    for c in claves:
        raiz = insertar_sin_balancear(raiz, c)
    print("\narbol antes (sin balancear):")
    dibujar(raiz)
    caso, f, fh = diagnosticar(raiz)
    if caso == "equilibrado":
        print(f"\ndiagnostico: equilibrado (fe de la raiz = {f}). no hay que rotar.")
        return raiz, caso
    print(f"\ndiagnostico: {caso}  (fe raiz = {f}, fe del hijo pesado = {fh})")
    print(f"rotacion: {accion[caso]}")
    raiz = rotar(raiz, caso)
    print("\narbol despues:")
    dibujar(raiz)
    return raiz, caso

def leer_clave(k, ya):
    while True:
        texto = input(f"clave {k} de 3: ").strip()
        cuerpo = texto[1:] if texto[:1] == "-" else texto
        if not cuerpo.isdecimal():
            print("  escriba un numero entero.")
            continue
        c = int(texto)
        if c in ya:
            print("  esa clave ya se ingreso; use una distinta.")
            continue
        return c

if __name__ == "__main__":
    print("rotacion manual: ingrese tres claves en el orden en que se insertarian.")
    claves = []
    for k in (1, 2, 3):
        claves.append(leer_clave(k, claves))
    procesar(claves)
