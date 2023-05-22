#Resolver el problema del factorial de un número utilizando una pila.
class Pila():
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

def factorial_pila (numero):
    pila = Pila()
    pila.push(numero)
    resultado = 1
    while not pila.is_empty():
        numero_actual = pila.pop()
        resultado *= numero_actual
        if numero_actual > 1:
            pila.push(numero_actual - 1)
    return resultado

numero = int(input("Ingrese un número: "))
factorial = factorial_pila(numero)
print("El factorial de", numero , "es:", factorial)