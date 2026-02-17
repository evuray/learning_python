"""Lasagna recipe helper functions."""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the remaining baking time.

    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time remaining (in minutes) baking.

    This function takes an integer representing the
    time already spent baking and calculates the remaining minutes to bake lasagna.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :return: int - total time elapsed (in minutes) preparing.

    This function takes an integer representing the number of lasagna layers
    and calculates the total minutes spent preparing the lasagna.
    """
    return PREPARATION_TIME * number_of_layers

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.

    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna.
    """
    total_prep_time = preparation_time_in_minutes(number_of_layers)
    return total_prep_time + elapsed_bake_time