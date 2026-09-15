def bubble_sort_estudiantes(arr):
    n = len(arr)
    intercambio = 0
    for i in range(n):
        # Ultimos i elementos ya ordenados 
        for j in range(0, n-i-1):
            # Intercambia si el elemento encontrado es
            if arr[j].get("Nota") > arr[j+1].get("Nota"):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                intercambio += 1
    
    return arr, intercambio
    #Complejidad Temporal cuadratica, espacial constante y es un algoritmo estable

estudiantes = [
    {"Nombre": "Camilo", "Nota": 3.8},
    {"Nombre": "Andrea", "Nota": 5.0},
    {"Nombre": "Luis", "Nota": 2.5},
    {"Nombre": "Sara", "Nota": 3.8},
    {"Nombre": "Diego", "Nota": 3.0},
    {"Nombre": "Andrea", "Nota": 4.5},
    {"Nombre": "Juan", "Nota": 4.8}
]

estudiantes_ordenados,  intercambios = bubble_sort_estudiantes(estudiantes)

print("Estudiantes ordenados:")

print(estudiantes_ordenados)

print(f"Intercambio ordenados: {intercambios}")

def bubble_sort(arr):
    n = len(arr)
    intercambios = 0
    cont = 0
    for i in range(n):
        # Ultimos i elementos ya ordenados 
        for j in range(0, n-i-1):
            cont += 1
            # Intercambia si el elemento encontrado es
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                intercambios += 1
    return arr, cont, intercambios

import time
import random

for n in [100, 500, 1000, 3000]:
    aleatoria = [random.randint(1,100) for _ in range(n)]
    inicio = time.time()
    _, conteo, intercambios = bubble_sort(aleatoria.copy())
    tiempo = time.time() - inicio
    print(f"Lista de {n} posiciones. Tiempo: {tiempo}, Comparaciones: {conteo}, Intercambios: {intercambios}")



def insertion_sort(arr):
    # Recorre desde el segundo elemento hasta el final
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Mueve los elementos de arr[0..i-1], que son mayores que key
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

nombres = ["Luis", "Ana", "Mario", "Andrea", "Carla", "Alberto", "Beatriz"]

print(insertion_sort(nombres))

class Ticket:
    def __init__(self, id_ticket, prioridad, tiempo):
        self.id_ticket = id_ticket
        self.prioridad = prioridad
        self.tiempo = tiempo
        self.siguiente = None

    def __str__(self):
        return f"Ticket: {self.id_ticket}, prioridad: {self.prioridad}"
    
class ColaTicket:
    def __init__(self):
        self.cabeza = None

    def agregar(self, id_ticket, prioridad, tiempo):
        nuevo = Ticket(id_ticket, prioridad, tiempo)
        if self.cabeza is None:
            self.cabeza = nuevo
            return
        
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo