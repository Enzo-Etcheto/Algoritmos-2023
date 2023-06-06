'''
Dada una cola con las notificaciones de las aplicaciones de redes sociales de un Smartphone,
de las cual se cuenta con la hora de la notificación, la aplicación que la emitió y el mensaje,
resolver las siguientes actividades:

a. escribir una función que elimine de la cola todas las notificaciones de Facebook;

b. escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya
la palabra Python, si perder datos en la cola;

c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las
11:43 y las 15:57, y determinar cuántas son.

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
        
        
class Pila ():
    """Clase pila"""
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
    
    
def elimina_noti_facebook(cola):
    cola_aux = Cola()
    while not cola.is_empty():
        notificacion = cola.atention()
        if notificacion["app"] != "Facebook":
            cola_aux.arrive(notificacion)
    return cola_aux

def mostrar_noti_twitter(cola):
    cola_aux = Cola()
    while not cola.is_empty():
        notificacion = cola.atention()
        if notificacion["app"] == "Twitter" and "Python" in notificacion["mensaje"]:
            print("Hora:", notificacion["hora"])
            print("App:", notificacion["app"])
            print("mensaje:", notificacion["mensaje"])
            print(' ')
        cola_aux.arrive(notificacion)
    return cola_aux

def contar_noti_temporales(cola):
    pila_temporal = Pila()
    contador = 0

    while not cola.is_empty():
        notificacion = cola.atention()

        if "11:43" <= notificacion["hora"] <= "15:57":
            contador += 1
            pila_temporal.push(notificacion)

    while not pila_temporal.is_empty():
        cola.arrive(pila_temporal.pop())

    return contador


notificaciones_lista = [
    {"hora": "10:30", "app": "Facebook", "mensaje": "Tienes una solicitud"},
    {"hora": "15:30", "app": "Twitter", "mensaje": "Hoy es el cumpleaños"},
    {"hora": "17:10", "app": "Facebook", "mensaje": "Tienes nuevos mensajes"},
    {"hora": "18:25", "app": "Facebook", "mensaje": "Facebook hara cambios"},
    {"hora": "12:30", "app": "Twitter", "mensaje": "Sabias que Python"},
    {"hora": "22:30", "app": "Twitter", "mensaje": "Python es el lenguaje..."}
]

cola_lista = Cola()
for noti in notificaciones_lista:
    cola_lista.arrive(noti)
    
cola_lista = elimina_noti_facebook(cola_lista)
    
cola_lista = mostrar_noti_twitter(cola_lista)    
print('                 ')    

cola_temporal = contar_noti_temporales(cola_lista)
print('La cantidad de notificaciones temporales son: ', cola_temporal)
