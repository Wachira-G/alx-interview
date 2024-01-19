#!/usr/bin/python3

"""In a text file, there is a single character H.
Your text editor can execute only two operations in this file:
Copy All and Paste.
Given a number n, write a method that calculates
the fewest number of operations needed to result
in exactly n H characters in the file.

Prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0
Example:

n = 9

H => Copy All => Paste => HH => Paste =>HHH =>
zCopy All => Paste => HHHHHH => Paste => HHHHHHHHH

Number of operations: 6"""

from typing import List


def minOperations(n: int) -> int:
    """Calculate fewest number of operations
    needed to result in exactly n H characters in a file."""
    if n <= 0:
        return 0
    if isPrime(n):
        return n
    prime_factors = getPrimeFactors(n)
    return sum(prime_factors)


def isPrime(n: int) -> bool:
    """Check if an integer is a prime number."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def getPrimeFactors(n: int) -> List[int]:
    """Calculates the prime factors of a number n."""
    factors = []
    divisor = 2
    while divisor <= n:
        if n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        else:
            divisor += 1

    return factors


def getFactors(n: int) -> List[int]:
    """Calculates all the factors of a number n."""
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors
