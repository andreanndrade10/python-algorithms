#check the challenge: https://www.hackerrank.com/challenges/sock-merchant
import random 

def count_element(i, array):
    i_count = 0
    for j in array:
        if i == j:
            i_count += 1
    return i_count

def sockMerchant(n, ar):
    count = 0
    ar.sort()
    ar.append('#')
    i = 0
    while i<n:
        if ar[i]==ar[i+1]:
            count = count+1
            i+=2
        else:
            i+=1
    return count
 

if __name__ == "__main__":
    socks =[]
    for i in range(10):
        socks.append(random.randint(1,10))
    print(socks, sockMerchant(len(socks), socks))


    