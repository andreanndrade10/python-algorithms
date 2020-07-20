#https://www.hackerrank.com/challenges/counting-valleys
#A valley is a sequence of consecutive steps below sea level,
#starting with a step down from sea level and ending with a step up to sea level.
#Given Gary's sequence of up and down steps during his last hike,
#find and print the number of valleys he walked through. 

def countingValleys(n, string):
    valley = 0
    level = 0
    
    for i in range(n):
        if string[i] == 'D' and level == 0:
            valley+=1
            level-=1
        elif string[i] == 'D':
            level-=1
        elif string[i] == 'U':
            level+=1

    return valley

if __name__ == "__main__":
    #example
    countingValleys(12,'DDUUDDUDUUUD')