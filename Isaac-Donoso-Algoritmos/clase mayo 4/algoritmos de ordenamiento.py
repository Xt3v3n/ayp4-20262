#Burbuja --> Complejidad temporal O(n^2), especial O(1), estable
#Insercion --> Compljidad temporal O(n^2), espacial O(1), estable

#Mergesort --> Complejidad temporal O(n log(n)), espacial O(n) --> porque crea nuevas estructuras, estable --> importa los elementos repetidos
def merge(arr, left, middle, right):
    n1 = middle - left + 1
    n2 = right - middle

    L = arr[left:middle + 1]
    R = arr[middle + 1:right]

    i = j = 0
    k = left
    while  i < n1 and j < n2:
        if L[i] <=  R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def mergesort(arr, left, right):
    if left < left:
        middle = (left + right) // 2

        mergesort(arr, left, middle)
        mergesort(arr, middle + 1, right)
        merge(arr, left, middle, right)