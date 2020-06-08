'''
Given an integer array, output all the unique pairs that sum up to a specific value 'k'
Example: pair_sum([1,3,2,2],4)
would return 2 pairs: (1,3) and (2,2)
'''

def pair_sum(vector, k):
    sum = 0
    for i in vector:
        temp_vector = vector
        a = temp_vector.pop(i) 
        for j in temp_vector:
            if a or j > k:
                pass
            else:
                sum = a + j
            if sum == k:
                print(a,j)


pair_sum([1,3,2,2],4)

