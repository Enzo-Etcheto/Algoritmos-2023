"""
El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u
otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos
objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con
ayuda de la fuerza” realizar las siguientes actividades:

a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no
queden más objetos en la mochila;

b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sa-
car para encontrarlo;

c. Utilizar un vector para representar la mochila.
"""

mochi = ["comida", "agua", "mapa", "linterna", "sable de luz", "comunicador"]

def extraer_mochila(mochila, indice=0, objetos=0):
    """Función recursiva que busca un sable de luz en la mochila de un jedi"""
    if len(mochila) == indice:
        return "mochila vacia"
    elif mochila[indice] == "sable de luz":
        return f"se encontro el sable y se sacaron {objetos} objetos"
    else:
        print("se extrajo un objeto de la mochila",mochila[indice])
        return extraer_mochila(mochila, indice + 1, objetos + 1)

print(extraer_mochila(mochi))
