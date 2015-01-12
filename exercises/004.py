"""
Project Euler Problem 4
=======================

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def palindrome(limit):
    results = []
    for n in range(limit):
        for on in range(limit):
            results.append(str(n * on))
    last_number = lambda x=results: max([int(n) for n in x if n == n[::-1]])
    return last_number()

print palindrome(1000)
