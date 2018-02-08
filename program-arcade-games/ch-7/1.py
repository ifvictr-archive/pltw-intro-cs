MONTHS = "JanFebMarAprMayJunJulAugSepOctNovDec"
n = int(input("Enter a month number: "))

if n < 1 or n > 12:
    print("Month `n` is not a valid month!")
else:
    # Month names are three characters long each.
    # Subtracted one so that the search would start at the beginning of `MONTHS`.
    start_pos = (n - 1) * 3
    print(MONTHS[start_pos:start_pos + 3])