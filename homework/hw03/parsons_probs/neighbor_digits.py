def neighbor_digits(num, prev_digit=-1):
    """
    Returns the number of digits in num that have the same digit to its right
    or left.
    >>> neighbor_digits(111)
    3
    >>> neighbor_digits(123)
    0
    >>> neighbor_digits(112)
    2
    >>> neighbor_digits(1122)
    4
    """
    "*** YOUR CODE HERE ***"
    if num < 10:
        return num == prev_digit # False,0; True,1
    last = num % 10
    rest = num // 10
    return int(prev_digit == last or rest % 10 == last) + \
            + neighbor_digits(num // 10, last)