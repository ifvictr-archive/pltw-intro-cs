def add_tax(amount, tax_rate):
    """
    Calculates amount with tax included
    Accepts numeric values for amount, tax_rate
    Returns int or float
    """
    return amount * (1 + tax_rate)