import timeit
from array import array

# ============================================================================
# PARTE 2: TEORÍA DE CONJUNTOS
# ============================================================================
print("\n" + "=" * 70)
print("PARTE 2: TEORÍA DE CONJUNTOS")
print("=" * 70)

# DEFINICIÓN
#   Un CONJUNTO es una colección NO ORDENADA de elementos ÚNICOS
#   (sin repeticiones), bien definidos (se puede decir con certeza si
#   un elemento pertenece o no al conjunto).
#
# FORMAS DE REPRESENTACIÓN
#   1) Por EXTENSIÓN: se listan todos los elementos.
#        A = {1, 2, 3, 4, 5}
#   2) Por COMPRENSIÓN: se describe una propiedad que cumplen los elementos.
#        A = {x | x es un número entero y 1 <= x <= 5}
#   3) Diagrama de VENN: representación gráfica con círculos/óvalos.
#
# NOTACIÓN CLAVE
#   x ∈ A     -> x pertenece a A
#   x ∉ A     -> x no pertenece a A
#   A ⊆ B     -> A es subconjunto de B (todo elemento de A está en B)
#   |A|       -> cardinalidad (número de elementos) de A
#   ∅ o {}    -> conjunto vacío
#
# EJEMPLOS
#   Matemático: P = {2, 3, 5, 7, 11, 13}  (números primos menores a 15)
#   Vida diaria: F = {"manzana", "pera", "uva"}  (frutas en mi nevera)
#                 E = {"Ana", "Luis", "Marta"}   (estudiantes que aprobaron)

print("\n--- 2.1 Conjuntos en Python (tipo set) ---")
P = {2, 3, 5, 7, 11, 13}          # conjunto matemático: primos < 15
F = {"manzana", "pera", "uva"}    # conjunto de la vida diaria: frutas
print("P (primos) :", P)
print("F (frutas) :", F)
print("3 in P?    :", 3 in P)     # pertenencia
print("|P| =      :", len(P))     # cardinalidad

# ----------------------------------------------------------------------
# 2.2 OPERACIONES BÁSICAS: Unión, Intersección, Diferencia, Complemento
# ----------------------------------------------------------------------
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
U = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}   # conjunto UNIVERSO para el complemento

print("\n--- 2.2 Operaciones (A y B) ---")
print("A =", A)
print("B =", B)

# UNIÓN (A ∪ B): todos los elementos que están en A, en B, o en ambos.
# Diagrama de Venn: se colorean COMPLETOS los dos círculos (A y B juntos).
print("Union         A ∪ B :", A | B)          # también: A.union(B)

# INTERSECCIÓN (A ∩ B): elementos que están en A Y en B simultáneamente.
# Diagrama de Venn: se colorea SOLO la zona donde los círculos se solapan.
print("Interseccion  A ∩ B :", A & B)          # también: A.intersection(B)

# DIFERENCIA (A - B): elementos que están en A pero NO en B.
# Diagrama de Venn: se colorea el círculo A EXCEPTO la zona de solape.
print("Diferencia    A - B :", A - B)          # también: A.difference(B)
print("Diferencia    B - A :", B - A)          # OJO: no es conmutativa

# DIFERENCIA SIMÉTRICA (A Δ B): elementos que están en A o en B, pero NO
# en ambos a la vez (unión menos la intersección).
# Diagrama de Venn: se colorean los dos círculos EXCEPTO el solape.
print("Dif. simetrica A Δ B:", A ^ B)          # también: A.symmetric_difference(B)

# COMPLEMENTO (A'): elementos del UNIVERSO que NO están en A.
# Requiere definir un conjunto universo U de referencia.
# Diagrama de Venn: se colorea TODO lo que está fuera del círculo A,
# dentro del rectángulo que representa el universo.
complemento_A = U - A
print("Universo U          :", U)
print("Complemento A' (U-A):", complemento_A)

