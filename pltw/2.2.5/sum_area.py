def sum_area(room_widths):
    """
    room_widths is a list of numeric values
    The shape of each room is square
    
    Returns the total area of the rooms.
    """
    total_area = 0
    for width in room_widths:
        total_area = total_area + width ** 2
    return total_area