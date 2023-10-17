from arbol import BinaryTree
# Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla y
# resuelva las siguientes consultas:
# a. listado inorden de las criaturas y quienes la derrotaron;
# b. se debe permitir cargar una breve descripción sobre cada criatura;
# c. mostrar toda la información de la criatura Talos;
# d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
# e. listar las criaturas derrotadas por Heracles;
# f. listar las criaturas que no han sido derrotadas;
# g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe
# o dios que la capturo;
# h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de
# Erimanto indicando que Heracles las atrapó;
# i. se debe permitir búsquedas por coincidencia;
# j. eliminar al Basilisco y a las Sirenas;
# k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles
# derroto a varias;
# l. modifique el nombre de la criatura Ladón por Dragón Ladón;
# m. realizar un listado por nivel del árbol;
# n. muestre las criaturas capturadas por Heracles
arbol = BinaryTree()

datos = [
    {'name': 'Ceto', 'derrotado': None, 'descripcion': 'Criatura marina mitológica.','capturado':None},
    {'name': 'Cerda de Cromión', 'derrotado': 'Teseo', 'descripcion': None,'capturado':None},
    {'name': 'Tifón', 'derrotado': 'Zeus', 'descripcion': None,'capturado':None},
    {'name': 'Ortro', 'derrotado': 'Heracles', 'descripcion': None,'capturado':None},
    {'name': 'Equidna', 'derrotado': 'Argos Panoptes', 'descripcion': None,'capturado':None},
    {'name': 'Toro de Creta', 'derrotado': 'Teseo', 'descripcion': None,'capturado':None},
    {'name': 'Dino', 'derrotado': None, 'descripcion': None,'capturado':None},
    {'name': 'Jabalí de Calidón', 'derrotado': 'Atalanta', 'descripcion': None,'capturado':None},
    {'name': 'Pefredo', 'derrotado': None, 'descripcion': None,'capturado':None},
    {'name': 'Carcinos', 'derrotado': None, 'descripcion': None,'capturado':None},
    {'name': 'Enio', 'derrotado': None, 'descripcion': None,'capturado':None},
    {'name': 'Gerión', 'derrotado': 'Heracles', 'descripcion': None,'capturado':None},
    {'name': 'Escila', 'derrotado': None, 'descripcion': None,'capturado':None},
    {'name': 'Cloto', 'derrotado': None, 'descripcion': None,'capturado':None},
    {'name': 'Caribdis', 'derrotado': None, 'descripcion': None,'capturado':None},
    {'name': 'Láquesis', 'derrotado': None, 'descripcion': None,'capturado':None},
    {'name': 'Euríale', 'derrotado': None, 'descripcion': None,'capturado':None},
    {'name': 'Átropos', 'derrotado': None, 'descripcion': None,'capturado':None},
    {'name': 'Esteno', 'derrotado': None, 'descripcion': None,'capturado':None},
    {'name': 'Minotauro de Creta', 'derrotado': 'Teseo', 'descripcion': None,'capturado':None},
    {'name': 'Medusa', 'derrotado': 'Perseo', 'descripcion': None,'capturado':None},
    {'name': 'Harpías', 'derrotado': None, 'descripcion': None,'capturado':None},
    {'name': 'Ladón', 'derrotado': 'Heracles', 'descripcion': None,'capturado':None},
    {'name': 'Argos Panoptes', 'derrotado': 'Hermes', 'descripcion': None,'capturado':None},
    {'name': 'Águila del Cáucaso', 'derrotado': None, 'descripcion': None,'capturado':None},
    {'name': 'Aves del Estínfalo', 'derrotado': None, 'descripcion': None,'capturado':None},
    {'name': 'Quimera', 'derrotado': 'Belerofonte', 'descripcion': None,'capturado':None},
    {'name': 'Talos', 'derrotado': 'Medea', 'descripcion': None,'capturado':None},
    {'name': 'Hidra de Lerna', 'derrotado': 'Heracles', 'descripcion': None,'capturado':None},
    {'name': 'Sirenas', 'derrotado': None, 'descripcion': None,'capturado':None},
    {'name': 'León de Nemea', 'derrotado': 'Heracles', 'descripcion': None,'capturado':None},
    {'name': 'Pitón', 'derrotado': 'Apolo', 'descripcion': None,'capturado':None},
    {'name': 'Esfinge', 'derrotado': 'Edipo', 'descripcion': None,'capturado':None},
    {'name': 'Cierva de Cerinea', 'derrotado': None, 'descripcion': None,'capturado':None},
    {'name': 'Dragón de la Cólquida', 'derrotado': None, 'descripcion': None,'capturado':None},
    {'name': 'Basilisco', 'derrotado': None, 'descripcion': None,'capturado':None},
    {'name': 'Cerbero', 'derrotado': None, 'descripcion': None,'capturado':None},
    {'name': 'Jabalí de Erimanto', 'derrotado': None, 'descripcion': None,'capturado':None}
]
for criatura in datos:
    arbol.insert_node(criatura['name'], {'derrotado': criatura['derrotado'],'descripcion': criatura['descripcion'],'capturado':criatura['capturado']})


