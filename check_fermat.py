def user_interface():
    print("Check if Fermat is righ")
    a = int(input("A: "))
    b = int(input("B: "))
    c = int(input("C: "))
    n = int(input("n: "))
    check_fermat(a,b,c,n)


def check_fermat(a,b,c,n):
    first_element = a**n
    second_element = b**n 
    third_element = c**n
    if first_element+second_element == third_element:
        print('Fermat was wrong!')
    else:
        print('Fermat is right!')
        user_interface()


user_interface()