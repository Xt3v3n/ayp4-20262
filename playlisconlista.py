class Cancion:
    
    def __init__(self, titulo, artista, duracion):
        self.titulo = titulo
        self.artista = artista
        self.duracion = duracion

    def duracion_formateada(self):
        minutos = self.duracion // 60
        segundos = self.duracion % 60
        return minutos, segundos