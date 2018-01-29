# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

from math import sqrt
import sys


def get_largest_prime_factor(n):
    primes = [2, 3] + range(5, int(sqrt(n)) + 1, 2)
    i = 0
    largest = 1
    while True:
        if n == 1:
            return prime
        prime = primes[i]
        if i == len(primes):
            return n
        if n % prime == 0:
            print prime, n
            n = n / prime
        else:
            i += 1

print get_largest_prime_factor(int(sys.argv[1]))
