#Exercise 12
#	The sequence of triangle numbers is generated by adding the natural
#  numbers. So the 7^th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 =
#   28. The first ten terms would be:
#                  1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# Let us list the factors of the first seven triangle numbers:
#
#    1: 1
#    3: 1,3
#    6: 1,2,3,6
#   10: 1,2,5,10
#   15: 1,3,5,15
#   21: 1,3,7,21
#   28: 1,2,4,7,14,28
#
# We can see that 28 is the first triangle number to have over five
# divisors.
#
# What is the value of the first triangle number to have over five hundred
# divisors?
def factorsnum(num):
    numfactors = 0
    sum = 0

    for x in range(1, num + 1):
        if num % x == 0:
            numfactors += 1
            sum += x

    return sum

def gettriangle(num):
    sum = 0
    for x in range(num, -1, -1):
        sum += x
    return sum

def getdivisorsnumber(num):
    totaldivisors = 0
    if num % 2 == 0:
        totaldivisors += 1
        num = int(num/2)
    elif num % 3 == 0:
        totaldivisors += 1
        num = int(num/3)

    for x in range(num, 0, -1):
        if num % x == 0:
            totaldivisors += 1
            #print(x)
    return totaldivisors

maxnum = 28
# 6, 10, 15
# print(gettriangle(3))
# print(gettriangle(4))
# print(gettriangle(5))
# print(gettriangle(7))
print(getdivisorsnumber(gettriangle(7)))

# for x in range(1, maxnum):
#     print(x)
#     print(getdivisorsnumber(gettriangle(x)))

print(getdivisorsnumber(gettriangle(100)))

# trianglenumber = 0
# sum = 0
# n = 11
#
# for x in range(1, n):
#     print(factorsnum(x))
#
# print(sum)



