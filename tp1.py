#batallas = (tiempo, importancia)
def minimizar_suma_ponderada(batallas):
    ordenadas_por_prioridad = sorted(batallas, key = lambda x:x[0]/x[1])
    return ordenadas_por_prioridad
