from sys import stdout

RED = "\033[1;31m"
CYAN = "\033[1;36m"
GREEN = "\033[0;32m"
BLUE = "\033[1;34m"
BOLD = "\033[1m"
RESET = "\033[0m"


def red():
    return RED


def cyan():
    return CYAN


def green():
    return GREEN


def blue():
    return BLUE


def bold():
    return BOLD


def reset():
    return RESET
