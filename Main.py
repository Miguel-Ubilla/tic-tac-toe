from Clases.Tablero import Tablero
from Clases.Usuario import User
from Funciones.Menu import chooseOption, determinarTam, quienEmpieza, escogeLetra
from Funciones.Jugadas import (
    jugadaUsuario,
    jugadaOrdenador,
    gameEnd,
    ganaUsuario,
    ganaOrdenador,
)
from Colores.Colors import green, cyan, bold, reset


def playTurn(player, tablero, letraUsuario, letraOrdenador):
    if player == "usuario":
        jugadaUsuario(tablero, letraUsuario, letraOrdenador)
        return ganaUsuario(tablero, letraUsuario) is not None
    else:
        jugadaOrdenador(tablero, letraUsuario, letraOrdenador)
        return ganaOrdenador(tablero, letraOrdenador) is not None


def mostrarDatosUsuario(newUser):
    bold()
    print("\n\n\nTus Datos Actuales son los siguientes: \n")
    estadisticas = (
        newUser.obtener_estadisticas()
    )  # Usa el método para obtener las estadísticas
    for key, value in estadisticas.items():
        bold()
        print("\t", key, ":", end=" ")
        cyan()
        print(value)
        reset()
    reset()


try:
    bold()
    print("Dime tu nombre de usuario: ", end="")
    cyan()
    userName = input()
    reset()

    # Creamos un objeto de la clase User
    newUser = User(userName)

    # Iniciamos el juego
    opcion = chooseOption()

    # Inicializamos las variables que se corresponden a los datos del jugador
    numPartidas = 1
    ganadas = 0
    perdidas = 0
    empates = 0

    # Bucle para saber si continuamos el juego o paramos
    while opcion != 0:
        green()
        bold()
        print("\n\n\nPARTIDA", numPartidas)
        ganadas = 0
        perdidas = 0
        empates = 0
        reset()

        # Condiciones Iniciales
        dimensionTab = determinarTam()
        tablero = Tablero(dimensionTab)
        tablero.mostrar()
        primerJugador = quienEmpieza()
        letraUsuario, letraOrdenador = escogeLetra()

        players = (
            ["usuario", "ordenador"]
            if primerJugador == "1"
            else ["ordenador", "usuario"]
        )

        while True:
            game_over = False
            if playTurn(players[0], tablero, letraUsuario, letraOrdenador):
                if players[0] == "usuario":
                    ganadas += 1
                else:
                    perdidas += 1
                game_over = True

            if not game_over and playTurn(
                players[1], tablero, letraUsuario, letraOrdenador
            ):
                if players[1] == "usuario":
                    ganadas += 1
                else:
                    perdidas += 1
                game_over = True

            if gameEnd(tablero):
                if not game_over:
                    empates += 1
                game_over = True

            if game_over:
                break

        # Final de la partida
        newUser.actualizar(ganadas, perdidas, empates)

        mostrarDatosUsuario(newUser)

        numPartidas += 1

except Exception as e:
    print("Ha ocurrido un error:", e)
