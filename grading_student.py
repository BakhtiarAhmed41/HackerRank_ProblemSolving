
import math
import os
import random
import re
import sys

def gradingStudents(grades):
    rounded_grade = []
    for i in range(len(grades)):
        if (grades[i]< 38):
            rounded_grade.append(grades[i])
            continue
        else:
            
            if ((grades[i]+1)%5 ==0):
                rounded_grade.append(grades[i]+1)
            
            elif((grades[i]+2)%5 ==0):
                rounded_grade.append(grades[i]+2)
            
            else:
                rounded_grade.append(grades[i])
        
    return rounded_grade

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
