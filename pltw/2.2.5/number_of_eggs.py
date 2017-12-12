def number_of_eggs(dozens):
    """
    dozens is a list of numeric values

    Returns the total number of eggs for the dozens in the list.
    """
    eggs = 0
    for number in dozens:
        eggs += number * 12
    return eggs