# -*- coding: utf-8 -*-
"""
Problem 0021 Project Euler
Amicable numbers

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.


Ray Cassani

"""

import numpy as np
import itertools

def find_first_factor(number):
    factor_seed = 2
    for ix in range(factor_seed, number + 1):
        if (number % ix) == 0 :
            break
    factor = number // ix
    return ix, factor

def find_prime_factors(number):
    prime_factors = np.array([])    
    while True:
        prime_factor, number = find_first_factor(number)
        prime_factors = np.append(prime_factors, prime_factor)
        if number == 1:
            break
    #factor_tmp_list = list(prime_factors)
    return prime_factors


def find_all_factors(number):
    # find all factors    
    all_factors = np.array([])    
    all_factors = np.append(all_factors, 1)
    prime_factors = find_prime_factors(number)
    all_factors = np.append(all_factors, prime_factors)    
    n_prime_factors = len(prime_factors)      
    
    for len_group in range(2, n_prime_factors):
        new_factors = np.prod(np.array(list(itertools.combinations(prime_factors , len_group))) , axis=1)
        all_factors = np.append(all_factors, new_factors)
    
    factors = np.unique(all_factors)
    factors = np.sort(factors)    
    return factors

def function_d(number):
    # sum of proper divisors of number (numbers less than n which divide evenly into n)
    factors = find_all_factors(number)
    # if number is prime, it only has two divisors 1 and number, as number is not < number, we remove it    
    if len(factors) == 2: 
        factors = np.delete(factors, -1)
    return sum(factors)


amicable_a = np.array([])
amicable_b = np.array([])

for i_num in range(4,10001):
    a = i_num
    b = int(function_d(a))
    if b!= 1:        
        if function_d(b) == a and b != a:
            amicable_a = np.append(amicable_a, a)
            amicable_b = np.append(amicable_b, b)
        
print(amicable_a)
print(amicable_b)

result = sum(amicable_a)
print(result)