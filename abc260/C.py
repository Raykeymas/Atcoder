import sys
from functools import lru_cache

sys.setrecursionlimit(10000)

N,X,Y = map(int,input().split(" "))

ans = 0

@lru_cache(maxsize=1000)
def operation(level, type, num):
    ans = 0
    if level == 1:
        if type=="blue":
            return num
        else:
            return 0
    if type == "red":
        ans += operation(level-1, "red", 1)
        ans += operation(level, "blue", X)
    else:
        for i in range(num):
            ans += operation(level-1, "red", 1)
            ans += operation(level-1, "blue", Y)
    return ans
ans = operation(N,"red",1)
print(ans)