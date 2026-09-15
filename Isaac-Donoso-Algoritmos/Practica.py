
class Nodo:
    """Clase que representa un nodo en la lista ligada"""
    def __init__(self, cedula, nombre, importancia):
        self.cedula = cedula
        self.nombre = nombre
        self.importancia = importancia  # 1, 2 o 3
        self.siguiente = None
    
    def __str__(self):
        return f"Cédula: {self.cedula}, Nombre: {self.nombre}, Importancia: {self.importancia}"


class ListaLigada:
    """Clase que representa una lista ligada con prioridad"""
    def __init__(self):
        self.cabeza = None
    
    def agregar(self, cedula, nombre, importancia):
        """
        Agrega un nuevo nodo a la lista manteniendo el orden por importancia
        1 = Sin importancia, 2 = Normal, 3 = Urgente
        """
        nuevo_nodo = Nodo(cedula, nombre, importancia)
        
        # Si la lista está vacía
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return
        
        # Si el nuevo nodo tiene mayor importancia, va al principio
        if nuevo_nodo.importancia > self.cabeza.importancia:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
            return
        
        # Buscar la posición correcta
        actual = self.cabeza
        while actual.siguiente is not None and actual.siguiente.importancia >= nuevo_nodo.importancia:
            actual = actual.siguiente
        
        nuevo_nodo.siguiente = actual.siguiente
        actual.siguiente = nuevo_nodo
    
    def mostrar(self):
        """Imprime todos los nodos de la lista"""
        if self.cabeza is None:
            print("\n--- La lista está vacía ---\n")
            return
        
        print("\n" + "="*60)
        print("LISTA DE REGISTROS (Ordenados por Importancia)")
        print("="*60)
        
        actual = self.cabeza
        contador = 1
        while actual is not None:
            nivel = ""
            if actual.importancia == 3:
                nivel = " URGENTE"
            elif actual.importancia == 2:
                nivel = " NORMAL"
            else:
                nivel = " SIN IMPORTANCIA"
            
            print(f"{contador}. {actual} [{nivel}]")
            actual = actual.siguiente
            contador += 1
        
        print("="*60 + "\n")
    
    def buscar_por_cedula(self, cedula):
        """Busca un registro por cédula"""
        actual = self.cabeza
        while actual is not None:
            if actual.cedula == cedula:
                return actual
            actual = actual.siguiente
        return None
    
    def eliminar(self, cedula):
        """Elimina un nodo de la lista por cédula"""
        if self.cabeza is None:
            print(" La lista está vacía\n")
            return False
        
        # Si es el primer nodo
        if self.cabeza.cedula == cedula:
            self.cabeza = self.cabeza.siguiente
            print(f"Registro con cédula {cedula} eliminado\n")
            return True
        
        # Buscar en el resto de la lista
        actual = self.cabeza
        while actual.siguiente is not None:
            if actual.siguiente.cedula == cedula:
                actual.siguiente = actual.siguiente.siguiente
                print(f"Registro con cédula {cedula} eliminado\n")
                return True
            actual = actual.siguiente
        
        print(f"Registro con cédula {cedula} no encontrado\n")
        return False


def menu():
    """Menú principal del programa"""
    lista = ListaLigada()
    
    while True:
        print("\n" + "="*60)
        print("SISTEMA DE GESTIÓN CON LISTA LIGADA PRIORIZADA")
        print("="*60)
        print("1. Agregar nuevo registro")
        print("2. Mostrar todos los registros")
        print("3. Buscar por cédula")
        print("4. Eliminar registro")
        print("5. Salir")
        print("="*60)
        
        opcion = input("Seleccione una opción (1-5): ").strip()
        
        if opcion == '1':
            print("\n--- AGREGAR NUEVO REGISTRO ---")
            try:
                cedula = input("Ingrese la cédula: ").strip()
                if not cedula:
                    print(" La cédula no puede estar vacía\n")
                    continue
                
                nombre = input("Ingrese el nombre: ").strip()
                if not nombre:
                    print(" El nombre no puede estar vacío\n")
                    continue
                
                while True:
                    try:
                        importancia = int(input("Ingrese el nivel de importancia (1-Sin importancia, 2-Normal, 3-Urgente): "))
                        if importancia not in [1, 2, 3]:
                            print(" Ingrese un valor entre 1 y 3\n")
                            continue
                        break
                    except ValueError:
                        print(" Ingrese un número válido\n")
                
                lista.agregar(cedula, nombre, importancia)
                print(f"Registro agregado correctamente\n")
            
            except Exception as e:
                print(f" Error: {e}\n")
        
        elif opcion == '2':
            lista.mostrar()
        
        elif opcion == '3':
            cedula = input("\nIngrese la cédula a buscar: ").strip()
            nodo = lista.buscar_por_cedula(cedula)
            if nodo:
                print(f"\n Registro encontrado:")
                print(f"   {nodo}\n")
            else:
                print(f"\n Registro con cédula {cedula} no encontrado\n")
        
        elif opcion == '4':
            cedula = input("\nIngrese la cédula del registro a eliminar: ").strip()
            lista.eliminar(cedula)
        
        elif opcion == '5':
            print("\n👋 ¡Hasta luego!\n")
            break
        
        else:
            print("\n Opción no válida. Intente nuevamente\n")


if __name__ == "__main__":
    menu()