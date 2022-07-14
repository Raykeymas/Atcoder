from collections import defaultdict
h, w, n = map(int, input().split(" "))
draw_point = defaultdict(int)
point_map = []
for i in range(n):
  a, b = map(int, input().split(" "))
  draw_point[(a, b)] = 1
  point_map.append((a, b))


# def black_or_white(i, j): return 1 if (i, j) in draw_point else 0


# board = [[black_or_white(i + 1, j + 1) for j in range(w)] for i in range(h)]
# for b in board:
#   print(b)

# 解法１：正攻法：計算量が足りない
# ans = [0] * 10
# for height in range(h-2):
#     for weight in range(w-2):
#         count = 0
#         for j in range(height,height+3):
#             for k in range(weight,weight+3):
#                 count += board[j][k]
#         ans[count] += 1
# for a in ans:
#     print(a)

# 解法2
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
      count += draw_point[(left_top[0] + dh + 1, left_top[1] + dw + 1)]
  already_check.append(left_top)
  return count


ans = [0] * 10
for point in point_map:
  for dh in range(3):
    for dw in range(3):
      # 正方形における黒マスの位置から観た左上
      left_top = (point[0] - dh, point[1] - dw)
      count = count_square(left_top)
      if count >= 0:
        ans[count] += 1
for k in ans:
  print(k)
