def is_ascending(n):
    """Returns True if the digits of N are in ascending order.

    >>> is_ascending(321)
    True
    >>> is_ascending(123)
    False
    >>> is_ascending(4432221)
    True
    >>> is_ascending(5492)
    False
    >>> is_ascending(5420)
    True
    """
    # while n // 10:
    #     rightmost = n % 10
    #     n = n // 10
    #     if rightmost > n % 10:
    #         return False
    # return True

    largest = 0
    while n > 0:
        ones = n % 10
        if ones < largest:
            return False
        largest = ones
        n = n // 10
    return True

def count_one(n):
    """Counts the number of 1s in the digits of n

    >>> count_one(7007)
    0
    >>> count_one(123)
    1
    >>> count_one(161)
    2
    >>> count_one(1)
    1
    """
    count = 0
    while n > 0:
        if n % 10 == 1:
            count += 1
        n //= 10
    return count

def total_ones(n):
    """Returns number of 1s in the digits of all numbers from 1 to
    n.

    >>> total_ones(10) # 1, 10 -> two 1s
    2
    >>> total_ones(15) # 1, 10, 11, 12, 13, 14, 15 -> eight 1s
    8
    >>> total_ones(21)
    13
    """
    i, total = 1, 0
    while i <= n:
        total += count_one(i)
        i += 1
    return total