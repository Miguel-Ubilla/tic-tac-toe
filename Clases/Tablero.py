from Funciones.Matriz import crearMatriz
from Colores.Colors import bold, reset, red, cyan


class Tablero:
    def __init__(self, tamaño):
        self.tamaño = tamaño
        self.tablero = crearMatriz(tamaño, tamaño)

    def escribir(self, letra, fila, columna):
        if self.tablero[fila][columna] == "*":
            self.tablero[fila][columna] = letra
            return True
        return False

    def mostrar(self):
        print("\n\n\nEl tablero es: \n\n")
        bold()
        for fila in self.tablero:
            print("    ".join(fila))
            print("\n")
        reset()

    def mostrarConColores(self, letraUsuario, letraOrdenador):
        print("\n\n\nEl tablero es: \n\n")
        for fila in self.tablero:
            for elemento in fila:
                bold()
                if elemento == letraUsuario:
                    cyan()
                elif elemento == letraOrdenador:
                    red()
                print(elemento, end="    ")
                reset()
            print("\n")

    def esTresRallaPorFilas(self):
        return any(
            all(e == fila[0] and e != "*" for e in fila) for fila in self.tablero
        )

    def esTresRallaPorColumnas(self):
        return any(
            all(
                self.tablero[i][col] == self.tablero[0][col]
                and self.tablero[i][col] != "*"
                for i in range(self.tamaño)
            )
            for col in range(self.tamaño)
        )

    def esTresRallaPorDiagonalPrincipal(self):
        primer_elemento = self.tablero[0][0]
        return all(
            self.tablero[i][i] == primer_elemento and primer_elemento != "*"
            for i in range(self.tamaño)
        )

    def esTresRallaPorDiagonalSecundaria(self):
        primer_elemento = self.tablero[0][-1]
        return all(
            self.tablero[i][-i - 1] == primer_elemento and primer_elemento != "*"
            for i in range(self.tamaño)
        )

    def tenemosTresRalla(self):
        return (
            self.esTresRallaPorFilas()
            or self.esTresRallaPorColumnas()
            or self.esTresRallaPorDiagonalPrincipal()
            or self.esTresRallaPorDiagonalSecundaria()
        )

    def tableroLleno(self):
        return all(elemento != "*" for fila in self.tablero for elemento in fila)
