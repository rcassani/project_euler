# -*- coding: utf-8 -*-
"""
Problem 0018 Project Euler
Maximum path sum I

By starting at the top of the triangle below and moving to adjacent numbers on the row below, 
the maximum total from top to bottom is 23.

   3
  7 4
 2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.
Ray: A is Down Left, B is Down Right. Therefore the path was ABB

Find the maximum total from top to bottom of the triangle below:


75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. 
However, Problem 67, is the same challenge with a triangle containing one-hundred rows; 
it cannot be solved by brute force, and requires a clever method! ;o)

Ray Cassani

"""
import numpy as np

# Load triangle
# It's a 15-level triangle, and the number of level is equal to the number of 
# elements in the level




num_str = (
'75 '
'95 64 '
'17 47 82 '
'18 35 87 10 '
'20 04 82 47 65 '
'19 01 23 75 03 34 '
'88 02 77 73 07 63 67 '
'99 65 04 28 06 16 70 92 '
'41 41 26 56 83 40 80 70 33 '
'41 48 72 33 47 32 37 16 94 29 '
'53 71 44 65 25 43 91 52 97 51 14 '
'70 11 33 28 77 73 17 78 39 68 17 57 '
'91 71 52 38 17 14 91 43 58 50 27 29 48 '
'63 66 04 68 89 53 67 30 73 16 69 87 40 31 '
'04 62 98 27 23 09 70 98 73 93 38 53 60 04 23');
n_levels = 15

''' These is the triagle for test
num_str = (
'3 '
'7 4 '
'2 4 6 '
'8 5 9 3');
n_levels = 4
'''

split_str = num_str.split(' ')
flat = np.array(list (map( float, split_str)))
triang = np.empty((n_levels,n_levels))
triang[:] = np.NAN
triang_sum = triang

ini_ix = 0

for i_level in range(0, n_levels):
    fin_ix = ini_ix + i_level + 1
    new_elem = flat[ini_ix : fin_ix]
    triang[i_level, 0 : new_elem.size] = flat[ini_ix : fin_ix]
    # new index to start to count elements
    ini_ix = fin_ix

# Triang is a <15,15> matrix containing the data of the triangle   
#print(triang)

# There are going to be several combinations of routes
routes = [ [''] * n_levels for i in range(n_levels)]


# Here, it's ll start from the second line (indexed as Row 1)
# Solutions are saved at "routes" list

# Find the longest route
for i_level in range(1, n_levels):
    n_elem = i_level + 1
    #print('')
    #print(i_level)   
    #print(n_elem)
    p_level = i_level - 1 #Previous level and maximum index for that previous level
    for i_elem in range(0 , n_elem):
        #print(i_elem)
        # Sum A This comes from Above Right, (goes Down Left), in the matrix is means only down
        index_a  = i_elem
        # Sum B This comes from Above Left, (goes Down Right), in the matrix is means UpLeft
        index_b = i_elem - 1
        
        # Validate indices flag_x = 1 if the index is valid     
        # The index of the current level (i_level) says how many elements are in previos level
        # therefore the indexx of the previous level only goes to its number of elements minus one
        flag_a = index_a >= 0 and index_a <= p_level
        flag_b = index_b >= 0 and index_b <= p_level       
        
        if flag_a and flag_b:
            result_a =  triang[i_level, i_elem] + triang[p_level, index_a]            
            result_b =  triang[i_level, i_elem] + triang[p_level, index_b]
            if result_a >= result_b:
                routes[i_level][i_elem] = routes[p_level][index_a] + 'A'                        
                result_sum = result_a
            else:
                routes[i_level][i_elem] = routes[p_level][index_b] + 'B'                        
                result_sum = result_b
                
            #print('AB')
    
        elif flag_a and not flag_b:
            result_a =  triang[i_level, i_elem] + triang[p_level, index_a]
            result_sum = result_a
            routes[i_level][i_elem] = routes[p_level][index_a] + 'A'                        
            #print('A')
            
        elif flag_b and not flag_a:
            result_b =  triang[i_level, i_elem] + triang[p_level, index_b]
            result_sum = result_b
            routes[i_level][i_elem] = routes[p_level][index_b] + 'B'
            #print('B') 
            
        
        #Update triangle
        triang[i_level, i_elem] = result_sum     
        #print(routes[i_level][i_elem])
                


# Find Maximum sum
i_max = np.argmax(triang[n_levels - 1,:])
print('\r\nFinal results')
print(triang[n_levels - 1, :])
print(routes[n_levels - 1][:])
print('\r\nLargest sum')
print(triang[n_levels - 1, i_max])
print(routes[n_levels - 1][i_max])







