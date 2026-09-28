import re

# ============================================================================
# PARTE 1: EXPRESIONES REGULARES (de básicas a complejas)
# ============================================================================
#
# ¿QUÉ ES UNA REGEX?
#   Un patrón que describe un CONJUNTO de cadenas de texto válidas.
#   El módulo 're' de Python evalúa (compila y ejecuta) ese patrón contra
#   una cadena para buscar coincidencias.
#
# EVALUACIÓN SEGÚN SU REPRESENTACIÓN
#   Una regex puede "representarse" de varias formas equivalentes que el
#   motor evalúa igual, aunque se escriban distinto:
#
#   1) Cadena normal vs cadena raw:
#         "\\d+"   (cadena normal: hay que escapar la barra invertida)
#         r"\d+"   (cadena raw: SIEMPRE se recomienda usar raw strings en
#                    regex, porque evita conflictos entre el escape de
#                    Python "\n", "\t"... y el escape de regex "\d", "\s")
#
#   2) Patrón sin compilar vs patrón compilado:
#         re.match(r"\d+", texto)              -> compila internamente
#                                                  cada vez que se llama
#         patron = re.compile(r"\d+")
#         patron.match(texto)                  -> compila UNA vez, se
#                                                  reutiliza -> más rápido
#                                                  si se usa muchas veces
#
#   3) Clases de caracteres explícitas vs atajos (equivalencias):
#         [0-9]        ==  \d      (dígito)
#         [^0-9]       ==  \D      (no dígito)
#         [ \t\n\r\f]  ==  \s      (espacio en blanco)
#         [^ \t\n\r]   ==  \S      (no espacio)
#         [a-zA-Z0-9_] ==  \w      (carácter de palabra)
#         [^a-zA-Z0-9_]==  \W      (no palabra)
#
#   4) Cuantificadores explícitos vs atajos (equivalencias):
#         {0,1}   ==  ?     (cero o una vez)
#         {0,}    ==  *     (cero o más veces)
#         {1,}    ==  +     (una o más veces)
#         {n,n}   ==  {n}   (exactamente n veces)
#
#   Estas equivalencias son un clásico de examen: te piden "reescribe
#   \d{1,} sin usar {}" -> respuesta: \d+

print("=" * 70)
print("PARTE 1: EXPRESIONES REGULARES")
print("=" * 70)

# ----------------------------------------------------------------------
# 1.1 Sintaxis y uso práctico: las funciones principales de `re`
# ----------------------------------------------------------------------
# re.match(patron, texto)    -> busca SOLO al inicio de la cadena
# re.search(patron, texto)   -> busca en TODA la cadena, primera coincidencia
# re.findall(patron, texto)  -> devuelve TODAS las coincidencias (lista)
# re.finditer(patron, texto) -> como findall pero devuelve iterador de
#                                objetos Match (con posición, grupos, etc.)
# re.sub(patron, repl, txt)  -> sustituye coincidencias
# re.split(patron, texto)    -> divide la cadena usando el patrón como
#                                separador

texto_demo = "Mi telefono es 300-123-4567 y el de la oficina 601-987-6543"

print("\n--- 1.1 Funciones básicas ---")
print("match :", re.match(r"Mi", texto_demo))          # coincide (inicio)
print("match2:", re.match(r"telefono", texto_demo))    # None (no es inicio)
print("search:", re.search(r"\d{3}-\d{3}-\d{4}", texto_demo).group())
print("findall:", re.findall(r"\d{3}-\d{3}-\d{4}", texto_demo))
print("sub    :", re.sub(r"\d{3}-\d{3}-\d{4}", "[TELEFONO]", texto_demo))
print("split  :", re.split(r"\s+y\s+", texto_demo))

# ----------------------------------------------------------------------
# 1.2 Grupos y captura
# ----------------------------------------------------------------------
# Paréntesis () -> crean un GRUPO DE CAPTURA (se puede extraer con .group(n))
# (?:...)       -> grupo NO capturante (agrupa para el cuantificador pero
#                  no se guarda en el resultado)
# (?P<nombre>..)-> grupo capturante CON NOMBRE, se accede con .group("nombre")

m = re.search(r"(\d{3})-(\d{3})-(\d{4})", texto_demo)
print("\n--- 1.2 Grupos ---")
print("Grupo completo :", m.group(0))
print("Codigo area    :", m.group(1))
print("Grupo 2        :", m.group(2))
print("Grupo 3        :", m.group(3))

m2 = re.search(r"(?P<area>\d{3})-(?P<medio>\d{3})-(?P<final>\d{4})", texto_demo)
print("Grupo con nombre 'area':", m2.group("area"))


# ============================================================================
# 1.3 CINCO EXPRESIONES REGULARES COMPLEJAS EXPLICADAS PARTE POR PARTE
# ============================================================================
print("\n--- 1.3 Regex complejas (5 ejemplos tipo examen) ---")

# --- EJEMPLO 1: Validación de correo electrónico -------------------------
# Patrón:  ^[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}$
#
#   ^                -> ancla: inicio de cadena
#   [\w.+-]+         -> uno o más caracteres de palabra, punto, +, o guion
#                       (esto es la parte local del correo: "juan.perez+ann")
#   @                -> el símbolo arroba literal
#   [\w-]+           -> uno o más caracteres de palabra o guion (dominio)
#   \.               -> un punto LITERAL (escapado, porque "." solo sin
#                       escapar significa "cualquier carácter")
#   [a-zA-Z]{2,}     -> el TLD (.com, .co, .info...), mínimo 2 letras
#   $                -> ancla: fin de cadena
regex_email = re.compile(r"^[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}$")
casos_email = ["juan.perez+ann@correo.com", "invalido@@x.com", "ana@dominio.co"]
print("\nEjemplo 1 - Emails:")
for c in casos_email:
    print(f"  {c!r:35} -> {'VALIDO' if regex_email.match(c) else 'INVALIDO'}")

