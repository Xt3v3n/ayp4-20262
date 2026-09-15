def formas_subir_memo(n, cache = {}):
    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    if n == 2:
        return 2
    
    if n in cache:
        return cache[n]

    cache[n] = formas_subir_memo(n-1, cache) + formas_subir_memo(n-2, cache)
    return cache[n]

def formas_subir(n):
    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    if n == 2:
        return 2
    
    return formas_subir(n-1) + formas_subir(n-2)

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
            return None
        dato = self.tope.dato
        self.tope = self.tope.siguiente
        self.tamaño -= 1
        return dato
    
    def peek(self):
        if self.esta_vacia():
            return None
        return self.tope.dato


def orden(expresion):
    pila = Pilas()
    mapa = {")":"(", "}":"{", "]":"["}
    apertura = set(mapa.values())
    cierre = set(mapa.keys())

    for token in expresion:
        if token in apertura:
            pila.push(token)
        elif token in cierre:
            if pila.esta_vacia():
                print("Error")
                return
            tope = pila.pop()
            if tope != mapa[token]:
                print("Error")
                return 

        
    if pila.esta_vacia():
        print("Exitoso")
    else:
        print("Error")

    
def verificar_expresion(expresion):

    pila = Pilas()

    mapa = {")":"(", "}":"{", "]":"["}
    apertura = set(mapa.values())
    cierre = set(mapa.keys())

    operadores = set("+-*/")

    anterior = None

    for i, token in enumerate(expresion):

        # ignorar espacios
        if token == " ":
            continue

        # NUMERO
        if token.isdigit():
            anterior = "numero"
            continue

        # APERTURA
        if token in apertura:
            pila.push(token)
            anterior = "apertura"
            continue

        # CIERRE
        if token in cierre:

            if anterior == "operador":
                print(f"Error: cierre despues de operador en posicion {i}")
                return False

            if pila.esta_vacia():
                print(f"Error: cierre inesperado en posicion {i}")
                return False

            tope = pila.pop()

            if tope != mapa[token]:
                print(f"Error: parentesis incorrectos en posicion {i}")
                return False

            anterior = "cierre"
            continue

        # OPERADOR
        if token in operadores:

            if anterior in (None, "operador", "apertura"):
                print(f"Error: operador mal ubicado en posicion {i}")
                return False

            anterior = "operador"
            continue

        print(f"Error: caracter invalido '{token}' en posicion {i}")
        return False

    # terminar con operador
    if anterior == "operador":
        print("Error: la expresion termina con operador")
        return False

    if not pila.esta_vacia():
        print("Error: faltan cierres de parentesis")
        return False

    return True

expresion = "[{(5+2)*3}+4]"

#orden(expresion)

if verificar_expresion(expresion):
    print("La expresion es correcta.")
else:
    print("La expresion es incorrecta.")


#print(formas_subir(40))
#print(formas_subir_memo(750))  