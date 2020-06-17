import random

'''
You are in charge of the cake for your niece's birthday and have decided the cake will
have one candle for each year of her total age. When she blows out the candles, she’ll
only be able to blow out the tallest ones. Your task is to find out how many candles 
she can successfully blow out. For example, if your niece is turning 4 years old, and
the cake will have 4 candles of height 4, 4, 1, 3, she will be able toblow out 2 candles
successfully, since the tallest candles are of height and there are such candles. 
'''
def birthdayCakeCandles(array):
    #Pick the max number of the array
    max_heigh = max(array)
    #Count how many time max number of array appears in array
    n = array.count(max_heigh)
    print(n)
    return n 


if __name__ == "__main__":
    arr = []
    for i in range(10):
        arr.append(random.randint(0,5))
    print(arr)
    birthdayCakeCandles(arr)