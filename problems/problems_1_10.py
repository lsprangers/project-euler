from problems import functions as mf
import numpy as np
from functools import reduce

# 1
# Find the sum of all the multiples of 3 or 5 below 1000.
ls_1 = []
for i in range(1000):
    if (i % 3 == 0) or (i % 5 == 0):
        ls_1.append(i)
np.sum(ls_1)

# 2
# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.

ls_2 = mf.fibonacci(4_000_000)
np.sum([i for i in ls_2 if i % 2 == 0])

# 3
# What is the largest prime factor of the number 600851475143 ?
np.max(mf.prime_factors(600_851_475_143))

# 4
# Find the largest palindrome made from the product of two 3-digit numbers.
max_p = 0
for i in range(999):
    for j in range(999):
        n = i * j
        bool_pal = mf.is_palindrome(n)
        if bool_pal and n > max_p:
            max_p = n

# 5
# What is the smallest positive number that is evenly divisible by
# all of the numbers from 1 to 20?
#   Exploit LCM(x0,x1,x2) = LCM(x0,LCM(x1,x2))
reduce(mf.lcm, range(2, 21))

# 6
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
first_hundred = list(range(1, 101))
sum_first_hundred = np.sum(first_hundred)
abs(
    np.sum([i * i for i in first_hundred]) -
    (sum_first_hundred * sum_first_hundred)
)

# 7
mf.get_nth_prime(10001)

# 8
# Find the thirteen adjacent digits (sliding window left right not up down)
# in the 1000-digit number that have the greatest product. What is the value of this product?
with open('./problems/helper_files/thousand_digit_number.txt', 'r') as f:
    num_str = f.read()

slider_len = 13
max_num = 0
for i in range(0, len(num_str) - slider_len):
    num_sub = num_str[i:i + slider_len]
    nums = [int(j) for j in num_sub]
    this_prod = np.prod(nums)
    max_num = this_prod if this_prod > max_num else max_num

# 9
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
triples = mf.naive_pythagorean_triplets(1001)
for t in triples:
    if np.sum(t) == 1000:
        print(np.product(t))

# 10
# Find the sum of all the primes below two million.
p_gen = mf.p_sieve()
prime_list = []
while True:
    next_prime = next(p_gen)
    if next_prime > 2_000_000:
        break
    prime_list.append(next_prime)
np.sum(prime_list)
