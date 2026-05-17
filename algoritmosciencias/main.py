#Kevin Daniel Agudelo Sotelo - 20222020125 
#Santiago Alejandro Guada Bohorquez - 20231020182 
#Johan Felipe Pinzon Garcia - 20222020176 
#Andres felipe correa mendez - 20221020141

from grafo import Grafo
from ford_fulkerson import ford_fulkerson
from edmonds_karp import edmonds_karp
import copy

# Crear grafo
g = Grafo()

#grafo de la imagen del enunciado hecha en clase
g.agregar_arista('S', 'V1', 17)
g.agregar_arista('S', 'V2', 14)
g.agregar_arista('S', 'V3', 14)
g.agregar_arista('S', 'V4', 9)

g.agregar_arista('V1', 'V5', 5)
g.agregar_arista('V1', 'V6', 7)
g.agregar_arista('V1', 'V2', 3)

g.agregar_arista('V2', 'V6', 4)
g.agregar_arista('V2', 'V7', 5)

g.agregar_arista('V5', 'V10', 17)

g.agregar_arista('V6', 'V5', 10)
g.agregar_arista('V6', 'V10', 11)

g.agregar_arista('V3', 'V7', 4)
g.agregar_arista('V3', 'V8', 7)
g.agregar_arista('V3', 'V4', 5)

g.agregar_arista('V4', 'V8', 7)
g.agregar_arista('V4', 'V9', 8)

g.agregar_arista('V7', 'V8', 2)
g.agregar_arista('V7', 'V11', 7)

g.agregar_arista('V8', 'V11', 15)

g.agregar_arista('V9', 'V11', 9)

g.agregar_arista('V11', 'V10', 6)

g.agregar_arista('V10', 'T', 25)
g.agregar_arista('V11', 'T', 29)

# Copias del grafo
g1 = copy.deepcopy(g)
g2 = copy.deepcopy(g)

# Ejecutar algoritmos
print("Ford-Fulkerson:")
print(flujo_ff := ford_fulkerson(g1))

print("\nEdmonds-Karp:")
print(flujo_ek := edmonds_karp(g2))