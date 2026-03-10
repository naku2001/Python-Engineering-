#Author: Perfect Makuwerere
#Date: March 4, 2026
#Description: Main file for the Print By Numbers program.

import pbnFunctions

def main():
    fname = pbnFunctions.getFileName()
    pbnFunctions.processFile(fname)
    print("Your image can be found in painting.txt. Enjoy!")

if __name__ == "__main__":
    main()