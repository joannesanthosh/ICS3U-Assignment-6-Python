#!/usr/bin/env python3

# Created by: Joanne Santhosh
# Created on: Dec 2022
# This program calculates the perimeter of a square using functions


import math


def calculate_square_perimeter(side: int) -> float:
    # Calculates a square perimeter

    if side < 0:
        return -1
    else:
        perimeter = 4 * side
        return perimeter


def main():
    # Gets input and calculate perimeter of square
    try:
        side_as_int = input("Enter side of a square (cm): ")
        side = float(side_as_int)
        square_perimeter = calculate_square_perimeter(side)
        print("\nThis square's perimeter is {} cm".format(square_perimeter))
    except ValueError:
        print("\nInvalid Input.")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
