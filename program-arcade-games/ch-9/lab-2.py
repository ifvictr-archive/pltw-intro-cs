def box(height, width):
    for _ in range(height):
        for _ in range(width):
            print("*", end="")
        print()

# Test cases
box(7, 5)
print()
box(3, 2)
print()
box(3, 10)