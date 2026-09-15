def fibonacci_memo(n , cache = {}):
    if n <= 1:
        return n
    
    if n in cache:
        return cache[n]
    
    cache[n] = fibonacci_memo(n-1, cache) + fibonacci_memo(n-2, cache)
    return cache[n]

def cambio(cantidad, monedas):
    if cantidad == 0:
        return 0
    
    if cantidad < 0:
        return float('inf')

    minimo = float('inf')

    for moneda in monedas:
        resultado = cambio(cantidad-moneda, monedas)
        minimo = min(resultado + 1, minimo)

    return minimo

""" ESTE ESTA MALO COMO LA CHIMBA :(
def cambio_memo(cantidad, monedas, cache = {}, moneda_actual = 0):
    if cantidad == 0:
        return 0
    
    if cantidad < 0:
        return float('inf')
    
    if moneda_actual in cache:
        return cache[moneda_actual]

    minimo = float('inf')

    for moneda in monedas:     
        cache[moneda] = cambio_memo(cantidad-moneda, monedas, cache, moneda)
        minimo = min(cache[moneda]+1, minimo)

    return minimo
"""
def cambio_memo_profe(cantidad, monedas, cache = {}):
    if cantidad in cache:
        return cache[cantidad]
    
    if cantidad == 0:
        return 0
    
    if cantidad < 0:
        return float('inf')

    minimo = float('inf')

    for moneda in monedas:
        resultado = cambio(cantidad-moneda, monedas)
        minimo = min(resultado + 1, minimo)
    cache[cantidad] = minimo

    return minimo

#AHORA VEREMOS PILAS
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None   

class Pilas:
    def __init__(self):
        self.tope = None
        self.tamaño = 0

    def esta_vacia(self):
        return self.tope is None
    
    def push(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.tope
        self.tope = nuevo
        self.tamaño += 1
        return nuevo

    def pop(self):
        if self.esta_vacia():
            raise Exception("Error: La pila esta vacia")
        dato = self.tope.dato
        self.tope = self.tope.dato.siguiente
        self.tamaño -= 1
        return dato
    
    def operacion(self, nodo = None):
        if self.esta_vacia:
            return "pila vacia"
        if nodo is None:
            nodo = self.tope
        operadores = {"+","-","*","/"}
        if nodo.dato in operadores:
            if nodo.dato == "+":
                operador = self.pop()
                dato1 = float(self.pop())
                dato2 = float(self.pop())
                return dato1 + dato2
            elif nodo.dato == "-":
                operador = self.pop()
                dato1 = float(self.pop())
                dato2 = float(self.pop())
                return dato1 + dato2
            
            elif nodo.dato == "*":
                operador = self.pop()
                dato1 = float(self.pop())
                dato2 = float(self.pop())
                return dato1 + dato2
            
            elif nodo.dato == "/":
                operador = self.pop()
                dato1 = float(self.pop())
                dato2 = float(self.pop())
                return dato1 + dato2
        else:
            return self.operacion(nodo.siguiente)
        
            
            


monedas = [25, 10, 5, 1]
 
print(fibonacci_memo(50))

print(cambio(11, monedas))
#print(cambio_memo(11, monedas)) MALO :(
print(cambio_memo_profe(11, monedas))

pila = Pilas()

pila.push("2")
pila.push("3")
pila.push("+")

print(pila.operacion())