def check_integer():
    n = int(input('Please Type a number between 0 and 10: '))
    try:
        if isinstance(int(n), int) == True:
            #check if number is between 0 e 10
            if n>0 and n<10:
                print('Congratulations, you know how to type a number between 0 and 10')
                exit()
            else:
                print('Are u dumb?')
                check_integer()
    except ValueError:
        print('Are u dumb?')
        check_integer() 

check_integer()