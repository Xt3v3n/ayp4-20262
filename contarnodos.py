class Node:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Lista:
    def __init__(self):
        self.cabeza = None

    def agregar_nodo(self, dato):
        nuevo_nodo = Node(dato)
        if self.cabeza == None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente != None:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def contar_nodos(self, nodo=None):
        
        if nodo is None:
            return 0

        return 1 + self.contar_nodos(nodo.siguiente)

def buscar(self, dato, nodo=None):
        if nodo is None:
            return False

        if nodo.dato == dato:
            return True

        return self.buscar(dato, nodo.siguiente)