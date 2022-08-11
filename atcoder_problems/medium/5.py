import math


N = int(input())

def min_calc(last: int) -> int:
    return last - 1

def calc(ans: int, last: int) -> int:
    print(ans)
    separate = 0
    if last % 2 == 0:
        ans += last - ((last / 2) + 1)
        separate = int((last / 2) + 1)
    else:
        ans += last - (math.floor(last / 2) + 1)
        separate = math.floor(last / 2) + 1
    print(separate,last)
    for i in reversed(range(separate, last)):
        ans += i
    if separate <= 3:
        ans += min_calc(separate-1)
        return ans
    else:
        return calc(ans, separate)

ans = 0
separate = 0
if N <= 2:
    print(min_calc(N))
    exit(0)
elif N == 3:
    print(3)
    exit(0)
ans = calc(ans, N)

print(int(ans))
