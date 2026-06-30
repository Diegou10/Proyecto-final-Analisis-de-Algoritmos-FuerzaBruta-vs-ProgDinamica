import random

n = int(input("Ingrese la cantidad de ciudades: "))
matriz_distancias = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            matriz_distancias[i][j] = random.randint(50, 1000)
def calcular_ruta_pd(ciudad_actual, visitados, memoria):
    if len(visitados) == n:
        return matriz_distancias[ciudad_actual][0], visitados + [0]
    
    estado = (ciudad_actual, tuple(sorted(visitados)))
    if estado in memoria:
        return memoria[estado]
    
    min_dist = float('inf')
    mejor_ruta = []
    
    for siguiente in range(n):
        if siguiente not in visitados:
            dist, ruta = calcular_ruta_pd(siguiente, visitados + [siguiente], memoria)
            dist_total = matriz_distancias[ciudad_actual][siguiente] + dist
            
            if dist_total < min_dist:
                min_dist = dist_total
                mejor_ruta = ruta
                
    memoria[estado] = (min_dist, mejor_ruta)
    return min_dist, mejor_ruta

print(f"\n--- Iniciando cálculo de ruta para {n} ciudades (Programacion Dinámica) ---")
memoria_cache = {}
resultado_dist, resultado_ruta = calcular_ruta_pd(0, [0], memoria_cache)

print(f"Distancia mínima a recorrer encontrada : {resultado_dist} km")
formato_ruta = ["CIUDAD: " + str(c) for c in resultado_ruta]
print(f"Ruta optimizada según la distancia mínima encontrada: {' -> '.join(formato_ruta)}")