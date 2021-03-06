#
# Problem 19
# ==========
#
#
#    You are given the following information, but you may prefer to do some
#    research for yourself.
#
#      * 1 Jan 1900 was a Monday.
#      * Thirty days has September,
#        April, June and November.
#        All the rest have thirty-one,
#        Saving February alone,
#        Which has twenty-eight, rain or shine.
#        And on leap years, twenty-nine.
#      * A leap year occurs on any year evenly divisible by 4, but not on a
#        century unless it is divisible by 400.
#
#    How many Sundays fell on the first of the month during the twentieth
#    century (1 Jan 1901 to 31 Dec 2000)?
#
# MORE INFO
# Return the day of the week as an integer, where Monday is 0 and Sunday is 6.
# >>> import datetime
# >>> datetime.datetime.today()
# datetime.datetime(2012, 3, 23, 23, 24, 55, 173504)
# >>> datetime.datetime.today().weekday()

import datetime
import monthdelta

date = datetime.date(1901, 1, 1)
sumsundays = 0

while date.year < 2001:

    if date.weekday() == 6:
        sumsundays += 1
    date = date + monthdelta.monthdelta(+1)

print(sumsundays)
# 
#
# Congratulations, the answer you gave to problem 19 is correct.
#
# You are the 94200th person to have solved this problem.



