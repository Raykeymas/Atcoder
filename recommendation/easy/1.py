N = int(input())

B = 1
while (N - 5**B) >= 0:
    tmp = (N - 5**B)
    A = 1
    while (tmp - 3**A) >= 0:
        if tmp == 3**A:
            print(A, B)
            exit(0)
        A += 1
    B += 1
print(-1)
