def digit_pos_match(n, k):
    """
    >>> digit_pos_match(980, 0) # .Case 1
    True
    >>> digit_pos_match(980, 2) # .Case 2
    False
    >>> digit_pos_match(98276, 2) # .Case 3
    True
    >>> digit_pos_match(98276, 3) # .Case 4
    False
    """
    "*** YOUR CODE HERE ***"
    n = n // (10 ** k)
    kth_digit = n % 10
    if kth_digit == k:
        return True
    else:
        return False

print(digit_pos_match(93376, 2))