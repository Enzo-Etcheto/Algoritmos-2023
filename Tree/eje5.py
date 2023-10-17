from arbol import BinaryTree
# Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Universe (MCU),
# desarrollar un algoritmo que contemple lo siguiente:
# a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo booleano que 
# indica si es un héroe o un villano, True y False respectivamente;
# b. listar los villanos ordenados alfabéticamente;
# c. mostrar todos los superhéroes que empiezan con C;
# d. determinar cuántos superhéroes hay el árbol;
# e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
# encontrarlo en el árbol y modificar su nombre;
# f. listar los superhéroes ordenados de manera descendente;
# g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
# los villanos, luego resolver las siguiente tareas:
# I. determinar cuántos nodos tiene cada árbol;
# II. realizar un barrido ordenado alfabéticamente de cada árbol.

arbol=BinaryTree()

nombres = [
    {'name': 'iron man', 'side': True},
    {'name': 'thanos', 'side': False},
    {'name': 'capitan america', 'side': True},
    {'name': 'red skull', 'side': False},
    {'name': 'hulk', 'side': True},
    {'name': 'black widow', 'side': True},
    {'name': 'rocket raccon', 'side': True},
    {'name': 'doctor strange', 'side': True},
    {'name': 'doctor octopus', 'side': True},
    {'name': 'deadpool', 'side': True},
]

for nombre in nombres:
    arbol.insert_node(nombre["name"],nombre["side"])

# a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo booleano que 
# indica si es un héroe o un villano, True y False respectivamente;

# b. listar los villanos ordenados alfabéticamente;
arbol.inorden_super_or_villano(False)
print()

# c. mostrar todos los superhéroes que empiezan con C;
arbol.inorden_start_with('C')
print()

# d. determinar cuántos superhéroes hay el árbol;
print('Cantidad de SuperHeroes:', arbol.contar_heroes())
print()

# e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
# encontrarlo en el árbol y modificar su nombre;

#value = input('ingrese el nombre que desea modificar ')
# pos = arbol.search(value)
# if pos:
#     is_hero = pos.other_values
#     arbol.delete_node(value)
#     print('modificar')
#     new_value = input('ingrese en nuevo nombre ')
#     arbol.insert_node(new_value, is_hero)
# else:
#     print('no esta')
# print()

# f. listar los superhéroes ordenados de manera descendente;
arbol.inorden()

# g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
# los villanos, luego resolver las siguiente tareas:

superheroes_Tree=BinaryTree()
villanos_Tree=BinaryTree()

for nombre in nombres:
    if nombre['side']:  
        superheroes_Tree.insert_node(nombre['name'])
    else:  
        villanos_Tree.insert_node(nombre['name'])

# I. determinar cuántos nodos tiene cada árbol;

print("Num de nodos superheroes",superheroes_Tree.contar_heroes())
print("Num de nodos villanos",villanos_Tree.contar_heroes())
print()
# II. realizar un barrido ordenado alfabéticamente de cada árbol.
print('SuperHeroes')
superheroes_Tree.inorden()
print()
print('Villanos')
villanos_Tree.inorden()
