#!/usr/bin/python3
"""
Prime Game
"""


def isWinner(x, nums):
    """
    Return the winner of prime game competetion
    """
    n = len(nums)
    prime = [True for i in range(n+1)]
    p = 2
    curr_player = 'Maria'
    maria_rounds = 0
    ben_rounds = 0

    while (p * p <= n):
        if (prime[p] is True):
            for i in range(p * p, n+1, p):
                prime[p] = False
                if curr_player == 'Maria':
                    curr_player = 'Ben'
                else:
                    curr_player = 'Maira'

            if curr_player == 'Maria':
                ben_rounds += 1
            else:
                maria_rounds += 1
                p += 1
    if maria_rounds > ben_rounds:
        return 'Maria'
    return 'Ben'
