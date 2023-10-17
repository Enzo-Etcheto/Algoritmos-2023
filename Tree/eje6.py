from arbol import BinaryTree, get_value_from_file
# Dado un archivo con todos los Jedi, de los que se cuenta con: nombre, especie, año de nacimiento,
# color de sable de luz, ranking (Jedi Master, Jedi Knight, Padawan) y maestro, los últimos
# tres campos pueden tener más de un valor. Escribir las funciones necesarias para resolver las
# siguientes consignas:
# a. crear tres árboles de acceso a los datos: por nombre, ranking y especie;
# b. realizar un barrido inorden del árbol por nombre y ranking;
# c. realizar un barrido por nivel de los árboles por ranking y especie;
# d. mostrar toda la información de Yoda y Luke Skywalker;
# e. mostrar todos los Jedi con ranking “Jedi Master”;
# f. listar todos los Jedi que utilizaron sabe de luz color verde;
# g. listar todos los Jedi cuyos maestros están en el archivo;
# h. mostrar todos los Jedi de especie “Togruta” o “Cerean”;
# i. listar los Jedi que comienzan con la letra A y los que contienen un “-” en su nombre.
import os
# ¡Utilice esta forma de abrir el archivo porque no me lo encuentra en el mismo directorio!
current_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_directory, "Jedis.txt")

with open(file_path, 'r') as file_jedi:
    read_lines = file_jedi.readlines()
# file_jedi = open('Jedis.txt')
# read_lines = file_jedi.readlines()
file_jedi.close()

# a. crear tres árboles de acceso a los datos: por nombre, ranking y especie;
name_tree = BinaryTree()
specie_tree = BinaryTree()
ranking_tree = BinaryTree()
read_lines.pop(0)
for index, linea_jedi in enumerate(read_lines):
    jedi = linea_jedi.split(';')
    jedi.pop() 
    name_tree.insert_node(jedi[0], index+2)
    specie_tree.insert_node(jedi[2], index+2)
    ranking_tree.insert_node(jedi[1], index+2)
    
# b. realizar un barrido inorden del árbol por nombre y ranking;
name_tree.inorden()
print()
ranking_tree.inorden()

# c. realizar un barrido por nivel de los árboles por ranking y especie;

# print('ranking')
# ranking_tree.by_level()
# print('especie')
# specie_tree.by_level()
# d. mostrar toda la información de Yoda y Luke Skywalker;
# pos = name_tree.search('yoda')
# if pos:
#     print(get_value_from_file('jedis.txt', pos.other_values))
# else:
#     print('no esta en la lista')
    
# pos = name_tree.search('luke skywalker')
# if pos:
#     print(get_value_from_file('jedis.txt', pos.other_values))
# else:
    # print('no esta en la lista')    

# e. mostrar todos los Jedi con ranking “Jedi Master”;
print()
print('jedi masters ')
name_tree.inorden_jedi_master('jedis.txt', 'jedi master')

# f. listar todos los Jedi que utilizaron sabe de luz color verde;
print()
print('jedis con sable verde ')
name_tree.inorden_file_lightsaber('jedis.txt', 'green')
# g. listar todos los Jedi cuyos maestros están en el archivo;
print()
print('jedis con maestros')
name_tree.inorden_have_master(('jedis.txt'))
# h. mostrar todos los Jedi de especie “Togruta” o “Cerean”;
print()
print('Jedis de especie “Togruta” o “Cerean”')
name_tree.inorden_specie('jedis.txt')
# i. listar los Jedi que comienzan con la letra A y los que contienen un “-” en su nombre.
print()
print('Jedis que empiezan con A')
name_tree.inorden_start_with_jedi('A')
print()
print('Jedis que contienen "-"')
name_tree.inorden_with_guion('jedis.txt')