from grafo1 import Grafo
"""Implementar sobre un grafo no dirigido los algoritmos necesario para dar solución a las si-
guientes tareas:
a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho,
baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;
b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la aris-
ta es la distancia entre los ambientes, se debe cargar en metros;
c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan
para conectar todos los ambientes;
d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para
determinar cuántos metros de cable de red se necesitan para conectar el router con el
Smart Tv.
"""

mi_grafo=Grafo(dirigido=False)

# a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho,
# baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;
mi_grafo.insert_vertice('cocina')
mi_grafo.insert_vertice('comedor')
mi_grafo.insert_vertice('cochera')
mi_grafo.insert_vertice('quincho')
mi_grafo.insert_vertice('banio 1')
mi_grafo.insert_vertice('banio 2')
mi_grafo.insert_vertice('habitacion 1')
mi_grafo.insert_vertice('habitacion 2')
mi_grafo.insert_vertice('sala de estar')
mi_grafo.insert_vertice('terraza')
mi_grafo.insert_vertice('patio')
# b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la aris-
# ta es la distancia entre los ambientes, se debe cargar en metros;

mi_grafo.insert_arist('cocina', 'comedor', 3)
mi_grafo.insert_arist('cocina', 'cochera', 5)


mi_grafo.insert_arist('comedor', 'cochera', 3)
mi_grafo.insert_arist('comedor', 'quincho', 5)

mi_grafo.insert_arist('cochera', 'quincho', 3)

mi_grafo.insert_arist('cocina', 'banio 1', 3)
mi_grafo.insert_arist('cocina', 'habitacion 1', 5)
mi_grafo.insert_arist('cocina', 'habitacion 2', 5)

mi_grafo.insert_arist('banio 1', 'habitacion 1', 3)
mi_grafo.insert_arist('banio 1', 'habitacion 2', 3)

mi_grafo.insert_arist('habitacion 1', 'habitacion 2', 3)

mi_grafo.insert_arist('habitacion 2', 'banio 2', 3)
mi_grafo.insert_arist('habitacion 2', 'sala de estar', 5)

mi_grafo.insert_arist('banio 2', 'sala de estar', 5)
mi_grafo.insert_arist('banio 2', 'quincho', 5)
mi_grafo.insert_arist('patio', 'quincho', 5)

mi_grafo.insert_arist('sala de estar', 'terraza', 3)
mi_grafo.insert_arist('sala de estar', 'patio', 3)

mi_grafo.insert_arist('terraza', 'patio', 3)
mi_grafo.insert_arist('terraza', 'cochera', 3)

mi_grafo.barrido()
# c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan
# para conectar todos los ambientes;
bosque, sumametros = mi_grafo.kruskal_peso()

for arbol in bosque:
    print('arbol')
    for nodo in arbol.split(';'):
        print(nodo)

print(f"Los metros necesarios de cables son {sumametros} metros")
print()
# d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para
# determinar cuántos metros de cable de red se necesitan para conectar el router con el
# Smart Tv.

print('Camino corto')
ori = 'habitacion 1'
des = 'sala de estar'
path=mi_grafo.has_path(ori,des)
origen = mi_grafo.search_vertice(ori)
destino = mi_grafo.search_vertice(des)
camino_mas_corto = None
cable=0
if(origen is not None and destino is not None):
    if path == True:
        camino_mas_corto = mi_grafo.dijkstra(ori, des, None)
        fin = des
        while camino_mas_corto.size() > 0:      
            value = camino_mas_corto.pop()
            if fin == value[0]:
                cable += value[1]  
                print(value[0],'Peso', value[1])
                fin = value[2]
            
        print(f'se necesitan {cable} metros de cable de red')
    else:
        print("No hay un camino entre", ori, "y", des)

