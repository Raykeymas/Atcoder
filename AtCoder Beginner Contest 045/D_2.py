from collections import defaultdict
h, w, n = map(int, input().split(" "))
draw_point = defaultdict(int)
point_map = []
for i in range(n):
  a, b = map(int, input().split(" "))
  draw_point[(a - 1, b - 1)] = 1
  point_map.append((a - 1, b - 1))

already_check = []


def count_square(left_top):
  if left_top in already_check:
    return -1
  if left_top[0] < 0 or left_top[1] < 0:
    return -1
  elif left_top[0] + 2 > h - 1 or left_top[1] + 2 > w - 1:
    return -1
  count = 0
  for dh in range(3):
    for dw in range(3):
      count += draw_point[(left_top[0] + dh, left_top[1] + dw)]
  already_check.append(left_top)
  return count


ans = [0] * 10
for point in point_map:
  for dh in range(3):
    for dw in range(3):
      # 3x3正方形における黒マスの位置から観た左上
      left_top = (point[0] - dh, point[1] - dw)
      count = count_square(left_top)
      if count >= 0:
        ans[count] += 1

# 全てが白いマス = 全ての3x3正方形パターン - 黒が1つでも含まれているパターン
black_count = 0
for k in ans:
  black_count += k
ans[0] = (h - 2) * (w - 2) - black_count

for k in ans:
  print(k)
