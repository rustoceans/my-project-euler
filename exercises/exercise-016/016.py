#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: 016.py
Author: Alexsander Falcucci
Email: alex.falcucci@gmail.com
Github: https://github.com/alexfalcucc
Description: Resolution of 16º euler exercise
"""


def calc_potency(numbers):
    """TODO: Return the multiplication at all numbers inside that list.
    """
    return reduce(lambda x, y: x * y, numbers)


def main(*args):
    """
    Project Euler Problem 16
    ========================

    2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

    What is the sum of the digits of the number 2^1000?
    """
    coeff = args[0]
    range_base = [2] * coeff
    mult_product = calc_potency(range_base)
    return reduce(lambda x, y: int(x) + int(y), [n for n in str(mult_product)])


if __name__ == "__main__":
    print main(1000)
