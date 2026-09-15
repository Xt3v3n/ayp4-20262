# =========================================================
# QUICK SORT
# =========================================================
#
# Quick Sort es un algoritmo de ordenamiento basado en:
#
# "Divide y vencerás"
#
# La idea principal es:
#
# 1. Escoger un pivote
# 2. Mover los números menores a la izquierda
# 3. Mover los números mayores a la derecha
# 4. Repetir el proceso en ambos lados
#
# ---------------------------------------------------------
# EJEMPLO
# ---------------------------------------------------------
#
# Arreglo:
#
# [7, 2, 9, 1, 5]
#
# Escogemos como pivote:
#
# 5
#
# Entonces reorganizamos:
#
# [2, 1] 5 [7, 9]
#
# Los menores quedaron a la izquierda
# Los mayores quedaron a la derecha
#
# IMPORTANTE:
#
# Quick Sort NO ordena todo de una vez.
#
# Solo coloca el pivote en su posición correcta.
#
# Luego aplica el mismo proceso:
#
# - al lado izquierdo
# - al lado derecho
#
# usando recursividad.
#
# ---------------------------------------------------------
# FUNCIÓN PARTITION
# ---------------------------------------------------------
#
# La función partition() es la parte más importante.
#
# Su trabajo es:
#
# 1. Escoger el pivote
# 2. Recorrer el arreglo
# 3. Mandar menores a la izquierda
# 4. Mandar mayores a la derecha
# 5. Colocar el pivote en el centro
#
# Al final devuelve:
#
# la posición final del pivote.
#
# ---------------------------------------------------------
# VARIABLES IMPORTANTES
# ---------------------------------------------------------
#
# low:
# índice inicial del fragmento del arreglo
#
# high:
# índice final del fragmento
#
# pivote:
# número usado para dividir
#
# i:
# marca el final de la zona de números menores
#
# j:
# recorre el arreglo buscando números menores
#
# ---------------------------------------------------------
# IDEA MENTAL
# ---------------------------------------------------------
#
# Quick Sort funciona como:
#
# "escoger un líder (pivote)
# y separar pequeños y grandes"
#
# Luego cada grupo vuelve a hacer lo mismo.
#
# ---------------------------------------------------------
# COMPLEJIDADES
# ---------------------------------------------------------
#
# Mejor caso:
#
# O(n log n)
#
# cuando el pivote divide bien el arreglo.
#
# Peor caso:
#
# O(n²)
#
# cuando el pivote divide muy mal.
#
# Ejemplo:
#
# arreglo ya ordenado y mal pivote.
#
# Espacio:
#
# O(log n)
#
# por la recursividad.
#
# ---------------------------------------------------------
# ESTABILIDAD
# ---------------------------------------------------------
#
# Quick Sort NO es estable.
#
# Porque elementos iguales
# pueden cambiar de posición.
#
# ---------------------------------------------------------
# VENTAJAS
# ---------------------------------------------------------
#
# - Muy rápido en la práctica
# - Muy usado en programación real
# - Excelente para arreglos grandes
#
# ---------------------------------------------------------
# DESVENTAJAS
# ---------------------------------------------------------
#
# - Puede volverse lento en el peor caso
# - Usa recursividad
# - No es estable
#
# =========================================================
def partition(arr, low, high):

    # escoger pivote
    pivote = arr[high]

    # índice del menor elemento
    i = low - 1

    # recorrer desde low hasta high-1
    for j in range(low, high):

        # si el elemento es menor o igual al pivote
        if arr[j] <= pivote:

            i += 1

            # intercambiar
            arr[i], arr[j] = arr[j], arr[i]

    # poner pivote en posición correcta
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    # devolver posición del pivote
    return i + 1


def quicksort(arr, low, high):

    # caso base
    if low < high:

        # organizar pivote
        pi = partition(arr, low, high)

        # izquierda del pivote
        quicksort(arr, low, pi - 1)

        # derecha del pivote
        quicksort(arr, pi + 1, high)




