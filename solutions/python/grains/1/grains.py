"""Functions in calculating grains based on squares."""

def square(number):
    """Return number of grains in a specific square.

    :param number: int - what number of square?
    :return: int - amount of grains
    """
    if not 1 <= number <= 64:
        raise ValueError("square must be between 1 and 64") 
    return 2 ** (number - 1)

def total():
    """Return sum of grains in all squares.

    :return: int - total number of grains based on square number
    """
    return (2 ** 64) - 1
        
