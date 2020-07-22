# https://www.hackerrank.com/challenges/jumping-on-the-clouds

def jumpingOnClouds(binaryArray):
    jump = 0 
    current = 0
    while current < len(binaryArray):
        if current + 2 < len(binaryArray) and binaryArray[current+2] == 0:
            jump+=1
            current+=2
        elif current + 1 < len(binaryArray) and binaryArray[current+1] == 0:
            jump+=1
            current+=1
        else:
            current+=1
    return jump

if __name__ == "__main__":
    binaries = [0, 0, 1, 0, 0, 1, 0]
    jumpingOnClouds(binaries)
