"""
═══════════════════════════════════════════════════════════════════════════════
                        PARCIAL - CONJUNTOS (B)
              Detector de Conflictos de Horario + Inventario con Listas
═══════════════════════════════════════════════════════════════════════════════

INSTRUCCIONES:
--------------
1. Completar las funciones donde dice TODO
2. No modificar el código base proporcionado
3. Tiempo: 90 minutos
4. Calificación: 0.0 a 5.0

═══════════════════════════════════════════════════════════════════════════════
                    PARTE 1: DETECTOR DE CONFLICTOS DE HORARIO (2.5)
═══════════════════════════════════════════════════════════════════════════════

Una universidad tiene 3 profesores que dictan materias en diferentes franjas.
Cada franja es un número del 1 al 8 (horas del día académico).
Usar conjuntos de Python para detectar conflictos y disponibilidad.
"""

prof_garcia = {1, 2, 3, 5}       # Franjas ocupadas
prof_martinez = {2, 4, 5, 7}
prof_lopez = {3, 5, 6, 8}

TODAS_LAS_FRANJAS = {1, 2, 3, 4, 5, 6, 7, 8}


# PUNTO 1.1 (0.8): Franjas en conflicto
def franjas_conflicto(prof_a, prof_b):
    conflictos = prof_a & prof_b

    return conflictos
    """
    Retorna el conjunto de franjas donde AMBOS profesores tienen clase
    (están ocupados al mismo tiempo).

    Ejemplo:
        franjas_conflicto(prof_garcia, prof_martinez) -> {2, 5}
    """
    # TODO: Implementar
    pass


# PUNTO 1.2 (0.8): Franjas libres de un profesor
def franjas_libres(profesor):
    libres = TODAS_LAS_FRANJAS - profesor

    return libres
    """
    Retorna el conjunto de franjas donde el profesor NO tiene clase.

    Ejemplo:
        franjas_libres(prof_garcia) -> {4, 6, 7, 8}
    """
    # TODO: Implementar
    pass


# PUNTO 1.3 (0.9): Franja disponible para reunión de los 3
def franja_reunion(prof_a, prof_b, prof_c):
    libre_a = franjas_libres(prof_a)
    libre_b = franjas_libres(prof_b)
    libre_c = franjas_libres(prof_c)
    horas_reunion = libre_a & libre_b & libre_c

    if len(horas_reunion) == 0:
        return "No coincide ninguna franja donde los 3 no tengan clases"
    return horas_reunion
    """
    Retorna el conjunto de franjas donde los TRES profesores están libres.

    Pista: Primero obtener las franjas libres de cada uno,
    luego encontrar las que tienen en común.

    Ejemplo:
        franja_reunion(prof_garcia, prof_martinez, prof_lopez)
        -> franjas donde ninguno de los 3 tiene clase
    """
    # TODO: Implementar
    pass


"""
═══════════════════════════════════════════════════════════════════════════════
                PARTE 2: INVENTARIO CON LISTAS ENLAZADAS (2.5)
═══════════════════════════════════════════════════════════════════════════════

Dos bodegas tienen productos almacenados como conjuntos con listas enlazadas.
Implementar operaciones para gestionar el inventario.
"""


# ═══════════════════════════════════════════════════════════════════════════════
# CÓDIGO BASE - NO MODIFICAR
# ═══════════════════════════════════════════════════════════════════════════════

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class Conjunto:
    def __init__(self, elementos=None):
        self.cabeza = None
        self.tamaño = 0
        if elementos:
            for e in elementos:
                self.agregar(e)

    def esta_vacio(self):
        return self.cabeza is None

    def pertenece(self, x):
        """Retorna True si x está en el conjunto"""
        actual = self.cabeza
        while actual:
            if actual.dato == x:
                return True
            actual = actual.siguiente
        return False

    def agregar(self, x):
        """Agrega x si no existe"""
        if self.pertenece(x):
            return False
        nuevo = Nodo(x)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo
        self.tamaño += 1
        return True

    def eliminar(self, x):
        if self.esta_vacio():
            return False
        
        if self.cabeza.dato == x:
            self.cabeza = self.cabeza.siguiente
            self.tamaño -= 1
            return True
        
        actual = self.cabeza
        while actual.siguiente:
            if actual.siguiente.dato == x:
                actual.siguiente = actual.siguiente.siguiente
                self.tamaño -= 1
                return True
            actual = actual.siguiente
        return False

    def union(self, otro):
        resultado = Conjunto()

        actual = self.cabeza
        while actual:
            resultado.agregar(actual.dato)
            actual = actual.siguiente

        actual = otro.cabeza
        while actual:
            resultado.agregar(actual.dato)
            actual = actual.siguiente

        return resultado
    
    def interseccion(self, otro):
        resultado = Conjunto()

        actual = self.cabeza
        while actual:
            if otro.pertenece(actual.dato):
                resultado.agregar(actual.dato)
            actual = actual.siguiente
        
        return resultado
    
    def diferencia(self, otro):
        resultado = Conjunto()

        actual = self.cabeza
        while actual:
            if not otro.pertenece(actual.dato):
                resultado.agregar(actual.dato)
            actual = actual.siguiente
        
        return resultado
    
    def diferencia_simetrica(self, otro):
        #Hacemos la union de la diferencia de mi conjunto con el otro y
        #la diferencia del otro conjunto con el mio
        return self.diferencia(otro).union(otro.diferencia(self))
    
    def subconjunto(self, otro):
        actual = self.cabeza
        while actual:
            if not otro.pertenece(actual.dato):
                return False
            actual = actual.siguiente
        return True
    
    def a_lista(self):
        resultado = []

        actual = self.cabeza
        while actual:
            resultado.append(actual.dato)
            actual = actual.siguiente
        return resultado
    
    def __str__(self):
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return "{" + ", ".join(elementos) + "}"


