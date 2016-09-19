# Problem 20
# ==========
#
#
#    n! means n * (n 1) * ... * 3 * 2 * 1
#
#    Find the sum of the digits in the number 100!


res = 100

for n in range(100, 1,  -1):
    res *= n - 1


print(res)

sum = 0
for i in str(res):
    sum += int(i)

print(sum)

# Congratulations, the answer you gave to problem 20 is correct.
#
# You are the 140049th person to have solved this problem.
#
# Return to Problems page.