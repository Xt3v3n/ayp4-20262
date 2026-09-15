def contar_lineal(n): #Crecimiento lineal al ciclo depender de la entrada f(n) = 2 + 2n == f(n) = n
    contador = 0
    for i in range(n):
        contador += 1
        print (i)
    return contador

def contar_constantante(n): #Crecimiento constante al ciclo no depender de la entrada f(n) = 2 + 2(1000) == f(n) = 2002
    contador = 0
    for i in range(1000):
        contador += 1
        print (i)
    return contador

#Un crecimiento lineal no tiene nada que ver su tiempo, literalmente es su forma de crecer y comportarse al ejecutarse

#El crecimiento lineal se come el crecimiento constante y el crecimiento cuadratico se come al lineal


def contar_cuadratico(n): #Crecimiento cuadratico al los ciclos anidados depender de la entrada f(n) = 2 + 2n^2 == f(n) = n^2
    contador = 0
    for i in range(n):
        for j in range(n):
            contador += 1
            print (i)
    return contador

def busqueda_binaria(arr, objetivo):
    izquierda, derecha = 0, len(arr)
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if arr(medio) == objetivo:
            return objetivo
        elif arr(medio) < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

#Hacer un funcion que reciba un arreglo que resiva una lista y devuelva el elemento que mas se repite

def busqueda_elemento_repetido_cuadratico(lista):
    mayor = 0
    valor = 0
    for i in range(len(lista)):
        contador = 0
        for j in range(len(lista)):
            if lista[j] == lista[i]:
                contador += 1
        if contador > valor:
            valor = contador
            mayor = i
    return valor, mayor

def busqueda_elemento_repetido(lista):
    memo = {}
    for i in lista:
        memo[i] = memo.get(i, 0) + 1    
    resultado = None
    mayor_conteo = 0
    for elemento, conteo in memo.items():
        if conteo > mayor_conteo:
            mayor_conteo = conteo
            resultado = elemento
    return resultado

#Cual es la menor diferencia que puedo optener de un arreglo(lista)

def menor_diferencia(lista):

    for i in range(len(lista)):
        diferencias = []
        j = 1
        while j < (len(lista)):
            diferencias.append(lista[i]-lista[j])
            pass
            #j += 
        
def menor_diferencia(lista):
    lista.sort()  # O(n log n)
    
    min_diff = float('inf')
    
    for i in range(len(lista) - 1):  # O(n)
        diff = abs(lista[i] - lista[i+1])
        if diff < min_diff:
            min_diff = diff
            
    return min_diff