'''
Given five positive integers, find the minimum and maximum values that can be calculated
by summing exactly four of the five integers. Then print the respective minimum and
maximum values as a single line of two space-separated long integers. 
'''
import random

def miniMaxSum(arr):
    print(sum(arr)-max(arr), sum(arr)-min(arr))


if __name__ == '__main__':
    #generate random array and calling the miniMaxSum function
    arr = []
    for i in range(5):
        arr.append(random.randint(0,50))
    miniMaxSum(arr)