# --- EJEMPLO 2: Validación de contraseña segura ---------------------------
# Patrón:  ^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$
#
#   ^                        -> inicio de cadena
#   (?=.*[a-z])              -> LOOKAHEAD positivo: en algún punto de la
#                                cadena debe existir una minúscula
#                                (no consume caracteres, solo "mira")
#   (?=.*[A-Z])              -> debe existir al menos una mayúscula
#   (?=.*\d)                 -> debe existir al menos un dígito
#   (?=.*[@$!%*?&])          -> debe existir al menos un carácter especial
#   [A-Za-z\d@$!%*?&]{8,}    -> ahora sí "consume": solo permite esos
#                                caracteres, y exige mínimo 8 de longitud
#   $                        -> fin de cadena
regex_password = re.compile(
    r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
)
casos_pass = ["Abcdef1!", "abcdefgh", "Abc1!", "Segura#2024"]
print("\nEjemplo 2 - Contraseñas seguras:")
for c in casos_pass:
    print(f"  {c!r:20} -> {'VALIDA' if regex_password.match(c) else 'INVALIDA'}")

# --- EJEMPLO 3: Extracción de fechas en formato dd/mm/aaaa -----------------
# Patrón:  \b(0[1-9]|[12]\d|3[01])/(0[1-9]|1[0-2])/(\d{4})\b
#
#   \b                -> límite de palabra (evita que "123/01/2024a" cuele)
#   (0[1-9]|[12]\d|3[01])  -> DÍA: 01-09, o 10-29, o 30-31 (alternancia |)
#   /                  -> separador literal
#   (0[1-9]|1[0-2])    -> MES: 01-09, o 10-12
#   /                  -> separador literal
#   (\d{4})            -> AÑO: exactamente 4 dígitos
#   \b                 -> límite de palabra
regex_fecha = re.compile(r"\b(0[1-9]|[12]\d|3[01])/(0[1-9]|1[0-2])/(\d{4})\b")
texto_fechas = "La reunión es el 15/08/2025, no el 31/02/2025 ni el 05/13/2025."
print("\nEjemplo 3 - Fechas dd/mm/aaaa extraídas:")
print(" ", regex_fecha.findall(texto_fechas))
# Nota: 31/02/2025 y 05/13/2025 NO deben aparecer (día/mes inválidos)

# --- EJEMPLO 4: Extracción de direcciones IPv4 -----------------------------
# Patrón:  \b(?:(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.){3}
#           (?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\b
#
#   (?: ... )            -> grupo NO capturante, agrupa la alternancia
#   25[0-5]              -> cubre 250-255
#   2[0-4]\d              -> cubre 200-249
#   1\d{2}                -> cubre 100-199
#   [1-9]?\d               -> cubre 0-9 y 10-99
#   \.                    -> el punto separador de octetos
#   {3}                   -> el bloque "octeto + punto" se repite 3 veces
#   luego un octeto final SIN punto
regex_ip = re.compile(
    r"\b(?:(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.){3}"
    r"(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\b"
)
texto_ip = "Servidores: 192.168.1.1 , 999.1.1.1 (invalida), 10.0.0.254"
print("\nEjemplo 4 - IPs válidas extraídas:")
print(" ", regex_ip.findall(texto_ip))

# --- EJEMPLO 5: Extracción de menciones y hashtags tipo redes sociales -----
# Patrón:  (?<![\w])([@#])(\w+)
#
#   (?<![\w])   -> LOOKBEHIND negativo: exige que justo ANTES del match
#                  NO haya un carácter de palabra (evita capturar
#                  "correo@dominio.com" como mención)
#   ([@#])      -> grupo 1: captura si es @ (mención) o # (hashtag)
#   (\w+)       -> grupo 2: el texto que sigue (nombre de usuario o tema)
regex_social = re.compile(r"(?<![\w])([@#])(\w+)")
texto_social = "Gran evento @PythonConf sobre #RegEx y #DataScience! correo@x.com"
print("\nEjemplo 5 - Menciones (@) y hashtags (#):")
for simbolo, contenido in regex_social.findall(texto_social):
    tipo = "Mención" if simbolo == "@" else "Hashtag"
    print(f"  {tipo}: {simbolo}{contenido}")


# ----------------------------------------------------------------------
# 1.4 MINI-CUESTIONARIO TIPO EXAMEN — Expresiones Regulares
# ----------------------------------------------------------------------
# P1) ¿Qué imprime re.findall(r"\d+", "a12b3c456")?
#     R1) ['12', '3', '456']
#
# P2) ¿Cuál es la diferencia entre re.match y re.search?
#     R2) match solo evalúa desde el INICIO de la cadena; search busca en
#         cualquier posición de la cadena.
#
# P3) Reescribe r"[0-9]{1,}" usando atajos.
#     R3) r"\d+"
#
# P4) ¿Qué hace (?:...) que (...) no hace?
#     R4) Agrupa sin crear un grupo de captura (no aparece en .group(n)
#         ni en el resultado de findall con grupos).
#
# P5) ¿Por qué se recomienda usar r"..." (raw strings) en regex?
#     R5) Porque evita que Python interprete secuencias como \n o \t antes
#         de que el motor de regex reciba el patrón; así \d llega tal cual
#         al motor en lugar de generar errores o comportamientos raros.
