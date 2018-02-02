n = int(input("How big do you want the box? "))

if n < 0:
    print("Input must be a positive number!")

# Top part of square
for row in range(1, n * 2, 2):
    # Left side of rectangle
    for col in range(row, n * 2, 2):
        print(col, end=" ")
    # Add spaces between sides
    for _ in range(row - 1):
        print("  ", end="")
    # Right side of rectangle
    for col in range(n * 2 - 1, row - 1, -2):
        print(col, end=" ")
    print()

# Bottom part of square
for row in range(n * 2 - 1, 0, -2):
    # Left side of rectangle
    for col in range(n * 2 - 1, row - 1, -2):
        print(col, end=" ")
    # Add spaces between sides
    for _ in range(row - 1):
        print("  ", end="")
    # Right side of rectangle
    for col in range(row, n * 2, 2):
        print(col, end=" ")    
    print()