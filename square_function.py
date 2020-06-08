import math 

def user_interface():
    print('Square function calculator: ax^2 + bx + c = 0')
    a = int(input('a: ')) 
    b = int(input('b: '))
    c = int(input('c: '))
    delta(a,b,c)

def delta(a,b,c):
    delta = (b**2) - (4*a*c)
    if delta < 0:
        print('We cannot persist with these values, delta must be greater than zero.')
        user_interface()
    else:
        square_function(a,b,c,delta)

def square_function(a,b,c,delta):
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print(x1,x2)
    return x1,x2

user_interface()
    
    



