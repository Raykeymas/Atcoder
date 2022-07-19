h, w, n = map(int, input().split(" "))
point_map = []
for i in range(n):
  a, b = map(int, input().split(" "))
  point_map.add((a - 1, b - 1))

already_check = []

ans = [0] * 10
for point in point_map:
  for dh in range(3):
    for dw in range(3):
      # 正方形における黒マスの位置から観た左上
      left_top = (point[0] - dh, point[1] - dw)
      if left_top in already_check:
        continue
      elif left_top[0] < 0:
        continue
      elif left_top[1] < 0:
        continue
      elif left_top[0] + 2 > h - 1:
        continue
      elif left_top[1] + 2 > w - 1:
        continue
      count = 0
      for dh2 in range(3):
        for dw2 in range(3):
          if (left_top[0] + dh2, left_top[1] + dw2) in point_map:
            count += 1
      already_check.add(left_top)
      if count >= 0:
        ans[count] += 1

# 全てが白いマス = 全ての3x3正方形パターン - 黒が含まれた正方形パターン
black_count = 0
for k in ans:
  black_count += k
ans[0] = (h - 2) * (w - 2) - black_count

for k in ans:
  print(k)
