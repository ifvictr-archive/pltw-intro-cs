def longest_word(words):
    """
    words is a list of strings

    Returns the longest word
    """
    most_letters = 0
    record_holder = ""
    for word in words:
        if len(word) > most_letters:
            most_letters = len(word)
            record_holder = word
    return record_holder