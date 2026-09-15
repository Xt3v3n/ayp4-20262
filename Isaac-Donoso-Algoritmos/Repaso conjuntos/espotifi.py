"""
═══════════════════════════════════════════════════════════════════════════════
CASO DE USO 1: SPOTIFY - PLAYLISTS COMPARTIDAS
Algoritmos y Programación 4 - Semana 6
═══════════════════════════════════════════════════════════════════════════════

ENUNCIADO:
----------
Spotify quiere implementar una función de "Playlists Compartidas".
Dados dos usuarios con sus canciones favoritas, el sistema debe:

1. Encontrar canciones que ambos disfrutan (para playlist compartida)
2. Sugerir canciones que uno tiene y el otro no
3. Mostrar el catálogo combinado de ambos
4. Verificar si un usuario escucha un subconjunto de lo que escucha otro

Implementar usando operaciones de conjuntos.
"""

# ═══════════════════════════════════════════════════════════════════════════════
# DATOS
# ═══════════════════════════════════════════════════════════════════════════════

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Conjunto:
    def __init__(self, elementos = None):
        self.cabeza = None
        self.tamaño = 0

        if elementos:
            for e in elementos:
                self.agregar(e)
    
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
        #Hacemos la union de la diferencia de mi conjunto con el otro y
        #la diferencia del otro conjunto con el mio
        return self.diferencia(otro).union(otro.diferencia(self))
    
    def subconjunto(self, otro):
        actual = self.cabeza
        while actual:
            if not otro.pertenece(actual.dato):
                return False
            actual = actual.siguiente
        return True
    
    def a_lista(self):
        resultado = []

        actual = self.cabeza
        while actual:
            resultado.append(actual.dato)
            actual = actual.siguiente
        return resultado
    
    def __str__(self):
        return "{" + ", ".join(str(x) for x in self.a_lista()) + "}"
    
canciones_juan = {
    "Blinding Lights", "Bohemian Rhapsody", "Shape of You",
    "Despacito", "Hotel California", "Billie Jean",
    "Rolling in the Deep", "Smells Like Teen Spirit"
}

canciones_maria = {
    "Shape of You", "Despacito", "Bad Guy",
    "Blinding Lights", "Watermelon Sugar", "Levitating",
    "Rolling in the Deep", "drivers license"
}

playlist_juan = Conjunto()
playlist_maria = Conjunto()

# ═══════════════════════════════════════════════════════════════════════════════
# SOLUCIÓN
# ═══════════════════════════════════════════════════════════════════════════════

print("=" * 60)
print("   SPOTIFY - PLAYLISTS COMPARTIDAS")
print("=" * 60)

print(f"\nCanciones de Juan ({len(canciones_juan)}):")
for c in sorted(canciones_juan):
    playlist_juan.agregar(c)
    print(f"  ♪ {c}")

print(f"\nCanciones de María ({len(canciones_maria)}):")
for c in sorted(canciones_maria):
    playlist_maria.agregar(c)
    print(f"  ♪ {c}")

# 1. Playlist compartida (intersección)
compartidas = playlist_juan.interseccion(playlist_maria)
print(f"\n1. Playlist compartida ({compartidas.cardinalidad()} canciones):")
for c in sorted(compartidas.a_lista()):
    print(f"  ♪ {c}")

# 2. Sugerencias (diferencia)
sugerencias_para_juan = playlist_maria.diferencia(playlist_juan)
sugerencias_para_maria = playlist_juan.diferencia(playlist_maria)

print(f"\n2. Sugerencias para Juan ({sugerencias_para_juan.cardinalidad()}):")
for c in sorted(sugerencias_para_juan.a_lista()):
    print(f"  → {c}")

print(f"\n   Sugerencias para María ({sugerencias_para_maria.cardinalidad()}):")
for c in sorted(sugerencias_para_maria.a_lista()):
    print(f"  → {c}")

# 3. Catálogo combinado (unión)
catalogo = playlist_juan.union(playlist_maria)
print(f"\n3. Catálogo combinado ({catalogo.cardinalidad()} canciones únicas):")
for c in sorted(catalogo.a_lista()):
    print(f"  ♪ {c}")

# 4. ¿Un usuario escucha subconjunto del otro?
print(f"\n4. ¿Juan escucha subconjunto de María? {playlist_juan.subconjunto(playlist_maria)}")
print(f"   ¿María escucha subconjunto de Juan? {playlist_maria.subconjunto(playlist_juan)}")

# Bonus: Canciones exclusivas (diferencia simétrica)
exclusivas = playlist_juan.diferencia_simetrica(playlist_maria)
print(f"\n5. Canciones que solo uno de los dos escucha ({exclusivas.cardinalidad()}):")
for c in sorted(exclusivas.a_lista()):
    print(f"  ♪ {c}")
