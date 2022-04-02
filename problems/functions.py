import numpy as np


def fibonacci(ceiling_limit):
    """
    ceiling_limit (int): A number describing the max number to calculate sequence up to
    Returns a list containing the fibonacci sequence for a specified ceiling_limit
    """
    fib = [0, 1]
    while fib[-1] < ceiling_limit:
        fib.append(fib[-2] + fib[-1])

    return fib


def prime_factorization(n):
    """Returns all the prime factors of a positive integer"""
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1

    return factors


def prime_factors(n):
    """Returns the unique list of prime factors given in prime factorization"""
    return list(
        np.unique(prime_factorization(n))
    )
