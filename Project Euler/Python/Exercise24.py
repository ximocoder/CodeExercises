# Problem 24
# ==========
#
#
#    A permutation is an ordered arrangement of objects. For example, 3124 is
#    one possible permutation of the digits 1, 2, 3 and 4. If all of the
#    permutations are listed numerically or alphabetically, we call it
#    lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
#
#                        012   021   102   120   201   210
#
#    What is the millionth lexicographic permutation of the digits 0, 1, 2, 3,
#    4, 5, 6, 7, 8 and 9?
import itertools as it

gen = it.permutations(range(0, 10))

count = 0
for i in gen:
   count += 1
   if count == 1000000:
      print(i)

#       Congratulations, the answer you gave to problem 24 is correct.
#
# You are the 80878th person to have solved this problem.
#
# Return to Problems page.