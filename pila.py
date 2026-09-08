class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Pila: # Pila LIFO
    def __init__(self):
        self.tope = None
        self.tamano = 0

    def esta_vacia(self):
        return self.tope is None

    def push(self, dato): # Agregar elemento a la pila (al inicio)
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.tope
        self.tope = nuevo_nodo
        self.tamano += 1

    def pop(self):
        if self.esta_vacia():
            raise Exception("Error: No hay elementos en pila")
        dato = self.tope.dato
        self.tope = self.tope.siguiente
        self.tamano -= 1
        return dato

    def pick(self): # Muestra pila sin eliminar
        if self.esta_vacia():
            raise Exception("Error: No hay elementos en pila")
        return self.tope.dato


    def __len__(self):
        return self.tamano

    def __str__(self):
        if self.esta_vacia():
            return "Pila vacia"
        elementos = []
        actual = self.tope
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return "Tope --> " + "-->".join(elementos) + "--> None"

def evaluar_postfija(expresion):

    tokens = expresion.split()
    pila = Pila()

    operadores = {
        '+': lambda a,b: a+b,
        '-': lambda a,b: a-b,
        '*': lambda a,b: a*b,
        '/': lambda a,b: a/b,
    }

    for token in tokens:
        if token.lstrip('-').replace('.', '').isdigit():
            valor = float(token) if '.' in token else int(token)
            pila.push(valor)
        elif token in operadores:
            a = pila.pop()
            b = pila.pop()
            resultado = operadores[token](a,b)
            pila.push(resultado)

    return pila.pop()



evaluar_postfija("3 4 5 * +")