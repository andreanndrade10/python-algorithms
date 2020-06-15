'''
Given five positive integers, find the minimum and maximum values that can be calculated
by summing exactly four of the five integers. Then print the respective minimum and
maximum values as a single line of two space-separated long integers. 
'''
import random

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arrMin = arr
    arrMax = arr
    print(sumMin(arrMin))
    print(sumMax(arrMax))
   
def sumMax(array):
    array.remove(min(array))
    sumMax=0
    for i in array:
        sumMax+=i
    return sumMax

def sumMin(array):
    array.remove(max(array))
    sumMin=0
    for i in array:
        sumMin+=i
    return sumMin

if __name__ == '__main__':
    #generate random array and calling the miniMaxSum function
    #arr = []
    #for i in range(5):
    #    arr.append(random.randint(0,50))
    #print(arr)
    miniMaxSum([1,2,3,4,5])
