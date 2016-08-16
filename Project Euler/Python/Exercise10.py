# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

sumprime = 0

# for num in range(1, 2000000):
#     prime = True
#     for i in range(2, num):
#         if num % i == 0:
#             prime = False
#
#     if prime:
#         sumprime += num

def primes_sieve(limit):
    limitn = limit+1
    not_prime = [False] * limitn
    primes = []
    sum = 0

    for i in range(2, limitn):
        if not_prime[i]:
            continue
        for f in range(i*2, limitn, i):
            not_prime[f] = True

        primes.append(i)
        sum += i
    return sum


sumprime = primes_sieve(2000000)
print(sumprime)

# result: 142913828922
# Congratulations, the answer you gave to problem 10 is correct.
# You are the 217767th person to have solved this problem.
