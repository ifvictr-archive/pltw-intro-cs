plain_text = "This is a string"
encrypted_text = ""

for char in plain_text:
    x = ord(char)
    x += 1
    encrypted_text += chr(x)

print(encrypted_text)