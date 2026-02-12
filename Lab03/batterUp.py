# Author: Perfect-Princess Makuwerere
# Date: 02/11/2026
# Description:This script simulates a baseball hit by generating a random integer and determining the outcome based on distance.


import random



distance = random.randint(0,450)

if distance > 400:
    print(f"The ball was hit {distance} feet. The batter hit a home run and scored a run for the team!")
elif 135 <= distance <= 400:
    print(f"The ball was hit {distance} feet. The batter hit the ball into the outfield and made it to third base.")
elif 10 <= distance <= 134:
    print(f"The ball was hit {distance} feet. The batter hit the ball into the infield and made it to second base.")
elif 1 <= distance <= 9:
    print(f"The ball was hit {distance} feet. The batter bunted the ball and made it to first base.")
else: 
    print("The batter made a strike.")
  