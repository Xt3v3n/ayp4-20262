class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Conjunto:
    def __init__(self, elementos = None):
        self.cabeza = None
        self.tamaño = 0

        if elementos:
            for e in elementos:
                self.agregar(e)
    
    def esta_vacio(self):
        return self.cabeza is None
    
    def cardinalidad(self):
        return self.tamaño
    
    def pertenece(self, x):
        actual = self.cabeza
        while actual:
            if actual.dato == x:
                return True
            actual = actual.siguiente
        return False
    
    def agregar(self, x):
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
        return "{" + ", ".join(str(x) for x in self.a_lista()) + "}"
    

roles = {
    "admin" : {
        "leer", "escribir", "eliminar", "crear_usuarios",
        "ver_logs", "configurar", "backup", "restaurar"
    },
    "editor" : {"leer", "escribir", "subir_archivos"},
    "viewer" : {"leer"},
    "moderador" : { "leer", "escribir", "eliminar", "ver_logs"},
    "auditor" : {"leer", "ver_logs", "exportar_reportes"}
}

usuarios = {
    "Juan" : "admin",
    "Maria" : "editor",
    "Jose" : "viewer",
    "Jesucristo" : "moderador",
    "Chaplin" : "auditor"
}

rol = set(roles.keys())
usuario = set(usuarios.keys())

i = input("Ingrese un usuario: ")
tarea = input("Ingrese la tarea: ")

if i in usuario:
    for j in rol:
        if usuarios[i] == j:
            valores = roles[j]
            if tarea in valores:
                print(f"El usuario {i} con el rol del {j} si puede cumplir con la tarea {tarea}")
                break
            print(f"El usuario {i} con el rol del {j} no puede cumplir con la tarea {tarea}")
else:
    print("El usuario ingresado es incorrecto")

rol1 = input("Ingrese el primer rol a comparar: ")
rol2 = input("Ingrese el segundo rol a comparar: ")

if rol1 in roles and rol2 in roles:
    comunes = roles[rol1] & roles[rol2]
    print(f"    {rol1} n {rol2}: {sorted(comunes)}")
    