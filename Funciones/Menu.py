from Colores import Colors


def apply_color(text, color_func):
    return color_func() + text + Colors.reset()


def determinarTam():
    while True:
        tamaño = int(
            input(
                "\n\nDe qué tamaño quieres el tablero ? (3 en ralla, 4 en ralla, etc): "
            )
        )
        if tamaño >= 3:
            return tamaño
        print("Me tienes que dar un tamaño mayor o igual a 3.")


def escogeLetra():
    while True:
        letra = input("\n\n\nQuieres jugar con la X o con 0 ?:  ").upper()
        if letra in ["X", "0"]:
            letraOrdenador = "0" if letra == "X" else "X"
            return letra, letraOrdenador
        print("Me tienes que dar una X o 0 (un cero).")


def quienEmpieza():
    prompt = apply_color(
        "\n\n\nQuién empieza, tú o el ordenador? (TÚ = 1 | ORDENADOR = 2): ",
        Colors.green,
    )
    while True:
        empieza = input(prompt)
        if empieza in ["1", "2"]:
            return empieza
        print("Me tienes que dar un Uno o un Dos.")


def chooseOption():
    while True:
        opcion = int(
            input(
                "\n\n\nPara comenzar el juego dame 1, para acabar el programa dame 0, (COMENZAR = 1 | ACABAR = 0):  "
            )
        )
        if opcion in [0, 1]:
            return opcion
        print("Intenta de nuevo, (COMENZAR = 1 | ACABAR = 0).")
