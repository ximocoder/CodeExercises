<<<<<<< .merge_file_a78132
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.


sumprime = 0

for num in range(1, 2000000):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False

    if prime:
        sumprime += num
=======
   # The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
   #
   # Find the sum of all the primes below two million.
>>>>>>> .merge_file_a16608
