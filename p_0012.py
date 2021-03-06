# -*- coding: utf-8 -*-
"""
Problem 0012 Project Euler
Highly divisible triangular number


The sequence of triangle numbers is generated by adding the natural numbers. 
So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

     1: 1
     3: 1,3
     6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.
What is the value of the first triangle number to have over five hundred divisors?

Ray Cassani

"""

import numpy as np
import itertools

def find_prime_factors(number, primes):
    prime_factors = np.array([])    
    while True:
        prime_factor, number = find_first_factor(number, primes)
        prime_factors = np.append(prime_factors, prime_factor)
        if number == 1:
            break
    #factor_tmp_list = list(prime_factors)
    return prime_factors

def find_first_factor(number, primes):
    for ix in primes :
        if (number % ix) == 0 :
            break
    new_number = number // ix
    first_prime_factor = ix
    return first_prime_factor, new_number

num_now = 1
triang = 1
primes = np.array([])

while True:
    # Check in the new number is prime    
    num_new = num_now + 1    
    if np.all(num_new % primes != 0):
        primes = np.append(primes, num_new)
    

    # Compute triangular
    triang = triang + num_new
    print(triang)
    
    # Find the prime factors for the triangular number 
    prime_factors = find_prime_factors(triang, primes)
    #print(prime_factors)    
    n_prime_factors = len(prime_factors)    
    
    # find all factors    
    all_factors = np.array([])    
    all_factors = np.append(all_factors, 1)
    all_factors = np.append(all_factors, prime_factors)    
    
    for len_group in range(2, n_prime_factors):
        new_factors = np.prod(np.array(list(itertools.combinations(prime_factors , len_group))) , axis=1)
        all_factors = np.append(all_factors, new_factors)
    
    factors = np.unique(all_factors)
    factors = np.sort(factors)
    factors = np.append(factors, triang)
    n_factors = len(factors)    
        
    print(factors)
    #print(n_factors)
    
    num_now = num_new        
    if n_factors > 500:
        break
    
print (triang)
