from datetime import date
   
# ═══════════════════════════════════════════════════════════════════════════════
# ESTRUCTURA
# ═══════════════════════════════════════════════════════════════════════════════
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class Biblioteca:
    def __init__(self):
        self.cabeza = None

    def esta_vacia(self):
        return self.cabeza is None

    def insertar(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    def buscar_recursivo(self, nodo, criterio):
        if nodo is None:
            return None
        if criterio(nodo.dato):
            return nodo.dato
        return self.buscar_recursivo(nodo.siguiente, criterio)

    def buscar(self, criterio):
        return self.buscar_recursivo(self.cabeza, criterio)

    def buscar_todos_recursivo(self, nodo, criterio, resultados):
        if nodo is None:
            return
        if criterio(nodo.dato):
            resultados.append(nodo.dato)
        self.buscar_todos_recursivo(nodo.siguiente, criterio, resultados)

    def buscar_todos(self, criterio):
        resultados = []
        self.buscar_todos_recursivo(self.cabeza, criterio, resultados)
        return resultados

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
        return " -> ".join(elementos)

# ═══════════════════════════════════════════════════════════════════════════════
# CATALOGO
# ═══════════════════════════════════════════════════════════════════════════════

catalogo = {}
generos_disponibles = set()

def agregar_libro(titulo, autor, genero):
    """
    Agrega un libro al catalogo en su genero correspondiente.
    Si el genero no existe, lo crea. O(1) amortizado.
    """
    libro = {
        "titulo": titulo,
        "autor": autor,
        "genero": genero,
        "disponible": True
    }

    if genero not in catalogo:
        catalogo[genero] = Biblioteca()
        generos_disponibles.add(genero)
    
    catalogo[genero].insertar(libro)

def buscar_libros_por_titulo(titulo):
    """
    Busca un libro por titulo o fragmento de titulo. O(n*m)
    """
    resultados = []

    for genero, lista in catalogo.items():
        resultado = lista.buscar_todos(lambda libro: titulo.lower() in libro["titulo"].lower())
        if resultado:
            resultados.extend(resultado)
    
    return resultados

def buscar_libros_por_autor(autor):
    """
    Busca todos los libros de un autor. O(n*m)
    """
    resultados = []

    for lista in catalogo.values():
        resultado = lista.buscar_todos(lambda libro: autor.lower() in libro["autor"].lower())
        if resultado:
            resultados.extend(resultado)
    
    return resultados,

def buscar_libros_por_genero(genero):
    """
    Retorna un set con los titulos disponibles de un genero. O(n)
    """
    if genero not in generos_disponibles:
        return set()
    
    libros = catalogo[genero].a_lista()
    titulos_disponibles = set()

    for libro in libros:
        if libro["disponible"]:
            titulos_disponibles.add(libro["titulo"])
    
    return titulos_disponibles

def mostrar_catalogo():
    """Muestra todos los libros organizados por genero. O(n*m)"""
    if not catalogo:
        print("El catalogo esta vacio.")
        return
    
    for genero, lista in catalogo.items():
        print(f"Genero: {genero}")
        libros = lista.a_lista()

        for libro in libros:
            if libro["disponible"]:
                estado = "Disponible"
            else:
                estado = "Prestado"
            
            print(f"   - {libro['titulo']} | {libro['autor']} | {estado}")


# ═══════════════════════════════════════════════════════════════════════════════
# USUARIOS
# ═══════════════════════════════════════════════════════════════════════════════

usuarios = Biblioteca()
documentos_registrados = set()

def registrar_usuario(documento, nombre, telefono, correo):
    """
    Registra un nuevo usuario si el documento no existe. O(1)
    """
    if documento in documentos_registrados:
        print(f"El documento {documento} ya esta registrado.")
        return False
    
    usuario = {
        "documento": documento,
        "nombre": nombre,
        "telefono": telefono,
        "correo": correo
    }

    usuarios.insertar(usuario)
    documentos_registrados.add(documento)
    return True

def buscar_usuario(documento):
    """
    Busca un usuario por documento usando recursividad. O(n)
    """
    return usuarios.buscar(lambda u: u["documento"] == documento)

def mostrar_usuarios():
    """
    Muestra todos los usuarios registrados. O(n)
    """
    if usuarios.esta_vacia():
        print("No hay usuarios registrados.")
        return
    
    lista = usuarios.a_lista()

    for u in lista:
        print(f"Documento: {u['documento']} | Nombre: {u['nombre']} | Telefono: {u['telefono']} | Correo: {u['correo']}")

# ═══════════════════════════════════════════════════════════════════════════════
# PRESTAMOS
# ═══════════════════════════════════════════════════════════════════════════════

prestamos = Biblioteca()

def registrar_prestamo(documento, titulo_libro):
    usuario = buscar_usuario(documento)
    if usuario is None:
        print("El usuario no esta registrado.")
        return False
    
    resultados = buscar_libros_por_titulo(titulo_libro)
    if not resultados:
        print("El libro no existe en el catalogo.")
        return False
    
    libro = resultados[0]  

    if not libro["disponible"]:
        print(f"El libro '{titulo_libro}' no esta disponible en este momento.")
        return False
    
    prestamo = {
        "documento": documento,
        "nombre_usuario": usuario["nombre"],
        "titulo_libro": titulo_libro,
        "fecha_prestamo": date.today(),
        "fecha_devolucion": None,
        "estado": "en curso"
    }

    libro["disponible"] = False
    prestamos.insertar(prestamo)
    print(f"Prestamo registrado exitosamente para {usuario['nombre']}.")
    return True

def registrar_devolucion(documento, titulo_libro):
    prestamo = prestamos.buscar(
        lambda p: p["documento"] == documento and
        p["titulo_libro"].lower() == titulo_libro.lower() and
        p["estado"] == "en curso"
    )

    if prestamo is None:
        print("No se encontro un prestamo activo con esos datos.")
        return False
    
    resultados = buscar_libros_por_titulo(titulo_libro)
    libro = resultados[0]

    prestamo["fecha_devolucion"] = date.today()
    prestamo["estado"] = "entregado"
    libro["disponible"] = True

    print("Devolucion registrada exitosamente.")
    return True

def verificar_atrasos():
    """
    Revisa todos los prestamos en curso y marca los atrasados. O(n)
    Se considera atrasado si lleva mas de 14 dias.
    """
    lista = prestamos.a_lista()
    hoy = date.today()

    for prestamo in lista:
        if prestamo["estado"] == "en curso":
            dias = (hoy - prestamo["fecha_prestamo"]).days
            if dias > 14:
                prestamo["estado"] = "atrasado"

def mostrar_prestamos_activos():
    """
    Muestra todos los prestamos en curso o atrasados. O(n)
    """
    lista = prestamos.a_lista()
    hay_activos = False

    for prestamo in lista:
        if prestamo["estado"] == "en curso" or prestamo["estado"] == "atrasado":
            hay_activos = True
            print(f"Usuario: {prestamo['nombre_usuario']} | Libro: {prestamo['titulo_libro']} | Desde: {prestamo['fecha_prestamo']} | Estado: {prestamo['estado']}")
    
    if not hay_activos:
        print("No hay prestamos activos.")


# ═══════════════════════════════════════════════════════════════════════════════
# EJECUCION
# ═══════════════════════════════════════════════════════════════════════════════
registrar_usuario("111", "Carlos Perez", "3001234567", "carlos@mail.com")
registrar_usuario("222", "Laura Gomez", "3109876543", "laura@mail.com")
registrar_usuario("333", "Andres Torres", "3205551234", "andres@mail.com")

agregar_libro("Cien años de soledad", "Gabriel Garcia Marquez", "Novela")
agregar_libro("El amor en los tiempos del colera", "Gabriel Garcia Marquez", "Novela")
agregar_libro("El principito", "Antoine de Saint-Exupery", "Fantasia")
agregar_libro("Harry Potter y la piedra filosofal", "J.K. Rowling", "Fantasia")
agregar_libro("Harry Potter y la camara de los secretos", "J.K. Rowling", "Fantasia")
agregar_libro("Sapiens", "Yuval Noah Harari", "Historia")
agregar_libro("El arte de la guerra", "Sun Tzu", "Historia")


while True:
    print("===== BIBLIOTECA =====")
    print("1. Registrar usuario")
    print("2. Buscar usuario")
    print("3. Mostrar usuarios")
    print("4. Agregar libro")
    print("5. Mostrar catalogo")
    print("6. Buscar libro por titulo")
    print("7. Buscar libros por autor")
    print("8. Buscar libros por genero")
    print("9. Registrar prestamo")
    print("10. Registrar devolucion")
    print("11. Mostrar prestamos activos")
    print("12. Verificar atrasos")
    print("0. Salir")

    opcion = input("Ingresa que deseas hacer: ")

    match opcion:

        case "1":
            documento = input("Documento: ")
            nombre = input("Nombre: ")
            telefono = input("Telefono: ")
            correo = input("Correo: ")
            registrar_usuario(documento, nombre, telefono, correo)

        case "2":
            documento = input("Documento a buscar: ")
            usuario = buscar_usuario(documento)

            if usuario:
                print(
                    f"Usuario encontrado: "
                    f"{usuario['nombre']} | "
                    f"{usuario['telefono']} | "
                    f"{usuario['correo']}"
                )
            else:
                print("Usuario no encontrado.")

        case "3":
            mostrar_usuarios()

        case "4":
            titulo = input("Titulo: ")
            autor = input("Autor: ")
            genero = input("Genero: ")

            agregar_libro(titulo, autor, genero)
            print(f"Libro '{titulo}' agregado exitosamente.")

        case "5":
            mostrar_catalogo()

        case "6":
            titulo = input("Titulo a buscar: ")
            resultados= buscar_libros_por_titulo(titulo)

            if resultados:
                for libro in resultados:
                    estado = "Disponible" if libro["disponible"] else "Prestado"

                    print(
                        f"{libro['titulo']} | "
                        f"{libro['autor']} |  "
                        f"{libro['genero']} |"
                        f"{estado}"
                    )
            else:
                print("No se encontro ningun libro.")

        case "7":
            autor = input("Autor a buscar: ")
            resultados = buscar_libros_por_autor(autor)

            if resultados:
                for libro in resultados:
                    estado = "Disponible" if libro["disponible"] else "Prestado"

                    print(
                        f"{libro['titulo']} | "
                        f"{libro['autor']} |  "
                        f"{libro['genero']} |"
                        f"{estado}"
                    )
            else:
                print("No se encontro ningun libro.")

        case "8":
            print(f"Generos disponibles: {generos_disponibles}")
            genero = input("Genero a buscar: ")

            titulos = buscar_libros_por_genero(genero)

            if titulos:
                print(f"Libros disponibles en '{genero}':")

                for titulo in titulos:
                        print(f" - {titulo}")
            else:
                print(
                    f"No hay libros disponibles en el genero '{genero}'."
                )

        case "9":
            documento = input("Documento del usuario: ")
            titulo = input("Titulo del libro: ")

            registrar_prestamo(documento, titulo)

        case "10":
            documento = input("Documento del usuario: ")
            titulo = input("Titulo del libro a devolver: ")

            registrar_devolucion(documento, titulo)

        case "11":
                mostrar_prestamos_activos()

        case "12":
            verificar_atrasos()
            print("Atrasos verificados.")

        case "0":
            print("Que tenga un feliz dia.")
            break

        case _:
            print("Opcion incorrecta--Ingrese un valor correcto.")