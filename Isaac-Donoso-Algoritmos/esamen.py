"""
═══════════════════════════════════════════════════════════════════════════════
                        QUIZ 1 - ESTRUCTURAS DE DATOS
                                  EXAMEN A
                    Sistema de Historial de Navegador Web
═══════════════════════════════════════════════════════════════════════════════

CONTEXTO:
---------
Google Chrome te ha contratado para implementar el historial de navegación.
Debes diseñar e implementar el sistema usando listas enlazadas.

INSTRUCCIONES:
--------------
1. Diseñar la clase Nodo (Pagina) con los atributos necesarios
2. Diseñar la clase Lista (Historial) con los métodos requeridos
3. Usar RECURSIVIDAD en los métodos donde se indique
4. No usar listas de Python [], solo tu estructura de nodos
5. Tiempo: 90 minutos

═══════════════════════════════════════════════════════════════════════════════
REQUERIMIENTOS DEL SISTEMA
═══════════════════════════════════════════════════════════════════════════════

PUNTO 1 (1.0): DISEÑO DE ESTRUCTURAS
-------------------------------------
Diseña las clases necesarias:

a) Clase NODO (Pagina):
   - Debe almacenar: URL, título de la página, tiempo en segundos
   - Debe poder enlazarse con otra página
   
b) Clase LISTA (Historial):
   - Debe mantener referencia al inicio de la lista
   - Las páginas más recientes van al INICIO


PUNTO 2 (0.75): AGREGAR PÁGINA
------------------------------
Implementa un método para agregar una nueva página visitada.
- La página más reciente debe quedar al INICIO de la lista
- Complejidad esperada: O(1)


PUNTO 3 (1.0): TIEMPO TOTAL - RECURSIVO
---------------------------------------
Implementa un método que calcule el tiempo total de navegación.
- OBLIGATORIO usar recursividad
- Retorna la suma de segundos de todas las páginas

Ejemplo:
    Si hay páginas con tiempos [30, 120, 45] segundos
    Debe retornar 195


PUNTO 4 (1.0): BUSCAR POR DOMINIO - RECURSIVO
---------------------------------------------
Implementa un método que retorne una NUEVA lista con páginas
que contengan cierto texto en su URL.
- OBLIGATORIO usar recursividad
- No modificar la lista original

Ejemplo:
    buscar_por_dominio("youtube") 
    Retorna nueva lista con páginas cuya URL contiene "youtube"


PUNTO 5 (1.25): ELIMINAR PÁGINAS RÁPIDAS - RECURSIVO
----------------------------------------------------
Implementa un método que elimine páginas donde el usuario
estuvo menos de X segundos (probablemente clicks accidentales).
- OBLIGATORIO usar recursividad
- Modificar la lista original

Ejemplo:
    eliminar_rapidas(10)
    Elimina todas las páginas con tiempo < 10 segundos

═══════════════════════════════════════════════════════════════════════════════
ESCRIBE TU CÓDIGO AQUÍ ABAJO
═══════════════════════════════════════════════════════════════════════════════
"""

# PUNTO 1a: Clase Nodo (Pagina)
# TODO: Diseñar e implementar


# PUNTO 1b: Clase Lista (Historial)
# TODO: Diseñar e implementar con los métodos de los puntos 2-5


# ═══════════════════════════════════════════════════════════════════════════════
# CÓDIGO DE PRUEBA - NO MODIFICAR
# (Descomenta cuando tengas tu implementación lista)
# ═══════════════════════════════════════════════════════════════════════════════


class Pagina:
    def __init__(self, URL, nombre, tiempo):
        self.URL = URL
        self.nombre = nombre
        self.tiempo = tiempo
        self.anterior = None
        self.siguiente = None
