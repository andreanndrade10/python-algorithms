'''
Consider a staircase of size n=4

   #
  ##
 ###
####

Write a program that prints a staircase of size 'n'

'''

def staircase(input):
    n = len(list(range(input+1)))
    for i in range(input+1):
        n-=1
        print(' '*n + '#'*i)  


if __name__ == '__main__':
    n = int(input('Insert a number: '))
    staircase(n)
