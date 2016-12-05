for num in range(1,101):
    if num % 5 == 0 and num % 3 == 0:
        msg = "foobar"
    elif num % 3 == 0:
        msg = "foo"
    elif num % 5 == 0:
        msg = "bar"
    else:
        msg = str(num)
    print(msg)