"""class ListaDoble:
    def __init__(self):
        self.cabeza = None
        self.cola = None
    
    

    def insertar_final(self, dato):
        nuevo = Nodo(dato)
        
        if self.esta_vacia():
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            self.cola.siguiente = nuevo
            nuevo.anterior = self.cola
            self.cola = nuevo

    def eliminar_inicio(self):
        if self.esta_vacia():
            return None
        
        if self.cabeza.dato == self.cola.dato:
            self.cabeza = None
            self.cola = None
        else:
            self.cabeza = self.cabeza.siguiente
            self.cabeza.anterior = None
    
    def eliminar_final(self):
        if self.esta_vacia():
            return None
        
        if self.cabeza.dato == self.cola.dato:
            self.cabeza = None
            self.cola = None
        else:
            self.cola = self.cola.anterior
            self.cola.siguiente = None

    def recorrer_adelante(self):
        if self.esta_vacia():
            print("Lista vacia.")
            return

        print("Recorriendo Inicio --> Fin") 
        actual = self.cabeza

        print("Inicio", end=" -> ")
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("Fin")

    def recorrer_reversa(self):
        if self.esta_vacia():
            print("Lista vacia.")
            return

        print("Recorriendo Fin --> Inicio") 
        actual = self.cola

        print("Fin", end=" -> ")
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.anterior
        print("Inicio")

    def buscar(self,dato):
        actual = self.cabeza

        while actual:
            if actual.dato == dato:
                return True
            actual = actual.siguiente
        
        return False
    
    def __len__(self):
        contador = 0
        actual = self.cabeza

        while actual:
            contador += 1
            actual = actual.siguiente
        
        return contador
    
    def __str__(self):
        if self.esta_vacia():
            return "Lista vacia."
        

        elementos = []
        actual = self.cabeza
       
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        
        return " <=> ".join(elementos) """
class Historial:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def esta_vacia(self):
        return self.cabeza is None
    
    def visitar(self, URL, nombre, tiempo):
        nuevo = Pagina(URL, nombre, tiempo)

        if self.esta_vacia():
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            nuevo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo
            self.cabeza = nuevo

    def mostrar(self):
        if self.esta_vacia():
            print("Lista vacia.")
            return
        actual = self.cabeza
        while actual:
            print("-" * 20)
            print(f"{actual.URL}--{actual.nombre}")
            actual = actual.siguiente
        

    def tiempo_total(self,nodo = None, total = 0):
        if self.esta_vacia():
            return "No hay nada en el historial"
        
        if nodo is None:
            nodo = self.cabeza
            total += nodo.tiempo

        if nodo.siguiente is None:
            return total
        
        return self.tiempo_total(nodo.siguiente, total + nodo.siguiente.tiempo)
    
    def eliminar_rapidas(self, tiempo, nodo = None):
        if self.esta_vacia():
            return None
        
        if nodo is None:
            nodo = self.cabeza
        
        if nodo == self.cabeza and nodo.tiempo <= tiempo:
            if self.cabeza.nombre == self.cola.nombre:
                print(f"{nodo.URL} fue eliminado")
                self.cabeza = None
                self.cola = None
            else:
                print(f"{nodo.URL} fue eliminado")
                self.cabeza = self.cabeza.siguiente
                self.cabeza.anterior = None
        elif nodo == self.cola and nodo.tiempo <= tiempo:
            if self.cabeza.nombre == self.cola.nombre:
                print(f"{nodo.URL} fue eliminado")
                self.cabeza = None
                self.cola = None
            else:
                print(f"{nodo.URL} fue eliminado")
                self.cola = self.cola.anterior
                self.cola.siguiente = None
        else:
            if nodo.tiempo <= tiempo:
                print(f"{nodo.URL} fue eliminado")
                nodo.anterior.siguiente = nodo.siguiente
                nodo.siguiente.anterior = nodo.anterior
                nodo = nodo.siguiente
            

        if nodo.siguiente is None:
            return 
        
        return self.eliminar_rapidas(tiempo, nodo.siguiente)
            
        


    
    
    
    
    

if __name__ == "__main__":
    print("=" * 60)
    print("         PRUEBAS DEL HISTORIAL DE NAVEGACIÓN")
    print("=" * 60)
    
    # Crear historial
    historial = Historial()
    
    # Agregar páginas (la más reciente queda primero)
    historial.visitar("https://www.google.com/search", "Búsqueda Google", 15)
    historial.visitar("https://www.youtube.com/watch", "Video YouTube", 300)
    historial.visitar("https://www.github.com/repo", "GitHub Repo", 180)
    historial.visitar("https://www.youtube.com/home", "YouTube Home", 45)
    historial.visitar("https://www.google.com/maps", "Google Maps", 5)
    
    print("\\n Historial inicial:")
    historial.mostrar()  # Implementa este método para visualizar
    
    # Prueba tiempo total
    print("\\n Tiempo total:", historial.tiempo_total(), "segundos")
    print("   Esperado: 545 segundos")
    
    # Prueba buscar por dominio
    #print("\\n Páginas de YouTube:")
    #youtube = historial.buscar_por_dominio("youtube")
    #youtube.mostrar()
    
    # Prueba eliminar rápidas
    print("\\n Eliminando páginas < 30 segundos...")
    historial.eliminar_rapidas(30)
    historial.mostrar()
    print("   (Google Maps y Búsqueda Google deberían estar eliminadas)")

