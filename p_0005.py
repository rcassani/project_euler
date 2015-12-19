# -*- coding: utf-8 -*-
"""
Problem 0005 Project Euler
Smallest multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

Ray Cassani

"""
import numpy as np
from collections import Counter as mset

def find_first_factor(number):
    factor_seed = 2
    for ix in range(factor_seed, number + 1):
        if (number % ix) == 0 :
            break
    factor = number // ix
    return ix, factor
    
def new_elements(a, b):
    union = mset(a) + mset(b)
    inter = mset(a) & mset(b)
    new = union - inter
    c = list(new.elements())
    return c
    
ini = 1
fin = 20
    
elements = np.arange(ini + 1, fin + 1)
factors_list = [1]

for ie in elements:
    prime_factors = np.array([])   
    while True:
        factor, ie = find_first_factor(ie)
        prime_factors = np.append(prime_factors, factor)
        if ie == 1:
            print(prime_factors)            
            break
    factor_tmp_list = list(prime_factors)
    
    # keep all but the intersection
    factors_list = new_elements(factors_list, factor_tmp_list)
    
# Least common multiple
tmp = np.array(factors_list)
LCM = np.prod(tmp)
print(LCM)
