#Author: Perfect Makuwerere
#Date: March 4, 2026
#Description: Reads a poem from a file and writes a summary to Output.txt.

import os

def main():
    poem_title = ""
    poem_author = ""
    poem_lines = []
    
    
    filename = input("Please input the name of the poem you wish summarized: ")
    while not os.path.exists(filename):
        print(f"{filename} does not exist!")
        filename = input("Please input the name of the poem you wish summarized: ")
    
    
    with open(filename, "r") as file:
        poem_title = file.readline().strip()
        poem_author = file.readline().strip()
        for line in file:
            poem_lines.append(line.strip())
            
    
    with open("Output.txt", "w") as out_file:
        out_file.write(f"The name of the poem is {poem_title}\n")
        out_file.write(f"The author of the poem is {poem_author}\n")
        out_file.write(f"The number of lines in the poem is {len(poem_lines)}\n")
        out_file.write("A preview of the poem is:\n")
       
        for i in range(min(3, len(poem_lines))):
            out_file.write(f"{poem_lines[i]}\n")

if __name__ == "__main__":
    main()