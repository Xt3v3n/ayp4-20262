import re

# . --> Representa cualquier caracter (una vez)
# ^ --> Al inicio del texto
# $ --> Al final del texto
# * --> Un caracter puede estar cero o mas veces
# + --> Un caracter puede estar cero o una vez
# {} --> Un caracter esta un numero definido de veces
# \w --> Todas la letras (mayusculas y minusculas, numero y gion bajo)
texto = "ac abc abbc abbbbc"
resultado = re.findall(r"ab+c", texto)
print(resultado)