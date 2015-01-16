"""
Project Euler Problem 5
=======================

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers
from 1 to 20?
"""

import sys


def minimal_divisor(limit):
    default = sys.maxint
    for n in xrange(limit, default, limit):
        if all([n % i == 0 for i in xrange(11, limit + 1)]):
            result = n
            break
    return result

print minimal_divisor(20)

"""
The time was 18,71s.
"""
