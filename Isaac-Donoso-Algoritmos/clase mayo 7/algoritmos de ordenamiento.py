#Heap sort (Arbol binario, cada nodo tiene max dos hijos y el padre siempre es mayor a sus hijos)
#Complejidades --> Complejidad temporal O(n log(n)), Espacial O(1) --> Esto es porque no crea nuevas estructuras, no es estable --> no importan los elemento repetidos
def heaptify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left    

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heaptify(arr, n, largest)


def heapsort(arr):
    n = len(arr)

    for i in range(n//2 - 1, -1, -1):
        heaptify(arr, n, i)
    
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heaptify(arr, i, 0)

    return arr 

#Counting sort --> solo ordena numeros enteros, nada mas y el rango de valores hay que tomarlo muy en cuenta mucho si es muy grande no seria muy viable para el tiempo de ejecucion
#Volviendo lo del rango si una lista es no es muy grande digamos [100,205,2,1503,55] se crearia un sub arreglo de rango 2 a 1503 donde casi que todas sus posiciones estaran en 0 menos los 6 digitos a ordenar se odernan(arre)
#No vale la pena hacerlo si el rango del sub arreglo es muy grande 
#Es estable porque los elemento repetido se organizan en orden, osea si hay un 5 en la posicion 4 y otro en la posicion 10, al ordenarse el 5 en la posicion 4 quedara de primeras

#Toca saber como y donde meter la mano en el codigo para adaptarlo a las necesidades

#Radix sort
#Quick sort
#Bucket sort
