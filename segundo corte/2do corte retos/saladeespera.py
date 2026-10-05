def sala_espera(llegadas):
    sillas = [None, None, None]  # Representa las 3 sillas disponibles
    cola_espera = []  # Cola de espera para los que no encuentran silla
    resultados = []  # Lista para almacenar el estado de la sala de espera

    for llegada in llegadas:
        # Verificar si hay una silla disponible
        if None in sillas:
            # Asignar la llegada a la primera silla disponible
            for i in range(len(sillas)):
                if sillas[i] is None:
                    sillas[i] = llegada
                    break
        else:
            # Si no hay sillas disponibles, agregar a la cola de espera
            cola_espera.append(llegada)

        # Registrar el estado actual de la sala de espera y la cola
        resultados.append((sillas.copy(), cola_espera.copy()))

    return resultados