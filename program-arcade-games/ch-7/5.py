# Encrypted version of "This is a string"
encrypted_text = "Uijt!jt!b!tusjoh"
plain_text = ""

for char in encrypted_text:
    x = ord(char)
    x -= 1
    plain_text += chr(x)

print(plain_text)