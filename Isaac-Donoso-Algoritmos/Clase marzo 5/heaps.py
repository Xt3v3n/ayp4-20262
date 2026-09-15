import heapq

def demo_operaciones_basicas():
    #Demuestra las operaciones basicas de heapq.

    print("=" * 60)
    print("OPERACIONES BASICAS DE HEAP")
    print("=" * 60)
    
    # 1. Crear un heap desde una linea

    print("\n1. CREAR HEAP {heapify}")
    print("-" * 40)
    datos = [5, 3, 8, 1, 2, 9, 4]

    print(f"    Lista original: {datos}")

    heapq.heapify(datos) # Convierte la lista en heap IN-PLACE
    print(f"    Despues del heapify: {datos}")
    print(f"    Minimo (datos[0]): {datos[0]}")

demo_operaciones_basicas()

pacientes = []
contador = 0

while True:

    print("\n1. Ingresar paciente")
    print("2. Atender paciente")
    print("3. Ver cola")
    print("4. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":

        nombre = input("Nombre del paciente: ")
        prioridad = int(input("Prioridad (1-3): "))

        contador += 1

        paciente = (prioridad, contador, nombre)

        heapq.heappush(pacientes, paciente)

        print("Paciente agregado")

    elif opcion == "2":

        if len(pacientes) == 0:
            print("No hay pacientes")
        else:
            paciente = heapq.heappop(pacientes)
            print(f"Atendiendo a: {paciente[2]} (Prioridad {paciente[0]})")

    elif opcion == "3":

        print("\nPacientes en espera:")
        for p in pacientes:
            print(p)

    elif opcion == "4":
        break

    else:
        print("Opcion invalida")