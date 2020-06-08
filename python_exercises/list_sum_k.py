'''
This program prints the elements that summed is equal 'k'
'''
import random

def check_list_k(list, k):
    for i in list:
        for j in list:
            if j+i==k:
                print(i,j)

if __name__ == "__main__":
    random_list=[]
    for i in range(10):
        random_list.append(random.randint(-10,10))

    k = random.randint(-10,10)
    print('List: {}'.format(random_list))
    print('K: {} \n'.format(k))
    check_list_k(random_list, k)
    
