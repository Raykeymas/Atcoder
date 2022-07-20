s = input()
stones = list(s)

count = 0
color = stones[0]
for i in range(1, len(stones)):
  if color != stones[i]:
    count += 1
    color = stones[i]
print(count)
