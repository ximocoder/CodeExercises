#exercise 5

 #  2520 is the smallest number that can be divided by each of the numbers
 #  from 1 to 10 without any remainder.
 #  What is the smallest number that is evenly divisible by all of the numbers
 #  from 1 to 20?

isOk = True
num = 0
while num < 100000000000:
    num += 1

    isOk = True
    for i in range(1, 21):
        if num % i != 0:
            isOk = False

    if isOk:
        print(num)
        break

#result> 232792560
#Congratulations, the answer you gave to problem 5 is correct.
#You are the 319467th person to have solved this problem.


