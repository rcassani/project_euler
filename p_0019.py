# -*- coding: utf-8 -*-
"""
Problem 0019 Project Euler
Maximum path sum I

Counting Sundays

You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?


Ray Cassani

"""
'''
Notes:
2000 was leap year
1800, 1900, 2100, 2200, 2300, 2500 are not
'''


import numpy as np

day30 = np.arange(1,31)
day31 = np.arange(1,32)
day28 = np.arange(1,29)
day29 = np.arange(1,30)

years = np.arange(1901 , 2001)
# initial value is the days for 1900, which was NOT leap year 
years_num = np.concatenate((day31, day28, day31, day30, day31, day30, day31, day31, day30, day31, day30, day31), axis=0)

for i_years in years:
    # Find leap years
    if i_years % 4 == 0:
        # Create arrays for normal year and leap year
        year_numbers = np.concatenate((day31, day29, day31, day30, day31, day30, day31, day31, day30, day31, day30, day31), axis=0)
    else:        
        year_numbers = np.concatenate((day31, day28, day31, day30, day31, day30, day31, day31, day30, day31, day30, day31), axis=0)
    # Concatenamte arrays
    years_num = np.append(years_num, year_numbers)

n_weeks = (len(years_num) // 7 ) + 1

# Create array that repeats 1 to 7 same size
days_week = np.arange(1,8)
days_weeks = np.tile(days_week, n_weeks)
days_weeks2 = days_weeks[0:len(years_num)]

# Remove the firs 365 days that correspond to 1900
days_weeks_final = days_weeks2[365::]
years_num_final = years_num[365::]

# Find places where array1 = 1 and array2 = 7
c = np.logical_and(days_weeks_final[:] == 7,  years_num_final[:] == 1)
count = sum(c)

