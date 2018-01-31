# Prints a right triangle of numbers, with longest row on top
for row in range(10):
    # Print spaces
    for _ in range(row):
        print(" ", end=" ")
    for col in range(10 - row):
        print(col, end=" ")
    print()