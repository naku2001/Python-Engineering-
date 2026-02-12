# Author: Perfect-Princess Makuwerere
# Date: 02/11/2026
# Description:A guessing game where the program tracks remaining attempts and provides directional hints

import random

chances = 3
x= 5
y= 7

print("The particle is somewhere in this space! You have 3 chances to guess it.")

    
while chances > 0:
       
        guess_x = int(input("What do you think its x coordinate is (1-10)? "))
        guess_y = int(input("What do you think its y coordinate is (1-10)? "))

        
        if guess_x == x and guess_y == y:
            print(f"Good guess! ({x},{y}) was the position!") 
            break
        
        elif guess_x < 1 or guess_x > 10 or guess_y < 1 or guess_y > 10:
            print(f"No good! ({guess_x},{guess_y}) is outside of the range!") 
        else:
            
            if guess_x > x:
                print("Bad luck! The particle's x position is less than your x position!") 
            elif guess_x < x:
                print("Bad luck! The particle's x position is greater than your x position!") 
            
            if guess_y > y:
                print("The particle's y position is less than your y position!") 
            elif guess_y < y:
                print("The particle's y position is greater than your y position!")

        chances -= 1 
        
        if chances > 0:
            print(f"The particle is somewhere in this space! You have {chances} chances to guess it.") 
        else:
            
            print(f"Oh no! You ran out of chances. ({x},{y}) was the particle's position!") 

