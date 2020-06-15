# Complete the staircase function below.
def staircase(input):
    n = len(list(range(input+1)))
    for i in range(input+1):
        n-=1
        print(' '*n + '#'*i)  


if __name__ == '__main__':
    n = int(input('Insert a number: '))
    staircase(n)
