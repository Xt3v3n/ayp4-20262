def busqueda_binaria(lista, objetivo, inicio, fin):

    if inicio > fin:
        return -1

    medio = (inicio + fin) // 2

    if objetivo == lista[medio]:
        return medio
    elif objetivo < lista[medio]:
        return busqueda_binaria(lista, objetivo, inicio, medio - 1)
    else:
        return busqueda_binaria(lista, objetivo, medio + 1, fin)

lista_nueva = [5,7,9,12,15]
print (busqueda_binaria(lista_nueva, 15, 0, len(lista_nueva)))