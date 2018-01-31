# Prints a grid of numbers with each column being multiplied by the column it is on
for row in range(1, 10):
    for col in range(1, 10):
        # Don't place spaces if the number is the first in its column
        if col * row < 10 and col != 1:
            print(" ", end="")
        print(col * row, end=" ")
    print()