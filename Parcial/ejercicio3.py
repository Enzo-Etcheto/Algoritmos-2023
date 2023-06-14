"""
Se recuperó la bitácora de la nave del cazarrecompensas Boba Fett, la
cual se almacenaban en una pila en cada misión de caza que
emprendió (con la siguiente información planeta visitado, a quien
capturado, costo de la recompensa), resolver las siguientes
actividades:
a. Mostrar los planetas visitados en el orden hizo las misiones.
b. Determinar cuántos créditos galácticos recaudo en total.
c. Determinar el número de la misión en que capturo a Han Solo
y en que planeta fue, suponga que dicha misión está cargada.
"""
from clases import Pila

bitacora = [
    {"planeta":"Melmak","capturado":"Alf","recompensa":"30000"},
    {"planeta":"Marte","capturado":"Han Solo","recompensa":"50000"},
    {"planeta":"SC012","capturado":"Obi Wan","recompensa":"50000"},
    {"planeta":"DS230","capturado":"Jabba el Hutt","recompensa":"30000"}
]

#A
pila_planetas = Pila()
pila_aux = Pila()

for mision in bitacora:
    pila_planetas.push(mision["planeta"])

while pila_planetas.size() > 0:
    pila_aux.push(pila_planetas.pop())

print("Los planetas visitados en orden son:")
while pila_aux.size() > 0:
    print(pila_aux.pop())


#B
pila_recompensas = Pila()

for mision in bitacora:
    pila_recompensas.push(int(mision["recompensa"]))

creditos = 0
while pila_recompensas.size() > 0:
    creditos += pila_recompensas.pop()
    
print("El total de creditos galacticos es", creditos)
    
#C
pila_personajes = Pila()
pila_aux_personaje = Pila()
for mision in bitacora:
    pila_personajes.push(mision["capturado"])

encontrado = False
i = 0

while pila_personajes.size() > 0:
    pila_aux_personaje.push(pila_personajes.pop())

while pila_aux_personaje.size() > 0 and encontrado == False :
    personaje = pila_aux_personaje.pop()
    i += 1
    if personaje == "Han Solo":
        encontrado = True    

if encontrado == True:
    print("Han solo fue encontrado en la mision num:", i)
else:
    print("Han solo no fue capturado")    