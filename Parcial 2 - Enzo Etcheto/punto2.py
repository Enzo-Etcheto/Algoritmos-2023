#Enzo Etcheto

# 2. Dado un grafo no dirigido con personajes de la saga Star Wars, implementar los
# algoritmos necesarios para resolver las siguientes tareas:
# a) cada vértice debe almacenar el nombre de un personaje, las aristas representan la
# cantidad de episodios en los que aparecieron juntos ambos personajes que se
# relacionan;
# b) hallar el árbol de expansión minino y determinar si contiene a Yoda;
# c) determinar cuál es el número máximo de episodio que comparten dos personajes,

from grafo1 import Grafo

mi_grafo=Grafo(dirigido=False)

mi_grafo.insert_vertice("Luke Skywalker")
mi_grafo.insert_vertice("Leia Organa")
mi_grafo.insert_vertice("Han Solo")
mi_grafo.insert_vertice("Darth Vader")
mi_grafo.insert_vertice("Yoda")
mi_grafo.insert_vertice("Boba Fett")
mi_grafo.insert_vertice("C-3PO")
mi_grafo.insert_vertice("Rey")
mi_grafo.insert_vertice("Kylo Ren")
mi_grafo.insert_vertice("Chewbacca")
mi_grafo.insert_vertice("R2-D2")
mi_grafo.insert_vertice("BB-8")


mi_grafo.insert_arist("Luke Skywalker","Leia Organa",3)
mi_grafo.insert_arist("Luke Skywalker","Han Solo",4)
mi_grafo.insert_arist("Leia Organa","Han Solo",2)
mi_grafo.insert_arist("Darth Vader","Han Solo",5)
mi_grafo.insert_arist("Darth Vader","Yoda",1)
mi_grafo.insert_arist("Boba Fett","Rey",1)
mi_grafo.insert_arist("C-3PO","R2-D2",8)
mi_grafo.insert_arist("Kylo Ren","BB-8",2)
mi_grafo.insert_arist("Han Solo","Chewbacca",6)


mi_grafo.barrido()

# b) hallar el árbol de expansión minino y determinar si contiene a Yoda;

bosque,control=mi_grafo.kruskal()

for arbol in bosque:
    print('arbol')
    for nodo in arbol.split(';'):
        print(nodo)

if control is not None:
    print('Esta yoda')
else:
    print('No esta Yoda')
    
# c) determinar cuál es el número máximo de episodio que comparten dos personajesy quienes son
mi_grafo.barrido_mayor()



