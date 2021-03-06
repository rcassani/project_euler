# -*- coding: utf-8 -*-
"""
Problem 0002 Project Euler
Even Fibonacci numbers

Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
find the sum of the even-valued terms.

Ray Cassani

"""

import numpy as np

# create Fibonacci sequence up to 4 000 000
fibo_limit = 4000000
x = np.array([])
x = np.append(x,1)
x = np.append(x,2)
ix = 0

while x[-1] < fibo_limit:
    x = np.append(x, x[ix] + x[ix+1])
    ix = ix +1

x = np.delete(x,-1)

# find even elements
numeven = x[x % 2 == 0]

# summatory of these numbers
result = sum(numeven)
print(result)
