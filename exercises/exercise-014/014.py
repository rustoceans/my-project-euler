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

    def get_chain(self, num):
        chain = []
        chain.append(num)
        while chain[-1] > 1:
            if self.is_even(chain[-1]):
                n_chain = chain[-1]/2
                chain.append(n_chain)
            else:
                n_chain = (3*chain[-1]) + 1
                chain.append(n_chain)
        return chain

    @staticmethod
    def get_chains_ordered(chains):
        return sorted(chains, key=lambda num: len(chains[num]), reverse=True)

    @staticmethod
    def is_even(num):
        """
        Just return a boolean value if the number is or isn't even.
        """
        return True if num % 2 == 0 else False

    @staticmethod
    def numbers(range_):
        """
        Generate a sequence of numbers
        """
        i = range_
        while i <= range_ and i > 1:
            yield i
            i -= 1

    def get_chains(self):
        chains = {}
        for n in self.numbers(self.number):
            chains[n] = self.get_chain(n)
            longest_key = self.get_chains_ordered(chains)[0]
            for key in chains.keys():
                if key != longest_key:
                    del chains[key]
        return longest_key


def main(n):
    return Chain(n).get_chains()


if __name__ == '__main__':
    print main(1000000)
