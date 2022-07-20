
def operation(stones, count, target):
  left_count = 0
  right_count = 0
  first_string = None

  for i, stone in enumerate(stones):
    if first_string is None:
      first_string = stone
    elif stone != first_string:
      left_count = i
      break

  first_string = None
  for i, stone in enumerate(reversed(stones)):
    if first_string is None:
      first_string = stone
    elif stone != first_string:
      right_count = len(stones) - i - 1
      break

  if left_count > right_count:
    for i in range(left_count):
      if target is None:
        stones[i] = stones[left_count]
        target = stones[left_count]
      else:
        stones[i] = target
  else:
    for i in range(right_count, len(stones)):
      if target is None:
        stones[i] = stones[right_count]
        target = stones[right_count]
      else:
        stones[i] = target
  count += 1
  return stones, count, target


s = input()
tmp_stones = list(s)
stones = []
w, b = 0, 0
for stone in tmp_stones:
  if stone == "W":
    w += 1
    stones.append(True)
  else:
    b += 1
    stones.append(False)
# 片方の身ならそこで終わり
if w == 0 or b == 0:
  print(0)
  exit(0)

# 現時点で多い方に変えていく
target = None
count = 0

# stones, count, taregt = operation(stones, count, target)
if len(set(stones)) == 1:
  print(count)
  exit(0)

for k in range(len(stones)):
  # stones, count, taregt = operation(stones, count, target)
  if len(set(stones)) == 1:
    break

print(count)
