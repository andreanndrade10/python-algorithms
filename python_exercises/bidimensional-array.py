def bidimensionalarray():
    biarray = []
    array = []
    for i in range(3):
        for j in range(3):
            array.append(input('add a number: '))
    biarray.append(array[0:3]) 
    biarray.append(array[3:6])
    biarray.append(array[6:9])

    return biarray


if __name__ == "__main__":
    bidimensionalarray()