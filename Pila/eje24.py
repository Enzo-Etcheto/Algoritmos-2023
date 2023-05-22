'''
Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de
su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones
necesarias para resolver las siguientes actividades:

a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posi-
ción uno la cima de la pila;

b. determinar los personajes que participaron en más de 5 películas de la saga, además indi-
car la cantidad de películas en la que aparece;

c. determinar en cuantas películas participo la Viuda Negra (Black Widow);

d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.
'''
class Pila ():
    """Stack class"""
    def __init__(self):
        self.elements = []

    def push(self, value):
        self.elements.append(value)
        
    def pop(self):
        if self.size() > 0:
            dato = self.elements.pop()
            return dato

    def is_empty(self):
        return len(self.elements) == 0

    def size(self):
        return len(self.elements)
    
    
        
def rocket_y_groot(pila):
    posicion = 1
    aux = Pila()  
    while not pila.is_empty():
        personaje = pila.pop()
        if personaje["nombre"] == "Rocket Raccoon":
            print("La posición de Rocket Raccoon es:", posicion)
        if personaje["nombre"] == "Groot":
            print("La posición de Groot es:", posicion)
        aux.push(personaje)
        posicion += 1

    while not aux.is_empty():
        pila.push(aux.pop())


def personajes_mas_5_peliculas(pila):
    personajes = []
    aux = Pila() 
    while not pila.is_empty():
        personaje = pila.pop()
        if personaje["peli"] >= 5:
            personajes.append(personaje)
        aux.push(personaje)

    while not aux.is_empty():
        pila.push(aux.pop())
    return personajes


def pelis_Viuda(pila):
    contador = 0
    aux = Pila()  
    while not pila.is_empty():
        personaje = pila.pop()
        if personaje["nombre"] == "Black Widow":
            contador = personaje["peli"]
        aux.push(personaje)

    while not aux.is_empty():
        pila.push(aux.pop())
    return contador


def personajes_con_iniciales(pila, iniciales):
    personajes = []
    aux = Pila()  
    while not pila.is_empty():
        personaje = pila.pop()
        if personaje["nombre"][0].upper() in iniciales:
            personajes.append(personaje)
        aux.push(personaje)
    
    while not aux.is_empty():
        pila.push(aux.pop())
    return personajes

pelis=[ {"nombre": "Groot", "peli": 3},
    {"nombre": "Rocket Raccoon", "peli": 5},
    {"nombre": "Black Widow", "peli": 4},
    {"nombre": "Iron man", "peli": 8},
    {"nombre": "Hulk", "peli": 6},
    {"nombre": "Ultron", "peli": 1},
    {"nombre": "Capitan America", "peli": 7}
]

MCU_Pila = Pila()
for pelicula in pelis:
    MCU_Pila.push(pelicula)
    
rocket_y_groot(MCU_Pila)

print("     ")

mas_de_5 = personajes_mas_5_peliculas(MCU_Pila)
print("Personajes con más de 5 películas:")
for pers in mas_de_5:
    print( pers["nombre"], "- Películas:", pers["peli"])

print("     ")

peliblackwidow = pelis_Viuda(MCU_Pila)
print("Black Widow participó en", peliblackwidow , "películas")

print("     ")

personajes_ini = personajes_con_iniciales(MCU_Pila, ['C', 'D', 'G'])
print("Personajes con nombres que empiezan con C, D y G:")
for personajes in personajes_ini:
    print(personajes["nombre"])