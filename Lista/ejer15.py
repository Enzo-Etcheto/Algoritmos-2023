# Enzo Etcheto

# Se cuenta con una lista de entrenadores Pokémon. De cada uno de estos se conoce: nombre, 
# cantidad de torneos ganados, cantidad de batallas perdidas y cantidad de batallas ganadas. 
# Y además la lista de sus Pokémons, de los cuales se sabe: nombre, nivel, tipo y subtipo. 
# Se pide resolver
# las siguientes actividades utilizando lista de lista implementando las funciones necesarias:

# a. obtener la cantidad de Pokémons de un determinado entrenador;
# b. listar los entrenadores que hayan ganado más de tres torneos;
# c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
# d. mostrar todos los datos de un entrenador y sus Pokémos;
# e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
# f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador
# (tipo y subtipo);
# g. el promedio de nivel de los Pokémons de un determinado entrenador;
# h. determinar cuántos entrenadores tienen a un determinado Pokémon;
# i. mostrar los entrenadores que tienen Pokémons repetidos;
# j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, 
# Terrakion o Wingull;
# k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
# como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se
# deberán mostrar los datos de ambos;
from lista_lista import Lista
from random import randint

class Entrenador():

    def __init__(self, nombre, ct_ganados=0, cb_perdidas=0, cb_ganadas=0):
        self.nombre = nombre
        self.ct_ganados = ct_ganados
        self.cb_perdidas = cb_perdidas
        self.cb_ganadas = cb_ganadas

    def __str__(self):
        return f'{self.nombre} --> ctg:{self.ct_ganados}-cbg{self.cb_ganadas}-cbp{self.cb_perdidas}'

class Pokemon():

    def __init__(self, nombre, tipo, nivel=1, subtipo=None):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo

    def __str__(self):
        return f'{self.nombre}-{self.nivel}-{self.tipo}-{self.subtipo}'


e1 = Entrenador('Juan', ct_ganados=randint(1, 10),cb_perdidas=randint(1, 10),cb_ganadas=randint(1,10))
e2 = Entrenador('Maria', ct_ganados=randint(1, 10),cb_perdidas=randint(1, 10),cb_ganadas=randint(1,10))
e3 = Entrenador('Ana', ct_ganados=randint(1, 10),cb_perdidas=randint(1, 10),cb_ganadas=randint(1,10))

entrenadores = [e1, e2, e3]

lista_entrenadores = Lista()

p1 = Pokemon('pikachu', 'electrico', randint(1, 20),'roca')
p2 = Pokemon('jolteon', 'electrico', randint(1, 20),'roca')
p3 = Pokemon('vaporeon', 'agua', randint(1, 20),'volador')
p4 = Pokemon('flareon', 'fuego', randint(1, 20),'planta')
p5 = Pokemon('leafeon', 'planta', randint(1, 20),'volador')
p6 = Pokemon('jolteon', 'electrico', randint(1, 20),'roca')
p7 = Pokemon('pikachu', 'electrico', randint(1, 20),'roca')
p8 = Pokemon('Tyrantrum', 'electrico', randint(1, 20),'roca')
pokemons = [p1, p2, p3, p4, p5, p6, p7, p8]

#! lista principal
for entrenador in entrenadores:
    lista_entrenadores.insert(entrenador, 'nombre')

#! lista secundaria
for pokemon in pokemons:
    numero_entrenador = randint(0, lista_entrenadores.size()-1)
    entrenador = lista_entrenadores.get_element_by_index(numero_entrenador)
    entrenador[1].insert(pokemon, 'nombre')


lista_entrenadores.barrido_entrenadores()
print()

#a. obtener la cantidad de Pokémons de un determinado entrenador;
pos = lista_entrenadores.search('Juan', 'nombre')
if pos is not None:
    valor = lista_entrenadores.get_element_by_index(pos)
    entrenador, sublista = valor[0], valor[1]
    print(f'{entrenador.nombre} tiene {sublista.size()} pokemons')

print()
#b. listar los entrenadores que hayan ganado más de tres torneos;
lista_entrenadores.barrido_cantidad_torneos_ganados(6)

print()
## c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados
mayor_cantidad = lista_entrenadores.get_element_by_index(0)[0].ct_ganados
pos_mayor = 0

for pos in range(1, lista_entrenadores.size()):
    entrenador = lista_entrenadores.get_element_by_index(pos)[0]
    if entrenador.ct_ganados > mayor_cantidad:
        pos_mayor = pos
        mayor_cantidad = entrenador.ct_ganados

valor = lista_entrenadores.get_element_by_index(pos_mayor)
entrenador, sublista = valor[0], valor[1]

if sublista.size() > 0:
    pokemon_mayor = sublista.get_element_by_index(0)
    for pos in range(1, sublista.size()):
        pokemon = sublista.get_element_by_index(pos)
        if pokemon.nivel > pokemon_mayor.nivel:
            pokemon_mayor = pokemon

