"""
═══════════════════════════════════════════════════════════════════════════════
        TALLER: ANÁLISIS DE ALGORITMOS
        Algoritmos y Programación 4
═══════════════════════════════════════════════════════════════════════════════

INSTRUCCIONES GENERALES:
------------------------
- Entregar archivo .py con todas las secciones resueltas
- El código debe ejecutar sin errores

DISTRIBUCIÓN:
- Sección A: Análisis teórico (1.0)         
- Sección B: Investigación (0.5)             
- Sección C: Resolver y optimizar (2.0)      
- Sección D: Proponer y justificar (1.5)     

═══════════════════════════════════════════════════════════════════════════════
"""

import time
import random


# ═══════════════════════════════════════════════════════════════════════════════
#                    SECCIÓN A: ANÁLISIS TEÓRICO (1.0)
#                         
# ═══════════════════════════════════════════════════════════════════════════════

"""
PUNTO A.1 (0.4): Clasificar complejidad

Para cada función, escribe:
  - La complejidad Big-O
  - UNA línea explicando por qué

Escribe tus respuestas como comentarios debajo de cada función.
"""


def alpha(lista):
    total = 0
    for x in lista:
        total += x
    promedio = total / len(lista)
    return promedio

# Complejidad: O(n) -- lineal
# Porque: Debido a que el ciclo depende de la entrada de la funcion por lo que se repite n veces


def beta(lista):
    for i in range(len(lista)):
        for j in range(len(lista)):
            if lista[i] == lista[j] and i != j:
                return True
    return False

# Complejidad: O(n^2)
# Porque: En este caso es porque los ciclos anidados dependes de la entrada de la funcion


