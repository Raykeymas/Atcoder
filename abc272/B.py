import itertools

N, M = map(int, input().split(" "))
numbers = [i + 1 for i in range(N)]
kanri_pair = set(itertools.combinations(numbers, 2))
pair = set(itertools.combinations(numbers, 2))
k_list = []
for _ in range(M):
    sanka_list = list(map(int, input().split(" ")))
    sanka_pair = set(itertools.combinations(sanka_list[1:], 2))
    for p in list(pair):
        if p in sanka_pair:
            kanri_pair.remove(p)
            if len(kanri_pair) == 0:
                print("Yes")
                exit(0)
    pair = kanri_pair

print("No")
