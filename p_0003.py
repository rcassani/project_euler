# -*- coding: utf-8 -*-
"""
Problem 0003 Project Euler
Largest prime factor


The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?

Ray Cassani

"""
import numpy as np


def find_first_factor(number):
    factor_seed = 2
    for ix in range(factor_seed, number + 1):
        if (number % ix) == 0 :
            break
    factor = number // ix
    return ix, factor


# number
number = 600851475143
#number = 13195

number_tmp = number
factors = np.array([])
 
while True:
    ix, number_tmp = find_first_factor(number_tmp)
    factors = np.append(factors, ix)
    if number_tmp == 1:
        break

print (factors)

        