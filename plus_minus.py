'''
Given an array of integers, calculate the fractions of its elements that are positive,
negative, and are zeros. Print the decimal value of each fraction on a new line.
'''

import random

def proportion_negative(array):
    negatives = 0
    for i in array:
        if i < 0:
            negatives+=1
    return negatives/len(array)

def proportion_zeros(array):
    zeros = 0 
    for i in array:
        if i == 0:
            zeros+=1
    return zeros/len(array)

def proportion_positives(array):
    positives = 0
    for i in array:
        if i > 0:
            positives+=1
    return positives/len(array)


def plus_minus(array):
    array = array
    proportion_negative(array)
    proportion_zeros(array)
    proportion_positives(array)
    print('\n List: {} \n\n Negative proportion: {} \n Zero proportion: {} \n Positive proportion: {} \n'.format(array, proportion_negative(array), proportion_zeros(array), proportion_positives(array)))

    

if __name__ == "__main__":
    array = []
    for i in list(range(10)):
        array.append(random.randint(-10,10))
    plus_minus(array)

    