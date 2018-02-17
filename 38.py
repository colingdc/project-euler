# coding: utf-8

# Take the number 192 and multiply it by each of 1, 2, and 3:

# 192 × 1 = 192
# 192 × 2 = 384
# 192 × 3 = 576
# By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

def get_concatenation(a):
    i = 1
    numbers = []
    while len(numbers) < 9:
        product = a * i
        numbers += list(str(product))
        i += 1
    return numbers, i

def is_concatenation_pandigital(concatenation):
    if "0" in concatenation:
        return False
    return len(concatenation) == 9 and len(set(concatenation)) == 9

pandigital_concatenations = []

for a in range(1, 10000):
    concatenation, i = get_concatenation(a)
    if is_concatenation_pandigital(concatenation):
        print a, concatenation, i
        pandigital_concatenations.append(concatenation)

numbers = [int("".join(c)) for c in pandigital_concatenations]

print max(numbers)
