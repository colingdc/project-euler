# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import sys

def gcd(a, b):
    if a < b:
        return gcd(b, a)
    while b > 0:
        a, b = b, a % b
    return a

def ppcm(n):
    result = 1
    for i in range(1, n + 1):
        g = gcd(result, i)
        result = result * i / g
    return result

print ppcm(int(sys.argv[1]))
