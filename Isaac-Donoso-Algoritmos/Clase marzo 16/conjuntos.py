import re

canciones_juan = {
    "Confeciones de invierno", "Libros sapienciales", "Me voy", "Tu misterioso alguien",
    "Rezo por vos", "Nada personal", "Bolero falaz", "De madrugada", "Rosa pastel"
    }

canciones_maria = {
    "Estoy aqui", "Rosa pastel", "Me voy", "Limon y sal", "En el 2000", " Ella es bonita",
    "Si te vas", "Tu misterioso alguien", "No necesito", "Nada personal"
}

#Comun(Interseccion)
playlist_comun = canciones_juan.intersection(canciones_maria)
playlist_comun = canciones_juan & canciones_maria

#Eliminar(Diferencia) --> el orden importa a-b != b-a
recomendaciones_juan = canciones_maria - canciones_juan

#Union
catalogo = canciones_juan | canciones_maria
catalogo = canciones_juan.union(canciones_maria)

#Subconjunto (Lo de la primera pertenece a la otra)
a = {canciones_juan <= canciones_maria}

#Diferencia simetrica --> a-b & b-a (esta es la forma mas clara en la que entiendo esta cosa)
exclusivas = canciones_juan ^ canciones_maria

algoritmos = {"Ana", "Carlos", "Eduardo", "Fernanda", "Gabriel", "Helena", "Ivan"}

bases_de_datos = {"Carlos", "Diana", "Juan", "Karen", "Gabriel", "Luis", "Maria"}

redes = {"Diana", "Eduardo", "Gabriel", "Karen", "Natalia", "Oscar", "Ivan"}

estudian_todas = algoritmos & bases_de_datos & redes

solo_en_algoritmos = algoritmos - bases_de_datos - redes

solo_bases_datos = bases_de_datos - algoritmos - redes

solo_en_redes = redes - bases_de_datos - algoritmos

solo_en_una = solo_en_algoritmos | solo_bases_datos | solo_en_redes

algoritmos_bases = algoritmos.intersection(bases_de_datos)

algoritmos_redes = algoritmos.intersection(redes)

bases_redes = bases_de_datos.intersection(redes)

print(len(solo_en_una))

estudiantes = algoritmos | bases_de_datos | redes

reporte = {}

#Forma hecha por mi 
for estudiante in sorted(estudiantes):
    if estudiante in estudian_todas:
        reporte[estudiante] = {"Algoritmos", "Bases de datos", "Redes"}
    elif estudiante in solo_en_algoritmos:
        reporte[estudiante] = {"Algoritmos"}
    elif estudiante in solo_bases_datos:
        reporte[estudiante] = {"Bases de datos"}
    elif estudiante in solo_en_redes:
        reporte[estudiante] = {"Redes"}
    elif estudiante in algoritmos_bases:
        reporte[estudiante] = {"Algoritmos", "Bases de datos"}
    elif estudiante in algoritmos_redes:
        reporte[estudiante] = {"Algoritmos", "Redes"}
    elif estudiante in bases_redes:
        reporte[estudiante] = {"Bases de datos", "Redes"}
    else:
        reporte[estudiante] = {"No esta en ninguna clase"}

print(reporte)

reporte = {}

print()
#Forma hecha por el profe
for estudiante in sorted(estudiantes):
    materias = []

    if estudiante in algoritmos:
        materias.append("Algoritmos")
    if estudiante in redes:
        materias.append("Redes")
    if estudiante in bases_de_datos:
        materias.append("Bases de datos")
    
    reporte[estudiante] = materias

print(reporte)


catalogo = {
    "Inception" : {"Ciencia ficcion", "Accion", "Thriller", "Drama"},
    "The matrix" : {"Ciencia ficcion", "Accion" , "Thriller"},
    "Titanic" : {"Romance", "Drama", "Historica"},
    "The notebook" : {"Romance", "Drama"},
    "Avengers" : {"Accion", "Ciencia ficcion", "Aventura"},
    "John Wick" : {"Accion", "Thriller", "Crimen"},
    "Interstellar" : {"Ciencia ficcion", "Drama", "Aventura"},
    "The Godfather" : {"Crimen", "Drama", "Thriller"},
    "Toy story" : {"Animacion", "Comedia","Aventura"},
    "Shrek" : {"Animacion", "Comedia","Aventura"}
}

peliculas = list(catalogo.keys())
peliculas_comunes = []


for i in range(len(peliculas)):
    for j in range(i+1, len(peliculas)):
        p1, p2 = peliculas[i], peliculas[j]
        comunes = catalogo[p1] & catalogo[p2]

        if len(comunes) >= 2:
            peliculas_comunes.append((p1, p2, comunes))

print(peliculas_comunes)

favoritos_mios = {"Accion", "Thriller", "Aventura"}
recomendaciones = []

for pelicula, genero in catalogo.items():
    coincidencia = genero & favoritos_mios
    if coincidencia:
        porcentaje = round((len(coincidencia)/len(favoritos_mios))*100, 2)
        recomendaciones.append((pelicula, F"{porcentaje}%"))

print(recomendaciones)