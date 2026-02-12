# Author: Perfect-Princess Makuwerere
# Date: 02/11/2026
# Description:Converts a user specified number in the range of 1-9, inclusively, into the equivalent Roman numeral

import random

first_number = random.randint(1,10)
second_number = random.randint(11,20)

sum = 0

for i in range(first_number,second_number + 1):
    if i % 2 != 0:
        sum += i
print(f"The first random number was {first_number}, the second random number was {second_number}, and the sum is {sum}")        