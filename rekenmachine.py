#!/usr/bin/env python
"""
info about project
"""

# imports


__author__ = "Fre Van Buynder"
__email__ = "fre.vanbuynder@student.kdg.be"
__status__ = "Development"


# global vars
number1 = 0
number2 = 0


# functions
def main():
    operation = int(input("1) add\n2) substract\n3) mulitply\n4) divide\n\nWhat do you want to do?: "))

    global number1
    global number2

    try:
        number1 = int(input("Gimme the first round number: "))
    except ValueError as err:
        print("this is not a good value:", err)

    try:
        number2 = int(input("Gimme the second round number: "))
    except ValueError as err:
        print("this is not a good value:", err)

    if operation == 1:
        result = add(number1, number2)
    elif operation == 2:
        result = substract(number1, number2)
    elif operation == 3:
        result = multiply(number1, number2)
    elif operation == 4:
        result = divide(number1, number2)
    else:
        print("This is not a legit operation")

    print("The result is: ", result)


def add(number1, number2):
    return number1 + number2


def substract(number1, number2):
    return number1 - number2


def multiply(number1, number2):
    return number1 * number2


def divide(number1, number2):
    return number1 / number2


if __name__ == '__main__':
    main()
