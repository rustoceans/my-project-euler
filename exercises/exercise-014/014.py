"""
Project Euler Problem 14
========================

The following iterative sequence is defined for the set of positive
integers:

n->n/2 (n is even)
n->3n+1 (n is odd)

Using the rule above and starting with 13, we generate the following
sequence:
                  13->40->20->10->5->16->8->4->2->1

It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms. Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""


class Chain(object):
    """
    Calculates the longest chain started by one million
    """
    def __init__(self, number):
        self.number = number

    @staticmethod
    def even(num):
        """
        Just return a boolean value if the number is or isn't even.
        """
        return True if num % 2 == 0 else False


def main(n):
    return Chain.even(n)


if __name__ == '__main__':
    print main(4)
