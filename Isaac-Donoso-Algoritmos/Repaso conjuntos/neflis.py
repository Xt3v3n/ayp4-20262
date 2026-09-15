"""
═══════════════════════════════════════════════════════════════════════════════
CASO DE USO 3: NETFLIX - SISTEMA DE RECOMENDACIONES
Algoritmos y Programación 4 - Semana 6
═══════════════════════════════════════════════════════════════════════════════

ENUNCIADO:
----------
Netflix quiere mejorar su sistema de recomendaciones usando conjuntos.
Cada película tiene un conjunto de géneros/etiquetas.
El sistema debe:

1. Encontrar películas similares (comparten géneros)
2. Recomendar películas según los géneros favoritos del usuario
3. Encontrar géneros únicos en el catálogo
4. Agrupar películas por género
5. Calcular un "puntaje de similitud" entre películas

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
    
catalogo = {
    "Inception": Conjunto(["ciencia ficción", "acción", "thriller", "drama"]),
    "The Matrix": Conjunto(["ciencia ficción", "acción", "thriller"]),
    "Titanic": Conjunto(["romance", "drama", "histórica"]),
    "The Notebook": Conjunto(["romance", "drama"]),
    "Avengers": Conjunto(["acción", "ciencia ficción", "aventura"]),
    "John Wick": Conjunto(["acción", "thriller", "crimen"]),
    "Interstellar": Conjunto(["ciencia ficción", "drama", "aventura"]),
    "The Godfather": Conjunto(["crimen", "drama", "thriller"]),
    "Toy Story": Conjunto(["animación", "comedia", "aventura"]),
    "Shrek": Conjunto(["animación", "comedia", "aventura"]),
}

# Géneros favoritos del usuario
favoritos_usuario = Conjunto(["ciencia ficción", "acción", "thriller"])

# ═══════════════════════════════════════════════════════════════════════════════
# SOLUCIÓN
# ═══════════════════════════════════════════════════════════════════════════════

print("=" * 60)
print("   NETFLIX - SISTEMA DE RECOMENDACIONES")
print("=" * 60)

print("\nCatálogo:")
for pelicula, generos in catalogo.items():
    print(f"  {pelicula}: {generos.a_lista()}")

# 1. Películas similares (comparten al menos 2 géneros)
print("\n" + "=" * 60)
print("1. PELÍCULAS SIMILARES (comparten 2+ géneros)")
print("=" * 60)

peliculas = list(catalogo.keys())
for i in range(len(peliculas)):
    for j in range(i + 1, len(peliculas)):
        p1, p2 = peliculas[i], peliculas[j]
        comunes = catalogo[p1].interseccion(catalogo[p2])
        if comunes.cardinalidad() >= 2:
            print(f"  {p1} <-> {p2}")
            print(f"    Géneros comunes: {comunes.a_lista()}")

# 2. Recomendaciones según gustos del usuario
print("\n" + "=" * 60)
print(f"2. RECOMENDACIONES (gustos: {favoritos_usuario})")
print("=" * 60)

recomendaciones = []
for pelicula, generos in catalogo.items():
    coincidencias = generos.interseccion(favoritos_usuario)
    if coincidencias:
        puntaje = coincidencias.cardinalidad() / favoritos_usuario.cardinalidad()
        recomendaciones.append((pelicula, puntaje, coincidencias.a_lista()))

# Ordenar por puntaje (mayor primero)
recomendaciones.sort(key=lambda x: x[1], reverse=True)

for pelicula, puntaje, coincidencias in recomendaciones:
    barra = "█" * int(puntaje * 10)
    print(f"  {pelicula:20} {barra} {puntaje:.0%} - {coincidencias}")

# 3. Todos los géneros del catálogo
print("\n" + "=" * 60)
print("3. GÉNEROS ÚNICOS EN EL CATÁLOGO")
print("=" * 60)

todos_generos = Conjunto()
for generos in catalogo.values():
    todos_generos = todos_generos.union(generos)

print(f"  Total: {todos_generos.cardinalidad()} géneros")
for g in sorted(todos_generos.a_lista()):
    print(f"  • {g}")

# 4. Agrupar películas por género
print("\n" + "=" * 60)
print("4. PELÍCULAS POR GÉNERO")
print("=" * 60)

for genero in sorted(todos_generos.a_lista()):
    peliculas_genero = Conjunto()
    for pelicula, generos in catalogo.items():
        if genero in generos.a_lista():
            peliculas_genero.agregar(pelicula)
    print(f"  {genero}: {peliculas_genero}")

# 5. Puntaje de similitud entre dos películas
print("\n" + "=" * 60)
print("5. SIMILITUD (índice de Jaccard)")
print("=" * 60)

def similitud_jaccard(pelicula1, pelicula2):
    """
    Índice de Jaccard = |A ∩ B| / |A ∪ B|
    1.0 = idénticos, 0.0 = nada en común
    """
    g1 = catalogo[pelicula1]
    g2 = catalogo[pelicula2]
    interseccion = g1.interseccion(g2).cardinalidad()
    union = g1.union(g2).cardinalidad()
    return interseccion / union if union > 0 else 0

pares = [
    ("Inception", "The Matrix"),
    ("Inception", "Titanic"),
    ("Toy Story", "Shrek"),
    ("The Godfather", "John Wick"),
]

for p1, p2 in pares:
    sim = similitud_jaccard(p1, p2)
    barra = "█" * int(sim * 20)
    print(f"  {p1:15} vs {p2:15} → {barra} {sim:.2f}")
