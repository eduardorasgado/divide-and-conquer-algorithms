#Pilas
"""
Una pila es una lista ordenada o estructura de datos en la que el modo de acceso a sus elementos es de tipo LIFO (Last In First Out, ultimo en entrar es el primero en salir) que permite almacenar datos.

Para el manejo de los datos se cuenta con dos operaciones basicas: apilar(push), que coloca un objeto en la pila y su operacion inversa, retirar(pop), que retira el último elemento apilado.

Operaciones:
Crear: Se crea la pila vacía.Contructor
Tamaño:Regresa el nuero de elementos de la pila(size)
Apilar: Se añade un elemento a la pila(push).
Desapilar: Se elimina el elemento frontal de la pila(pop)
Cima: devuelve el elemento que está en la cima de la pila(topo peek)
Vacía: Devuelve cierto si la pila está sin elementos o falso en caso de que contenga uno(empty)

Las pilas pueden ser de tmaaño estático y dinámico, se pueden implementar en las listas, arreglos, colecciones de datos o en las listas enlazadas
"""
#Pila estática
print("Pilas!")
class Pila:
    def __init__(self,size):
        self.lista = []
        self.tope = 0
        self.size = size
        
    def empty(self):
        if self.tope == 0:
            return True
        else:
            return False
        
    def push(self,dato):
        if self.tope < self.size:
            self.lista += [dato]
            self.tope += 1
        else:
            print("La pila está llena")
            
    def pop(self):
        if self.empty():
            print("La pila está vacía")
        else:
            self.tope -= 1
            self.lista = [self.lista[x] for x in range(self.tope)]
    def show(self):
        for i in range(self.tope):
            print("index[%d] => %d"%(self.tope-1-i,self.lista[self.tope-i-1]))
            
    def size_of(self):
        return "tamaño actual: %d"%(self.tope)
    
    def tope_of(self):
        return "tope=> [%d]: %d"%(self.tope-1,self.lista[-1])
    
pila = Pila(5)
pila.push(23)
pila.push(90)
pila.push(45)
pila.push(100)
pila.show()
print(pila.size_of())
print(pila.tope_of())
print("poping...")
pila.pop()
pila.show()
input()