import re

texto = "gato, geto, gito, goto, guto, g4to, g--to"

"""resultado = re.match("Estoy", texto)
print(resultado)"""

"""resultado = re.search("Python", texto)
print(resultado)

resultado = re.findall("o", texto)
print(resultado)"""

resultado = re.findall(r"g..to", texto) # El punto es un metacaracter / comodin
print(resultado)