import os


def line(dots=False):
    if dots:
        print(30 * "*")
    else:
        print(30 * "-")


def header(text):
    n = j = (28 - len(text)) / 2
    if not n.is_integer():
        j = j + 1
    print("|" + (int(n) * " ") + text + (int(j) * " ") + "|")


def echo(text):
    print("| " + text)


def prompt(text):
    return input("| " + text + " > ")


def clear():
    if os.name == "posix":
        os.system('clear')
    elif os.name == "nt":
        os.system("cls")


def print_header():
    clear()
    line()
    header("ARTIST DATABASE")
    line()
