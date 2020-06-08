'''
Given an array of integers, calculate the fractions of its
elements that are positive, negative, and are zeros. Print
the decimal value of each fraction on a new line.
'''
import random

def n_negatives(array):
    negatives = 0
    for i in array:
        if i < 0:
            negatives+=1
    return negatives

def n_positives(array):
    positives = 0
    for i in array:
        if i > 0:
            positives+=1
    return positives

def n_zeros(array):
    zeros = 0
    for i in array:
        if i == 0:
            zeros+=1
    return zeros 


def plusMinus(array):
    positive_proportion = n_positives(array)/len(array)
    negative_proportion = n_negatives(array)/len(array)
    zero_proportion = n_zeros(array)/len(array)

if __name__ == "__main__":
    array = []
    for i in range(10):
        array.append(random.randint(-10,10))
    plusMinus(array)


