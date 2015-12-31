# -*- coding: utf-8 -*-
"""
Problem 0016 Project Euler
Power digit sum

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000?


Ray Cassani

"""

import numpy as np

pow1000 = 2 ** 1000
str_pow = str(pow1000)
nums = np.array(list( map(int, list(str_pow) ) ) )
result = sum(nums)
print(result)
