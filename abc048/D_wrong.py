from collections import defaultdict
s = list(input())

counter = defaultdict(int)
pointers = defaultdict(lambda: [])
for i, v in enumerate(s):
  if i != 0 and i != len(s) - 1:
    counter[v] += 1
    pointers[v].append(i)

loop = 0
while True:
  sorted_counter = sorted(counter.items(), key=lambda x: x[1], reverse=True)
  target_index = -1
  for j in range(len(counter.keys())):
    target = sorted_counter[j][0]
    if len(pointers[target]) == 0:
      continue
    for i in range(sorted_counter[j][1]):
      point = pointers[target][i] - loop
      if s[point - 1] != s[point + 1]:
        counter[target] -= 1
        pointers[target].remove(point + loop)
        target_index = point
        loop += 1
        break
    if target_index != -1:
      break
  if target_index == -1:
    break

if loop % 2 == 0:
  print("Second")
else:
  print("First")
