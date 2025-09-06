#CODIGO A CHEQUEAR
import time
import numpy as np

def leer_entrada(ruta):
    datos = []
    with open(ruta) as f:
        for linea in f:
            tiempo, batalla = map(int, linea.strip().split())
            datos.append((tiempo, batalla))
    return datos 

def mediciones(datos, reps_para_promedio = 10, algoritmo_greedy = None):
    tiempos = []
    for _ in range(reps_para_promedio):
        inicio = time.perf_counter()
        algoritmo_greedy(datos)
        final = time.perf_counter()
        tiempos.appen(fin-inicio)
    return sum(tiempos)/len(tiempos)

#para los graficos despues:

def guardar_datos(ruta, datos):
    with open(ruta, 'w', newline = '', encodign='utf-8') as archivo:
        escritor = csv.writer(archivo)
        for linea in datos:
            escritor.writerow(linea)
