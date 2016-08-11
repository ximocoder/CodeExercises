#exercise 7

#  By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
#  that the 6^th prime is 13.
#   What is the 10001^st prime number?

numprime = 0

for num in range(1, 100000000000000000):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
    if prime:
        numprime += 1
        if numprime == 10002:
            print(num)

# TODO: Improve speed
#104743
#Congratulations, the answer you gave to problem 7 is correct.
#You are the 275430th person to have solved this problem.