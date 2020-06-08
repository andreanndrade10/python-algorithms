def largest_sum_list(list):
    max1 = list[0]
    max2 = list[0]
    for i in list:
        if i > max1:
            max1 = i
    list.remove(max1)
    for j in list:
        if j > max2:
            max2=j
    return max1+max2


if __name__ == "__main__":
    list = [2,4,-3,2,5,6,-4]
    print(largest_sum_list(list))