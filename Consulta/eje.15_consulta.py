"""Se requiere implementar un grafo para almacenar las siete maravillas arquitectónicas moder-
nas y naturales del mundo, para lo cual se deben tener en cuenta las siguientes actividades:
a. de cada una de las maravillas se conoce su nombre, país de ubicación (puede ser más de
uno en las naturales) y tipo (natural o arquitectónica); 
b. cada una debe estar relacionada con las otras seis de su tipo, para lo que se debe almacenar
la distancia que las separa;
c. hallar el árbol de expansión mínimo de cada tipo dinsert_ariste las maravillas;
d. determinar si existen países que dispongan de maravillas arquitectónicas y naturales;
e. determinar si algún país tiene más de una maravilla del mismo tipo;
f. deberá utilizar un grafo no dirigido.
"""
from grafo1 import Grafo
from grafo1 import maravilla
mi_grafo = Grafo(dirigido=False)
# a. de cada una de las maravillas se conoce su nombre, país de ubicación (puede ser más de
# uno en las naturales) y tipo (natural o arquitectónica);
mi_grafo.insert_vertice("Gran Muralla China",criterio=['china','Arquitectónica'])
mi_grafo.insert_vertice("Machu Picchu", criterio=["Perú", "Arquitectónica"])
mi_grafo.insert_vertice("Cristo Redentor",criterio=[ "Brasil", "Arquitectónica"])
mi_grafo.insert_vertice("Coliseo Romano", criterio=["Italia", "Arquitectónica"])
mi_grafo.insert_vertice("Chichén Itzá",criterio=[ "México", "Arquitectónica"])
mi_grafo.insert_vertice("Petra",criterio=["Jordania", "Arquitectónica"])
mi_grafo.insert_vertice("Parque Nacional de Yellowstone",criterio=[ "Estados Unidos", "Natural"])
mi_grafo.insert_vertice("Gran Barrera de Coral", criterio=["Australia", "Natural"])
mi_grafo.insert_vertice("Monte Everest",criterio=[ "Nepal/Tíbet", "Natural"])
mi_grafo.insert_vertice("Cataratas del Iguazú",criterio= ["Argentina/Brasil", "Natural"])
mi_grafo.insert_vertice("Parque Nacional de Banff",criterio=["Canadá "," Natural"])
mi_grafo.insert_vertice("Monte Kilimanjaro ",criterio=["Tanzania","Natural"])

# list_maravillas = [maravilla("Gran Muralla China",'china','Arquitectónica'),
# maravilla("Machu Picchu", "Perú", "Arquitectónica"),
# maravilla("Cristo Redentor", "Brasil", "Arquitectónica"),
# maravilla("Coliseo Romano", "Italia", "Arquitectónica"),
# maravilla("Chichén Itzá", "México", "Arquitectónica"),
# maravilla("Petra","Jordania", "Arquitectónica"),
# maravilla("Parque Nacional de Yellowstone", "Estados Unidos", "Natural"),
# maravilla("Gran Barrera de Coral", "Australia", "Natural"),
# maravilla("Monte Everest", "Nepal/Tíbet", "Natural"),
# maravilla("Cataratas del Iguazú","Argentina/Brasil", "Natural"),
# maravilla("Parque Nacional de Banff","Canadá "," Natural"),
# maravilla("Monte Kilimanjaro ","Tanzania","Natural")]

# for i in list_maravillas:
#     mi_grafo.insert_vertice(i.nombre,i)
    
# b. cada una debe estar relacionada con las otras seis de su tipo, para lo que se debe almacenar
# la distancia que las separa;
mi_grafo.insert_arist("Gran Muralla China", "Machu Picchu", 150)
mi_grafo.insert_arist("Gran Muralla China", "Cristo Redentor", 200)
mi_grafo.insert_arist("Gran Muralla China", "Coliseo Romano", 250)
mi_grafo.insert_arist("Gran Muralla China", "Chichén Itzá", 180)
mi_grafo.insert_arist("Gran Muralla China", "Petra", 220)
mi_grafo.insert_arist("Gran Muralla China", "Parque Nacional de Yellowstone", 350)
mi_grafo.insert_arist("Machu Picchu", "Cristo Redentor", 180)
mi_grafo.insert_arist("Machu Picchu", "Coliseo Romano", 210)
mi_grafo.insert_arist("Machu Picchu", "Chichén Itzá", 160)
mi_grafo.insert_arist("Machu Picchu", "Petra", 200)
mi_grafo.insert_arist("Machu Picchu", "Parque Nacional de Yellowstone", 280)
mi_grafo.insert_arist("Cristo Redentor", "Coliseo Romano", 130)
mi_grafo.insert_arist("Cristo Redentor", "Chichén Itzá", 170)
mi_grafo.insert_arist("Cristo Redentor", "Petra", 230)
mi_grafo.insert_arist("Cristo Redentor", "Parque Nacional de Yellowstone", 300)
mi_grafo.insert_arist("Coliseo Romano", "Chichén Itzá", 190)
mi_grafo.insert_arist("Coliseo Romano", "Petra", 220)
mi_grafo.insert_arist("Coliseo Romano", "Parque Nacional de Yellowstone", 270)
mi_grafo.insert_arist("Chichén Itzá", "Petra", 250)
mi_grafo.insert_arist("Chichén Itzá", "Parque Nacional de Yellowstone", 320)
mi_grafo.insert_arist("Petra", "Parque Nacional de Yellowstone", 180)
mi_grafo.insert_arist("Gran Barrera de Coral", "Monte Everest", 200)
mi_grafo.insert_arist("Gran Barrera de Coral", "Cataratas del Iguazú", 250)
mi_grafo.insert_arist("Gran Barrera de Coral", "Parque Nacional de Banff", 280)
mi_grafo.insert_arist("Monte Everest", "Cataratas del Iguazú", 190)
mi_grafo.insert_arist("Monte Everest", "Parque Nacional de Banff", 220)
mi_grafo.insert_arist("Cataratas del Iguazú", "Parque Nacional de Banff", 260)
mi_grafo.insert_arist("Monte Kilimanjaro", "Gran Barrera de Coral", 150)
mi_grafo.insert_arist("Monte Kilimanjaro", "Monte Everest", 180)
mi_grafo.insert_arist("Monte Kilimanjaro", "Cataratas del Iguazú", 210)
mi_grafo.insert_arist("Monte Kilimanjaro", "Parque Nacional de Banff", 240)

mi_grafo.barrido()
# c. hallar el árbol de expansión mínimo de cada tipo de las maravillas;
bosque_arquitectónica=mi_grafo.kruskal_maravilla("Arquitectónica")
bosque_natural=mi_grafo.kruskal_maravilla('Natural')
print('Arquitectonica')
for arbol in bosque_arquitectónica:
    print(arbol)

print()
print(bosque_natural)
for arbol in bosque_natural:
    print(arbol)

# d. determinar si existen países que dispongan de maravillas arquitectónicas y naturales;
# e. determinar si algún país tiene más de una maravilla del mismo tipo;
# f. deberá utilizar un grafo no dirigido.

