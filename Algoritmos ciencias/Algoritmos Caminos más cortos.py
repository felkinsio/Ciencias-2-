
import time
import random
import heapq
import numpy as np

# ----------------------------
# Generador de grafos
# ----------------------------
def generar_grafo(n, densidad=0.3, pesos_negativos=False):
    grafo = {i: [] for i in range(n)}

    for i in range(n):
        for j in range(n):
            if i != j and random.random() < densidad:
                peso = random.randint(1, 10)
                if pesos_negativos and random.random() < 0.2:
                    peso *= -1
                grafo[i].append((j, peso))

    return grafo


# ----------------------------
# Dijkstra
# ----------------------------
def dijkstra(grafo, inicio):
    dist = {nodo: float('inf') for nodo in grafo}
    dist[inicio] = 0
    pq = [(0, inicio)]

    while pq:
        d, nodo = heapq.heappop(pq)

        if d > dist[nodo]:
            continue

        for vecino, peso in grafo[nodo]:
            nueva = d + peso
            if nueva < dist[vecino]:
                dist[vecino] = nueva
                heapq.heappush(pq, (nueva, vecino))

    return dist


# ----------------------------
# Bellman-Ford
# ----------------------------
def bellman_ford(grafo, inicio):
    dist = {nodo: float('inf') for nodo in grafo}
    dist[inicio] = 0

    for _ in range(len(grafo) - 1):
        for nodo in grafo:
            for vecino, peso in grafo[nodo]:
                if dist[nodo] + peso < dist[vecino]:
                    dist[vecino] = dist[nodo] + peso

    # detectar ciclos negativos
    for nodo in grafo:
        for vecino, peso in grafo[nodo]:
            if dist[nodo] + peso < dist[vecino]:
                return None  # ciclo negativo

    return dist


# ----------------------------
# Floyd-Warshall
# ----------------------------
def floyd_warshall(grafo):
    n = len(grafo)
    dist = np.full((n, n), float('inf'))

    for i in range(n):
        dist[i][i] = 0

    for nodo in grafo:
        for vecino, peso in grafo[nodo]:
            dist[nodo][vecino] = peso

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


# ----------------------------
# Comparador de eficiencia
# ----------------------------
def comparar_algoritmos(n, densidad=0.3, negativos=False):
    grafo = generar_grafo(n, densidad, negativos)

    print(f"\n--- Grafo con {n} nodos ---")

    # Dijkstra
    if not negativos:
        inicio = time.time()
        dijkstra(grafo, 0)
        fin = time.time()
        print(f"Dijkstra: {fin - inicio:.6f} segundos")
    else:
        print("Dijkstra: no aplicable (pesos negativos)")

    # Bellman-Ford
    inicio = time.time()
    bellman_ford(grafo, 0)
    fin = time.time()
    print(f"Bellman-Ford: {fin - inicio:.6f} segundos")

    # Floyd-Warshall (solo para grafos pequeños)
    if n <= 200:
        inicio = time.time()
        floyd_warshall(grafo)
        fin = time.time()
        print(f"Floyd-Warshall: {fin - inicio:.6f} segundos")
    else:
        print("Floyd-Warshall: omitido (muy costoso)")


# ----------------------------
# Ejecución de pruebas
# ----------------------------
if __name__ == "__main__":
    tamaños = [10, 50, 100, 200]

    for n in tamaños:
        comparar_algoritmos(n, densidad=0.3, negativos=False)

    print("\n--- PRUEBA CON PESOS NEGATIVOS ---")
    comparar_algoritmos(50, densidad=0.3, negativos=True)
