def to_inches(heights):
    """
    heights is a list of numeric values in feet

    Returns a list of the measurements in inches.
    """
    new_heights = []
    for height in heights:
        new_heights.append(height * 12)
    return new_heights