# ----------------------------------------------------------------------
# 2.3 Diagramas de Venn descritos en texto (ASCII) para visualizar
# ----------------------------------------------------------------------
diagrama_venn = r"""
    UNIÓN (A ∪ B)                 INTERSECCIÓN (A ∩ B)
    ┌────────────────┐            ┌────────────────┐
    │▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓│            │        ░░░░    │
    │▓▓( A )(  B  )▓▓│            │   A   ░(∩)░  B │
    │▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓│            │        ░░░░    │
    └────────────────┘            └────────────────┘
    (todo sombreado)              (solo el solape sombreado)

    DIFERENCIA (A - B)             COMPLEMENTO (A')
    ┌────────────────┐            ┌──────────────────────┐
    │▓▓▓▓▓▓          │            │▓▓▓▓▓▓▓▓  ( A )  ▓▓▓▓▓▓│  <- rectángulo = U
    │▓( A )(  B  )   │            │▓▓▓▓▓▓▓▓          ▓▓▓▓▓│
    │▓▓▓▓▓▓          │            │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│
    └────────────────┘            └──────────────────────┘
    (A sin la parte que          (todo el universo sombreado
     comparte con B)              EXCEPTO el círculo A)
"""
print(diagrama_venn)

# ----------------------------------------------------------------------
# 2.4 MINI-CUESTIONARIO TIPO EXAMEN — Teoría de Conjuntos
# ----------------------------------------------------------------------
# P1) Si A = {1,2,3} y B = {3,4,5}, ¿cuánto es A ∩ B?
#     R1) {3}
#
# P2) ¿Cuál es la diferencia entre A - B y la diferencia simétrica A Δ B?
#     R2) A - B solo quita de A lo que está en B (unidireccional).
#         A Δ B es todo lo que está en A o en B pero no en ambos
#         (equivale a (A - B) ∪ (B - A)).
#
# P3) ¿Por qué el complemento necesita un conjunto universo U?
#     R3) Porque "todo lo que no está en A" solo tiene sentido si se
#         define un marco de referencia (universo) del cual A es
#         subconjunto; sin U, "no estar en A" sería infinito/indefinido.
#
# P4) ¿Es la diferencia de conjuntos conmutativa? Justifica.
#     R4) No. A - B ≠ B - A en general (salvo que A = B).


# ============================================================================
# PARTE 3: IMPLEMENTACIÓN PRÁCTICA DE CONJUNTOS
# ============================================================================
print("\n" + "=" * 70)
print("PARTE 3: IMPLEMENTACIÓN PRÁCTICA (VECTORES vs LISTAS)")
print("=" * 70)

# ----------------------------------------------------------------------
# 3.1 CONJUNTOS MEDIANTE VECTORES (ARRAYS)
# ----------------------------------------------------------------------
# Un "vector" (array) en sentido clásico de algoritmos es una estructura
# de TAMAÑO FIJO y TIPO HOMOGÉNEO en memoria contigua. En Python se
# simula con el módulo `array`, que es más cercano a un array de C que
# una lista (todos los elementos deben ser del mismo tipo, ej. 'i' int).
#
# IMPLEMENTACIÓN CLÁSICA "conjunto como vector de booleanos" (bitmap):
#   Si el universo es {0, 1, ..., n-1}, el conjunto se representa con
#   un vector de n booleanos: presente[i] = True si i pertenece al
#   conjunto. Esto es EXTREMADAMENTE eficiente para universos pequeños
#   y acotados (ej. conjuntos de letras del alfabeto, dígitos, etc.)

print("\n--- 3.1 Conjuntos como VECTOR de presencia (bitmap) ---")


def crear_conjunto_vector(tam_universo):
    """Crea un vector (array de enteros 0/1) que representará un conjunto
    sobre el universo {0, 1, ..., tam_universo - 1}."""
    # 'b' = signed char (1 byte), suficiente para guardar 0 o 1
    return array('b', [0]) * 0 or array('b', [0] * tam_universo)


