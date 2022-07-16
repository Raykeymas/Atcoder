W, H, N = map(int, input().split(" "))
square = [[1 for j in range(W)] for i in range(H)]
for i in range(N):
  x, y, a = map(int, input().split(" "))
  if a == 1:
    for x_i in range(0, x):
      for y_i in range(0, H):
        square[y_i][x_i] = 0
  elif a == 2:
    for x_i in range(x, W):
      for y_i in range(0, H):
        square[y_i][x_i] = 0
  elif a == 3:
    for x_i in range(0, W):
      for y_i in range(H - y, H):
        square[y_i][x_i] = 0
  else:
    for x_i in range(0, W):
      for y_i in range(0, H - y):
        square[y_i][x_i] = 0

left_top_point = None
right_bottom_point = None

for j in range(H):
  for i in range(W):
    if square[j][i] == 1:
      if left_top_point is None:
        left_top_point = (j, i)
      else:
        right_bottom_point = (j, i)

if left_top_point is None:
  print(0)
elif right_bottom_point is None:
  print(1)
else:
  print((right_bottom_point[0] - left_top_point[0] + 1) * (right_bottom_point[1] - left_top_point[1] + 1))
