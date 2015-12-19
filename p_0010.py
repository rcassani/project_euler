# -*- coding: utf-8 -*-
"""
Problem 0000 Project Euler
Summation of primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.

Ray Cassani

"""
import numpy as np

primes = np.array([2,3], ndmin=1) 
prime_limit = 10


while primes[-1] < prime_limit:
    tmp = primes[-1] # last prime
    while True:
        found = np.alltrue(tmp % primes != 0) # not (is tmp divisible over any prime already found?)
        if found:
            primes = np.append(primes, tmp) # if it is not divisible then is prime
            print(tmp)
            break
        else: # if it is divisible, then try new candidate
            tmp = tmp + 2

primes = np.delete(primes, -1)
prime_int64 = primes.astype(np.int64)
b = sum(prime_int64)
print(b) # print summatory of primes 

