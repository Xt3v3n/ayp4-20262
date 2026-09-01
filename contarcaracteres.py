def contar_caracteres(s, c):
    if len(s) == 0:
        return 0

    cuenta = 1 if s[0] == c else 0

    return cuenta + contar_caracteres(s[1:], c)

print(contar_caracteres("alicia", "a"))
