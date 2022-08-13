N = int(input())
S = input()

max_count = 0
for i in range(1,N):
    left = set(S[0:i])
    right = set(S[i:])
    max_count = max(max_count, len(left & right))
print(max_count)