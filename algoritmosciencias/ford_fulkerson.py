def dfs(grafo, capacidad, origen, sumidero, visitados, flujo):
    if origen == sumidero:
        return flujo

    visitados.add(origen)

    for vecino in grafo[origen]:
        capacidad_residual = capacidad[(origen, vecino)]

        if vecino not in visitados and capacidad_residual > 0:

            flujo_minimo = min(flujo, capacidad_residual)

            resultado = dfs(
                grafo,
                capacidad,
                vecino,
                sumidero,
                visitados,
                flujo_minimo
            )

            if resultado > 0:
                capacidad[(origen, vecino)] -= resultado
                capacidad[(vecino, origen)] += resultado

                return resultado

    return 0


def ford_fulkerson(g):
    origen = 'S'
    sumidero = 'T'

    flujo_maximo = 0

    while True:
        visitados = set()

        flujo = dfs(
            g.grafo,
            g.capacidad,
            origen,
            sumidero,
            visitados,
            float('inf')
        )

        if flujo == 0:
            break

        flujo_maximo += flujo

    return flujo_maximo