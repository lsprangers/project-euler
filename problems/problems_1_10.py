from problems import functions as mf
import numpy as np

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

# 5

# 6

# 7

# 8

# 9

# 10