def agregar_vector(vec, elemento):
    """Inserta un elemento en el conjunto-vector. O(1)."""
    vec[elemento] = 1


def pertenece_vector(vec, elemento):
    """Verifica pertenencia. O(1) -> ventaja clave del vector."""
    return vec[elemento] == 1


def union_vector(vecA, vecB):
    """Unión elemento a elemento (OR lógico). O(n) donde n = tam_universo."""
    resultado = array('b', [0]) * len(vecA)
    for i in range(len(vecA)):
        resultado[i] = 1 if (vecA[i] or vecB[i]) else 0
    return resultado


def interseccion_vector(vecA, vecB):
    """Intersección elemento a elemento (AND lógico). O(n)."""
    resultado = array('b', [0]) * len(vecA)
    for i in range(len(vecA)):
        resultado[i] = 1 if (vecA[i] and vecB[i]) else 0
    return resultado


def diferencia_vector(vecA, vecB):
    """A - B: está en A y NO está en B. O(n)."""
    resultado = array('b', [0]) * len(vecA)
    for i in range(len(vecA)):
        resultado[i] = 1 if (vecA[i] and not vecB[i]) else 0
    return resultado


def complemento_vector(vec):
    """Complemento respecto al universo completo del vector. O(n)."""
    resultado = array('b', [0]) * len(vec)
    for i in range(len(vec)):
        resultado[i] = 0 if vec[i] else 1
    return resultado


def vector_a_conjunto(vec):
    """Convierte el vector de presencia a un set de Python (para leerlo)."""
    return {i for i, presente in enumerate(vec) if presente}


# Demostración: universo = {0..9}
UNIVERSO_TAM = 10
vA = crear_conjunto_vector(UNIVERSO_TAM)
vB = crear_conjunto_vector(UNIVERSO_TAM)
for e in (1, 2, 3, 4, 5):
    agregar_vector(vA, e)
for e in (4, 5, 6, 7, 8):
    agregar_vector(vB, e)

print("vA representa:", vector_a_conjunto(vA))
print("vB representa:", vector_a_conjunto(vB))
print("Union         :", vector_a_conjunto(union_vector(vA, vB)))
print("Interseccion  :", vector_a_conjunto(interseccion_vector(vA, vB)))
print("Diferencia A-B:", vector_a_conjunto(diferencia_vector(vA, vB)))
print("Complemento A :", vector_a_conjunto(complemento_vector(vA)))

# ----------------------------------------------------------------------
# 3.2 CONJUNTOS MEDIANTE LISTAS
# ----------------------------------------------------------------------
# Aquí el conjunto se representa como una LISTA de elementos (sin
# duplicados, mantenida "a mano"), NO como un vector de presencia.
# Esto es más parecido a como se implementaría un conjunto en un
# lenguaje sin arrays tipados nativos, o cuando el universo es muy
# grande / no numérico (ej. conjuntos de strings).

print("\n--- 3.2 Conjuntos como LISTA de elementos ---")


def agregar_lista(lista, elemento):
    """Inserta el elemento solo si no existe (evita duplicados).
    O(n) porque hay que recorrer la lista para verificar 'in'."""
    if elemento not in lista:      # búsqueda lineal: O(n)
        lista.append(elemento)


def pertenece_lista(lista, elemento):
    """Verifica pertenencia. O(n) -> DESVENTAJA frente al vector,
    que es O(1)."""
    return elemento in lista


def union_lista(listaA, listaB):
    """Unión: todos los elementos de A, más los de B que no estén ya."""
    resultado = list(listaA)                 # copia de A: O(n)
    for elemento in listaB:                  # recorre B: O(m)
        if elemento not in resultado:         # búsqueda lineal: O(n)
            resultado.append(elemento)
    return resultado                          # total: O(n*m) peor caso


def interseccion_lista(listaA, listaB):
    """Intersección: elementos de A que también están en B."""
    return [elemento for elemento in listaA if elemento in listaB]


