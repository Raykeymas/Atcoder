a = int(input())
b = int(input())

if a > b:
    if (10 - a + b) > abs(a-b):
        print(abs(a-b))
    else:
        print((10 - a + b))
else:
    if (10 + a - b) > abs(a-b):
        print(abs(a-b))
    else:
        print((10 + a - b))
