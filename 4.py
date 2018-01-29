# coding: utf-8

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(n):
    return str(n) == str(n)[::-1]

palindromes = []
for i in range(100, 1000):
    for j in range(100, 1000):
        ij = i * j
        if is_palindrome(ij):
            palindromes.append(ij)

print palindromes
print max(palindromes)
