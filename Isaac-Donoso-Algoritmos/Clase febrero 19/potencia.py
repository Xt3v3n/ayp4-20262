
def potencia (a, b):
    if b==0:
        return 1
    return a * potencia(a, b -1)

def potencia_optimizado(a,b):
    if b==0:
        return 1
    if b % 2 == 0:
        mitad = potencia_optimizado(a, b // 2)
        return mitad * mitad
    else:
        return a * potencia_optimizado(a, b - 1)


# Ingresado un número, retorne la suma de sus dígitos
# Caso base: Que el número sea menor a 10 

def suma_digitos(n):
    if n < 10:
        return n    
    digito = n % 10
    return digito + suma_digitos(n//10)

# Búsqueda binaria
def busqueda_binaria(lista,objetivo, inicio =0, fin=None):
    # Inicializar fin en la primera llamada
    if fin is None:
        fin = len(lista) - 1
    # Caso base: rango inválido (elemento no encontrado)
    if inicio > fin:
        return -1
    
    # Calcular punto medio
    medio = (inicio+fin) // 2

    #Comparar y decidir en qué mitad buscar
    if lista[medio] == objetivo:
        return medio # Encontrado
    elif objetivo < lista[medio]:
        #Buscar en la mitad izquierda
        return busqueda_binaria(lista, objetivo, inicio, medio - 1)
    else:
        #Buscar en la mitad derecha
        return busqueda_binaria(lista, objetivo, medio + 1, fin)

"""# Case base: lista vacía o un solo elemento
if len(lista) <= 1:
    return [lista[:]] # Retornar copia de la lista

resultado = []

# Para cada elemento de la lista
for i in range(len(lista)):
    # Elemento actual
    elemento = lista[i]
    # Lista sin el elemento actual
    resto = lista[:i] + lista[i+1:]
    #Obtener permutaciones del resto
    for perm in permutaciones(resto):
        #Agregar elemento al inicio de cada permutación
        resultado.append([elemento] + perm)

return resultado"""


def factorial_tail(n, acumulador = 1):
    if n <= 1:
        return acumulador
    return factorial_tail(n - 1, n * acumulador)

def fibonacci_tail(n, actual = 0, siguiente = 1):
    if n <= 0:
        return actual
    return fibonacci_tail(n - 1, siguiente, actual+siguiente)

#print(fibonacci_tail(998))

def suma_lista_normal(lista):
    if len(lista) == 0:
        return 0
    return lista[0] + suma_lista_normal(lista[1:])

def suma_lista_tail(lista, total = 0):
    if len(lista) == 0:
        return total
    return suma_lista_tail(lista[1:], lista[0] + total)

def potencia_tail(base, exp, total=1):
    if exp == 0:
        return total
    return potencia_tail(base, exp - 1, total * base)

def invertir_tail(lista, acumulador = None):
    if acumulador is None:
        acumulador = []
    if len(lista) == 0:
        return acumulador
    return invertir_tail(lista[1:], [lista[0]] + acumulador)

lista = [1,2,3,4,5]

print(suma_lista_normal(lista))
print(suma_lista_tail(lista))

print(potencia_tail(2,6))

print(invertir_tail(lista))

