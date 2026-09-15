"""
═══════════════════════════════════════════════════════════════════════════════
CASO DE USO 2: UNIVERSIDAD - CRUCE DE HORARIOS
Algoritmos y Programación 4 - Semana 6
═══════════════════════════════════════════════════════════════════════════════

ENUNCIADO:
----------
La universidad necesita un sistema para analizar la matrícula de estudiantes.
Dados los estudiantes inscritos en diferentes materias, el sistema debe:

1. Encontrar estudiantes que cursan ambas materias (para evitar cruces)
2. Encontrar estudiantes que solo cursan una materia
3. Total de estudiantes únicos entre todas las materias
4. Verificar si todos los de una materia están en otra
5. Encontrar estudiantes que cursan las 3 materias

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
    
algoritmos = {
    "Ana", "Carlos", "Diana", "Eduardo", "Fernanda",
    "Gabriel", "Helena", "Ivan"
}

bases_datos = {
    "Carlos", "Diana", "Juan", "Karen",
    "Gabriel", "Luis", "Maria"
}

redes = {
    "Diana", "Eduardo", "Gabriel", "Karen",
    "Natalia", "Oscar", "Ivan"
}

a = Conjunto()
b = Conjunto()
r = Conjunto()

# ═══════════════════════════════════════════════════════════════════════════════
# SOLUCIÓN
# ═══════════════════════════════════════════════════════════════════════════════

print("=" * 60)
print("   UNIVERSIDAD - CRUCE DE HORARIOS")
print("=" * 60)

for c in sorted(algoritmos):
    a.agregar(c)

for c in sorted(bases_datos):
    b.agregar(c)

for c in sorted(redes):
    r.agregar(c)

print(f"\nAlgoritmos ({a.cardinalidad()}): {sorted(a.a_lista())}")
print(f"Bases de Datos ({b.cardinalidad()}): {sorted(b.a_lista())}")
print(f"Redes ({r.cardinalidad()}): {sorted(r.a_lista())}")

# 1. Estudiantes en Algoritmos Y Bases de Datos (posible cruce)
cruce_alg_bd = a.interseccion(b)
print(f"\n1. Cursan Algoritmos Y Bases de Datos: {sorted(cruce_alg_bd.a_lista())}")

cruce_alg_redes = a.interseccion(r)
print(f"   Cursan Algoritmos Y Redes: {sorted(cruce_alg_redes.a_lista())}")

cruce_bd_redes = b.interseccion(r)
print(f"   Cursan Bases de Datos Y Redes: {sorted(cruce_bd_redes.a_lista())}")

# 2. Estudiantes que SOLO cursan una materia
solo_algoritmos = a.diferencia(b)  
solo_algoritmos = solo_algoritmos.diferencia(r)
solo_bd = b.diferencia(a)
solo_bd = solo_bd.diferencia(r)
solo_redes = r.diferencia(a)
solo_redes = solo_redes.diferencia(b)

print(f"\n2. Solo Algoritmos: {sorted(solo_algoritmos.a_lista())}")
print(f"   Solo Bases de Datos: {sorted(solo_bd.a_lista())}")
print(f"   Solo Redes: {sorted(solo_redes.a_lista())}")

# 3. Total de estudiantes únicos
todos = a.union(b)
todos = todos.union(r)
print(f"\n3. Total estudiantes únicos: {todos.cardinalidad()}")
print(f"   Estudiantes: {sorted(todos.a_lista())}")

# 4. ¿Todos los de Algoritmos están en Bases de Datos?
print(f"\n4. ¿Algoritmos ⊆ Bases de Datos? {a.subconjunto(b)}")
print(f"   ¿Cruce Alg-BD ⊆ Algoritmos? {cruce_alg_bd.subconjunto(a)}")

# 5. Estudiantes en las 3 materias
en_las_tres = cruce_alg_bd.interseccion(r)
print(f"\n5. Cursan las 3 materias: {sorted(en_las_tres.a_lista())}")

# Bonus: Resumen por estudiante
print("\n" + "=" * 60)
print("RESUMEN POR ESTUDIANTE")
print("=" * 60)
for estudiante in sorted(todos.a_lista()):
    materias = []
    if estudiante in a.a_lista():
        materias.append("Algoritmos")
    if estudiante in b.a_lista():
        materias.append("BD")
    if estudiante in r.a_lista():
        materias.append("Redes")
    print(f"  {estudiante}: {', '.join(materias)} ({len(materias)} materias)")
