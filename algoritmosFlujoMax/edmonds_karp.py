from collections import deque


def bfs(grafo, capacidad, origen, sumidero, padre):
    visitados = set()
    cola = deque()

    cola.append(origen)
    visitados.add(origen)

    while cola:
        u = cola.popleft()

        for v in grafo[u]:

            if v not in visitados and capacidad[(u, v)] > 0:
                cola.append(v)
                visitados.add(v)
                padre[v] = u

                if v == sumidero:
                    return True

    return False


def edmonds_karp(g):
    origen = 'S'
    sumidero = 'T'

    padre = {}

    flujo_maximo = 0

    while bfs(g.grafo, g.capacidad, origen, sumidero, padre):

        flujo_camino = float('inf')
        s = sumidero

        while s != origen:
            flujo_camino = min(
                flujo_camino,
                g.capacidad[(padre[s], s)]
            )
            s = padre[s]

        flujo_maximo += flujo_camino

        v = sumidero

        while v != origen:
            u = padre[v]

            g.capacidad[(u, v)] -= flujo_camino
            g.capacidad[(v, u)] += flujo_camino

            v = padre[v]

    return flujo_maximo