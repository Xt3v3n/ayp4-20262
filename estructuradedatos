"""
═══════════════════════════════════════════════════════════════════════════════
                        QUIZ 1 - ESTRUCTURAS DE DATOS
                                  EXAMEN A
                    Sistema de Historial de Navegador Web
═══════════════════════════════════════════════════════════════════════════════
"""

# PUNTO 1a: Clase Nodo (Pagina)
class Pagina:
    def __init__(self, url, titulo, tiempo):
        self.url = url
        self.titulo = titulo
        self.tiempo = tiempo
        self.siguiente = None

# PUNTO 1b: Clase Lista (Historial)
class Historial:
    def __init__(self):
        self.cabeza = None

    # Método de utilidad para imprimir la lista en pantalla
    def mostrar(self):
        actual = self.cabeza
        if actual is None:
            print("  [Historial vacío]")
            return
        while actual:
            print(f"  [{actual.tiempo}s] {actual.titulo} -> {actual.url}")
            actual = actual.siguiente

    # PUNTO 2: AGREGAR PÁGINA (O(1))
    def visitar(self, url, titulo, tiempo):
        nueva_pagina = Pagina(url, titulo, tiempo)
        # La página más reciente queda al inicio de la lista
        nueva_pagina.siguiente = self.cabeza
        self.cabeza = nueva_pagina

    # PUNTO 3: TIEMPO TOTAL - RECURSIVO
    def tiempo_total(self):
        return self._tiempo_total_recursivo(self.cabeza)
        
    def _tiempo_total_recursivo(self, nodo_actual):
        if nodo_actual is None:
            return 0
        return nodo_actual.tiempo + self._tiempo_total_recursivo(nodo_actual.siguiente)

    # PUNTO 4: BUSCAR POR DOMINIO - RECURSIVO
    def buscar_por_dominio(self, texto):
        nuevo_historial = Historial()
        self._buscar_por_dominio_recursivo(self.cabeza, texto, nuevo_historial)
        return nuevo_historial

    def _buscar_por_dominio_recursivo(self, nodo_actual, texto, nuevo_historial):
        if nodo_actual is None:
            return
        
        # Recorremos primero hasta el final para que al insertar con visitar() 
        # (que inserta al inicio), se mantenga el orden cronológico original.
        self._buscar_por_dominio_recursivo(nodo_actual.siguiente, texto, nuevo_historial)
        
        if texto in nodo_actual.url:
            nuevo_historial.visitar(nodo_actual.url, nodo_actual.titulo, nodo_actual.tiempo)

    # PUNTO 5: ELIMINAR PÁGINAS RÁPIDAS - RECURSIVO
    def eliminar_rapidas(self, limite_segundos):
        self.cabeza = self._eliminar_rapidas_recursivo(self.cabeza, limite_segundos)

    def _eliminar_rapidas_recursivo(self, nodo_actual, limite_segundos):
        if nodo_actual is None:
            return None
        
        # Procesar el resto de la lista de forma recursiva
        nodo_actual.siguiente = self._eliminar_rapidas_recursivo(nodo_actual.siguiente, limite_segundos)
        
        # Si el tiempo es menor al límite, saltamos (eliminamos) este nodo
        if nodo_actual.tiempo < limite_segundos:
            return nodo_actual.siguiente
            
        return nodo_actual


# ═══════════════════════════════════════════════════════════════════════════════
# CÓDIGO DE PRUEBA
# ═══════════════════════════════════════════════════════════════════════════════

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
    
    print("\n Historial inicial:")
    historial.mostrar()
    
    # Prueba tiempo total
    print("\n Tiempo total:", historial.tiempo_total(), "segundos")
    print("   Esperado: 545 segundos")
    
    # Prueba buscar por dominio
    print("\n Páginas de YouTube:")
    youtube = historial.buscar_por_dominio("youtube")
    youtube.mostrar()
    
    # Prueba eliminar rápidas
    print("\n Eliminando páginas < 30 segundos...")
    historial.eliminar_rapidas(30)
    historial.mostrar()
    print("   (Google Maps y Búsqueda Google deberían estar eliminadas)")