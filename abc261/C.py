from collections import defaultdict
N = int(input())

store = defaultdict(int)
for i in range(N):
    s = input()
    if store[s] != 0:
        print(f"{s}({store[s]})")
    else:
        print(s)
    store[s] += 1
