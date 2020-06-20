# To see de problem check the following link: https://www.hackerrank.com/challenges/grading/problem
import random

def checkGrade(grade):
    if grade < 38:
        return grade
    elif (grade+1)%5 == 0:
        return grade+1
    elif (grade+2)%5 == 0:
        return grade+2
    else:
        return grade


def gradingStudents(array):
    for i in array:
        print(checkGrade(i))


if __name__ == "__main__":
    grades=[]
    for i in range(10):
        grades.append(random.randint(0,100))
    print(grades)
    gradingStudents(grades)