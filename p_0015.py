# -*- coding: utf-8 -*-
"""
Problem 0015 Project Euler
Lattice paths



Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

RRDD, RDRD, RDDR, DRRD, DRDR and DDRR

How many such routes are there through a 20×20 grid?

Ray Cassani

"""
#This poblem can be solved analytically.

#1. Using only R and D movements, the only was to get from the top-left corner to the bottom-right corner in a 
# 20x20 grid, is to have 20 times R and 20 tomes D
#2. The number of paths is equal to the number of different combinations of 20R and 20D
#3. All Rs as equal, and all Ds are equal, for that reason the number of paths is not computed as 4P4 (24)
#4. There are 40 elements, which can be ordered as 40P40 (8.159x10^47) ways
# The number of lattice paths from (0,0) to (a,b) counts the number of combinations 
# of 'a' objects out of a set of 'a + b' objects. 4C2 = nCk where n = a + b; and k = a
# nCk = n! / (n-k)!
# as n-k = k
# nCk = n! / k!


from scipy.special import factorial

a = 20
b = 20

n = a + b
k = a

num_paths = factorial(n) / (factorial(k) * factorial(n-k) )
print(int(num_paths))

