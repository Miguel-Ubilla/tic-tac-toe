class User:
    def __init__(self, nombre):
        self.nombre = nombre
        self.partidas_jugadas = 0
        self.partidas_ganadas = 0
        self.partidas_perdidas = 0
        self.empates = 0

    def actualizar(self, partidas_ganadas=0, partidas_perdidas=0, empates=0):
        self.partidas_ganadas += partidas_ganadas
        self.partidas_perdidas += partidas_perdidas
        self.empates += empates
        self.partidas_jugadas += partidas_ganadas + partidas_perdidas + empates

    def obtener_estadisticas(self):
        return {
            "Nombre": self.nombre,
            "Partidas Jugadas": self.partidas_jugadas,
            "Partidas Ganadas": self.partidas_ganadas,
            "Partidas Perdidas": self.partidas_perdidas,
            "Empates": self.empates,
        }
