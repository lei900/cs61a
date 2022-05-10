def prune(d, keys):
    """Return a copy of D which only contains key/value pairs
    whose keys are also in KEYS.
    >>> prune({"a": 1, "b": 2, "c": 3, "d": 4}, ["a", "b", "c"])
    {'a': 1, 'b': 2, 'c': 3}
    """
    return {k: d[k] for k in keys}

def index(keys, values, match):
    """Return a dictionary from keys k to a list of values v for which 
    match(k, v) is a true value.
    
    >>> index([7, 9, 11], range(30, 50), lambda k, v: v % k == 0)
    {7: [35, 42, 49], 9: [36, 45], 11: [33, 44]}
    """
    return {k: [v for v in values if match(k, v)] for k in keys}

index([7, 9, 11], range(30, 50), lambda k, v: v % k == 0)

def sum_nums(nums):
    """Returns the sum of the numbers in NUMS.
    >>> sum_nums([6, 24, 1984])
    2014
    >>> sum_nums([-32, 0, 32])
    0
    """
    if nums == []:
        return 0
    else:
        return nums[0] + sum_nums(nums[1:])

def reverse(s):
    """Returns a string with the letters of S
    in the inverse order.
    >>> reverse('ward')
    'draw'
    """
    if len(s) == 1:
        return s 
    else:
        return reverse(s[1:]) + s[0]

def reverse_digits(n):
    """Returns N with the digits reversed.
    >>> reverse_digits(123)
    321
    >>> reverse_digits(45725)
    52754
    """
    if n // 10 == 0:
        return n 
    else:
        return (n % 10) * (10 ** (num_digits(n)-1)) + reverse_digits(n // 10)

def num_digits(x):
    x_count = 1
    while x >= 10:
        x_count += 1
        x //= 10
    return x_count

# Alternative solution
def reverse(n, r):
    if n==0:
        return r
    else:
        return reverse(n // 10, r * 10 + n % 10)

# Read number
number = int(input("Enter number: "))

# Function call
reversed_number = reverse(number, 0)

# Display output
print("Reverse of %d is %d" %(number, reversed_number))