class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Conjunto:
    def __init__(self):
        self.cabeza = None
        self.tamaño = 0

    def esta_vacio(self):
        return self.cabeza is None

    def cardinalidad(self):
        return self.tamaño

    def pertenece(self, x):
        actual = self.cabeza
        while actual:
            if actual.dato == x:
                return True
            actual = actual.siguiente
        return False

    def agregar(self, x):
        if self.pertenece(x):
            return False

        nuevo = Nodo(x)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo
        self.tamaño += 1
        return True

    def eliminar(self, x):
        if self.esta_vacio():
            return False

        if self.cabeza.dato == x:
            self.cabeza = self.cabeza.siguiente
            self.tamaño -= 1
            return True

        actual = self.cabeza
        while actual.siguiente:
            if actual.siguiente.dato == x:
                actual.siguiente = actual.siguiente.siguiente
                self.tamaño -= 1
                return True
            actual = actual.siguiente
        
        return False

    def mostrar(self):
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        print("{" + ",".join(elementos) + "}")

    def union(self, otro):
        resultado = Conjunto()
        actual = self.cabeza
        while actual:
            resultado.agregar(actual.dato)
            actual = actual.siguiente

        actual = otro.cabeza
        while actual:
            resultado.agregar(actual.dato)
            actual = actual.siguiente

        return resultado

    def interseccion(self, otro):
        resultado = Conjunto()

        actual = self.cabeza
        while actual:
            if otro.pertenece(actual.dato):
                resultado.agregar(actual.dato)
            actual = actual.siguiente
        return resultado

    def diferencia(self, otro):
        resultado = Conjunto()
        actual = self.cabeza
        while actual:
            if not otro.pertenece(actual.dato):
                resultado.agregar(actual.dato)
            actual = actual.siguiente
        return resultado

    def diferencia_simetrica(self, otro):
        return self.diferencia(otro).union(otro.diferencia(self))

A = Conjunto()
B = Conjunto()
