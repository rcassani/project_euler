# -*- coding: utf-8 -*-
"""
Problem 0020 Project Euler
Factorial digit sum

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

Ray Cassani

"""

from scipy.special import factorial
import numpy as np

number = 100
fact_result = factorial(number, exact=True)
print(fact_result)
str_fact = str(fact_result)

nums = np.array(list( map(int, list(str_fact) ) ) )
result = sum(nums)
print(result)