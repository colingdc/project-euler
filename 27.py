# Euler discovered the remarkable quadratic formula:
#
# n2+n+41
# It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39.
# However, when n=40,402+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41
# is clearly divisible by 41.
#
# The incredible formula n2−79n+1601 was discovered, which produces 80 primes for the consecutive values 0≤n≤79.
# The product of the coefficients, −79 and 1601, is −126479.
#
# Considering quadratics of the form:
#
# n2+an+b, where |a|<1000 and |b|≤1000
#
# where |n| is the modulus/absolute value of n
# e.g. |11|=11 and |−4|=4
# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number
# of primes for consecutive values of n, starting with n=0.

from math import sqrt


def is_prime(n):
    if n < 2:
        return False
    candidates = [2] + list(range(3, int(sqrt(n)) + 1, 2))
    for x in candidates:
        if n % x == 0:
            return False
    return True


def generated_primes(a, b):
    n = 0
    count = 0
    while is_prime(n ** 2 + a * n + b):
        count += 1
        n += 1
    return count


max_number = 0
max_a, max_b = None, None

for a in range(-999, 1000):
    for b in range(-1000, 1001):
        number = generated_primes(a, b)
        if number > max_number:
            print(number, a, b)
            max_number = number
            max_a, max_b = a, b

print(max_a, max_b, max_a * max_b, max_number)
