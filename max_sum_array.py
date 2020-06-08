'''
Take an array w/ positive and negative integers and find the maximun sum of that array
'''

def max_sum_array(list):
    #suppress repeated elements with set() function
    set_list = set(list)
    for i in set_list:
        for j in set_list:
            sum = i+j
            
            


max_sum_array([2,2,1,4,-4,2,-4,1])