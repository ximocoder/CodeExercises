# Problem 17
# ==========
#
#
#    If the numbers 1 to 5 are written out in words: one, two, three, four,
#    five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
#    If all the numbers from 1 to 1000 (one thousand) inclusive were written
#    out in words, how many letters would be used?
#
#    NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
#    forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
#    20 letters. The use of "and" when writing out numbers is in compliance
#    with British usage.

words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
tens = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
dec = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
hun = ['hundred']
thou = ['thousand']

print(words)


def sumwords(number):
    res = 0
    if str(number).endswith("10"):
        res = len(words[9])
    if str(number).endswith("100"):
        res = len(hun[0])
    return res

for w in words:
    print(w)

print(str(sumwords(10)))
print(str(sumwords(100)))



