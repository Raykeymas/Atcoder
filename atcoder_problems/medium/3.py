S = list(input())
N = len(S) + 1

a = [0] * N
for i in range(N-1):
    if S[i] == "<":
        a[i+1] = a[i] + 1
for i in reversed(range(N-1)):
    if S[i] == ">":
        a[i] = max(a[i], a[i+1]+1)

print(sum(a))