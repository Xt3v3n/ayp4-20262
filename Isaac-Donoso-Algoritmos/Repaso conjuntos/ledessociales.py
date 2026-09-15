"""
═══════════════════════════════════════════════════════════════════════════════
CASO DE USO 5: RED SOCIAL - ANÁLISIS DE CONEXIONES
Algoritmos y Programación 4 - Semana 6
═══════════════════════════════════════════════════════════════════════════════

ENUNCIADO:
----------
Una red social necesita analizar las conexiones entre usuarios.
Cada usuario tiene un conjunto de amigos. El sistema debe:

1. Encontrar amigos en común entre dos usuarios
2. Sugerir amigos (amigos de amigos que no conoces)
3. Encontrar grupos aislados (usuarios sin amigos en común)
4. Calcular el "grado de conexión" entre usuarios
5. Encontrar el usuario más conectado

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

red = {
    "Ana": Conjunto({"Carlos", "Diana", "Eduardo", "Fernanda"}),
    "Carlos": Conjunto({"Ana", "Diana", "Gabriel"}),
    "Diana": Conjunto({"Ana", "Carlos", "Eduardo", "Helena"}),
    "Eduardo": Conjunto({"Ana", "Diana", "Fernanda"}),
    "Fernanda": Conjunto({"Ana", "Eduardo", "Gabriel", "Helena"}),
    "Gabriel": Conjunto({"Carlos", "Fernanda", "Ivan"}),
    "Helena": Conjunto({"Diana", "Fernanda", "Ivan"}),
    "Ivan": Conjunto({"Gabriel", "Helena"}),
}

# ═══════════════════════════════════════════════════════════════════════════════
# SOLUCIÓN
# ═══════════════════════════════════════════════════════════════════════════════

print("=" * 60)
print("   RED SOCIAL - ANÁLISIS DE CONEXIONES")
print("=" * 60)

print("\nConexiones:")
for usuario, amigos in red.items():
    print(f"  {usuario} ({amigos.cardinalidad()} amigos): {sorted(amigos.a_lista())}")

# 1. Amigos en común
print("\n" + "=" * 60)
print("1. AMIGOS EN COMÚN")
print("=" * 60)

pares = [("Ana", "Carlos"), ("Ana", "Gabriel"), ("Diana", "Fernanda")]
for u1, u2 in pares:
    comunes = red[u1].interseccion(red[u2])
    print(f"  {u1} y {u2}: {sorted(comunes.a_lista()) if not comunes.esta_vacio() else 'ninguno'}")

# 2. Sugerir amigos (amigos de amigos que no conoces)
print("\n" + "=" * 60)
print("2. SUGERENCIAS DE AMISTAD")
print("=" * 60)

for usuario in sorted(red.keys()):
    amigos_de_amigos = Conjunto()
    for amigo in red[usuario].a_lista():
        amigos_de_amigos = amigos_de_amigos.union(red[amigo])
    
    # Quitar al usuario mismo y sus amigos actuales
    sugerencias = amigos_de_amigos.diferencia(red[usuario]) #- {usuario}
    sugerencias = sugerencias.diferencia(Conjunto([usuario]))
    
    if not sugerencias.esta_vacio():
        print(f"  {usuario} → Sugerencias: {sorted(sugerencias.a_lista())}")

# 3. Usuarios sin amigos en común (disjuntos)
print("\n" + "=" * 60)
print("3. USUARIOS SIN AMIGOS EN COMÚN")
print("=" * 60)

usuarios = list(red.keys())
for i in range(len(usuarios)):
    for j in range(i + 1, len(usuarios)):
        u1, u2 = usuarios[i], usuarios[j]
        #Aqui un disjunto se puede representar si una interseccion esta vacia, osea que no compartan nada arre
        if red[u1].interseccion(red[u2]).esta_vacio(): 
            print(f"  {u1} y {u2} no tienen amigos en común")

# 4. Grado de conexión (amigos en común / total amigos)
print("\n" + "=" * 60)
print("4. GRADO DE CONEXIÓN")
print("=" * 60)

u1, u2 = "Ana", "Diana"
comunes = red[u1].interseccion(red[u2])
total = red[u1].union(red[u2])
grado = comunes.cardinalidad() / total.cardinalidad() if total else 0
print(f"  {u1} y {u2}:")
print(f"    Amigos en común: {sorted(comunes.a_lista())}")
print(f"    Total amigos: {sorted(total.a_lista())}")
print(f"    Grado de conexión: {grado:.2%}")

# 5. Usuario más conectado
print("\n" + "=" * 60)
print("5. USUARIO MÁS CONECTADO")
print("=" * 60)

ranking = []
for usuario, amigos in red.items():
    ranking.append((usuario, amigos.cardinalidad()))

ranking.sort(key=lambda x: x[1], reverse=True)

for i, (usuario, num_amigos) in enumerate(ranking, 1):
    barra = "█" * num_amigos
    print(f"  {i}. {usuario:10} {barra} ({num_amigos} amigos)")
