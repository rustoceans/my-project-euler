"""
Project Euler Problem 3
=======================

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

def factoring(n):
    if n <= 300000: rangen = n//2+1 
    else: rangen = n//100000
    divisors = [ d for d in range(2,rangen) if n % d == 0 ]
    return [i for i in divisors if \
            all(i % other_divisor != 0 for other_divisor in divisors if\
            other_divisor != i)][-1] 
    
print factoring(600851475143)
