def problem():
    count = 0
    for i in range(500):
        if i%2 != 0 and  i%3 == 0:
            count+=i
        else:
            pass
    return count

if __name__ == "__main__":
    print(problem())