#Listas doblemente ligadas

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.anterior = None
        self.siguiente = None
    
class ListaDoble:
    def __init__(self):
        self.cabeza = None
        self.cola = None
    
    def esta_vacia(self):
        return self.cabeza is None
    
    def insertar_inicio(self, dato):
        nuevo = Nodo(dato)

        if self.esta_vacia():
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            nuevo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo
            self.cabeza = nuevo

    def insertar_final(self, dato):
        nuevo = Nodo(dato)
        
        if self.esta_vacia():
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            self.cola.siguiente = nuevo
            nuevo.anterior = self.cola
            self.cola = nuevo

    def eliminar_inicio(self):
        if self.esta_vacia():
            return None
        
        if self.cabeza.dato == self.cola.dato:
            self.cabeza = None
            self.cola = None
        else:
            self.cabeza = self.cabeza.siguiente
            self.cabeza.anterior = None
    
    def eliminar_final(self):
        if self.esta_vacia():
            return None
        
        if self.cabeza.dato == self.cola.dato:
            self.cabeza = None
            self.cola = None
        else:
            self.cola = self.cola.anterior
            self.cola.siguiente = None

    def recorrer_adelante(self):
        if self.esta_vacia():
            print("Lista vacia.")
            return

        print("Recorriendo Inicio --> Fin") 
        actual = self.cabeza

        print("Inicio", end=" -> ")
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("Fin")

    def recorrer_reversa(self):
        if self.esta_vacia():
            print("Lista vacia.")
            return

        print("Recorriendo Fin --> Inicio") 
        actual = self.cola

        print("Fin", end=" -> ")
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.anterior
        print("Inicio")

    def buscar(self,dato):
        actual = self.cabeza

        while actual:
            if actual.dato == dato:
                return True
            actual = actual.siguiente
        
        return False
    
    def __len__(self):
        contador = 0
        actual = self.cabeza

        while actual:
            contador += 1
            actual = actual.siguiente
        
        return contador
    
    def __str__(self):
        if self.esta_vacia():
            return "Lista vacia."
        """ resultado = "Inicio -> "
        actual = self.cabeza

        while actual:
            resultado += str(actual.dato) + " -> "
            actual = actual.siguiente
        
        resultado += "Fin"
        return resultado"""

        elementos = []
        actual = self.cabeza
       
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        
        return " <=> ".join(elementos) 
    
lista = ListaDoble()
lista.insertar_final(10)
lista.insertar_final(20)
lista.insertar_final(30)
print(lista)

lista.insertar_inicio(40)

print(lista)

lista.recorrer_adelante()
lista.recorrer_reversa()

print(f"Tamaño de la lista: {len(lista)}")

print(f"¿Está el 20? {lista.buscar(20)}")