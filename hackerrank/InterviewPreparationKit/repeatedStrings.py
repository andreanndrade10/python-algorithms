'''def repeatedString(s,n):
    #count_a = 0
    interator = 1
    infiniteString = s
    while len(infiniteString) < n:
        infiniteString *= interator
        interator+=1 
    consideredString = infiniteString[:n]
    count_a=consideredString.count('a')
    return count_a
'''

def repeatedString(s,n):
    count_a = (s[:n%len(s)].count('a')+(s.count('a')*(n//len(s))))
    return count_a
    
if __name__ == "__main__":
    pass
