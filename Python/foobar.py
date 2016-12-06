# python foobar implementation.

for num in range(1,101):
    if num % 5 == 0 and num % 3 == 0:
        print("foobar")
    elif num % 3 == 0:
        print("foo")
    elif num % 5 == 0:
        print("bar")
    else:
        print(str(num))

