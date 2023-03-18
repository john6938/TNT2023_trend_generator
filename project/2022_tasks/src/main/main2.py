import random

Max_sentence= 4

rise_word = 0
fall_word = 0
remain_word = 0


Monthnum = [["Jan",10],["Feb",12],["Mar",12],["Apl",8],["May",15]]

for i in range(Max_sentence):

    if Monthnum[i][1] > Monthnum[i+1][1]:
        result1 = Monthnum[i][1] - Monthnum[i+1][1]
        Re1 = str(result1)
        if fall_word == 0:
            print('The number of students decreases from ' + str(Monthnum[i][1]) + ' in ' + Monthnum[i][0] + ' by ' + Re1 + ' to ' + str(Monthnum[i+1][1]) + ' in ' + Monthnum[i+1][0])
            fall_word+=1

        elif fall_word == 1:
            print('The number of students falls from ' + str(Monthnum[i][1]) + ' in ' + Monthnum[i][0] + ' by ' + Re1 + ' to ' + str(Monthnum[i+1][1]) + ' in ' + Monthnum[i+1][0])
            fall_word+=1

        else:
            print('The number of students goes down from ' + str(Monthnum[i][1]) + ' in ' + Monthnum[i][0] + ' by ' + Re1 + ' to ' + str(Monthnum[i+1][1]) + ' in ' + Monthnum[i+1][0])
            fall_word = 0


    elif Monthnum[i][1] == Monthnum[i+1][1]:
        if remain_word == 0:
            print('The number of students remains the same at ' + str(Monthnum[i+1][1]) + ' from ' + Monthnum[i][0] + ' to ' + Monthnum[i+1][0])
            remain_word+=1

        elif remain_word == 1:
            print('The number of students stable at ' + str(Monthnum[i+1][1]) + ' from ' + Monthnum[i][0] + ' to ' + Monthnum[i+1][0])
            remain_word+=1

        else:
            print('The number of students stays flat ' + str(Monthnum[i+1][1]) + ' from ' + Monthnum[i][0] + ' to ' + Monthnum[i+1][0])
            fall_word = 0

    else:
        result1 = Monthnum[i+1][1] - Monthnum[i][1]
        Re1 = str(result1)
        if rise_word == 0:
            print('The number of students increases from ' + str(Monthnum[i][1]) + ' in ' + Monthnum[i][0] + ' by ' + Re1 + ' to ' + str(Monthnum[i+1][1]) + ' in ' + Monthnum[i+1][0])
            rise_word+=1

        elif rise_word == 1:
            print('The number of students rises from ' + str(Monthnum[i][1]) + ' in ' + Monthnum[i][0] + ' by ' + Re1 + ' to ' + str(Monthnum[i+1][1]) + ' in ' + Monthnum[i+1][0])
            rise_word+=1

        else:
            print('The number of students goes up from ' + str(Monthnum[i][1]) + ' in ' + Monthnum[i][0] + ' by ' + Re1 + ' to ' + str(Monthnum[i+1][1]) + ' in ' + Monthnum[i+1][0])
            rise_word = 0