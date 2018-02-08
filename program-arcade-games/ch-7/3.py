plain_text = "This is a string"

for char in plain_text:
    x = ord(char)
    x += 1
    print(chr(x), end="")