def diferencia_lista(listaA, listaB):
    """A - B: elementos de A que NO están en B."""
    return [elemento for elemento in listaA if elemento not in listaB]


def complemento_lista(universo, lista):
    """Complemento respecto a una lista-universo dada explícitamente
    (con listas no hay 'tamaño de universo' implícito como con el
    vector, así que el universo se debe pasar como parámetro)."""
    return [elemento for elemento in universo if elemento not in lista]


# Demostración con conjuntos NO numéricos (algo que el vector-bitmap
# NO podría hacer directamente sin antes mapear cada string a un índice)
frutasA = ["manzana", "pera", "uva"]
frutasB = ["pera", "kiwi", "mango"]
universo_frutas = ["manzana", "pera", "uva", "kiwi", "mango", "piña"]

print("Lista A       :", frutasA)
print("Lista B       :", frutasB)
print("Union         :", union_lista(frutasA, frutasB))
print("Interseccion  :", interseccion_lista(frutasA, frutasB))
print("Diferencia A-B:", diferencia_lista(frutasA, frutasB))
print("Complemento A :", complemento_lista(universo_frutas, frutasA))

# ----------------------------------------------------------------------
# 3.3 VECTORES vs LISTAS: diferencias de rendimiento y lógica
# ----------------------------------------------------------------------
comparacion = """
--- 3.3 Comparación de enfoques ---

  VECTOR (bitmap de presencia)
    + Pertenencia:      O(1)  (acceso directo por índice)
    + Unión/Intersec.:  O(n)  donde n = tamaño del universo (recorrido fijo)
    + Muy eficiente en memoria y tiempo SI el universo es pequeño y
      los elementos son enteros consecutivos (o mapeables a índices).
    - Requiere conocer o fijar el tamaño del universo de antemano.
    - No sirve directamente para datos no numéricos (strings, objetos)
      sin antes construir un mapeo elemento -> índice.

  LISTA (colección dinámica de elementos)
    + Flexible: crece dinámicamente, admite cualquier tipo de dato
      (strings, tuplas, objetos), no necesita conocer el universo.
    - Pertenencia:      O(n)  (hay que recorrer para buscar)
    - Unión/Intersec.:  O(n*m) en el peor caso (por cada elemento de una
      lista se busca linealmente en la otra)
    - Para universos grandes, es notablemente más lenta que el vector.

  ¿Y el 'set' nativo de Python (Parte 2)?
    Internamente usa una TABLA HASH: pertenencia e inserción son O(1)
    en promedio, SIN necesitar que el universo sea numérico ni acotado.
    Por eso en código real de producción se usa `set`, y los vectores
    o listas "hechas a mano" se estudian para entender CÓMO funciona
    un conjunto por dentro (fines académicos / de examen).
"""
print(comparacion)

# ----------------------------------------------------------------------
# 3.4 Benchmark rápido: lista vs vector vs set nativo (pertenencia)
# ----------------------------------------------------------------------
print("--- 3.4 Benchmark de pertenencia (elemento in estructura) ---")
n = 5000
lista_grande = list(range(n))
vector_grande = array('i', range(n))
set_grande = set(range(n))
buscado = n - 1   # peor caso para lista/vector: está al final

t_lista = timeit.timeit(lambda: buscado in lista_grande, number=1000)
t_vector = timeit.timeit(lambda: buscado in vector_grande, number=1000)
t_set = timeit.timeit(lambda: buscado in set_grande, number=1000)

print(f"  Lista  (búsqueda lineal) : {t_lista:.6f} s / 1000 búsquedas")
print(f"  Vector (búsqueda lineal) : {t_vector:.6f} s / 1000 búsquedas")
print(f"  Set    (tabla hash)      : {t_set:.6f} s / 1000 búsquedas")
print("  -> El set nativo debería ser órdenes de magnitud más rápido.")
