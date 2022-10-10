N = int(input())
a_list = list(map(int, input().split(" ")))
a_list = sorted(a_list, reverse=True)

max = 0
for a in a_list:
    for a_2 in a_list:
        if max > a+a_2:
            break
        if a != a_2 and (a + a_2) % 2 == 0:
            max = a+a_2

if max == 0:
    print(-1)
else:
    print(max)
