# coding: utf-8

# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once;
# for example, the 5-digit number, 15234, is 1 through 5 pandigital.
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

def is_pandigital(a, b):
    p = a * b
    digits = list(str(a)) + list(str(b)) + list(str(p))
    return len(digits) == 9 and set(digits) == set(list("123456789"))

def has_distincts_digits(a):
    chars = list(str(a))
    return len(set(chars)) == len(chars)

products = []

# Works, not very efficient tho
for a in range(1, 1000):
    if has_distincts_digits(a):
        print a
        for b in range(a, 10000):
            if has_distincts_digits(str(a) + str(b)):
                p = a * b
                if is_pandigital(a, b):
                    products.append(p)

print sum(set(products))
