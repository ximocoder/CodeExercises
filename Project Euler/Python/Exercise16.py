# Problem 16
# ==========
#
#
#    2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
#    What is the sum of the digits of the number 2^1000?


res = 2**1000
sres = str(res)
sum = 0

for i in sres:
    print(i)
    sum += int(i)
print(res)
print(sum)

# Congratulations, the answer you gave to problem 16 is correct.
# You are the 156917th person to have solved this problem.