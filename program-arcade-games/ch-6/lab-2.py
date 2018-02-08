def print_horizontal(size):
    """
    Prints the top and bottom sides of the box.
    """
    # Length will always be greater than height
    for _ in range(size * 2):
        print("o", end="")
    print()

def print_vertical(size):
    """
    Prints the left and right sides of the box.
    """
    # Exclude the top and bottom sides
    for y in range(size - 2):
        # Left "o"
        print("o", end="")
        # Printing space inside the box, and excludes the two vertical sides
        for _ in range((size * 2) - 2):
            print(" ", end="")
        # Right "o"
        print("o", end="")
        print()

size = int(input("Enter the desired box size: "))
print_horizontal(size)
print_vertical(size)
print_horizontal(size)