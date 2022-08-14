A,B,C = map(int, input().split(" "))
mod_list = set()

for i in range(B):
    if A*i % B == C:
        print("YES")
        exit(0)
print("NO")