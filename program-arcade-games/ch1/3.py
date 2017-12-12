import math

PI = math.pi

def circle_area(radius):
    return PI * (radius ** 2)

def ellipse_area(axis_a, axis_b):
    return PI * axis_a * axis_b

def equilateral_triangle_area(length):
    return (math.sqrt(3) / 4) * (length ** 2)

def cone_volume(radius, height):
    return (PI * (radius ** 2) * height) / 3

def sphere_volume(radius):
    return (4 * PI * (radius ** 3)) / 3

def days_to_seconds(days):
    return days * (60 * 60 * 24)