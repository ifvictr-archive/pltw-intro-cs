# Prints a right triangle of numbers, with longest row on bottom
for row in range(10):
    for col in range(row + 1):
        print(col, end=" ")
    print()