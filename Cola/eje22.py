'''
Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se conoce 
el nombre del personaje, el nombre del superhéroe y su género 
(Masculino M y FemeninoF) por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M},
{Natasha Romanoff, Black Widow, F}, etc., desarrollar un algoritmo que resuelva las siguientes actividades:
a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
b. mostrar los nombre de los superhéroes femeninos;
c. mostrar los nombres de los personajes masculinos;
d. determinar el nombre del superhéroe del personaje Scott Lang;
e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan
con la letra S;
f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre
de superhéroes.
'''

class Cola():
    """Clase cola"""
    def __init__(self):
        self.__elementos = []
   
    def arrive(self, value):
        self.__elementos.append(value)

    def atention(self):
        if self.size() > 0:
            return self.__elementos.pop(0)

    def size(self):
        return len(self.__elementos)

    def on_front(self):
        if self.size() > 0:
            return self.__elementos[0]

    def is_empty(self):
        return len(self.__elementos) == 0
    
    def move_to_end(self):
        if self.size() > 0:
            aux = self.atention()
            self.arrive(aux)
            return aux
        
        
def determina_nombre_personaje(cola, superheroe):
    cola_aux = Cola()
    nombre_personaje = None
    while not cola.is_empty():
        personaje = cola.atention()
        if personaje["superheroe"] == superheroe:
            nombre_personaje = personaje["nombre"]
        cola_aux.arrive(personaje)
    while not cola_aux.is_empty():
        cola.arrive(cola_aux.atention())
    return nombre_personaje

def muestra_superheroes_femeninos(cola):
    cola_aux = Cola()
    while not cola.is_empty():
        personaje = cola.atention()
        if personaje["genero"] == "F":
            print(personaje["superheroe"])
        cola_aux.arrive(personaje)
    while not cola_aux.is_empty():
        cola.arrive(cola_aux.atention())

def muestra_superheroes_masculinos(cola):
    cola_aux = Cola()
    while not cola.is_empty():
        personaje = cola.atention()
        if personaje["genero"] == "M":
            print(personaje["nombre"])
        cola_aux.arrive(personaje)
    while not cola_aux.is_empty():
        cola.arrive(cola_aux.atention())

def determina_superheroe_personaje(cola, personaje):
    cola_aux = Cola()
    nombre_superheroe = None
    while not cola.is_empty():
        superheroe = cola.atention()
        if superheroe["nombre"] == personaje:
            nombre_superheroe = superheroe["superheroe"]
        cola_aux.arrive(superheroe)
    while not cola_aux.is_empty():
        cola.arrive(cola_aux.atention())
    return nombre_superheroe


def muestra_nombre_con_S(cola):
    cola_aux = Cola()
    while not cola.is_empty():
        personaje = cola.atention()
        if personaje["nombre"][0] == "S" or personaje["superheroe"][0] == "S":
            print("Nombre:", personaje["nombre"])
            print("Superheroe:", personaje["superheroe"])
            print("Género:", personaje["genero"])
            print('  ')
        cola_aux.arrive(personaje)
    while not cola_aux.is_empty():
        cola.arrive(cola_aux.atention())

def verifica_personaje(cola, personaje):
    cola_aux = Cola()
    while not cola.is_empty():
        personaje_actual = cola.atention()
        if personaje_actual["nombre"] == personaje:
            return personaje_actual["superheroe"]
        cola_aux.arrive(personaje_actual)
    while not cola_aux.is_empty():
        cola.arrive(cola_aux.atention())
    return "El personaje no se encuentra"



super_lista = [
    {"nombre": "Tony Stark", "superheroe": "Iron Man", "genero": "M"},
    {"nombre": "Natasha Romanoff", "superheroe": "Black Widow", "genero": "F"},
    {"nombre": "Carol Danvers", "superheroe": "Capitana Marvel", "genero": "F"},
    {"nombre": "Stephen Strange", "superheroe": "Doctor Strange", "genero": "M"},
    {"nombre": "Peter Parker", "superheroe": "Spider-Man", "genero": "M"},
    {"nombre": "Wanda Maximoff", "superheroe": "Scarlet Witch", "genero": "F"},
    {"nombre": "Scott Lang", "superheroe": "Ant-Man", "genero": "M"}  
]

cola_lista = Cola()
for super in super_lista:
    cola_lista.arrive(super)
 
nombre_perso = determina_nombre_personaje(cola_lista,"Capitana Marvel")
print('El nombre de la Capitana Marvel es:', nombre_perso)

print('  ')

print('Supeheroes femeninos')
muestra_superheroes_femeninos(cola_lista)

print('  ')

print('Personajes Masculinos')
muestra_superheroes_masculinos(cola_lista)

print('  ')

nombre_super = determina_superheroe_personaje(cola_lista,"Scott Lang")
print('El nombre de superheroe de Scott Lang es:', nombre_super)

print('  ')

print('Nombre de personaje o Superheroes con "S"')
muestra_nombre_con_S(cola_lista)


nombre_carol = verifica_personaje(cola_lista, "Carol Danvers")
if nombre_carol != "El personaje no se encontro":
    print("Carol Danvers se encuentra en la cola y su nombre de superheroe es:", nombre_carol)
else:
    print("Carol Danvers no se encontro")

