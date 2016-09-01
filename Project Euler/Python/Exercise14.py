# #Exercise 14

# The following iterative sequence is defined for the set of positive
# integers:
#
# n n/2 (n is even)
# n 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following
# sequence:
#                          13 40 20 10 5 16 8 4 2 1
#
# It can be seen that this sequence (starting at 13 and finishing at 1)
# contains 10 terms. Although it has not been proved yet (Collatz Problem),
# it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.

num = 13
sizechain = 0
notone = True

numbigsizechain = 0
biggersizechain = 0

for num in range(1, 1000000):
    if sizechain > biggersizechain:
        numbigsizechain = num - 1
        biggersizechain = sizechain
        sizechain = 0

    while notone:
        #print(num)
        sizechain += 1
        if num == 1:
            break
        if num % 2 == 0:
            num /= 2
        else:
            num = (num * 3) + 1

print(numbigsizechain)
print(biggersizechain)


