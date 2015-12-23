# -*- coding: utf-8 -*-
"""
Problem 0014 Project Euler
Longest Collatz sequence


The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3*n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?
NOTE: Once the chain starts the terms are allowed to go above one million.

Ray Cassani

"""

import numpy as np
import matplotlib.pyplot as plt

limit = 1000000

numbers = np.arange(2, limit)
n_steps = np.zeros(numbers.shape)
 
for ix in range(0, numbers.shape[0]):
    step = 2
    x = numbers[ix]
    while True:
        if x % 2 == 0:
            x = x / 2
        else:
            x = 3*x + 1
        if x == 1:
            n_steps[ix] = step
            break
        else:
            step = step + 1

iy = np.argmax(n_steps)
result = numbers[iy]
print(result)            
        
        


