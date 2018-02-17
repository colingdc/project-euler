# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

from math import factorial

def is_factorial_sum(n):
    digits = [int(x) for x in str(n)]
    s = sum(factorial(x) for x in digits)
    return n == s

for p in range(1, 10):
    print p, 10 ** (p - 1), p * factorial(9)
# For a number with more than 7 digits, 10^p-1 > p*9!

numbers = []

for n in range(10, 1000000):
    if n % 100000 == 0:
        print n
    if is_factorial_sum(n):
        numbers.append(n)

print sum(numbers)
