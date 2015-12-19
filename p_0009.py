# -*- coding: utf-8 -*-
"""
Problem 0000 Project Euler
Special Pythagorean triplet

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

Ray Cassani

"""

# There is formula Euclid formular to generate Pythagorean triples
# a^2 + b^2 = c^2 with a < b < c and a,b,c belongs to positive integers
#
# a = m^2 - n^2
# b = 2 * m * n
# c = m^2 + n^2
#
# with m > n and m,n belong to positive integers
#
# we need that a + b + c = 1000 and a < b < c
#
# then m^2 - n^2 + 2*m*n + m^2 + n^2 = 1000
#
# m^2 + m*n = 500      EQ(!)
# where m > n, then m^2 > m*n then m^2 > 250 but m ^ 2 < 500
# therefore 16 < m < 22
# we evaluate for this range the EQ(1)

import numpy as np

m_array = np.arange(16,23)
m_mod = (500 % m_array) == 0

m_t = m_array[m_mod != 0]
m = m_t[0]
n = (500 - m**2) // m

a = m**2 - n**2
b = 2 * m * n
c = m**2 + n**2

print(a + b + c)
print(a**2 + b**2, c**2)

print(a * b * c)
