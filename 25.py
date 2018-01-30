# coding: utf-8

# The Fibonacci sequence is defined by the recurrence relation:

# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:

# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
# The 12th term, F12, is the first term to contain three digits.

# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

import sys

class Fibonacci(object):

    def __init__(self):
        self.cache = dict()

    def get(self, n):
        if n == 0 or n == 1:
            return 1
        if n in self.cache:
            return self.cache[n]
        result = self.get(n - 2) + self.get(n - 1)
        self.cache[n] = result
        return result

f = Fibonacci()
NUMBER_DIGITS = int(sys.argv[1])

print f.get(3)
print f.get(7)

n = 1
while True:
    fn = f.get(n)
    if fn > 10**(NUMBER_DIGITS - 1):
        print n + 1
        break
    n += 1
