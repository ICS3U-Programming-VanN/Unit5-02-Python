#!/usr/bin/env python3

# Created by: Van Nguyen
# Created on: November 23, 2022
# This program asks the user for the base and the height
# of a triangle and then calculates and displays the area


# This function calculates and displays the area of a triangle
def calc_area(height, base):
    """
    Calculates and displays the area (of a triangle) to the user

    :param height: Height measurement of the Triangle
    :param base: Base measurement of the Triangle
    """

    # Calculates the area
    area = round((base * height) / 2, 2)

    # Displays the area of the triangle to the user
    print(f"The area of the triangle: {area}cm^2")


def main():
    # Checks for exceptions
    try:
        # Asks user for the height of the triangle
        user_height = float(
            input("Enter the height measurement of the triangle (cm): ")
        )

        # Asks user for the base of the triangle
        user_base = float(input("Enter the base measurement of the triangle (cm): "))

    # In the event of an exception
    except Exception:
        print("You must enter a non-negative number!")

    # In the event of valid input
    else:

        # If the height or base of the triangle is negative
        if user_height < 0 or user_base < 0:
            print("You must enter a base and a height that is not negative.")

        # If the user's inputs are valid
        else:
            # Calls to calculate and display the area
            calc_area(user_base, user_height)


if __name__ == "__main__":
    main()
