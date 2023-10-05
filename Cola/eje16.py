"""
Utilice cola de prioridad, para atender la cola de impresión tomando en cuenta el siguiente
criterio (1- empleados, 2- staff de tecnologías de la información “TI”, 3- gerente), y resuelva la
siguiente situación:
a. cargue tres documentos de empleados (cada documento se representa solamente con
un nombre).
b. imprima el primer documento de la cola (solamente mostrar el nombre de este por pantalla).
c. cargue dos documentos del staff de TI.
d. cargue un documento del gerente.
e. imprima los dos primeros documentos de la cola.
f. cargue dos documentos de empleados y uno de gerente.
g. imprima todos los documentos de la cola de impresión.
"""
class ColaPrioridad:

    def __init__(self):
        self.vector = []

    def add_element(self, value):
        self.vector.append(value)
        self.flotar(len(self.vector)-1)

    def remove_element(self):
        self.vector[0], self.vector[-1] = self.vector[-1], self.vector[0]
        value = self.vector.pop()
        self.hundir(0)
        return value

    def flotar(self, index):
        while index > 0 and self.vector[index] > self.vector[(index-1)//2]:
            padre = (index-1)//2
            self.vector[index], self.vector[padre] = self.vector[padre], self.vector[index]
            index = padre

    def hundir(self, index):
        hijo_izq = (index*2) + 1
        control = True
        while control and hijo_izq < len(self.vector):
            hijo_der = hijo_izq + 1
            mayor = hijo_izq
            if hijo_der < len(self.vector):
                if self.vector[hijo_der] > self.vector[hijo_izq]:
                    mayor = hijo_der

            if self.vector[index] < self.vector[mayor]:
                self.vector[index], self.vector[mayor] = self.vector[mayor], self.vector[index]
                index = mayor
                hijo_izq = (index*2) + 1
            else:
                control = False


    def size(self):
        return len(self.vector)

    def montculizar(self):
        for i in range(len(self.vector)):
            self.flotar(i)
    
    def hepasort(self):
        vector = []
        for i in range(len(self.vector)):
            vector.append(self.remove_element())
        return vector

    def arrive(self, value, priority):
        self.add_element([priority, value])

    def atention(self):
        return self.remove_element()
    

cola = ColaPrioridad()

#a. cargue tres documentos de empleados (cada documento se representa solamente con
#un nombre).

cola.arrive("empleado 1", 1)
cola.arrive("empleado 2", 1)
cola.arrive("empleado 3", 1)

#b. imprima el primer documento de la cola (solamente mostrar el nombre de este por pantalla).
print('Punto B')
print("El primer documento en la cola es",cola.atention()[1])   

#c. cargue dos documentos del staff de TI.
cola.arrive("Staff 1 ",2)
cola.arrive("Staff 2 ",2)

#d. cargue un documento del gerente.
cola.arrive("Gerente 1 ",3)

#e. imprima los dos primeros documentos de la cola.
print(' ')
print('Punto E')
for i in range(2):
    print(cola.atention()[1])

#f. cargue dos documentos de empleados y uno de gerente.
cola.arrive("Empleado 4 ",1)
cola.arrive("Empleado 5 ",1)
cola.arrive("Gerente 2 ",3)

#g. imprima todos los documentos de la cola de impresión.
print(' ')
print('Punto G')
while cola.size() >0:
    print(cola.atention()[1])
