"""
Will Luxbacher 11/6/2023
rocketv4-scalable.py
This program will make a rocket that can be scaled via an input variable
"""

# Variables:

number = int(input("How big do you want your rocket? \n"))
if number % 2 != 0:
    oddeven = 1
if number % 2 == 0:
    oddeven = 2
# if number % 2 == 0:
#  number = number + 1
# print("Sorry, that number was even, I made it odd for you")


# Functions:
def cone():
    for i in range(0, number + 1, 1):
        print(
            (" " * (number - i)) + ("/" * (i + oddeven)) + "**" + ("\\" * (i + oddeven))
        )


def top():
    for i in range(0, number + oddeven, 2):
        print(
            "|"
            + ("." * int((number - i) / 2))
            + ("/\\" * int(((i) + 2) / 2))
            + ("." * int((number - i) / 2))
            + ("." * int((number - i) / 2))
            + ("/\\" * int(((i) + 2) / 2))
            + ("." * int((number - i) / 2))
            + "|"
        )


def bottom():
    for i in range(0, number + oddeven, 2):
        print(
            "|"
            + ("." * int(i / 2))
            + ("\\/" * int(((number - i) + 2) / 2))
            + ("." * int(i / 2))
            + ("." * int(i / 2))
            + ("\\/" * int(((number - i) + 2) / 2))
            + ("." * int(i / 2))
            + "|"
        )


def divider():
    print(("+" + "=*" * (number + oddeven) + "+"))


# Actual code:
cone()
divider()
top()
bottom()
divider()
bottom()
top()
divider()
cone()
