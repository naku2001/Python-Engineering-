# Author: Perfect Makuwerere
# Date: February 18, 2026
# Description: Main entry point for the modular painting program.

import painterFuncs as pf
import sys

def main():
    
    choice, border = pf.intro()
    
    
    if choice == 1:
        pf.sailingShip(border)
    elif choice == 2:
        pf.sleepingCat(border)
    elif choice == 3:
        pf.lonePine(border)
    elif choice == 4:
        pf.tinyGhost(border)
    else:
    
        pf.blank(border)
        print("Hmmmm....we don't seem to have that painting.")
        sys.exit(-1)
        
    print("We hope you enjoy your art!")

if __name__ == "__main__":
    main()