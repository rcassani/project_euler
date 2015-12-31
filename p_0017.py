# -*- coding: utf-8 -*-
"""
Problem 0017 Project Euler
Number letter counts

If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
how many letters would be used?

NOTE: Do not count spaces or hyphens. 
For example, 342 (three hundred and forty-two) contains 23 letters and 115 
(one hundred and fifteen) contains 20 letters. 

The use of "and" when writing out numbers is in compliance with British usage.


Ray Cassani

"""


'''
Notes

Separation between hundreds and tens
Hundreds and tens are usually separated by 'and' (in American English 'and' is not necessary).
110 - one hundred and ten
1,250 - one thousand, two hundred and fifty
2,001 - two thousand and one 

Numbers up to 19 are unique

20 - 99 follow the rule tens-unit 
ninety-nine
twenty-one
fourty

101 - 999 follow
hundreds and tens-units

one hundred and twenty-one (121)
'''


import numpy as np

# Create dictionary for numbers 1 - 19
# Create dictionary for thens 20, 30, ... 90

b20 = {'1': 'one', '2':'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven',
       '8': 'eight', '9': 'nine','10': 'ten','11': 'eleven','12': 'twelve','13': 'thirteen','14': 'fourteen','15': 'fifteen',
       '16': 'sixteen', '17': 'seventeen','18': 'eighteen','19':'nineteen'};
       
decs = {'20': 'twenty', '30': 'thirty', '40': 'forty', '50': 'fifty', '60': 'sixty', '70': 'seventy',
        '80': 'eighty', '90': 'ninety'};


# I'm going to run the algorithm for 1 - 999
ini = 1
fin = 1001

num_names = []
num_name_size = np.array([])
num_ints = np.arange(ini, fin)

for ix in num_ints:
    ix_str = str(ix)
    ix_name= ''

    if ix == 1000:
        ix_name = 'one thousand'
    else:
        
        # Compute the hundreds        
        n_hundreds = ix // 100
        # Compute rest bu hundreds (0 - 99)
        ix99 = ix - (n_hundreds * 100)    
        # If the number is larger than 100
        if n_hundreds > 0:
            ix_name = b20[str(n_hundreds)] + ' hundred'           
            # if the number is larger than 100 and has tens and units different to zero        
            if ix99 != 0:
                ix_name = ix_name + ' and '
    
        # if the number has tens and units different to zero        
        if ix99 != 0:    
            # If the number is less than 20, direct name
            if ix99 < 20:
                ix_name = ix_name + b20[str(ix99)]
            # Else, generate its name tens-units
            else:
                n_tens = ix99 // 10
                ix_name = ix_name + decs[str(n_tens*10)]
        
                # if units are different from 0?
                ix9 = ix99 - (n_tens * 10)    
                if ix9 != 0:
                    ix_name = ix_name + '-' + b20[str(ix9)]
    
    num_names.append(ix_name)    
    # remove spaces and hyphens        
    fixed_name =  ix_name.replace("-",'').replace(' ','')      
    # count characters
    num_name_size = np.append(num_name_size, len(fixed_name))
    # print name
    print(str(ix) + ' ' + ix_name + ' ' + str(len(fixed_name)) )

    
result = sum(num_name_size)
print(result)
        
      







