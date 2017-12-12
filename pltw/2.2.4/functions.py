import random

def square(x):
    return x ** 2

def absolute_value(x):
    if x >= 0:
        print "x is positive. absolute value is " + str(x)
    else:
        print "x is negative. absolute value is " + str(x * -1)

def rectangle_area(width, height):
    """
    Calculate the area of a rectangle
    width, height are numeric
    returns int or float
    """
    return width * height

def five(x):
    return 5

def roll_die(x):
    """
    Return a random integer from 1 to x, inclusive
    """
    return random.randint(1, x)

def cube(x):
    return x ** 3