"""
═══════════════════════════════════════════════════════════════════════════════
CASO DE USO 4: SEGURIDAD - CONTROL DE ACCESO
Algoritmos y Programación 4 - Semana 6
═══════════════════════════════════════════════════════════════════════════════

ENUNCIADO:
----------
Una empresa necesita un sistema de control de acceso basado en roles.
Cada rol tiene un conjunto de permisos. El sistema debe:

1. Verificar si un usuario puede realizar una acción
2. Encontrar permisos comunes entre roles
3. Encontrar permisos exclusivos de cada rol
4. Verificar si un rol es "superior" a otro (tiene todos sus permisos)
5. Crear un nuevo rol combinando permisos de otros

Implementar usando operaciones de conjuntos.
"""

# ═══════════════════════════════════════════════════════════════════════════════
# DATOS
# ═══════════════════════════════════════════════════════════════════════════════

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
    "admin": Conjunto({
        "leer", "escribir", "eliminar", "crear_usuarios",
        "ver_logs", "configurar", "backup", "restaurar"
    }),
    "editor": Conjunto({"leer", "escribir", "subir_archivos"}),
    "viewer": Conjunto({"leer"}),
    "moderador": Conjunto({"leer", "escribir", "eliminar", "ver_logs"}),
    "auditor": Conjunto({"leer", "ver_logs", "exportar_reportes"}),
}

usuarios = {
    "Juan": "admin",
    "María": "editor",
    "Pedro": "viewer",
    "Ana": "moderador",
    "Carlos": "auditor",
}

# ═══════════════════════════════════════════════════════════════════════════════
# SOLUCIÓN
# ═══════════════════════════════════════════════════════════════════════════════

print("=" * 60)
print("   SEGURIDAD - CONTROL DE ACCESO")
print("=" * 60)

print("\nRoles y permisos:")
for rol, permisos in roles.items():
    print(f"  {rol}: {permisos}")

print("\nUsuarios:")
for usuario, rol in usuarios.items():
    print(f"  {usuario} → {rol}")

# 1. Verificar si un usuario puede realizar una acción
print("\n" + "=" * 60)
print("1. VERIFICAR ACCESO")
print("=" * 60)

def puede_hacer(usuario, acciones_requeridas):
    """Verifica si el usuario tiene todos los permisos necesarios"""
    rol = usuarios.get(usuario)
    if not rol:
        return False
    permisos = roles.get(rol)
    return acciones_requeridas.subconjunto(permisos)  # subconjunto

verificaciones = [
    ("Juan", Conjunto({"leer", "eliminar"})),
    ("María", Conjunto({"leer", "escribir"})),
    ("María", Conjunto({"eliminar"})),
    ("Pedro", Conjunto({"leer"})),
    ("Pedro", Conjunto({"escribir"})),
    ("Ana", Conjunto({"leer", "ver_logs"})),
]

for usuario, acciones in verificaciones:
    resultado = "✓" if puede_hacer(usuario, acciones) else "✗"
    print(f"  {resultado} {usuario} → {acciones}")

# 2. Permisos comunes entre roles
print("\n" + "=" * 60)
print("2. PERMISOS COMUNES")
print("=" * 60)

pares_roles = [
    ("editor", "moderador"),
    ("moderador", "auditor"),
    ("editor", "auditor"),
]

for r1, r2 in pares_roles:
    comunes = roles[r1].interseccion(roles[r2])
    print(f"  {r1} ∩ {r2}: {comunes}")

# 3. Permisos exclusivos de cada rol
print("\n" + "=" * 60)
print("3. PERMISOS EXCLUSIVOS")
print("=" * 60)

for nombre, permisos in roles.items():
    otros_permisos = Conjunto()
    for otro_nombre, otros in roles.items():
        if otro_nombre != nombre:
            otros_permisos = otros_permisos.union(otros)
    exclusivos = permisos.diferencia(otros_permisos)
    if not exclusivos.esta_vacio():
        print(f"  {nombre}: {exclusivos}")
    else:
        print(f"  {nombre}: (ninguno exclusivo)")

# 4. ¿Un rol es "superior" a otro?
print("\n" + "=" * 60)
print("4. JERARQUÍA DE ROLES")
print("=" * 60)

for r1 in roles:
    for r2 in roles:
        if r1 != r2 and roles[r2].subconjunto(roles[r1]) and not roles[r1].subconjunto(roles[r2]): #Esto representa un subconjunto propio
            print(f"  {r1} contiene todos los permisos de {r2}")

# 5. Crear nuevo rol combinando otros
print("\n" + "=" * 60)
print("5. CREAR ROL COMBINADO")
print("=" * 60)

nuevo_rol = roles["editor"].union(roles["auditor"])
print(f"  editor + auditor = {nuevo_rol}")

# Verificar que no tenga permisos peligrosos
permisos_peligrosos = Conjunto({"eliminar", "crear_usuarios", "configurar"})
conflictos = nuevo_rol.interseccion(permisos_peligrosos)

if not conflictos.esta_vacio():
    print(f"  Alerta: tiene permisos peligrosos: {conflictos}")
else:
    print(f"  Sin permisos peligrosos")
