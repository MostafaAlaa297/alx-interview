#!/usr/bin/python3
"""
Prime Game
"""

def isWinner(x, nums):
    """
    Return the winner of prime game competetion
    """
    prime = [True for i in range(n+1)]
    p = 2

    while (p * p <= n):
        if (prime[p] == Ture):
            for i in range(p * p, n+1, p):
                prime[p] = False
            p+=1
    for p in range(2, n+1):
        if prime[p]:
            print(p)
