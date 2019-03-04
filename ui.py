import os

#Prints out a line of "*" when True, otherwise a line of "-".
def line(dots = False):
    if dots == True:
        print(30 * "*")
    else:
        print(30 * "-")

#Calculates the blank space between the interface edges and the written header,
# when len(text) is odd, n is a fraction. Add one to j,
# the right side of the banner, to center it.
def header(text):
    n = j = (28 - len(text)) / 2
    if not n.is_integer():
        j = j + 1
    print("|" + (int(n) * " ") + text + (int(j) * " ") + "|")
    
#Prints out the left-side interface edge + a string.
def echo(text):
    print("| " + text)
    
#Prompts the user for input.
def prompt(text):
    return input("| " + text + " > ")
    
#clear for UNIX
#cls for WINDOWS NT
def clear():
    if os.name == "posix":
        os.system('clear')
    elif os.name == "nt":
        os.system("cls")
