roles = {
    "admin": {
        "leer", "escribir", "eliminar", "crear_usuarios",
        "ver_logs", "configurar", "backup", "restaurar"
    },
    "editor": {"leer", "escribir", "subir_archivos"},
    "viewer": {"leer"},
    "moderador": {"leer", "escribir", "eliminar", "ver_logs"},
    "auditor": {"leer", "ver_logs", "exportar_reportes"},
}
usuarios = {
    "Juan": "admin",
    "María": "editor",
    "Pedro": "viewer",
    "Ana": "moderador",
    "Carlos": "auditor",
}
"""crear un metodo que reciba un conjunto de acciones y un usuario, y retorno True o Flase
dependiendo si el usuario puede o no realizar ese conjunto de acciones"""
def validar_acciones(usuario, acciones):
    rol = usuarios.get(usuario)
    if not rol:
        return False
    permisos = roles.get(rol, set())
    return acciones <= permisos

print(validar_acciones("Ana", {"ver_logs"}))

#Determinar permisos exclusivos de cada rol
for nombre, permisos in roles.items():
    otros_permisos = set()
    for otro_nombre, otros in roles.items():
        if otro_nombre != nombre:
            otros_permisos = otros_permisos | otros
    exclusivos = permisos - otros_permisos
    if exclusivos:
        print(f"Los permisos exclusivos del rol {nombre} son {exclusivos}")
    else:
        print(f"el rol {nombre} no tiene permisos exclusivos")