# ═══════════════════════════════════════════════════════════════════════════════
# PUNTOS A IMPLEMENTAR
# ═══════════════════════════════════════════════════════════════════════════════

# PUNTO 2.1 (0.8): Productos en ambas bodegas (intersección)
def productos_en_ambas(bodega_a, bodega_b):
    ambas = bodega_a.interseccion(bodega_b)

    return ambas
    """
    Retorna un NUEVO Conjunto con los productos que están en AMBAS bodegas.

    Recorrer bodega_a y agregar al resultado solo los que también
    están en bodega_b.

    Ejemplo:
        A = Conjunto(["arroz", "leche", "pan"])
        B = Conjunto(["leche", "huevos", "pan"])
        productos_en_ambas(A, B) -> {leche, pan}
    """
    # TODO: Implementar
    pass


# PUNTO 2.2 (0.8): Productos exclusivos de una bodega (diferencia)
def productos_exclusivos(bodega_a, bodega_b):
    exclusivo = bodega_a.diferencia(bodega_b)
    return exclusivo
    """
    Retorna un NUEVO Conjunto con productos que están en bodega_a
    pero NO en bodega_b.

    Ejemplo:
        A = Conjunto(["arroz", "leche", "pan"])
        B = Conjunto(["leche", "huevos", "pan"])
        productos_exclusivos(A, B) -> {arroz}
    """
    # TODO: Implementar
    pass


# PUNTO 2.3 (0.9): Verificar si una bodega tiene todo lo de otra (subconjunto)
def bodega_contiene_todo(bodega_grande, bodega_chica):
    contiene = bodega_chica.subconjunto(bodega_grande)
    return contiene
    """
    Retorna True si bodega_grande tiene TODOS los productos de bodega_chica.
    Es decir: bodega_chica ⊆ bodega_grande

    Ejemplo:
        grande = Conjunto(["arroz", "leche", "pan", "huevos"])
        chica = Conjunto(["leche", "pan"])
        bodega_contiene_todo(grande, chica) -> True

        bodega_contiene_todo(chica, grande) -> False
    """
    # TODO: Implementar
    pass


# ═══════════════════════════════════════════════════════════════════════════════
# CÓDIGO DE PRUEBA - NO MODIFICAR
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("=" * 60)
    print("PARTE 1: CONFLICTOS DE HORARIO")
    print("=" * 60)

    print(f"\n  García:   {sorted(prof_garcia)}")
    print(f"  Martínez: {sorted(prof_martinez)}")
    print(f"  López:    {sorted(prof_lopez)}")

    print(f"\n🔴 Conflictos García-Martínez: {franjas_conflicto(prof_garcia, prof_martinez)}")
    print(f"   Esperado: {{2, 5}}")

    print(f"\n🔴 Conflictos García-López: {franjas_conflicto(prof_garcia, prof_lopez)}")
    print(f"   Esperado: {{3, 5}}")

    print(f"\n🟢 Franjas libres García: {franjas_libres(prof_garcia)}")
    print(f"   Esperado: {{4, 6, 7, 8}}")

    print(f"\n🟢 Franjas libres Martínez: {franjas_libres(prof_martinez)}")
    print(f"   Esperado: {{1, 3, 6, 8}}")

    print(f"\n📅 Franjas para reunión de los 3: {franja_reunion(prof_garcia, prof_martinez, prof_lopez)}")

    print("\n" + "=" * 60)
    print("PARTE 2: INVENTARIO CON LISTAS ENLAZADAS")
    print("=" * 60)

    bodega_norte = Conjunto(["arroz", "leche", "pan", "aceite", "sal"])
    bodega_sur = Conjunto(["leche", "huevos", "pan", "azúcar", "sal"])

    print(f"\n  Bodega Norte: {bodega_norte}")
    print(f"  Bodega Sur:   {bodega_sur}")

    print(f"\n🔵 En ambas bodegas: {productos_en_ambas(bodega_norte, bodega_sur)}")
    print(f"   Esperado: {{leche, pan, sal}}")

    print(f"\n🟡 Solo en Norte: {productos_exclusivos(bodega_norte, bodega_sur)}")
    print(f"   Esperado: {{arroz, aceite}}")

    print(f"\n🟡 Solo en Sur: {productos_exclusivos(bodega_sur, bodega_norte)}")
    print(f"   Esperado: {{huevos, azúcar}}")

    pedido = Conjunto(["leche", "sal"])
    print(f"\n  Pedido: {pedido}")
    print(f"  ¿Norte tiene todo el pedido? {bodega_contiene_todo(bodega_norte, pedido)}")
    print(f"   Esperado: True")

    pedido2 = Conjunto(["leche", "huevos"])
    print(f"\n  Pedido: {pedido2}")
    print(f"  ¿Norte tiene todo el pedido? {bodega_contiene_todo(bodega_norte, pedido2)}")
    print(f"   Esperado: False")
