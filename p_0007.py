# -*- coding: utf-8 -*-
"""
Problem 0000 Project Euler
10001st prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?

Ray Cassani

"""

import numpy as np

primes = np.array([2], ndmin=1) 
n_prime = 10001


while primes.shape[0] < n_prime:
    tmp = primes[-1] # last prime
    while True:
        found = np.alltrue(tmp % primes != 0) # not (is tmp divisible over any prime already found?)
        if found:
            primes = np.append(primes, tmp) # if it is not divisible then is prime
            break
        else: # if it is divisible, then try new candidate
            tmp = tmp + 1

print(primes[n_prime - 1]) # print the 10001 prime 