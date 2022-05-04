# What't the differences?
def func1(fn):
    def inner():
        return fn(2)
    return inner   # a = func1(add)()

def func2(fn):
    def inner():
        return fn(2)
    return inner()

func1(lambda x: x * x)  # <function inner at ...>
func2(lambda x: x * x)  # 4

def make_mod(n):
    """Returns a function that takes an argument x.
    That function will return x modulo n.

    >>> mod_7 = make_mod(7)
    >>> mod_7(3)
    3
    >>> mod_7(41)
    6
    """
    "*** YOUR CODE HERE ***"
    def mod(x):
        return x % n
    return mod


lambda f, g: lambda x: f(g(x))