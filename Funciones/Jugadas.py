from Colores import Colors
from random import randint


def getRandomPosition(tablero):
    return randint(0, len(tablero) - 1), randint(0, len(tablero) - 1)


def computerMove(tablero, letra):
    fila, columna = getRandomPosition(tablero.tablero)
    while not tablero.escribir(letra, fila, columna):
        fila, columna = getRandomPosition(tablero.tablero)
    return fila, columna


def getValidInput(prompt, valid_range):
    value = int(input(prompt))
    while value not in valid_range:
        value = int(input(f"NO VÁLIDO. {prompt}"))
    return value


def playerMove(tablero, letra):
    valid_range = range(1, len(tablero.tablero) + 1)
    fila = getValidInput("\nEn qué fila quieres escribir?  ", valid_range) - 1
    columna = getValidInput("\nEn qué columna quieres escribir?  ", valid_range) - 1

    while not tablero.escribir(letra, fila, columna):
        print("\nCasilla OCUPADA")
        fila = getValidInput("\nEn qué fila quieres escribir?  ", valid_range) - 1
        columna = getValidInput("\nEn qué columna quieres escribir?  ", valid_range) - 1

    return fila, columna


def displayMove(tablero, letraUsuario, letraOrdenador, letra, move_type, row, col):
    tablero.mostrarConColores(letraUsuario, letraOrdenador)
    print(f"La jugada de {move_type} ha sido:", end=" ")
    color_func = Colors.cyan if move_type == "usuario" else Colors.red
    color_func()
    Colors.bold()
    print(letra, end=" ")
    Colors.reset()
    print(f"en la fila {row + 1} y columna {col + 1}")


def jugadaUsuario(tablero, letraUsuario, letraOrdenador):
    fila, columna = playerMove(tablero, letraUsuario)
    displayMove(
        tablero, letraUsuario, letraOrdenador, letraUsuario, "usuario", fila, columna
    )


def jugadaOrdenador(tablero, letraUsuario, letraOrdenador):
    fila, columna = computerMove(tablero, letraOrdenador)
    displayMove(
        tablero,
        letraUsuario,
        letraOrdenador,
        letraOrdenador,
        "ordenador",
        fila,
        columna,
    )


def gameEnd(tablero):
    return tablero.tenemosTresRalla() or tablero.tableroLleno()


def ganador(tablero, letra):
    if tablero.tenemosTresRalla():
        return letra
    elif tablero.tableroLleno():
        return 0
    return None


def declareWinner(tablero, letra, player_type):
    winner = ganador(tablero, letra)
    if winner == letra:
        color = Colors.cyan if player_type == "usuario" else Colors.red
        color()
        Colors.bold()
        print(f"\n\nGANA {player_type.upper()}")
    elif winner == 0:
        Colors.bold()
        print("\nNo ha ganado nadie, tenemos un EMPATE")
    Colors.reset()
    return winner


def ganaUsuario(tablero, letraUsuario):
    return declareWinner(tablero, letraUsuario, "usuario")


def ganaOrdenador(tablero, letraOrdenador):
    return declareWinner(tablero, letraOrdenador, "ordenador")
