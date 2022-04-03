import numpy as np
import itertools


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


def reverse_number(n):
    """Reverse a number"""
    rev = 0
    while n > 0:
        remainder = n % 10
        rev = (rev * 10) + remainder
        n = n // 10
    return rev


def is_palindrome(n):
    """Check if a numer is a palindrome"""
    rev = reverse_number(n)
    return 1 if n == rev else 0


def gcd(a, b):
    """Greatest common denominator"""
    return gcd(b, a % b) if b else a


# Exploit lcm(a, b) * gcd(a, b) = a * b

def lcm(a, b):
    """Least common multiple"""
    return (a * b) / gcd(a, b)


def p_sieve():
    """
        Proposed sieve prime number generator from
        https://stackoverflow.com/questions/2211990/how-to-implement-an-efficient-infinite-generator-of-prime-numbers-in-python/10733621#10733621
    """
    yield from [2, 3, 5, 7]
    D = {}
    ps = p_sieve()
    next(ps)
    p = next(ps)
    assert p == 3
    psq = p * p
    for i in itertools.count(9, 2):
        if i in D:  # composite
            step = D.pop(i)
        elif i < psq:  # prime
            yield i
            continue
        else:  # composite, = p*p
            assert i == psq
            step = 2 * p
            p = next(ps)
            psq = p * p
        i += step
        while i in D:
            i += step
        D[i] = step


def get_nth_prime(n):
    idx = 0
    prime_gen = p_sieve()
    while idx < n:
        pr_num = next(prime_gen)
        idx += 1
    return pr_num


def naive_pythagorean_triplets(ceiling_limit):
    c, m = 0, 2
    pairs_list = []

    # Limiting c would limit
    # all a, b and c
    while c < ceiling_limit:

        # Now loop on n from 1 to m-1
        for n in range(1, m):
            a = m * m - n * n
            b = 2 * m * n
            c = m * m + n * n

            # if c is greater than
            # limit then break it
            if c > ceiling_limit:
                break

            pairs_list.append((a, b, c))

        m += 1

    return pairs_list

