"""
Enzo Etcheto

Dada una lista con nombres de personajes de la saga de Avengers
ordenados por nombre del superhéroes, de los cuales se conoce:
nombre del superhéroe, nombre del personaje (puede ser vacio),
grupo al que (perteneces puede ser vacio), año de aparición, por
ejemplo (Star Lord – Peter Quill – Guardianes de la galaxia - 1976).
Resolver las siguientes tareas:

a. Determinar si “Capitana Marvel” está en la lista y mostrar su
nombre de personaje;

b. Almacenar los superhéroes que pertenezcan al grupo
“Guardianes de la galaxia” en una cola e indicar cuantos son.

c. Mostrar de manera descendente los superhéroes que
pertenecen al grupo “Los cuatro fantásticos” y “Guardoanes de
la galaxia”.

d. Listar los superhéroes que tengan nombre de personajes cuyo
año de aparición sea posterior a 1960.

e. Hemos detectado que la superhéroe “Black Widow” está mal
cargada por un error de tipeo, figura como “Vlanck Widow”,
modifique dicho superhéroe para solucionar este problema.

f. Dada una lista auxiliar con los siguientes personajes (‘Black
Cat’, ‘Hulk’, ‘Rocket Racoonn’, ‘Loki’, complete el resto de la
información), agregarlos a la lista principal en el caso de no
estar cargados.

g. Mostrar todos los personajes que comienzan con C, P o S.

h. Cargue al menos 20 personajes a la lista.
"""

from clases import Cola

super_lista = [
    {"nombre": "Tony Stark", "personaje": "Iron Man", "grupo":"Los Vengadores","anio": "1956"},
    {"nombre": "Natasha Romanoff", "personaje": "Black Widow", "grupo":"Los Vengadores", "anio": "1998"},
    {"nombre": "Carol Danvers", "personaje": "Capitana Marvel", "grupo":"Los Vengadores", "anio": "1990"},
    {"nombre": "Stephen Strange", "personaje": "Doctor Strange", "grupo":"Los Vengadores", "anio": "1952"},
    {"nombre": "Peter Parker", "personaje": "Spider-Man", "grupo":"Los Vengadores", "anio": "1957"},
    {"nombre": "Wanda Maximoff", "personaje": "Scarlet Witch", "grupo":"Los Vengadores", "anio": "1975"},
    {"nombre": "Susan Storm", "personaje": "Mujer Invisible", "grupo":"4 Fantásticos", "anio": "1970"},
    {"nombre": "Reed Richards", "personaje": "Mr. Fantástico", "grupo":"4 Fantásticos","anio": "1972"},
    {"nombre": "Johnny Storm", "personaje": "Antorcha Humana", "grupo":"4 Fantásticos", "anio": "1973"},
    {"nombre": "Ben Grimm", "personaje": "La Mole", "grupo":"4 Fantásticos", "anio": "1979"},
    {"nombre": "Peter Quill ", "personaje": "Star Lord", "grupo":"Guardianes de la galaxia", "anio": "2000"},
    {"nombre": "Gamora", "personaje": "Gamora", "grupo":"Guardianes de la galaxia", "anio": "2003"},
    {"nombre": "Drax", "personaje": "El Destructor", "grupo":"Guardianes de la galaxia", "anio": "2000"},
    {"nombre": "Rocket Raccoon", "personaje": "Ranger Rocket", "grupo":"Guardianes de la galaxia", "anio": "2000"},
    {"nombre": "James Rhodes", "personaje": "War Machine", "grupo":"Los Vengadores", "anio": "1988"},
    {"nombre": "Hope van Dyne", "personaje": "Wasp", "grupo":"Los Vengadores", "anio": "1980"},
    {"nombre": "Bucky Barnes", "personaje": "Winter Soldier", "grupo":"Hydra", "anio": "1974"},
    {"nombre": "Scott Lang", "personaje": "Ant-Man", "grupo":"Los Vengadores", "anio": "1974"} 
]
#A
def buscar_personaje(lista, nombre_superheroe):
    for personaje in lista:
        if personaje["personaje"] == nombre_superheroe:
            return personaje["nombre"]
  
carols = buscar_personaje(super_lista, "Capitana Marvel")
print('El nombre de la capitana es:',carols)

#B 
cola_guardianes = Cola()
for personaje in super_lista:
    if personaje["grupo"] == "Guardianes de la galaxia":
        cola_guardianes.arrive(personaje["personaje"])
        
print("Los personajes de los guardianes son:",cola_guardianes.size())    

#C
Lista_guardianes = []
Lista_4fanta = []

for personaje in super_lista:
    if personaje["grupo"] == "4 Fantásticos":
        Lista_4fanta.append(personaje["nombre"])
    elif personaje["grupo"] == "Guardianes de la galaxia":
        Lista_guardianes.append(personaje["nombre"])
        
Lista_guardianes = sorted(Lista_guardianes, reverse=True)
Lista_4fanta = sorted(Lista_4fanta, reverse=True)

print("Los Guardianes de la galaxia")
for personaje in Lista_guardianes:
    print(personaje)
    
print("los 4 Fantásticos")
for personaje in Lista_4fanta:
    print(personaje)
    
#D

Lista_anio = []

for personaje_anio in super_lista:
    if personaje_anio["anio"] > "1960":
        Lista_anio.append(personaje_anio["personaje"])
        
print("Mas del 1960")
for personaje in Lista_anio:
    print(personaje)        
    
    
#E
for personaje in super_lista:
    if personaje["personaje"] == "Vlanck Widow":
        personaje["personaje"] = "Black Widow"
        
#F
List_Aux = ['Hulk', 'Black Cat' , 'Rocket Racoonn', 'Loki']

for personaje_aux in List_Aux:
    personaje_existente = False
    for personaje in super_lista:
        if personaje["personaje"] == personaje_aux:
            personaje_existente = True
    if not personaje_existente:
        super_lista.append({"nombre": "D", "personaje": personaje_aux, "grupo": "", "anio": ""})
 
print("Personajes actualizados")        
for personaje in super_lista:
    print(personaje)  
    
    
#g
List_iniciales = []
for personaje in super_lista:
    nombresuper = personaje["personaje"]
    if nombresuper[0] == "C" or nombresuper[0] == "P" or nombresuper[0] == "S":
        List_iniciales.append(nombresuper)
        
for personaje in List_iniciales:
    print(personaje)
    
