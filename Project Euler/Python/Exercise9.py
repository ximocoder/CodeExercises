# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

for i in range(1, 1001):
    for j in range(1, 1001):
        for z in range(1, 1001):
            if i < j < z:
                if i**2 + j**2 == z**2:
                    if i+j+z == 1000:
                        print(i)
                        print(j)
                        print(z)

# 200
# 375
# 425
# You are the 236731st person to have solved this problem.
