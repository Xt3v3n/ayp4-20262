import re

"""
resultado = re.match("genial", texto) # busca si una expresion esta al inicio

search = re.search("monty python", texto) # busca si una expresion esta en el texto

findall = re.findall("geniales", texto) # busca la cantidad de veces que esta una expresion

mayus_minus = re.findall("geniales", texto, re.IGNORECASE) # con el re.IGNORECASE toma en cuenta las palabras no importa si son en mayusculas o minusculas

print(resultado)
print(search)
print(findall)
print(mayus_minus)

encontrar_numeros_separados = re.findall(r"\d", texto)

encontrar_numeros_juntos = re.findall(r"\d+", texto)

print(encontrar_numeros_separados)
print(encontrar_numeros_juntos)

p = re.findall(r"g.to", texto) # busca palabras que comparten caracteres

a = re.findall(r"g..to", texto)

o = re.findall(r"\.", texto) # el \ toma literalmente el valor que se pide

e = re.findall(r".", texto) # el punto representa a todos los valores de la expresion

i = re.findall(r"g...", texto)

r = re.findall(r"^gato", texto) # determina el inicio

g = re.findall(r"gaato.$", texto) # determina el final

print(p)
print(a)
print(o)
print(e)
print(i)
print(r)
print(g)

a = re.findall(r"ab+c", texto)

b = re.findall(r"ab*c", texto)

print(a)
print(b)

correo = re.findall(r".+@", texto)
correo2 = re.findall(r".*@", texto) # El * sirve para ver todos lo elementos anteriores o que estan estre algo
correo3 = re.findall(r".?@", texto)
correo4 = re.findall(r".{3}@", texto) # Antes del @ deben haber 3 caracteres
correo5 = re.findall(r"^.{3}@", texto) # Al inicio deben haber 3 caracteres antes del @
correo6 = re.findall(r"^.{5,}@") # El texto debe tener al menos 5 caracteres antes del @
correo7 = re.findall(r"^.{5,10}@") # El texto debe tener entre 5 y 10 caracteres antes del @

print(correo)
print(correo2)
print(correo3)

# Aun tiene algunos problemas para validar un correo pero es un primer paso
if len(correo) > 0: 
    print("Correo valido")
else:
    print("Correo invalido")

algo = re.findall(r"g[aeiou]to", texto)
algo2 = re.findall(r"g[a-z,\d]to", texto)
algo3 = re.findall(r"g\d+to", texto)
algo4 = re.findall(r"g[^aeiou]to", texto) #^ en este caso es una negacion

print(algo)
print(algo2)
print(algo3)
print(algo4)

pn = re.findall(r"perro|gato|pez", texto)

print(pn)

pr = re.findall(r"\$\d+\.\d+", texto) #Es una combinacion para buscar un precio con esta estructura $100.00
pm = re.findall(r"\(.*\)", texto)

print(pr)
print(pm)

aa = re.findall(r"(Java|Type|Coffe)Script", texto)

print(aa)
"""
texto = "juan@gmail.com.co"

pt = re.findall(r"^\w+@\w+\.\w{2,3}", texto) #El \w es como el punto pero no toma en cuenta los puntos y los espacios

print(pt)