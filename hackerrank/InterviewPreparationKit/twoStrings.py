#https://www.hackerrank.com/challenges/two-strings
from collections import Counter

def twoStrings(string1, string2):
    dict1 = Counter(string1)
    dict2 = Counter(string2)

    for i in dict1:
        for j in dict2:
            if i == j:
                return 'Yes'
    return 'No'

if __name__ == "__main__":
    q = int(input('number of pairs to compare: ')) 
    for i in range(q):
        s1=input()
        s2=input()
        result = twoStrings(s1,s2)
        print(result)

