def print_num(num, align):
    print(("{:" + align + str(n_len) + "d}").format(num), end=" ")

def print_spaces():
    print((" " * n_len), end=" ")

n = int(input("How big do you want the box? "))

if n < 0:
    print("Input must be a positive number!")

n_len = len(str(n * 2 - 1))

# Top part of square
for row in range(1, n * 2, 2):
    # Left side of rectangle
    for col in range(row, n * 2, 2):
        print_num(col, "<")
    # Add spaces between sides
    for _ in range(row - 1):
        print((" " * n_len), end=" ")
    # Right side of rectangle
    for col in range(n * 2 - 1, row - 1, -2):
        print_num(col, ">")
    print()

# Bottom part of square
for row in range(n * 2 - 1, 0, -2):
    # Left side of rectangle
    for col in range(row, n * 2, 2):
        print_num(col, "<")
    # Add spaces between sides
    for _ in range(row - 1):
        print((" " * n_len), end=" ")
    # Right side of rectangle
    for col in range(n * 2 - 1, row - 1, -2):
        print_num(col, ">")
    print()