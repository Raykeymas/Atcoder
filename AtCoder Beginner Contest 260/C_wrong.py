import sys

sys.setrecursionlimit(10000)

N,X,Y = map(int,input().split(" "))

ans = 0

# 再起関数はメモ化しないと、答えが合っていても処理速度で損をすることになる
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