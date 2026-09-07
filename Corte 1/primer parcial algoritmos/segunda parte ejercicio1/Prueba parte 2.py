# ============================================================
#  Cívica Software  ·  TCK-5510  ·  Severidad P3
#  Sistema: RedAcopio  —  Mapa de cobertura de rutas
#  NO MODIFIQUE la matriz de datos ni el archivo de pruebas.
# ============================================================

# filas = rutas del camion, columnas = zonas del barrio
# cada celda = kilos recogidos por esa ruta en esa zona
cobertura = [
    [5, 0, 3, 0, 2, 4, 0],
    [0, 0, 7, 0, 1, 0, 6],
    [2, 0, 0, 0, 4, 3, 1],
    [0, 0, 5, 0, 0, 8, 2],
]

def total_por_ruta(m):
    """Devuelve una lista con el total recogido por cada ruta (fila)."""
    totales = []
    for fila in m:
        s = 0
        for v in fila:
            s += v
        totales.append(s)
    return totales


def cobertura_por_zona(m):

    totales = []
    for j in range(len(m[0])):          # se quito el -1 para que tome todas las columnas
        s = 0
        for i in range(len(m)):
            s += m[i][j]
        totales.append(s)
    return totales


def ruta_mas_productiva(m):
    
    max_kilos = -1
    ruta_max = -1
    for i in range(len(m)):
        s = sum(m[i])  # suma de kilos recogidos por la ruta i
        if s > max_kilos:
            max_kilos = s  #se usa sum para obtener la suma de las filas y poder compararlas y no comparar columnas
            ruta_max = i
    return ruta_max
    pass


def zonas_sin_cubrir(m):

    count = 0
    for j in range(len(m[0])):
        cubierta = False
        for i in range(len(m)):
            if m[i][j] > 0:     
                cubierta = True #se usa para saber si al menos se paso una vez en la ruta
                break
        if not cubierta:
            count += 1   #se usa contador para contar cuantas zonas no tuvieron una ruta pero que no arroje en que columnas es sino la cantidad
    return count

#imprimir resultados de prueba
print("total por ruta:", total_por_ruta(cobertura))
print("cobertura por zona:", cobertura_por_zona(cobertura))
print("ruta más productiva:", ruta_mas_productiva(cobertura))
print("zonas sin cubrir:", zonas_sin_cubrir(cobertura))
