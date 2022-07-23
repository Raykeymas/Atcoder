from collections import defaultdict

N, T = map(int, input().split(" "))
values = list(map(int, input().split(" ")))

distances = defaultdict(int)
min_value = values[0]

for i in range(1, N):
  distances[values[i] - min_value] += 1
  min_value = min(min_value, values[i])

print(distances[max(distances.keys())])