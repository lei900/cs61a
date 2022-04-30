from numpy import kaiser


def count_until_larger(num):
    """
    Complete the function count_until_larger that takes in a positive integer num.
    count_until_larger examines the rightmost digit and counts digits from right to
    left until it encounters a digit larger than the rightmost digit, then returns that count.

    >>> count_until_larger(117) # .Case 1
    -1
    >>> count_until_larger(8117) # .Case 2
    3
    >>> count_until_larger(9118117) # .Case 3
    3
    >>> count_until_larger(8777)  # .Case 4
    3
    >>> count_until_larger(22) # .Case 5
    -1
    >>> count_until_larger(0) # .Case 6
    -1
    """
    "*** YOUR CODE HERE ***"
    # rightmost = num % 10
    # count = 1
    # num = num // 10  
    # while num > 0:
    #     next = num % 10
    #     if next > rightmost:
    #         return count
    #     count += 1
    #     num = num // 10  # repeating myself!
    # return -1


    rightmost = num % 10
    count = 0
    while num:
        if num % 10 > rightmost:
            return count
        num = num // 10
        count = count + 1
    return -1