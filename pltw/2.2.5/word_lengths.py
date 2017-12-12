def word_lengths(words):
    lens = []
    for word in words:
        word = word.strip(".,?!")
        lens.append(len(word))
    return lens