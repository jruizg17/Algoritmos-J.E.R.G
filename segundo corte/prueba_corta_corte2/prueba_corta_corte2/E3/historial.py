# ============================================================
#  Prueba corta · Segundo corte · EJERCICIO 3  (25 puntos)
#  Tema: pilas
#  Sistema: PrestaLab — historial de acciones del operador
#
#  NO MODIFIQUE el archivo pruebas_e3.py
#  Ejecute:   python3 pruebas_e3.py
# ============================================================


def historial_final(acciones):
    pila = []
    for a in acciones:
        if a == "DESHACER":
            if pila: 
                pila.pop()
        else:
            pila.append(a)
    return pila


def profundidad_maxima(acciones):

    pila= []
    max_profundidad= 0
    for a in acciones:
        if a == "DESHACER":
            if pila:
                pila.pop()
        else:
            pila.append(a)
            max_profundidad = max(max_profundidad, len(pila))
    return max_profundidad


