#Write a Python program that prints each item and its corresponding type from the following list
list = [1, "hello", 1.3, False, 3+2j, [1,2,3]]

def printType(vector):
    for i in range(len(vector)):
        print(type(vector[i]))

printType(list)