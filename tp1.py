def minimizar_suma_ponderada(batallas):
    prioridad = []
    for batalla in batallas:
        ratio = batalla[1] / batalla[0]
        prioridad.append(batalla)

    batallas_por_prioridad = sorted(prioridad, key=lambda x: x[1]/x[0], reverse=True)

    return batallas_por_prioridad