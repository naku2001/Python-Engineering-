# Author:Perfect Makuwerere
# Date: 2026-02-18
# Description: A program that allows users to choose ASCII art with a custom border.

import sys

def intro():
    """
    Welcomes the user, lists options, and collects choice and border character.
    :return: A tuple of (int choice, str border) 
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
    Outputs the border character size number of times[cite: 94].
    :param border: The character to print.
    :param size: The length of the line.
    """
    print(border * size)

def sailingShip(border):
    """
    Stores and prints the ship art with a border [cite: 100-104].
    :param border: The character for the frame.
    """
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
    Stores and prints the cat art with a border 
    :param border: The character for the frame.
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
    :param border: The character for the frame.
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
    :param border: The character for the frame.
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
    Prints a blank 5x5 canvas if an invalid choice is made .
    :param border: The character for the frame.
    """
    width = 5
    printHeaderFooter(border, width + 2) 
    for _ in range(5):
        print(f"{border}{' ' * width}{border}")
    printHeaderFooter(border, width + 2) 

def main():
    """
    Main function to coordinate program execution
    """
    
    try:
        choice, border = intro()
    except ValueError:
       
        print("Invalid input.")
        sys.exit(-1)
    
     
    if choice == 1:
        sailingShip(border)
    elif choice == 2:
        sleepingCat(border)
    elif choice == 3:
        lonePine(border)
    elif choice == 4:
        tinyGhost(border)
    else:
        
        blank(border)
        print("Hmmmm....we don't seem to have that painting.") 
        sys.exit(-1) 
        
    print("We hope you enjoy your art!") 

if __name__ == "__main__":
    main() 