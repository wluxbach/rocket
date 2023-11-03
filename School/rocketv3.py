"""
Will Luxbacher, 11/3/2023
rocket v3.py
This program with make a rocket through functions of ASCII art
"""

# Variables:

# Divider between different sections of the rocket
divider = "+" + "=*" * 6 + "+"


# Functions:


# Pointed section of rocket (bottom and top)
def cone():
    print("     /**\\")
    print("    //**\\\\")
    print("   ///**\\\\\\")
    print("  ////**\\\\\\\\")
    print(" /////**\\\\\\\\\\")


# Triangular pattern wider at the bottom
def top():
    print("|../\\..../\\..|")
    print("|./\\/\\../\\/\\.|")
    print("|/\\/\\/\\/\\/\\/\\|")


# Triangular pattern wider at the top
def bottom():
    print("|\\/\\/\\/\\/\\/\\/|")
    print("|.\\/\\/..\\/\\/.|")
    print("|..\\/....\\/..|")


# Code for program:


cone()
print(divider)
top()
bottom()
print(divider)
bottom()
top()
print(divider)
cone()
