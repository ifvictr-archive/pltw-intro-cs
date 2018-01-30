# Print top section of diamond
for i in range(1, 10):
    # Space needed to center numbers
    for j in range(10 - i):
        print(" ", end = " ")
    # Upwards-sloping side
    for j in range(1, i + 1):
        print(j, end = " ")
    # Downwards-sloping side
    for j in range(i - 1, 0, -1):
        print(j, end = " ")
    print()

# Print bottom section of diamond
for i in range(8, 0, -1):
    # Space needed to center numbers
    for j in range(10 - i):
        print(" ", end = " ")
    # Downwards-sloping side
    for j in range(1, i + 1):
        print(j, end = " ")
    # Upwards-sloping side
    for j in range(i - 1, 0, -1):
        print(j, end = " ")
    print()