print(f'El pokemon de mayor nivel del entrenador {entrenador.nombre} es {pokemon_mayor.nombre} {pokemon_mayor.nivel} ')

#d. mostrar todos los datos de un entrenador y sus Pokémos;

pos = lista_entrenadores.search('Maria', 'nombre')
if pos is not None:
    entrenador, sublista = lista_entrenadores.get_element_by_index(pos)
    print(f'Entrenador: {entrenador}')
    print(f'Pekemons:{sublista.barrido()}')
    
# e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
print('  ')
lista_entrenadores_aux = lista_entrenadores.obtener_ele()
for entrenador, sublista in lista_entrenadores_aux:
    porcentaje_victorias = (entrenador.cb_ganadas / (entrenador.cb_ganadas + entrenador.cb_perdidas)) * 100
    if porcentaje_victorias > 79:
        print(f'Entrenador con 79% de victorias: {entrenador}')
# f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador (tipo y subtipo);

for entrenador, sublista in lista_entrenadores_aux:
    sublista_aux = sublista.obtener_ele()
    for pokemon in sublista_aux:
        if pokemon.tipo == 'fuego' and pokemon.subtipo == 'planta':
            print(f'Entrenador con pokemones fuego Tipo planta: {entrenador.nombre}')
        elif pokemon.tipo == 'agua' and pokemon.subtipo == 'volador':
            print(f'Entrenador con pokemones agua tipo volador: {entrenador.nombre}')


# g. el promedio de nivel de los Pokémons de un determinado entrenador;
print('  ')
pos = lista_entrenadores.search('Maria', 'nombre')
if pos is not None:
    entrenador, sublista = lista_entrenadores.get_element_by_index(pos)
    acumulador_niveles = 0
    cantidad_pokemon = sublista.size()
    sublista_aux = sublista.obtener_ele()
    for pokemon in sublista_aux:
        acumulador_niveles += pokemon.nivel
    promedio_niveles = acumulador_niveles / cantidad_pokemon
    print(f'El promedio de nivel de los pokemones de {entrenador.nombre} es {promedio_niveles}')
# h. contador_entrenadores = 0
print('  ')
nombre_pokemon = 'pikachu'
contador_entrenadores = 0

for entrenador, sublista in lista_entrenadores_aux:
    sublista_aux = sublista.obtener_ele()
    for pokemon in sublista_aux:
        if pokemon.nombre == nombre_pokemon:
            contador_entrenadores += 1

print(f'{contador_entrenadores} entrenadores tienen al Pekemon {nombre_pokemon}')
# i. mostrar los entrenadores que tienen Pokémons repetidos;

contador_pokemon = {}
for entrenador, sublista in lista_entrenadores_aux:
    sublista_aux = sublista.obtener_ele()
    for pokemon in sublista_aux:
        if pokemon.nombre in contador_pokemon:
            contador_pokemon[pokemon.nombre] += 1
        else:
            contador_pokemon[pokemon.nombre] = 1
entrenadores_con_repetidos = []
for pokemon, cantidad in contador_pokemon.items():
    if cantidad > 1:
        for entrenador, sublista in lista_entrenadores_aux:
            sublista_aux = sublista.obtener_ele()
            for p in sublista_aux:
                if p.nombre == pokemon and entrenador not in entrenadores_con_repetidos:
                    entrenadores_con_repetidos.append(entrenador)
print('  ')                   

for entrenador in entrenadores_con_repetidos:
    print(f'Entrenadores con Pokemons repetidos:{entrenador.nombre}')
# j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum,  Terrakion o Wingull;
print('  ') 
nombres_pokemons_buscados = ['Tyrantrum', 'Terrakion', 'Wingull']
entrenadores_con_pokemon_buscado = []
for entrenador, sublista in lista_entrenadores_aux:
    sublista_aux = sublista.obtener_ele()
    for pokemon in sublista_aux:
        if pokemon.nombre in nombres_pokemons_buscados and entrenador not in entrenadores_con_pokemon_buscado:
            entrenadores_con_pokemon_buscado.append(entrenador)

for entrenador in entrenadores_con_pokemon_buscado:
    print(f'El entrenador que tiene alguno de los buscados es {entrenador.nombre}')
    
# k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
# como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se
# deberán mostrar los datos de ambos;
print(' ')
nombre_entrenador = input('Ingrese el nombre del entrenador: ')
nombre_pokemon = input('Ingrese el nombre del Pokemon: ')
encontrado = False
print('  ')
for entrenador, sublista in lista_entrenadores_aux:
    if entrenador.nombre == nombre_entrenador:
        sublista_aux = sublista.obtener_ele()
        for pokemon in sublista_aux:
            if pokemon.nombre == nombre_pokemon:
                encontrado = True
                print(f'Entrenador: {entrenador}')
                print(f'pokemon: {pokemon}')
                
        
if not encontrado:
    print('No se encontro el entrenador o el Pokemon')




