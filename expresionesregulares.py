import re

texto = "Estoy usando Python"

"""resultado = re.match("Estoy", texto)
print(resultado)"""

"""resultado = re.search("Python", texto)
print(resultado)"""

resultado = re.findall("o", texto)
print(resultado)