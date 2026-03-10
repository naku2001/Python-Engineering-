#Author: Perfect Makuwerere
#Date: March 4, 2026
#Description: Reads integers from numbers.txt and calculates their average.

def main():
    total = 0
    count = 0
    
    
    file = open("numbers.txt", "r")
    
    for line in file:
       
        clean_line = line.strip()
        print(clean_line)
        
        
        total += int(clean_line)
        count += 1
        
    
    file.close()
    
    
    if count > 0:
        average = total / count
        print(f"The average of the numbers is {average}")

if __name__ == "__main__":
    main()