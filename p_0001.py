# -*- coding: utf-8 -*-
"""
Problem 0001 Project Euler
Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

Ray Cassani

"""

import numpy as np

# integers below 1000 (1, 2, 3, ..., 998, 999)
x = np.arange(999) + 1

# find indices for multiples of 5
div5 = x % 5
ix5 = div5 == 0

# find indices for multiples of 3
div3 = x % 3
ix3 = div3 == 0

# find indices for multiples of 5 or 3
ixt = np.logical_or(ix3,ix5)

# find elements that are multiples of 5 or 3
num3or5 = x[ixt]

# summatory of these number
result = sum(num3or5)
print(result)
