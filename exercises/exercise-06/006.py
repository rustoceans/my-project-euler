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


def _squares(number):
    square_number = number ** 2
    return square_number


def get_sum(extension):
    sum_of = reduce(lambda a, b: a + b, extension)
    return sum_of


def find_difference(squares_hundred, sum_squares):
    find_difference = squares_hundred - sum_squares
    return find_difference


def main(limit):
    hundred = range(1, limit + 1)
    squares_each = map(lambda x: x ** 2, hundred)
    sum_squares = get_sum(squares_each)
    sum_hundred = get_sum(hundred)
    squares_hundred = _squares(sum_hundred)
    return find_difference(squares_hundred, sum_squares)

if __name__ == "__main__":
    print main(100)
