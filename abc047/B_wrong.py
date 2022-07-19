W, H, N = map(int, input().split(" "))
# ここが間違い、乗算演算子を利用して配列を作成すると行単位で同じオブジェクトになってしまう
square = [[1] * W] * H
for i in range(N):
  x, y, a = map(int, input().split(" "))
  print(x, y, a)
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
      for y_i in range(y, H):
        square[y_i][x_i] = 0
  else:
    for x_i in range(0, W):
      for y_i in range(0, H - y):
        square[y_i][x_i] = 0
  for s in square:
    print(s)
