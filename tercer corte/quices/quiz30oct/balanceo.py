class nodo:
    def __init__(self, clave):
        self.clave = clave
        self.izq = None
        self.der = None
        self.fe = 0  # factor de equilibrio para calcular el balanceo despues
    
def insertar(raiz, clave):
    if raiz is None:
        return nodo(clave)
    elif clave < raiz.clave:
        raiz.izq = insertar(raiz.izq, clave)
    else:
        raiz.der = insertar(raiz.der, clave) #agregamos los nodos en el arbol
    
    raiz.fe = altura(raiz.izq) - altura(raiz.der)#revisamos y cambiamos el FE en el arbol
    
    return raiz

def altura(nodo):
    if nodo is None:
        return 0
    else:
        return 1 + max(altura(nodo.izq), altura(nodo.der)) #calculamos la altura para calcular el FE
def imprimir_arbol(raiz, nivel=0):
    if raiz is not None:
        imprimir_arbol(raiz.der, nivel + 1)
        print(' ' * 4 * nivel + '->', raiz.clave, f'(FE: {raiz.fe})') 
        imprimir_arbol(raiz.izq, nivel + 1) #imprimimos los nodos mas a la derecha izquierda buscandolos primero 
def diagnosticar(raiz):
    if raiz is None:
        return "El árbol está vacío."
    
    if raiz.fe > 1:  # subarbol izquierdo pesado
        if raiz.izq.fe >= 0:
            return "Caso LL (Rotación Simple a la Derecha)"
        else:
            return "Caso LR (Rotación Doble: Izquierda-Derecha)"
    elif raiz.fe < -1:  # subarbol derecho pesado
        if raiz.der.fe <= 0:
            return "Caso RR (Rotación Simple a la Izquierda)"
        else:
            return "Caso RL (Rotación Doble: Derecha-Izquierda)"
    else:
        return "El árbol está equilibrado."
def rotacion_simple_derecha(raiz):
    nueva_raiz = raiz.izq
    raiz.izq = nueva_raiz.der
    nueva_raiz.der = raiz
    
    raiz.fe = altura(raiz.izq) - altura(raiz.der)
    nueva_raiz.fe = altura(nueva_raiz.izq) - altura(nueva_raiz.der)
    
    return nueva_raiz #nos da la raiz despues de rotar 
def rotacion_simple_izquierda(raiz):
    nueva_raiz = raiz.der
    raiz.der = nueva_raiz.izq
    nueva_raiz.izq = raiz
    
    raiz.fe = altura(raiz.izq) - altura(raiz.der)
    nueva_raiz.fe = altura(nueva_raiz.izq) - altura(nueva_raiz.der)
    
    return nueva_raiz #tambien nos da la raiz despues de rotarla
print("ingrese una clave para insertar en el arbol:")
clave1 = int(input())
print("ingrese una clave para insertar en el arbol:")
clave2 = int(input())
print("ingrese una clave para insertar en el arbol:")
clave3 = int(input())

raiz = None
raiz = insertar(raiz, clave1)
raiz = insertar(raiz, clave2)
raiz = insertar(raiz, clave3)

print("\nÁrbol antes de la rotación:")
imprimir_arbol(raiz)
diagnostico = diagnosticar(raiz)
print("\nDiagnóstico:", diagnostico)

        