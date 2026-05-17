class Grafo:
    def __init__(self):
        self.grafo = {}
        self.capacidad = {}

    def agregar_arista(self, u, v, capacidad):
        # Lista de adyacencia
        if u not in self.grafo:
            self.grafo[u] = []

        if v not in self.grafo:
            self.grafo[v] = []

        # Agregar conexiones
        self.grafo[u].append(v)
        self.grafo[v].append(u)  # residual

        # Capacidad
        self.capacidad[(u, v)] = capacidad
        self.capacidad[(v, u)] = 0