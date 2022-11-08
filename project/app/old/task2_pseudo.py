# Task 2 pseudo code

import random

MAX_SENTENCE_NUM = 4
min_num = 0
max_num = 2

def generate_num():
    return random.randint(min_num, max_num)

month1 = input()
val1 = input()
month2 = input()
val2 = input()
month3 = input()
val3 = input()
month4 = input()
val4 = input()
month5 = input()
val5 = input()

num1 = int(val1)
num2 = int(val2)
num3 = int(val3)
num4 = int(val4)
num5 = int(val5)

if num1 > num2:
    result1 = num1 - num2
    Re1 = str(result1)
    number = [generate_num()]
    diction = {"0": "fall", "1": "go down", "2": "decrease"}
    print('The number of students ' + ' from ' + val1 + ' in ' + month1 + ' by ' + Re1 + ' to ' + val2 + ' in ' + month2)
elif num1 == num2:
    print('The number of students remain at ' + val2 + ' from ' + month1 + ' to ' + month2)
else:
    result1 = num2 - num1
    Re1 = str(result1)
    print('The number of students rise from ' + val1 + ' in ' + month1 + ' by ' + Re1 + ' to ' + val2 + ' in ' + month2)



if num2 > num3:
    result2 = num2 - num3
    Re2 = str(result2)
    print('The number of students falls from ' + val2 + ' in ' + month2 + ' by ' + Re + ' to ' + val3 + ' in ' + month3)
elif num2 == num3:
    print('The number of students remain at ' + val3 + ' from ' + month2 + ' to ' + month3)
else:
    result2 = num3 - num2
    Re2 = str(result2)
    print('The number of students rise from ' + val2 + ' in ' + month2 + ' by ' + Re2 + ' to ' + val3 + ' in ' + month3)



if num3 > num4:
    result3 = num3 - num4
    Re3 = str(result3)
    print('The number of students falls from ' + val3 + ' in ' + month3 + ' by ' + Re3 + ' to ' + val4 + ' in ' + month4)
elif num3 == num4:
    print('The number of students remain at ' + val4 + ' from ' + month3 + ' to ' + month4)
else:
    result3 = num4 - num3
    Re3 = str(result3)
    print('The number of students rise from ' + val3 + ' in ' + month3 + ' by ' + Re3 + ' to ' + val4 + ' in ' + month4)



if num4 > num5:
    result4 = num4 - num5
    Re4 = str(result4)
    print('The number of students falls from ' + val4 + ' in ' + month4 + ' by ' + Re4 + ' to ' + val5 + ' in ' + month5)
elif num4 == num5:
    print('The number of students remain at ' + val5 + ' from ' + month4 + ' to ' + month5)
else:
    result4 = num5 - num4
    Re4 = str(result4)
    print('The number of students rise from ' + val4 + ' in ' + month4 + ' by ' + Re4 + ' to ' + val5 + ' in ' + month5)


print(f"Number of bananas: {num_bananas}")