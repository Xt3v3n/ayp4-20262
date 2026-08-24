class Node:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaDoble:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def esta_vacia(self):
        return self.cabeza is None

    def insertar_inicio(self, dato):
        nuevo_nodo = Node(dato)

        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = nuevo_nodo
            self.cabeza = nuevo_nodo

    def insertar_final(self, dato):
        nuevo_nodo = Node(dato)

        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.cola
            self.cola = nuevo_nodo

    def eliminar_inicio(self):

        if self.esta_vacia():
            return None

        dato = self.cabeza.dato

        if self.cabeza == self.cola:
            self.cabeza = None
            self.cola = None

        else:
            self.cabeza = self.cabeza.siguiente
            self.cabeza.anterior = None

    def eliminar_ultimo(self):
        if self.esta_vacia():
            return None

        dato = self.cabeza.dato
        
        if self.cabeza == self.cola:
            self.cabeza = None
            self.cola = None
        else:
            self.cola = self.cola.anterior
            self.cola.siguiente = None