# -*- coding: utf-8 -*-
"""
Problem 0004 Project Euler
Largest palindrome product

A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

Ray Cassani

"""
import numpy as np

# determine the maximum product for two n-digit numbers
n_digit = 3
num_max = int('9' * n_digit)
num_min = int('1' + '0' * (n_digit - 1))

numbers = np.arange(num_max, num_min, -1)
pal = np.array([0,0,0], ndmin=2)
# find the products and verify if ther are palindromes

for ix in numbers:
    for iy in numbers:
        prod = ix * iy
        str_num = str(prod)
        len_str = len(str_num)
        simetry = np.array([])
        for ic in range(0, len_str//2):
            simetry = np.append(simetry, str_num[ic] == str_num[len_str - 1 - ic] )
        if np.alltrue(simetry):
            pal = np.vstack((pal,[ix, iy, prod]))
            print(ix)
        
ind = np.argmax(pal[:,2])
print(pal[ind,:])
    
    