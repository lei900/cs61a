def remove_odd_indices(lst, odd):
    """ 
    Remove elements of lst that have odd indices.
    >>> s = [1, 2, 3, 4]
    >>> t = remove_odd_indices(s, True)
    >>> s
    [1, 2, 3, 4]
    >>> t
    [1, 3]
    >>> l = [5, 6, 7, 8]
    >>> m = remove_odd_indices(l, False)
    >>> m
    [6, 8]
    """
    "*** YOUR CODE HERE ***"
    # if odd:
    #     return [x for x in lst if lst.index(x) % 2 == 0]
    # else:
    #     return [x for x in lst if lst.index(x) % 2 != 0]

    # solution
    if not lst:
        return lst
    if odd:
        return [lst[0]] + remove_odd_indices(lst[1:], not odd)
    else:
        return remove_odd_indices(lst[1:], not odd)