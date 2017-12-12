def points(word):
    """
    `word` is a string
    The function calculates the points for a word based on
    a = 1 point, b = 2 points, ..., z = 26 points

    Returns an int for the total points
    """
    points = 0
    for letter in word:
        value = ord(letter) - 96
        points += value
        print value
    return points