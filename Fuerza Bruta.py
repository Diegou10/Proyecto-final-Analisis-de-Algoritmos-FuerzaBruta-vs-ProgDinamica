import random

n = int(input("Ingrese la cantidad de ciudades: "))
matriz_distancias = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            matriz_distancias[i][j] = random.randint(50, 1000)
def calcular_ruta_fb(ciudad_actual, visitados):
    if len(visitados) == n:
        return matriz_distancias[ciudad_actual][0], visitados + [0]
    
    min_dist = float('inf')
    mejor_ruta = []
    
    for siguiente in range(n):
        if siguiente not in visitados:
            dist, ruta = calcular_ruta_fb(siguiente, visitados + [siguiente])
            dist_total = matriz_distancias[ciudad_actual][siguiente] + dist
            
            if dist_total < min_dist:
                min_dist = dist_total
                mejor_ruta = ruta
                
    return min_dist, mejor_ruta

print(f"\n--- Iniciando cálculo de ruta para {n} ciudades (Fuerza Bruta) ---")
resultado_dist, resultado_ruta = calcular_ruta_fb(0, [0])

print(f"Distancia mínima a recorrer encontrada: {resultado_dist} km")
formato_ruta = ["CIUDAD: " + str(c) for c in resultado_ruta]
print(f"Ruta optimizada según la distancia mínima encontrada: {' -> '.join(formato_ruta)}")