# =========================================================
# RADIX SORT
# =========================================================
#
# Radix Sort es un algoritmo que ordena números:
#
# "dígito por dígito"
#
# IMPORTANTE:
#
# Radix Sort NO compara números directamente.
#
# En vez de eso:
#
# 1. Ordena por unidades
# 2. Luego por decenas
# 3. Luego por centenas
# 4. Y así sucesivamente
#
# ---------------------------------------------------------
# EJEMPLO
# ---------------------------------------------------------
#
# Arreglo:
#
# [170, 45, 75, 90]
#
# ---------------------------------------------------------
# PASO 1 → unidades
# ---------------------------------------------------------
#
# 170 → 0
# 45  → 5
# 75  → 5
# 90  → 0
#
# Ordenado por unidades:
#
# [170, 90, 45, 75]
#
# ---------------------------------------------------------
# PASO 2 → decenas
# ---------------------------------------------------------
#
# 170 → 7
# 90  → 9
# 45  → 4
# 75  → 7
#
# Resultado:
#
# [45, 170, 75, 90]
#
# ---------------------------------------------------------
# PASO 3 → centenas
# ---------------------------------------------------------
#
# 45  → 0
# 170 → 1
# 75  → 0
# 90  → 0
#
# Resultado final:
#
# [45, 75, 90, 170]
#
# ---------------------------------------------------------
# IDEA IMPORTANTE
# ---------------------------------------------------------
#
# Radix Sort funciona porque:
#
# el orden anterior NO se destruye.
#
# Por eso necesita usar
# un algoritmo ESTABLE.
#
# Normalmente usa:
#
# Counting Sort
#
# ---------------------------------------------------------
# ¿QUÉ ES exp?
# ---------------------------------------------------------
#
# exp representa el dígito actual.
#
# exp = 1
#
# → unidades
#
# exp = 10
#
# → decenas
#
# exp = 100
#
# → centenas
#
# ---------------------------------------------------------
# LÍNEA MÁS IMPORTANTE
# ---------------------------------------------------------
#
# (arr[i] // exp) % 10
#
# Esta fórmula extrae el dígito actual.
#
# ---------------------------------------------------------
# EJEMPLO
# ---------------------------------------------------------
#
# Número:
#
# 170
#
# Si exp = 1:
#
# 170 // 1 = 170
#
# 170 % 10 = 0
#
# → unidades
#
# ---------------------------------------------------------
#
# Si exp = 10:
#
# 170 // 10 = 17
#
# 17 % 10 = 7
#
# → decenas
#
# ---------------------------------------------------------
#
# Si exp = 100:
#
# 170 // 100 = 1
#
# 1 % 10 = 1
#
# → centenas
#
# ---------------------------------------------------------
# COMPLEJIDADES
# ---------------------------------------------------------
#
# Tiempo:
#
# O(d(n+k))
#
# donde:
#
# d = cantidad de dígitos
# n = cantidad de números
# k = rango de dígitos
#
# En la práctica suele ser muy rápido.
#
# Espacio:
#
# O(n+k)
#
# porque usa arreglos auxiliares.
#
# ---------------------------------------------------------
# ESTABILIDAD
# ---------------------------------------------------------
#
# Radix Sort SÍ es estable.
#
# Mantiene el orden original
# de elementos iguales.
#
# ---------------------------------------------------------
# VENTAJAS
# ---------------------------------------------------------
#
# - Muy rápido para enteros
# - No usa comparaciones
# - Excelente para números grandes
#
# ---------------------------------------------------------
# DESVENTAJAS
# ---------------------------------------------------------
#
# - Más difícil de entender
# - Consume memoria extra
# - No sirve bien con decimales
#
# =========================================================
def counting_sort(arr, exp):

    n = len(arr)

    output = [0] * n

    count = [0] * 10

    # contar ocurrencias
    for i in range(n):

        index = (arr[i] // exp) % 10

        count[index] += 1

    # acumular posiciones
    for i in range(1, 10):

        count[i] += count[i - 1]

    # construir arreglo ordenado
    i = n - 1

    while i >= 0:

        index = (arr[i] // exp) % 10

        output[count[index] - 1] = arr[i]

        count[index] -= 1

        i -= 1

    # copiar resultado
    for i in range(n):

        arr[i] = output[i]


def radix_sort(arr):

    maximo = max(arr)

    exp = 1

    while maximo // exp > 0:

        counting_sort(arr, exp)

        exp *= 10

    return arr

# =========================================================
# BUCKET SORT
# =========================================================
#
# Bucket Sort es un algoritmo de ordenamiento que funciona:
#
# "dividiendo los datos en grupos llamados buckets
# (cubetas o baldes)"
#
# La idea principal es:
#
# 1. Dividir los números en buckets
# 2. Ordenar cada bucket individualmente
# 3. Unir todos los buckets
#
# ---------------------------------------------------------
# IDEA GENERAL
# ---------------------------------------------------------
#
# En vez de ordenar todo el arreglo directamente,
# Bucket Sort separa los números según rangos.
#
# Por ejemplo:
#
# Bucket 0 → números pequeños
# Bucket 1 → números medianos
# Bucket 2 → números grandes
#
# Luego cada grupo se ordena por separado.
#
# ---------------------------------------------------------
# EJEMPLO
# ---------------------------------------------------------
#
# Arreglo:
#
# [29, 25, 3, 49, 9, 37, 21]
#
# Supongamos buckets:
#
# 0-9
# 10-19
# 20-29
# 30-39
# 40-49
#
# Entonces:
#
# Bucket 0 → [3, 9]
# Bucket 1 → []
# Bucket 2 → [29, 25, 21]
# Bucket 3 → [37]
# Bucket 4 → [49]
#
# Luego se ordena cada bucket:
#
# [3,9]
# []
# [21,25,29]
# [37]
# [49]
#
# Finalmente se unen:
#
# [3, 9, 21, 25, 29, 37, 49]
#
# ---------------------------------------------------------
# IDEA IMPORTANTE
# ---------------------------------------------------------
#
# Bucket Sort NO ordena directamente.
#
# Primero:
#
# divide los datos en grupos.
#
# Luego:
#
# ordena grupos pequeños.
#
# Finalmente:
#
# une todos los resultados.
#
# ---------------------------------------------------------
# ¿QUÉ ES UN BUCKET?
# ---------------------------------------------------------
#
# Un bucket es simplemente:
#
# una lista o contenedor
# donde se guardan números similares.
#
# Ejemplo:
#
# Bucket de números entre 20 y 29:
#
# [21,25,29]
#
# ---------------------------------------------------------
# FÓRMULA MÁS IMPORTANTE
# ---------------------------------------------------------
#
# index = (num * num_buckets) // (maximo + 1)
#
# Esta fórmula calcula:
#
# "a qué bucket pertenece un número"
#
# ---------------------------------------------------------
# EJEMPLO DE LA FÓRMULA
# ---------------------------------------------------------
#
# num = 29
# maximo = 49
# num_buckets = 5
#
# Paso 1:
#
# 29 * 5 = 145
#
# Paso 2:
#
# 145 // 50 = 2
#
# Entonces:
#
# 29 pertenece al bucket 2.
#
# ---------------------------------------------------------
# ORDENAMIENTO INTERNO
# ---------------------------------------------------------
#
# Cada bucket normalmente se ordena usando:
#
# - Insertion Sort
# - QuickSort
# - MergeSort
# - sort()
#
# Bucket Sort realmente funciona porque:
#
# ordenar pequeños grupos
# es más fácil que ordenar uno gigante.
#
# ---------------------------------------------------------
# COMPLEJIDADES
# ---------------------------------------------------------
#
# Mejor caso:
#
# O(n + k)
#
# cuando los datos están bien distribuidos.
#
# Promedio:
#
# O(n + k)
#
# Peor caso:
#
# O(n²)
#
# cuando todos los elementos
# caen en el mismo bucket.
#
# Espacio:
#
# O(n + k)
#
# porque necesita memoria extra
# para crear los buckets.
#
# ---------------------------------------------------------
# ESTABILIDAD
# ---------------------------------------------------------
#
# Bucket Sort puede ser estable.
#
# DEPENDE del algoritmo usado
# para ordenar cada bucket.
#
# Si el algoritmo interno es estable:
#
# ✅ Bucket Sort es estable.
#
# Si no:
#
# ❌ no será estable.
#
# ---------------------------------------------------------
# VENTAJAS
# ---------------------------------------------------------
#
# - Muy rápido con datos bien distribuidos
# - Fácil de paralelizar
# - Bueno para números en rangos conocidos
#
# ---------------------------------------------------------
# DESVENTAJAS
# ---------------------------------------------------------
#
# - Consume memoria extra
# - Depende mucho de la distribución
# - Puede volverse lento en el peor caso
# - Si los elementos son variables, los buckets no estaran bien distrubuidos
#
# =========================================================

def bucket_sort(arr):

    # encontrar máximo
    maximo = max(arr)

    # cantidad de buckets
    num_buckets = 5

    # crear buckets vacíos
    buckets = []

    for i in range(num_buckets):
        buckets.append([])

    # distribuir números en buckets
    for num in arr:

        # calcular bucket correspondiente
        index = (num * num_buckets) // (maximo + 1)

        buckets[index].append(num)

    # ordenar cada bucket
    for bucket in buckets:
        bucket.sort()

    # unir buckets
    resultado = []

    for bucket in buckets:
        resultado.extend(bucket)

    return resultado