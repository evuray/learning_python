def steps(number):
    """Calculates POSITIVE INTEGERS number's amount of steps to get to 1"""
    if number < 1:
        raise ValueError("Only positive integers are allowed")
    num_steps = 0
    while number > 1:
        is_even = number % 2
        if not bool(is_even):
            number = number / 2
        if bool(is_even):
            number = (number * 3) + 1
        num_steps += 1
    return num_steps
            
    
