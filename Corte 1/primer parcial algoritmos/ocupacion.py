# ============================================================
#  Cívica Software  ·  TCK-4420  ·  Severidad P3
#  Sistema: RedAcopio  —  Reporte de ocupación
#  NO MODIFIQUE la seccion de datos ni el archivo de pruebas.
# ============================================================

# filas = puntos de acopio, columnas = dias de la semana
ocupacion = [
    [4, 2, 6, 1, 3, 0],
    [0, 5, 5, 2, 7, 1],
    [8, 1, 0, 4, 2, 6],
    [3, 3, 3, 0, 0, 5],
]

def total_por_punto(m):
    """Devuelve una lista con el total recogido por cada punto (fila)."""
    totales = []
    for fila in m:
        s = 0
        for v in fila:
            s += v
        totales.append(s)
    return totales



def total_por_dia(m):
    """Devuelve una lista con el total recogido cada dia (columna).
       BUG REPORTADO: entrega totales incorrectos."""
    totales = []
    for j in range(len(m[0])):          # <-- revise este recorrido
        s = 0
        for i in range(len(m)):   #se cambio el recorrido para que sume por columna
            s += m[i][j]          #cambiando los indices de las matrices y intercambiandolos
        totales.append(s)
    return totales


def dia_mas_flojo(m):
    """Devuelve el indice del dia con MENOR recoleccion total.
       PENDIENTE: implementar."""
    #encontrar el total por dia y luego buscar el minimo
    totales = total_por_dia(m)      #se busca el total del dia
    return totales.index(min(totales))    #se sortea para encontrar el minimo y se devuelve el indice del dia con menor recoleccion
    pass


def puntos_inactivos(m):
    """Devuelve cuantos registros estan en 0 (el punto no opero ese dia).
       PENDIENTE: implementar."""
    #contar los ceros en la matriz
    count = 0
    for fila in m:  #se cuentan los ceros en la matriz
        for v in fila:
            if v == 0: 
                count += 1  #se va sumando el contador cada vez que se encuentra un cero
    return count    #se retorna el contador con la cantidad de ceros encontrados

#imprimir el total de puntos, total por dia, dia mas flojo y puntos inactivos
print("Total por punto:", total_por_punto(ocupacion))
print("Total por dia:", total_por_dia(ocupacion))
print("Dia mas flojo:", dia_mas_flojo(ocupacion))
print("Puntos inactivos:", puntos_inactivos(ocupacion))

