def min3(x, y, z):
    if x >= y:
        if y >= z:
            return z
        else:
            return y
    else:
        if x >= z:
            return z
        else:
            return x

# Test cases
print(min3(0, 1, 2) == 0)
print(min3(1, 2, 0) == 0)
print(min3(2, 0, 1) == 0)
print(min3(2, 1, 0) == 0)
print(min3(1, 0, 2) == 0)
print(min3(0, 2, 1) == 0)
print(min3("a", "b", "c") == "a")