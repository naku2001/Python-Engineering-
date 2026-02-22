# Author: Perfect Makuwerere
# Date: 02/18/2026
# Description: Calculates the base and side surface area of a square pyramid.

import math

# function definitions
def calcBaseArea(side):
    return side ** 2

# add your function definition for calcSideArea here
def calcSideArea(side, height):
    """
    Calculates the total surface area of the four triangular sides.
    :param side: The length of the base side
    :type side: float
    :param height: The height of the pyramid
    :type height: float
    :return: Total area of the four sides
    """
    # Formula: 2 * a * sqrt((a^2 / 4) + h^2)
    return 2 * side * math.sqrt((side ** 2 / 4) + height ** 2)

# add your function definition for prntSurfArea here
def prntSurfArea(base_area, side_area):
    """
    Prints the total surface area of the pyramid.
    :param base_area: Area of the base
    :type base_area: float
    :param side_area: Total area of the sides
    :type side_area: float
    """
    total = base_area + side_area
    print(f"The total surface area of the square pyramid is {total} square feet.")

def main():
    side = float(input("Enter the side length of the base of the square pyramid in feet: "))

    height = float(input("Enter the height of the square pyramid in feet: "))

    base_area = calcBaseArea(side)
    print(f"Base surface area of the square pyramid is {base_area} square feet.")

    #the result to side_area, then print the result
    side_area = calcSideArea(side, height)
    print(f"Total surface area of all four sides of the square pyramid is {side_area} square feet.")

    # add your function call to print the total surface area
    prntSurfArea(base_area,side_area)


if __name__ == "__main__":
    main()