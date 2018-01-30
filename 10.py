# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

import math
import sys

def erathostenes_crib(n):
    numbers = range(2, n)
    candidates = [2] + [x for x in range(2, int(math.sqrt(n)) + 1) if x % 2]

    for candidate in candidates:
        numbers = [number for number in numbers if number % candidate > 0 or number == candidate]
    return numbers



s = erathostenes_crib(int(sys.argv[1]))
print sum(s)
