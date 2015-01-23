"""
Project Euler Problem 1
=======================

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

lista = lambda x: sum([l for l in range(1, x) if l % 3 == 0 or l % 5 == 0])
print lista(1000)

"""
Usage
=====

For you to use, it's very simple. Just pass lista(number)
and the function will return your result.

"""
