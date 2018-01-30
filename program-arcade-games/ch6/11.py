# Prints a centered triangle with longest row on bottom
for i in range(1, 10):
    # Space needed to center numbers
    for j in range(10 - i):
        print(" ", end = " ")
    # Upwards-sloping side of triangle
    for j in range(1, i + 1):
        print(j, end = " ")
    # Downwards-sloping side of triangle
    for j in range(i - 1, 0, -1):
        print(j, end = " ")
    print()