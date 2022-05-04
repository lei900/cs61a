"""The Luhn Algorithm
1. From the rightmost digit, which is the check digit, 
   moving left, double the value of every second digit;
   if product of this doubling operation is greater than 9,
   then sum the digits of the products (e.g. 10: 1 + 0 = 1)

2. Take the sum of all the digits.

The Luhn sum of a valid credit card number is a multiple of 10.

"""
def split(n):
    return n // 10, n % 10

def sum_digits(n):
	if n < 10:
		return n
	else:
		all_but_last, last = split(n)
		return sum_digits(all_but_last) + last

def luhn_sum(n):
    if n < 0:
        return n
    else:
        all_but_last, last = split(n)
        return luhn_sum_double(all_but_last) + last

def luhn_sum_double(n):
    all_but_last, last = split(n)
    luhn_digit = sum_digits(2 * last)
    if n < 10:
        return luhn_digit
    else:
        return luhn_sum(all_but_last) + luhn_digit

luhn_sum(5210120063353404)