'''
Dada una pila de películas de las que se conoce su título, estudio cinematográfico y año de es-
treno, desarrollar las funciones necesarias para resolver las siguientes actividades:

a. mostrar los nombre películas estrenadas en el año 2014;
b. indicar cuántas películas se estrenaron en el año 2018;
c. mostrar las películas de Marvel Studios estrenadas en el año 2016.

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
    
class PeliculaMarvel():

    def __init__(self, title, year):
        self.title = title
        self.year = year

    def get_title(self):
        return self.title

    def get_year(self):
        return self.year

    def __str__(self):
        return f'{self.title} - {self.year}'
    
    
def peliculas_2014 (pila):
    estreno_2014 = []
    aux = Pila()
    while not pila.is_empty():
        pelicula = pila.pop()
        if pelicula.get_year() == 2014:
            estreno_2014.append(pelicula.get_title())
        aux.push(pelicula)

    while not aux.is_empty():
        pila.push(aux.pop())

    return estreno_2014


def peliculas_2018(pila):
    contador = 0
    aux = Pila()
    while not pila.is_empty():
        pelicula = pila.pop()
        if pelicula.get_year() == 2018:
            contador += 1
        aux.push(pelicula)

    while not aux.is_empty():
        pila.push(aux.pop())

    return contador


def peliculas_2016(pila):
    estreno_2016 = []
    aux = Pila()
    while not pila.is_empty():
        pelicula = pila.pop()
        if pelicula.get_year() == 2016:
            estreno_2016.append(pelicula)
        aux.push(pelicula)

    while not aux.is_empty():
        pila.push(aux.pop())

    return estreno_2016


peli = [
    PeliculaMarvel('iron man 2', 2010),
    PeliculaMarvel('Avengers: Infinity War', 2018),
    PeliculaMarvel('Guardianes de la Galaxia', 2014),
    PeliculaMarvel('Capitán América y el Soldado del Invierno', 2014),
    PeliculaMarvel('Doctor Strange: hechicero supremo', 2016),
]

pelis = Pila()
for pelicula in peli:
    pelis.push(pelicula)

estrenos_2014 = peliculas_2014(pelis)
print("Películas estrenadas en 2014:")
for pelicula in estrenos_2014:
    print(pelicula)

print("     ")

estrenos_2018 = peliculas_2018(pelis)
print("Cantidad de películas estrenadas en 2018:", estrenos_2018)

print("     ")

estrenos_2016 = peliculas_2016(pelis)
print("Películas estrenadas en 2016:")
for pelicula in estrenos_2016:
    print(pelicula)