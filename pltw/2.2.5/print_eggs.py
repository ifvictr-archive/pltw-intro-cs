def print_eggs(numbers_of_dozens):
    """
    numbers_of_dozens is a list of numeric values
    Prints the number of eggs in each number of dozens.
    Also prints "There are 12 eggs per dozen."

    Returns a str stating the number of values in numbers_of_dozens.
    """ 
    for number in numbers_of_dozens:
        print str(number) + " dozen contains " + str(number * 12) + " eggs."
    print "There are 12 eggs per dozen."
    return "That\"s " + str(len(numbers_of_dozens)) + " groups of dozens."