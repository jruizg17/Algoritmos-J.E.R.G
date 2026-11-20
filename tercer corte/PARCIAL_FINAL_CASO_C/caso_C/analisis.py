# ============================================================
#  analisis.py · CASO C · PARTE F del parcial  (10 puntos)
#  TurnoJusto — Atencion de solicitudes estudiantiles
#
#  VERIFICACION CRUZADA
#  Esta es la MISMA logica de Sistema::mejorSeleccion, escrita en el otro
#  lenguaje. El verificador compara los dos resultados: si no coinciden,
#  uno de los dos esta mal y el parcial no cierra.
#
#  MODIFIQUE SOLO ESTE ARCHIVO.  NO TOQUE pruebas.py
# ============================================================


def mejor_seleccion(codigos, pesos, valores, capacidad):
    """Devuelve la lista ORDENADA de codigos de la seleccion de mayor
       valor total que no pasa de 'capacidad'.

       codigos[i], pesos[i] y valores[i] describen el mismo punto.
       Cada punto se lleva o no se lleva. Si hay empate en valor, la
       seleccion con MENOS puntos.

       Debe dar exactamente el mismo resultado que la version en C++.

       PENDIENTE: implementar con recursion de tomar / no tomar y poda."""
       
    def _mejor_seleccion(i, capacidad):
        if i == len(codigos):
            return 0, []
        valor_sin_i, seleccion_sin_i = _mejor_seleccion(i + 1, capacidad)
        if pesos[i] <= capacidad:
            valor_con_i, seleccion_con_i = _mejor_seleccion(i + 1, capacidad - pesos[i])
            valor_con_i += valores[i]
            seleccion_con_i = [codigos[i]] + seleccion_con_i
            if valor_con_i > valor_sin_i or (valor_con_i == valor_sin_i and len(seleccion_con_i) < len(seleccion_sin_i)):
                return valor_con_i, seleccion_con_i
        return valor_sin_i, seleccion_sin_i

    _, mejor_seleccion_codigos = _mejor_seleccion(0, capacidad)
    return sorted(mejor_seleccion_codigos)