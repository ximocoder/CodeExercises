#exercise 4


#    A palindromic number reads the same both ways. The largest palindrome made
#    from the product of two 2-digit numbers is 9009 = 91 * 99.
#    Find the largest palindrome made from the product of two 3-digit numbers.

# def ReverseNumber(n, partial=0):
#     if n == 0:
#         return partial
#     return ReverseNumber(n / 10, partial * 10 + n % 10)

palind = 0

for num1 in range(100, 1000):
    for num2 in range(100, 1000):
        palind = num1 * num2
        reverse = str(palind)[::-1]
        if reverse == str(palind):
            print(str(palind) + "-" + str(num1) + "-" + str(num2))

# solved: 906609-993-913