def gamma(n):
    if n <= 1:
        return 1
    return gamma(n // 2) + 1

# Complejidad: O(log n)
# Porque: Pese a que el ciclo tambien depende de la entrada de la funcion esta entrada va disminuyendo de forma logaritmica


def delta(lista):
    resultado = set()
    for x in lista:
        resultado.add(x)
    return resultado

# Complejidad: O(n)
# Porque: Misma razon que el primero, el ciclo depende de la entrada de la funcion


def epsilon(lista):
    for x in lista:
        if x in lista:
            pass

# Complejidad: O(n^2)
# Porque: La pista es clave, en este caso el primer ciclo depende de la entrada, pero el if tambien, ya que en el peor de los casos debe recorrer toda la lista para encontrar el resultado
# PISTA: ¿cuánto cuesta `x in lista`?


def zeta(n):
    for i in range(n):
        j = 1
        while j < n:
            j *= 3

# Complejidad: O(n log n)
# Porque: Aunque ambos ciclos dependen de la entrada, en una su crecimiento el lineal al rango de la entrada, pero en el otro su crecimiento es de forma logaritmica, porque el crecimiento de j es exponencial


def eta(lista):
    if len(lista) <= 1:
        return lista
    medio = len(lista) // 2
    izq = eta(lista[:medio])
    der = eta(lista[medio:])
    return izq + der

# Complejidad: O(n log n)
# Porque: ___
# PISTA: ¿cuánto cuesta lista[:medio]?


def theta(n):
    i = 1
    while i * i <= n:
        i += 1
    return i

# Complejidad: O(√n) or O(log(log n))
# Porque: Es debido a que el crecimiento de i funciona como una raiz, tambien en cualquien caso donde la condicion se multiplica por ella misma seria log de log


"""
PUNTO A.2 (0.3): Ordenar de menor a mayor complejidad

Ordena las siguientes complejidades de la MÁS RÁPIDA a la MÁS LENTA:

O(n!), O(1), O(n log n), O(2^n), O(n²), O(log n), O(n), O(n³), O(√n)

Tu respuesta (de más rápida a más lenta):
1. O(1)
2. O(log n)
3. O(√n)
4. O(n log n)
5. O(n)
6. O(n^2)
7. O(n^3)
8. O(2^n)
9. O(n!)
"""


"""
PUNTO A.3 (0.3): Verdadero o Falso

Escribe V o F y justifica brevemente las falsas.

1. (F) O(2n) es más lento que O(n)
   Justificación: Las contantes se ignoran

2. (F) Un algoritmo O(n²) siempre es más lento que uno O(n log n)
   Justificación:En un escenario donde n sea pequeña, un algoritmo O(n^2) puede ser mas rapido que O(n log n)

3. (F) Si un algoritmo tiene un for de n y dentro un for de 5,
       su complejidad es O(n²)
   Justificación: No porque solo uno de los for depende de la entrada de la funcion, el otro es constante

4. (F) `x in set` tiene la misma complejidad que `x in list`
   Justificación: No porque un in en lista la debe recorrer si o si por lo que su complejidad es O(n), mientras que en un conjunto no, ahi encuentra directamente el dato por lo que su complejidad es O(1)

5. (F) Un algoritmo recursivo que se llama a sí mismo 2 veces
       siempre es O(2^n)
   Justificación: Depende de cuánto se reduce el problema en cada llamada; no siempre genera complejidad exponencial

6. (F) O(n) + O(n²) = O(n³)
   Justificación: O(n) + O(n²) = O(n²), porque domina el término de mayor crecimiento   

7. (V) La complejidad espacial de un algoritmo in-place es O(1)
   Justificación: Un algoritmo in-place tiene complejidad espacial O(1) porque no utiliza estructuras auxiliares proporcionales al tamaño de la entrada

8. (V) Memorización mejora la complejidad temporal pero empeora la espacial
   Justificación: Porque guarda resultados intermedios en memoria para evitar recomputarlos
"""


# ═══════════════════════════════════════════════════════════════════════════════
#                    SECCIÓN B: INVESTIGACIÓN (0.5)
#                         
# ═══════════════════════════════════════════════════════════════════════════════

"""
PUNTO B.1 (0.25): Complejidad de operaciones de Python

Investiga y completa la tabla con la complejidad de cada operación.
Agrega una justificación de por qué es la complejidad.
Puedes consultar: https://wiki.python.org/moin/TimeComplexity

┌──────────────────────────────┬──────────────┬──────────────┐
│ Operación                    │ Lista []     │ Set/Dict {}  │
├──────────────────────────────┼──────────────┼──────────────┤
│ Acceder por índice [i]       │ O(1)         │ N/A          │
│ Buscar elemento (x in ...)   │ O(n)         │ O(1)*        │
│ Agregar al final (.append)   │ O(1)*        │ O(1)* (.add) │
│ Insertar al inicio           │ O(n)         │ N/A          │
│ Eliminar por valor (.remove) │ O(n)         │ O(1)*        │
│ Obtener longitud (len)       │ O(1)         │ O(1)         │
│ Ordenar (.sort / sorted)     │ O(n log n)   │ N/A          │
│ Copiar (.copy / [:])         │ O(n)         │ O(n)         │
└──────────────────────────────┴──────────────┴──────────────┘
-- El * significa que su complejidad general puede ser diferente a la complejidad de su peor caso.

Justificacion

-- Acceder por índice [i]
    Lista: O(1)
    El acceso por índice en una lista es constante porque los elementos se almacenan en posiciones contiguas de memoria,
    lo que permite calcular directamente la dirección del elemento sin necesidad de recorrer la estructura.

    Set/Dict: N/A
    No aplica, ya que estas estructuras no manejan acceso por posición o índice.

-- Buscar elemento (x in ...)
    Lista: O(n)
    La búsqueda en una lista es lineal porque puede ser necesario recorrer todos los elementos hasta encontrar el valor o determinar que no existe.

    *Set/Dict: O(1) **
    La búsqueda se realiza mediante una tabla hash, permitiendo acceso directo al elemento en tiempo constante promedio. 
    Sin embargo, en el peor caso puede degradarse a O(n) debido a colisiones.

-- Agregar al final (append / add)
    *Lista: O(1) **
    Insertar al final de una lista es constante en promedio, ya que normalmente hay espacio disponible; sin embargo, 
    cuando la lista se redimensiona, se requiere copiar todos los elementos, lo que implica un costo O(n) ocasional.
    
    *Set/Dict: O(1) **
    La inserción se realiza utilizando una función hash que permite ubicar rápidamente la posición del elemento,
    aunque puede degradarse en presencia de colisiones o redimensionamientos.

-- Insertar al inicio
    Lista: O(n)
    Insertar un elemento al inicio implica desplazar todos los elementos existentes una posición hacia la derecha, 
    lo que requiere recorrer toda la lista.
    
    Set/Dict: N/A
    No aplica, ya que estas estructuras no tienen un orden posicional que permita definir un inicio.

-- Eliminar por valor (remove)
    Lista: O(n)
    Primero es necesario localizar el elemento mediante una búsqueda lineal, y posteriormente reorganizar los elementos restantes, 
    lo que implica un costo total lineal.
    
    *Set/Dict: O(1) **
    La eliminación se realiza directamente mediante el hash del elemento, permitiendo un acceso rápido en promedio, 
    aunque puede degradarse en casos de colisiones.

-- Obtener longitud (len)
    Lista: O(1)
    La longitud se almacena internamente en la estructura, por lo que no es necesario recorrer los elementos para calcularla.

    Set/Dict: O(1)
    De igual manera, estas estructuras mantienen un contador interno del número de elementos.

-- Ordenar (sort / sorted)
    Lista: O(n log n)
    El algoritmo de ordenamiento utilizado (Timsort) divide la lista en partes más pequeñas y luego las combina ordenadamente, 
    lo que implica un costo de n log n.

    Set/Dict: N/A
    No aplica, ya que estas estructuras no están diseñadas para mantener un orden de sus elementos.

-- Copiar (copy / [:])
    Lista: O(n)
    Copiar una lista implica recorrer todos sus elementos para crear una nueva estructura con los mismos valores.

    Set/Dict: O(n)
    De forma similar, copiar un conjunto o diccionario requiere iterar sobre todos sus elementos.
"""


"""
    PUNTO B.2 (0.25): Caso real

    Investiga y responde:

    1. ¿Qué algoritmo de ordenamiento usa Python internamente (sorted/list.sort)?
    Respuesta: Timsort
    Python utiliza Timsort, un algoritmo híbrido basado en Merge Sort + Insertion Sort, diseñado específicamente para datos del mundo real.

    2. ¿Cuál es su complejidad en el mejor, peor y caso promedio?
    Mejor: O(n)
    Peor: O(n log n)
    Promedio: O(n log n)
    
    Justificación breve:
    Mejor caso (O(n)): cuando la lista ya está ordenada o casi ordenada.
    Peor y promedio (O(n log n)): debido a la división y combinación de sublistas.

    3. ¿Por qué Python eligió ese algoritmo y no Quick Sort?
    Respuesta: Python eligió Timsort porque es más eficiente en datos reales, es estable y garantiza un rendimiento O(n log n) en el peor caso.
    A diferencia de Quick Sort, que puede degradarse a O(n²) en el peor caso, Timsort aprovecha secuencias ya ordenadas y ofrece mejor desempeño práctico.
"""


# ═══════════════════════════════════════════════════════════════════════════════
#                SECCIÓN C: RESOLVER Y OPTIMIZAR (2.0)
#                         
# ═══════════════════════════════════════════════════════════════════════════════

"""
En cada problema:
1. Analiza la versión LENTA y escribe su complejidad
2. Implementa la versión RÁPIDA
3. Escribe la complejidad de tu versión
4. Ejecuta las pruebas para verificar que funciona
"""


# ─── PROBLEMA C.1 (0.4): Elementos únicos ────────────────────────────────────

def unicos_lento(lista):
    """
    Retorna lista sin duplicados manteniendo el orden.
    COMPLEJIDAD: O(n^2)  ← analiza y escribe
    """
    resultado = []
    for x in lista:
        if x not in resultado:
            resultado.append(x)
    return resultado


def unicos_rapido(lista):
    """
    Misma funcionalidad pero más eficiente.
    USA un set auxiliar para búsqueda O(1).

    TODO: Implementar
    Complejidad: O(n)
    Porque: Se recorre la lista una sola vez y las operaciones en set son O(1) en promedio
    """
    vistos = set()
    resultado = []
    for x in lista:
        if x not in vistos:
            vistos.add()
            resultado.append(x)
    return resultado


# ─── PROBLEMA C.2 (0.4): Frecuencia del más común ────────────────────────────

def mas_comun_lento(lista):
    """
    Retorna el elemento que más se repite y cuántas veces.
    COMPLEJIDAD: O(n^2)  ← analiza y escribe
    """
    max_elem = None
    max_count = 0
    for x in lista:
        count = 0
        for y in lista:
            if y == x:
                count += 1
        if count > max_count:
            max_count = count
            max_elem = x
    return max_elem, max_count


def mas_comun_rapido(lista):
    """
    Misma funcionalidad usando diccionario contador.

    TODO: Implementar
    Complejidad: O(n)
    Porque: Se recorre la lista una vez para contar frecuencias (O(n)) y luego se recorre el diccionario (O(n)), resultando en O(n) total
    """
    conteo = {}
    for x in lista:
        conteo[x] = conteo.get(x, 0) + 1
    max_elem = None
    max_count = 0
    for x in conteo:
        if conteo[x] > max_count:
            max_count = conteo[x]
            max_elem = x 
    return max_elem, max_count

    


# ─── PROBLEMA C.3 (0.4): Pares que suman K ───────────────────────────────────

def pares_suma_lento(lista, k):
    """
    Retorna todos los pares (i, j) donde lista[i] + lista[j] == k.
    COMPLEJIDAD: O(n^2)  ← analiza y escribe
    """
    pares = []
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == k:
                pares.append((lista[i], lista[j]))
    return pares


def pares_suma_rapido(lista, k):
    """
    Misma funcionalidad usando set para buscar complementos.

    Estrategia:
    - Para cada x, el complemento es k - x
    - Si el complemento ya está en un set de "vistos", es un par

    TODO: Implementar
    Complejidad: O(n)
    Porque: Se recorre la lista una sola vez y cada búsqueda en el set es O(1) en promedio
    """
    vistos = set()
    pares = []
    for x in lista:
        complemento = k - x
        if  complemento in vistos:
            pares.append((complemento,x))
        vistos.add(x)
    return pares



# ─── PROBLEMA C.4 (0.4): Anagramas ───────────────────────────────────────────

def son_anagramas_lento(palabra1, palabra2):
    """
    Verifica si dos palabras son anagramas (mismas letras, diferente orden).
    COMPLEJIDAD: O(n log n)  ← analiza y escribe
    Este me confundio pero ahora entendi que en el peor de los casos al usar el sorted la complejidad es O(n log nx)
    """
    if len(palabra1) != len(palabra2):
        return False
    return sorted(palabra1) == sorted(palabra2)


def son_anagramas_rapido(palabra1, palabra2):
    """
    Misma funcionalidad sin ordenar.

    Estrategia: contar frecuencia de cada letra con diccionario.

    TODO: Implementar
    Complejidad: O(n)
    Porque: se recorren ambas palabras una sola vez y las operaciones en diccionario son O(1) en promedio
    """
    if len(palabra1) != len(palabra2):
        return False
    conteo = {}
    for c in palabra1:
        conteo[c] = conteo.get(c, 0) + 1
    for c in palabra2:
        if c not in conteo: 
            return False
        conteo[c] -= 1
        if conteo[c] == 0:
            del conteo[c]
    return len(conteo) == 0


# ─── PROBLEMA C.5 (0.4): Subarray de suma máxima ─────────────────────────────

def max_subarray_lento(lista):
    """
    Encuentra la suma máxima de un subarray contiguo.
    Ejemplo: [-2, 1, -3, 4, -1, 2, 1, -5, 4] → 6 (subarray [4, -1, 2, 1])

    COMPLEJIDAD: O(n^3)  ← analiza y escribe
    """
    n = len(lista)
    max_suma = lista[0]
    for i in range(n):
        for j in range(i, n):
            suma = 0
            for k in range(i, j + 1):
                suma += lista[k]
            max_suma = max(max_suma, suma)
    return max_suma


def max_subarray_rapido(lista):
    """
    Algoritmo de Kadane: un solo recorrido.

    Idea: mantener la suma actual. Si se vuelve negativa, reiniciar.
    - suma_actual = max(x, suma_actual + x)
    - max_suma = max(max_suma, suma_actual)

    TODO: Implementar
    Complejidad: O(n)
    Porque: Se recorre la lista una sola vez realizando operaciones constantes en cada iteración
    """
    suma_actual = lista[0]
    max_suma = lista[0]
    
    for x in lista[1:]:
        suma_actual = max(x, suma_actual + x)
        max_suma = max(max_suma, suma_actual)
    
    return max_suma


# ═══════════════════════════════════════════════════════════════════════════════
#                SECCIÓN D: PROPONER Y JUSTIFICAR (1.5)
#                         
# ═══════════════════════════════════════════════════════════════════════════════

"""
PUNTO D.1 (0.5): Diseñar un algoritmo

PROBLEMA: Sistema de autocompletado
Un buscador tiene una lista de 1 millón de palabras. Cuando el usuario
escribe las primeras letras, debe mostrar las 5 palabras que empiezan
con ese prefijo.

Ejemplo:
  palabras = ["python", "programar", "programa", "prueba", "pizza", ...]
  autocompletar("pro") → ["programar", "programa"]

Propón DOS soluciones con diferente complejidad:

SOLUCIÓN 1 (fuerza bruta):
  Descripción: Se recorre toda la lista de palabras y se seleccionan aquellas que comienzan con el prefijo dado, 
  deteniéndose cuando se encuentran 5 coincidencias.
  Complejidad: O(n)
  Código:
"""


def autocompletar_v1(palabras, prefijo):
    """
    Versión fuerza bruta.
    TODO: Implementar
    COMPLEJIDAD: O(n)
    """
    resultado = []
    for palabra in palabras:
        if palabra.startswith(prefijo):
            resultado.append(palabra)
            if len(resultado) == 5:
                break
    
    return resultado
  


"""
SOLUCIÓN 2 (optimizada):
Descripción:
Se utiliza búsqueda binaria para encontrar la primera palabra que coincide con el prefijo en una lista ordenada, 
y luego se toman las siguientes coincidencias.

Complejidad: O(log n)
¿Qué estructura de datos usarías? Lista ordenada
Código:
"""


def autocompletar_v2(palabras_ordenadas, prefijo):
    """
    Versión optimizada.
    PISTA: Si las palabras están ordenadas, puedes usar búsqueda binaria
    para encontrar dónde empiezan las que tienen el prefijo.

    TODO: Implementar
    COMPLEJIDAD: O(?)
    """
    izquierda = 0
    derecha = len(palabras) - 1
    inicio = -1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        
        if palabras[medio].startswith(prefijo):
            inicio = medio
            derecha = medio - 1 
        elif palabras[medio] < prefijo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    if inicio == -1:
        return []
    resultado = []
    i = inicio
    while i < len(palabras) and palabras[i].startswith(prefijo) and len(resultado) < 5:
        resultado.append(palabras[i])
        i += 1
    return resultado

"""
PUNTO D.2 (0.5): Analizar un sistema real

ESCENARIO: Red social con 10 millones de usuarios.
Cada usuario tiene una lista de amigos (promedio 200 amigos).

Analiza la complejidad de estas operaciones y propón la mejor
estructura de datos para cada una:

1. Verificar si dos usuarios son amigos
    - Con lista de amigos: O(n)
    - Con set de amigos: O(1)
    - ¿Cuál elegirías? Set

2. Encontrar amigos en común entre dos usuarios
   - Con listas: O(n²)
    - Con sets: O(n)
    - ¿Cuál elegirías? Set

3. Sugerir "personas que quizás conozcas" (amigos de amigos que no son tus amigos)
   - Describe tu algoritmo: Para un usuario, se recorren sus amigos y luego los amigos de esos amigos. 
   Se agregan a una estructura (como un set o diccionario) aquellos usuarios que no son amigos directos ni el propio usuario, 
   contando cuántas veces aparecen para priorizar sugerencias.
   - Complejidad estimada: O(n²)
   - ¿Es viable para 10M de usuarios? Sí, porque aunque es O(n²), n es pequeño (≈200), por lo que en la práctica es manejable.

4. Si cada usuario tiene en promedio 200 amigos y hay 10M de usuarios:
   - ¿Cuánta memoria ocupa almacenar TODAS las relaciones de amistad?
    Tenemos:
    10 millones usuarios -> 10^7
    200 amigos por usuario

    Total relaciones:
    10^7 * 200 relaciones
    Cada ID de usuario ocupa 4 bytes aproximadamente
   - Con lista: 4 bytes * 10^7 * 200 es aproximadamente 8 GB
   - Con set:  Son 16 GB aproximadamente debido a que un set() ocupa mas o menos el doble de almacenamiento que una lista.
"""


"""
PUNTO D.3 (0.5): Reflexión y comparación

Escribe un párrafo (mínimo 5 líneas) respondiendo:

¿Por qué es importante analizar la complejidad de un algoritmo
ANTES de implementarlo? Da un ejemplo concreto de un caso donde
elegir el algoritmo incorrecto podría causar problemas reales
(tiempo de espera, costos de servidor, mala experiencia de usuario, etc.)

Tu respuesta:
Analizar la complejidad de un algoritmo antes de implementarlo es fundamental porque permite anticipar cómo se comportará cuando el tamaño de los datos crezca, 
evitando soluciones que funcionen en pequeño pero fallen en escenarios reales. Elegir un algoritmo ineficiente puede provocar tiempos de respuesta muy altos, 
mayor consumo de recursos y costos elevados en servidores. Por ejemplo, si una red social utiliza un algoritmo O(n²) para buscar amigos en común entre millones de usuarios, 
el sistema podría volverse extremadamente lento o incluso colapsar. En cambio, usando estructuras como sets y algoritmos O(n), se mejora significativamente el rendimiento. 
En general, un buen análisis de complejidad permite tomar decisiones más inteligentes y construir sistemas escalables y eficientes.
"""


# ═══════════════════════════════════════════════════════════════════════════════
#                         CÓDIGO DE PRUEBA
# ═══════════════════════════════════════════════════════════════════════════════

def medir(funcion, *args):
    inicio = time.time()
    resultado = funcion(*args)
    return resultado, time.time() - inicio


if __name__ == "__main__":
    print("=" * 70)
    print("     TALLER: ANÁLISIS DE ALGORITMOS - PRUEBAS SECCIÓN C")
    print("=" * 70)

    # ── C.1: Únicos ──────────────────────────────────────────────
    print("\n" + "─" * 70)
    print("C.1: ELEMENTOS ÚNICOS")
    print("─" * 70)

    for n in [1000, 5000, 10000]:
        lista = [random.randint(1, n // 2) for _ in range(n)]

        r1, t1 = medir(unicos_lento, lista)
        r2, t2 = medir(unicos_rapido, lista) if unicos_rapido(lista) is not None else (None, 0)

        print(f"  n={n:>6}: lento={t1:.4f}s  rápido={t2:.4f}s", end="")
        if r2 is not None:
            print(f"  ✓ correcto" if r1 == r2 else f"  ✗ DIFERENTE")
        else:
            print("  (sin implementar)")

    # ── C.2: Más común ───────────────────────────────────────────
    print("\n" + "─" * 70)
    print("C.2: ELEMENTO MÁS COMÚN")
    print("─" * 70)

    for n in [500, 2000, 5000]:
        lista = [random.randint(1, 20) for _ in range(n)]

        r1, t1 = medir(mas_comun_lento, lista)
        r2, t2 = medir(mas_comun_rapido, lista) if mas_comun_rapido(lista) is not None else (None, 0)

        print(f"  n={n:>6}: lento={t1:.4f}s  rápido={t2:.4f}s", end="")
        if r2 is not None:
            print(f"  ✓" if r1 == r2 else f"  resultado: {r1} vs {r2}")
        else:
            print("  (sin implementar)")

    # ── C.3: Pares que suman K ───────────────────────────────────
    print("\n" + "─" * 70)
    print("C.3: PARES QUE SUMAN K")
    print("─" * 70)

    for n in [500, 2000, 5000]:
        lista = [random.randint(1, 100) for _ in range(n)]
        k = 50

        r1, t1 = medir(pares_suma_lento, lista, k)
        r2, t2 = medir(pares_suma_rapido, lista, k) if pares_suma_rapido(lista, k) is not None else (None, 0)

        print(f"  n={n:>6}: lento={t1:.4f}s  rápido={t2:.4f}s", end="")
        if r2 is not None:
            print(f"  pares encontrados: {len(r1)} vs {len(r2)}")
        else:
            print("  (sin implementar)")

    # ── C.4: Anagramas ───────────────────────────────────────────
    print("\n" + "─" * 70)
    print("C.4: ANAGRAMAS")
    print("─" * 70)

    casos_anagramas = [
        ("listen", "silent", True),
        ("hello", "world", False),
        ("anagram", "nagaram", True),
        ("python", "typhon", True),
        ("abc", "abcd", False),
    ]

    for p1, p2, esperado in casos_anagramas:
        r_lento = son_anagramas_lento(p1, p2)
        r_rapido = son_anagramas_rapido(p1, p2) if son_anagramas_rapido(p1, p2) is not None else "N/A"
        marca = "✓" if r_rapido == esperado else "✗"
        print(f"  {marca} '{p1}' vs '{p2}': lento={r_lento}, rápido={r_rapido}, esperado={esperado}")

    # ── C.5: Subarray máximo ─────────────────────────────────────
    print("\n" + "─" * 70)
    print("C.5: SUBARRAY DE SUMA MÁXIMA")
    print("─" * 70)

    casos_subarray = [
        [-2, 1, -3, 4, -1, 2, 1, -5, 4],
        [1, 2, 3, 4, 5],
        [-1, -2, -3, -4],
        [5, -9, 6, -2, 3],
    ]

    for lista in casos_subarray:
        r_lento = max_subarray_lento(lista)
        r_rapido = max_subarray_rapido(lista)
        marca = "✓" if r_rapido == r_lento else "✗"
        print(f"  {marca} {lista} → lento={r_lento}, rápido={r_rapido}")

    for n in [500, 2000, 5000]:
        lista = [random.randint(-50, 50) for _ in range(n)]
        r1, t1 = medir(max_subarray_lento, lista)
        r2, t2 = medir(max_subarray_rapido, lista) if max_subarray_rapido(lista) is not None else (None, 0)
        print(f"  n={n:>6}: lento={t1:.4f}s  rápido={t2:.4f}s")

    # ── D.1: Autocompletar ───────────────────────────────────────
    print("\n" + "─" * 70)
    print("D.1: AUTOCOMPLETAR")
    print("─" * 70)

    palabras = [f"palabra_{random.randint(1000, 9999)}" for _ in range(50000)]
    palabras.extend(["python", "programar", "programa", "prueba", "pizza",
                      "proyecto", "profesor", "promedio", "proceso", "producir"])
    random.shuffle(palabras)
    palabras_ord = sorted(palabras)

    for prefijo in ["pro", "pyt", "piz", "xyz"]:
        r1, t1 = medir(autocompletar_v1, palabras, prefijo) if autocompletar_v1(palabras, prefijo) is not None else (None, 0)
        r2, t2 = medir(autocompletar_v2, palabras_ord, prefijo) if autocompletar_v2(palabras_ord, prefijo) is not None else (None, 0)

        print(f"  Prefijo '{prefijo}': v1={t1:.4f}s  v2={t2:.4f}s", end="")
        if r1:
            print(f"  → {len(r1)} resultados")
        else:
            print("  (sin implementar)")
