import sys
sys.setrecursionlimit(10000)
N = int(input())


def calc(k):
    if k == 0:
        return 1
    return k * calc(k-1)


print(calc(N))
