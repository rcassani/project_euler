# -*- coding: utf-8 -*-
"""
Problem 0006 Project Euler
Sum square difference

The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural 
numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred 
natural numbers and the square of the sum.

Ray Cassani

"""

import numpy as np

ini = 1
fin = 100

x = np.arange(ini, fin + 1)

sum_squares = sum (x ** 2)
square_sum = np.sum(x) ** 2

diff = square_sum - sum_squares
print(diff)
    