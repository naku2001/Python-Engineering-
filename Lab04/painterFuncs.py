# Author: Perfect Makuwerere
# Date: February 18, 2026
# Description: Functional logic and ASCII art for the painting program.
import sys

def intro():
    """
    Welcomes the user and collects their art choice and border preference.
    :return: A tuple containing the choice (int) and the border symbol (str).
    """
    print("Welcome to the painting printer!")
    print("We have many options:")
    print("1. The S.S. Satisfaction")
    print("2. Mina in Repose")
    print("3. The Lone Pine")
    print("4. Tiny Ghost")
    
    choice = int(input("Please select a painting to print: "))
    border = input("What border would you like around your painting: ")
    return choice, border

def printHeaderFooter(border, size):
    """
    Prints a single line of the border symbol.
    :param border: The character to use for the border.
    :param size: How many times to repeat the character.
    """
    print(border * size)

def sailingShip(border):
    """
    Displays the sailing ship ASCII art with a border.
    :param border: The character to use for the border.
    """
    # Escaping backslashes as required [cite: 84]
    ship = [
        "    |    |    |          ",
        "     )_)  )_)  )_)       ",
        "    )___))___))___)\\\\   ",
        "   )____)____)_____)\\\\\\\\ ",
        " _____|____|____|____\\\\\\\\\\\\",
        " \\    Satisfaction   /   ",
        "^^^^^^^^^^^^^^^^^^^^^^^^ "
    ]
    
    width = 30
    printHeaderFooter(border, width + 2)
    for line in ship:
        print(f"{border}{line.ljust(width)}{border}")
    printHeaderFooter(border, width + 2)

def sleepingCat(border):
    """
    Displays the sleeping cat ASCII art with a border.
    :param border: The character to use for the border.
    """
    cat = [
        "|\\      _,,,---,,_      ",
        "ZZZzz /,`.-'`'    -.    ",
        ";-;;,_                  ",
        "     |,4-  ) )-,_. ,\\ ( `'-'",
        "    '---''(_/--'  `-'\\_) "
    ]
    
    width = 30
    printHeaderFooter(border, width + 2)
    for line in cat:
        print(f"{border}{line.ljust(width)}{border}")
    printHeaderFooter(border, width + 2)

def lonePine(border):
    """
    Additional Art 1: A simple pine tree.
    :param border: The character to use for the border.
    """
    tree = [
        "      ^       ",
        "     / \\      ",
        "    /   \\     ",
        "   /_____\\    ",
        "     | |      "
    ]
    width = 20
    printHeaderFooter(border, width + 2)
    for line in tree:
        print(f"{border}{line.ljust(width)}{border}")
    printHeaderFooter(border, width + 2)

def tinyGhost(border):
    """
    Additional Art 2: A small ghost.
    :param border: The character to use for the border.
    """
    ghost = [
        "  .-.  ",
        " (o o) ",
        " | O | ",
        " |   | ",
        " '---' "
    ]
    width = 15
    printHeaderFooter(border, width + 2)
    for line in ghost:
        print(f"{border}{line.ljust(width)}{border}")
    printHeaderFooter(border, width + 2)

def blank(border):
    """
    Displays a blank canvas of 5x5 spaces with a border.
    :param border: The character to use for the border.
    """
    width = 5
    printHeaderFooter(border, width + 2)
    for _ in range(5):
        print(f"{border}{' ' * width}{border}")
    printHeaderFooter(border, width + 2)