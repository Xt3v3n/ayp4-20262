import re

#^3\d{2}[-\s]?\d{3}[-\s]?\d{2}[-\s]?\d{2}$ busca un numero de celular que empiece con 3 seguido de 2 digitos,
#  luego puede haber un guion o un espacio, luego 3 digitos, luego puede haber un guion o un espacio,
#  luego 2 digitos, luego puede haber un guion o un espacio y finalmente 2 digitos, el $ indica el final del texto
def validar_celular(numero):
    telefono_valido = re.match(r"^3\d{2}[-\s]?\d{3}[-\s]?\d{2}[-\s]?\d{2}$", numero) 
    if bool(telefono_valido):
        return "Numero celular valido"
    return "Numero celular invalido"
    


print(validar_celular("301-960-60-60"))
print(validar_celular("3226146194"))
print(validar_celular("301 960 60 60"))


def validar_fecha(fecha):
    fecha_valida = re.match(r"^(0[1-9]|[12]\d|3[01])[-/](0[1-9]|1[0-2])[-/](19|20)\d{2}$", fecha)
    return bool(fecha_valida)

def validar_clave(clave):
    mayusculas = r"[A-Z]"
    minusculas = r"[a-z]"
    numeros = r"\d"
    caracteres_especiales = r"[$!@%<>()?]"
    if len(clave) >= 8:
        if not re.search(mayusculas, clave):
            return "Falta mayuscula"
         
        if not re.search(minusculas, clave):
            return "Falta minuscula"
        
        if not re.search(numeros, clave):
            return "Falta numero"
         
        if not re.search(caracteres_especiales, clave):
            return "Falta caracter especial"
        return "La clave esta correcta"
    else:
        return "La clave le faltan caracteres"
        
print(validar_clave("fut4@eraA3"))