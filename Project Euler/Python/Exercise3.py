#exercise 3

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

x = True
num = 13195
num2 = num
n = num

for p in range(2, n+1):
    for i in range(2, p):
        if p % i == 0:
            break
    else:
        print (p)
print ('Done')

# while x:
#     num2 = num2 - 1
#     if num % num2 == 0:
#         print(num2)
#         x = False



