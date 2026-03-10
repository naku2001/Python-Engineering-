#Author: Perfect Makuwerere
#Date: March 4, 2026
#Description: Helper functions for ASCII art conversion.

import os

def getFileName():
    """
    Prompts user for a filename and validates existence.
    :return: Validated filename
    :rtype: str
    """
    filename = input("Please input file you wish to have painted: ")
    while not os.path.exists(filename):
        print(f"{filename} does not exist!")
        filename = input("Please input file you wish to have painted: ")
    return filename

def convertLine(line):
    """
    Converts a string of numbers into ASCII symbols.
    :param line: Comma separated string of numbers
    :type line: str
    :return: Converted symbol string
    """
    line = line.strip()
    new_line = ""
    parts = line.split(",")
    
    for val in parts:
        if val == "1": new_line += " "
        elif val == "2": new_line += ","
        elif val == "3": new_line += "_"
        elif val == "4": new_line += "("
        elif val == "5": new_line += "O"
        elif val == "6": new_line += ")"
        elif val == "7": new_line += "-"
        elif val == "8": new_line += '"'
    return new_line

def processFile(filename):
    """
    Reads input file and writes converted art to painting.txt.
    :param filename: Name of input file
    """
    input_f = open(filename, "r")
    output_f = open("painting.txt", "w")
    
    for line in input_f:
        converted = convertLine(line)
        output_f.write(converted + "\n")
        
    input_f.close()
    output_f.close()