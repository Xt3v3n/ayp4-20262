import re
"""
ME DIO MUCHOS ERRORES Y NO ME DIO, LA VERDAD PERDI MUCHO TIEMPO EN ESTE PUNTO; ESPERO QUE AL MENOS LA LOGICA SUME ALGO
validacion = r"^[A-Z]{3}+[-]*[0-9]{3}$"
    
if re.match(validacion, "ABC123"):
        print(True)
else:
    print(False)
"""

def validacion_placas(placa):
    patron = r'^[A-Z]{3}-?\d{3}$'
    return bool(re.match(patron, placa))

"""
def extraer_hashtags(texto):
    findall = re.findall(r"^#*/w{1,}", texto)
    print(findall)

extraer_hashtags()
 Extrae todos los hashtags de un texto.
 Un hashtag empieza con # seguido de letras, números o guion bajo.

 Ejemplo:
 extraer_hashtags("Hola #python es #genial y #100dias")
 -> ["#python", "#genial", "#100dias"]
 """

"""
Sistema de gestión de pedidos para un restaurante de domicilios.
Cada pedido tiene: cliente, dirección, valor y si está entregado.
Los pedidos se almacenan en una lista enlazada.
"""

class Pedido:
    def __init__(self, cliente, direccion, valor, entregado=False):
        self.cliente = cliente
        self.direccion = direccion
        self.valor = valor
        self.entregado = entregado
        self.siguiente = None
    def __str__(self):
        estado = "✓" if self.entregado else "○"
        return f"[{estado}] {self.cliente} - ${self.valor:,} - {self.direccion}"


class ListaPedidos:
    def __init__(self):
        self.cabeza = None
    def mostrar(self):
        actual = self.cabeza
        if actual is None:
            print(" Sin pedidos")
            return
        while actual:
            print(f" {actual}")
            actual = actual.siguiente

    def esta_vacio(self):
        return self.cabeza is None

    def agregar(self, cliente, direccion, valor, nodo = None):
        """
        Agrega un nuevo pedido al FINAL de la lista.
        OBLIGATORIO usar recursividad.
        """
        if nodo is None:
            nodo = self.cabeza
        nuevo_pedido = Pedido(cliente, direccion, valor)
        if self.esta_vacio():
            self.cabeza = nuevo_pedido
        else:
            
            if nodo.siguiente:
                return self.agregar(cliente, direccion, valor, nodo.siguiente)
            nodo.siguiente = nuevo_pedido
        return
        
    def valor_pendiente(self, nodo = None, valor_pedidos_ne = 0):
        """
        Retorna la suma de valores de pedidos NO entregados.
        OBLIGATORIO usar recursividad.

        Ejemplo:
        Pedido1 (entregado, $25000) + Pedido2 (pendiente, $30000)
        + Pedido3 (pendiente, $15000)
        -> Retorna 45000
        """
        if self.esta_vacio():
            return "Sin pedidos"
        
        
        if nodo is None:
            nodo = self.cabeza

        if not nodo.entregado:
            valor_pedidos_ne += nodo.valor
        
        if nodo.siguiente:
            return self.valor_pendiente(nodo.siguiente, valor_pedidos_ne)
        
        return valor_pedidos_ne

    def entregar(self, n):
        nodo = self.cabeza
        while n > 0:
            nodo.entregado = True
            nodo = nodo.siguiente
            n -= 1
        return f"Numero de pedidos entregados {n}"

    def eliminar_entregados(self, nodo = None):
        """
        Elimina todos los pedidos que ya fueron entregados.
        OBLIGATORIO usar recursividad.
        Modifica la lista original.
        """
        if self.esta_vacio():
            return "Sin pedidos"
    
        if nodo is None:
           nodo = self.cabeza
        if nodo == self.cabeza:
            if nodo.entregado:
                self.cabeza = self.cabeza.siguiente
        else:
            if nodo.entregado:
                nodo = nodo.siguiente

        if nodo.siguiente:
            return self.valor_pendiente(nodo.siguiente)
        
        return nodo
        

Pedidos = ListaPedidos()

Pedidos.agregar("Pepe", "Casa 1", 15000)
Pedidos.agregar("Tino", "Casa 2", 20000)
Pedidos.agregar("El pibe", "Casa 3", 10000)
Pedidos.agregar("Goku", "Montaña Paoz", 100000)