# a. listado inorden de las criaturas y quienes la derrotaron;
arbol.inorden_Criaturas()

# b. se debe permitir cargar una breve descripción sobre cada criatura;
# value = input('ingrese el nombre de la criatura ')
# pos = arbol.search(value)
# if pos:
#     nueva_descripcion = input('Ingrese la nueva descripcion para la criatura: ')
#     pos.other_values['descripcion'] = nueva_descripcion
#     print('Descripcion modificada')
# else:
#     print("Criatura no encontrada")
    

# c. mostrar toda la información de la criatura Talos;
# value = input('ingrese el nombre de la criatura ')
# pos = arbol.search(value)
# if pos:
#     if pos.other_values['descripcion'] is not None:
#         informacion_descripcion=pos.other_values['descripcion']
#         print(f"descripcion:",informacion_descripcion)
#     else:
#         print("No hay descripcion")
# else:
#     print("Criatura no encontrada.")

# d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
# dic_ranking = {}
# arbol.inorden_ranking(dic_ranking)
# def order_por(item):
#     print(item)
#     return item[1]

# ordenados = list(dic_ranking.items())
# ordenados.sort(key=order_por, reverse=True)
# print(ordenados[:3])
# e. listar las criaturas derrotadas por Heracles;
print()
criaturas_derrotadas_por_heracles = []
for criatura in datos:
    if criatura['derrotado'] == 'Heracles':
        criaturas_derrotadas_por_heracles.append(criatura['name'])

print("Criaturas derrotadas por Heracles:")
for criatura in criaturas_derrotadas_por_heracles:
    print(criatura)
    
# f. listar las criaturas que no han sido derrotadas;
print()
criaturas_no_derrotadas = []
for criatura in datos:
    if criatura['derrotado'] is None:
        criaturas_no_derrotadas.append(criatura['name'])

print("Criaturas que no han sido derrotadas:")
for criatura in criaturas_no_derrotadas:
    print(criatura)
    
# g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe
# o dios que la capturo;
# h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de
# Erimanto indicando que Heracles las atrapó;
print()
print('Capturados por Heracles')
lista_atrapo=['Cerbero', 'Toro de Creta', 'Cierva Cerinea', 'Jabalí de Erimanto']

for atrapo in lista_atrapo:
    pos = arbol.search(atrapo)
    if pos:
        pos.other_values['capturado'] = 'Heracles'

arbol.inorden_add_field()
    
# i. se debe permitir búsquedas por coincidencia;
# arbol.search_by_coincidence()

# j. eliminar al Basilisco y a las Sirenas;
print()
arbol.delete_node('Basilisco')
arbol.delete_node('Sirenas')

i=arbol.search('Basilisco')
if i:
    nombre=i.value
    print(nombre)
else:
    print('Basilisco eliminado')    
# k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles
# derroto a varias;
print()
pos = arbol.search('Aves del Estínfalo')
if pos:
    nueva_descripcion = 'Heracles derroto a varias '
    pos.other_values['descripcion'] = nueva_descripcion
    print('Descripcion modificada')
else:
    print("Criatura no encontrada")

# l. modifique el nombre de la criatura Ladón por Dragón Ladón;
print()
pos = arbol.search('Ladón')
if pos:
    nuevo_nombre= 'Dragón Ladón'
    pos.value=nuevo_nombre
    print('Nombre cambiado',pos.value)
else:
    print("Criatura no encontrada")
# m. realizar un listado por nivel del árbol;
arbol.by_level()
# n. muestre las criaturas capturadas por Heracles
print()
print('Capturados por Heracles')
arbol.inorden_add_field()