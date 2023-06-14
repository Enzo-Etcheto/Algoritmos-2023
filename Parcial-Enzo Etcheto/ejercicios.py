
"""
Enzo Etcheto

Desarrollar una función recursiva que permita contar cuantas veces
aparece una determinada palabra, en un vector de palabras.

"""

def funcion_recursiva(lista, palabra):
    if len(lista) == 0:
        return 0
    else:
        contador = 0
        if lista[0] == palabra:
            contador += 1
        return contador + funcion_recursiva(lista[1:], palabra)
    
palabras = ['rojo', 'azul', 'amarillo', 'rojo', 'azul','azul']
buscar = 'azul'
print("La palabra aparece",funcion_recursiva(palabras, buscar),"veces") 