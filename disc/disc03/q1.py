def multiply(m, n):
    """ Takes two positive integers and returns their product using recursion.
    >>> multiply(5, 3)
    15
    """
    "*** YOUR CODE HERE ***"
    if n == 1:
        return m
    else:
        return m + multiply(m, n-1)

def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    "*** YOUR CODE HERE ***"
    # step = 0
    # while n > 1:
    #     print(n)
    #     if n % 2 == 0:
    #         n = n / 2
    #     else:
    #         n = n * 3 + 1
    #     step += 1
    # print(n)
    # return step

    print(n)
    if n == 1:
        return 1
    elif n % 2 ==0:
        return hailstone(n // 2) + 1
    else:
        return hailstone(n * 3 + 1) + 1

def merge(n1, n2):
    """ Merges two numbers by digit in decreasing order
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31) 
    3211
    """
    "*** YOUR CODE HERE ***"
    if n2 == 0:
        return n1
    elif n1 == 0:
        return n2
    elif n1 % 10 < n2 % 10:
        return merge(n1 // 10, n2) * 10 + n1 % 10
    else:
        return merge(n1, n2 // 10) * 10 + n2 % 10

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    # i = 2
    # while i < n:
    #     if n % i == 0:
    #         return False
    #     i += 1
    # return True
    def helper(i):
        if i == n:
            return True
        elif n % i == 0:
            return False
        else:
            return helper(i + 1)
    return helper(2)