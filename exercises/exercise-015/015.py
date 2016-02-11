#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: 015.py
Author: Alexsander Falcucci
Email: alex.falcucci@gmail.com
Github: https://github.com/alexfalcucc
Description: Resolution of 15º euler exercise
"""


def get_routes(*args):
    """
    Project Euler Problem 15
    ========================

    Starting in the top left corner of a 2 * 2 grid, there are 6 routes
    (without backtracking) to the bottom right corner.

    How many routes are there through a 20 * 20 grid?

    There is a good article with the better explanation of it bellow:

    Article link:
        http://betterexplained.com/articles/navigate-a-grid-using-combinations-and-permutations/
    link with the formula: http://joaoff.com/2008/01/20/a-square-grid-path-problem/
    """
    top = args[0]
    left = args[1]
    forty_factorial = reduce(lambda x, y: x * y, range(1, 41))
    list_ = range(1, 21)
    twenty__factorial = reduce(lambda x, y: x * y, list_)
    print forty_factorial/(twenty__factorial * twenty__factorial)
    return True


if __name__ == "__main__":
    get_routes(20, 20)


