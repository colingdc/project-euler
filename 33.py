# coding: utf-8

# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify
# it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.


from fractions import gcd


fractions = []

for a in range(11, 99):
    for b in range(a + 1, 100):
        if a % 10 and b % 10:
            if int(str(a)[1]) == int(str(b)[0]):
                new_a = int(str(a)[0])
                new_b = int(str(b)[1])
                if a * new_b == b * new_a:
                    fractions.append([a, b])


numerator =  reduce(lambda x, y: x * y, [x[0] for x in fractions], 1)
denominator =  reduce(lambda x, y: x * y, [x[1] for x in fractions], 1)

print denominator / gcd(numerator, denominator)
