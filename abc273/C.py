from copy import copy

N = int(input())
a_list = list(map(int, input().split(" ")))
sorted_list = copy(a_list)
sorted_list = sorted(set(a_list))
ans = [0] * N

dic = {}
for i, s in enumerate(sorted_list):
    dic[s] = len(sorted_list) - (i+1)

for k in range(N):
    ans[dic[a_list[k]]] = ans[dic[a_list[k]]] + 1

print("\n".join(map(str, ans)))
