"""
Project Euler Problem 6
=======================

The sum of the squares of the first ten natural numbers is,
                       1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
                    (1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten
natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one
hundred natural numbers and the square of the sum.
"""


def find_difference(limit):
    hundred = range(1, limit + 1)
    squares_each = map(lambda x: x ** 2, hundred)
    sum_squares = reduce(lambda x, y: x + y, squares_each)

    sum_hundred = reduce(lambda a, b: a + b, hundred)
    squares_hundred = sum_hundred ** 2

    find_difference = squares_hundred - sum_squares
    return find_difference

print find_difference(100)
