#!/usr/bin/python3
"""
minoperations module
"""


def minOperations(n):
    """calculates the fewest number of operations"""
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += 1
            n //= factor

        factor += 1

    return operations
