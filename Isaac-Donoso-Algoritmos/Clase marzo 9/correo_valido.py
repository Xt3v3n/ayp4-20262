import re

correo = input("Ingrese un correo: ")

patron = r"^\w+[\w\.]*@\w+(\.[a-z]{2,})+$"

if re.match(patron, correo):
    print("Correo valido")
else:
    print("Correo invalido")