Pedidos.mostrar()

print(f"Valor de pedidos sin entregar: {Pedidos.valor_pendiente()}")

Pedidos.entregar(3)
Pedidos.mostrar()
Pedidos.eliminar_entregados()
print(f"Valor de pedidos sin entregar: {Pedidos.valor_pendiente()}")
Pedidos.mostrar()

"""
Un colegio tiene 3 clubes extracurriculares. Cada club tiene un conjunto
de estudiantes inscritos. Responde las preguntas usando operaciones de conjuntos.
"""

club_ciencias = {"Ana", "Carlos", "Diana", "Elena", "Felipe"}
club_deportes = {"Carlos", "Felipe", "Gabriel", "Hugo", "Isabel"}
club_arte = {"Ana", "Diana", "Gabriel", "Julia", "Karen"}
def estudiantes_en_todos():
    esta_en_todos = club_ciencias & club_deportes & club_arte
    print(f"   Esta en todos los club: {sorted(esta_en_todos)}")
    """
 Retorna el conjunto de estudiantes inscritos en LOS TRES clubes.
 (Intersección de los tres)
 """
 
def solo_un_club():
    solo_cienias = club_ciencias - club_deportes - club_arte
    solo_deportes = club_deportes - club_ciencias - club_arte
    solo_arte = club_arte - club_deportes - club_ciencias
    print(f"\n  Solo ciencias: {sorted(solo_cienias)}")
    print(f"   Solo deportes: {sorted(solo_deportes)}")
    print(f"   Solo arte: {sorted(solo_arte)}")
    solo_un_club = solo_deportes | solo_arte | solo_cienias
    print(f"   Solo un club: {sorted(solo_un_club)}")
    """
 Retorna el conjunto de estudiantes que están en EXACTAMENTE un club.

 Pista: Un estudiante está en exactamente un club si está en ese club
 pero NO en los otros dos.

 Ejemplo esperado: {"Elena", "Hugo", "Isabel", "Julia", "Karen"}
 """


def clubes_de_estudiante():
    todos = club_arte | club_ciencias | club_deportes
    for estudiante in sorted(todos):
        materias = []
        if estudiante in club_ciencias:
            materias.append("Ciencias")
        if estudiante in club_deportes:
            materias.append("Deportes")
        if estudiante in club_arte:
            materias.append("Arte")
        print(f"  {estudiante}: {', '.join(materias)} ({len(materias)} materias)")
    """
 Retorna una lista con los nombres de los clubes a los que pertenece
 el estudiante.

 Ejemplo:
 clubes_de_estudiante("Carlos") -> ["Ciencias", "Deportes"]
 clubes_de_estudiante("Julia") -> ["Arte"]
 """
 # TODO: Implementar

print(estudiantes_en_todos())
print(solo_un_club())
print(clubes_de_estudiante())
 
"""
Tienes una escalera de N escalones. En cada paso puedes subir 1 o 2 escalones.
¿De cuántas formas distintas puedes llegar al escalón N?
Ejemplo:
 N=1: 1 forma → [1]
 N=2: 2 formas → [1+1, 2]
 N=3: 3 formas → [1+1+1, 1+2, 2+1]
 N=4: 5 formas → [1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2]
"""
def escalones_sin_memo(n):
    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    if n == 2:
        return 2
    
    return escalones_sin_memo(n-1) + escalones_sin_memo(n-2)

print(escalones_sin_memo(10))
"""
 Calcula de cuántas formas se puede subir una escalera de n escalones.
 En cada paso puedes subir 1 o 2 escalones.

 Implementar con recursividad pura (sin memorización).

 Casos base:
 n == 0 -> 1 (hay una forma de "no subir")
 n == 1 -> 1

 Caso recursivo:
 escalones(n) = escalones(n-1) + escalones(n-2)
 """

def escalones_con_memo(n, memo={}):
    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    if n == 2:
        return 2
    
    if n in memo:
        return memo[n]

    memo[n] = escalones_con_memo(n-1, memo) + escalones_con_memo(n-2, memo)
    return memo[n]
"""
 Misma función pero usando un diccionario para guardar resultados
 ya calculados y evitar recalcular.

 Ejemplo:
 escalones_con_memo(10) -> 89
 escalones_con_memo(30) -> 1346269 (sin memo esto tardaría mucho)
 """
print(escalones_con_memo(10))